#!/usr/bin/env python3
"""Analyse descriptive d'un extrait audio, sans modifier la source.
Dépendances : numpy, soundfile. Pas d'écoute, d'identification de synthé ou de true peak.
"""
import argparse
import json
import math
from pathlib import Path
import sys

try:
    import numpy as np
    import soundfile as sf
except ImportError:
    raise SystemExit('Bibliothèques requises : numpy et soundfile. Utiliser un environnement qui les fournit, ou les installer dans un environnement de travail isolé.')


def db(value):
    return round(20 * math.log10(value), 4) if value > 0 else None


def periodicity_hint(signal, sr, fmin, fmax):
    """Pic d'autocorrélation normalisée ; hypothèse monophonique seulement."""
    x = signal.astype(float) - float(np.mean(signal))
    n = len(x)
    first = max(2, math.ceil(sr / fmax))
    last = min(math.floor(sr / fmin), n // 3)
    if last <= first or float(np.mean(x * x)) < 1e-12:
        return None
    size = 1 << (2 * n - 1).bit_length()
    fft = np.fft.rfft(x, n=size)
    autocorr = np.fft.irfft(fft * fft.conj(), n=size)[:last + 2]
    sums = np.concatenate(([0.0], np.cumsum(x * x)))
    lags = np.arange(last + 2)
    denom = sums[n - lags] + sums[n] - sums[lags]
    nsdf = np.divide(2 * autocorr, denom, out=np.zeros_like(autocorr), where=denom > 1e-20)
    peaks = [k for k in range(first, last + 1)
             if nsdf[k] > nsdf[k - 1] and nsdf[k] >= nsdf[k + 1]]
    if not peaks:
        return None
    best = max(float(nsdf[k]) for k in peaks)
    if best < 0.80:
        return None
    k = next(k for k in peaks if nsdf[k] >= max(0.80, best * 0.93))
    curvature = nsdf[k - 1] - 2 * nsdf[k] + nsdf[k + 1]
    offset = 0.5 * (nsdf[k - 1] - nsdf[k + 1]) / curvature if abs(curvature) > 1e-12 else 0.0
    freq = sr / (k + float(np.clip(offset, -0.5, 0.5)))
    midi_float = 69 + 12 * math.log2(freq / 440)
    midi = round(midi_float)
    names = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
    return {'frequency_hz': round(freq, 3), 'periodicity': round(min(float(nsdf[k]), 1.0), 4),
            'midi_nearest': midi, 'cents_from_note': round(100 * (midi_float - midi), 2),
            'note_scientific_C4_equals_60': names[midi % 12] + str(midi // 12 - 1),
            'note_ableton_C3_equals_60': names[midi % 12] + str(midi // 12 - 2)}


def analyze(path, start=0.0, duration=8.0, mono_note=False, fmin=30., fmax=2000.):
    if not all(math.isfinite(v) for v in [start, duration, fmin, fmax]):
        raise ValueError('Les paramètres numériques doivent être finis.')
    if start < 0 or not 0 < duration <= 60 or not 20 <= fmin < fmax <= 5000:
        raise ValueError('Début >= 0, durée comprise entre 0 et 60 s, 20 <= fmin < fmax <= 5000 Hz.')
    with sf.SoundFile(str(path)) as source:
        sr, channels, frames = source.samplerate, source.channels, len(source)
        if channels not in (1, 2) or not 8000 <= sr <= 192000:
            raise ValueError('Ce helper traite uniquement mono/stéréo, de 8 à 192 kHz ; préparer une copie adaptée.')
        if fmax >= sr / 2:
            raise ValueError('fmax doit être inférieur à la fréquence de Nyquist.')
        start_frame = round(start * sr)
        if start_frame >= frames:
            raise ValueError('Début hors du fichier ou fichier vide.')
        source.seek(start_frame)
        data = source.read(min(round(duration * sr), frames - start_frame), dtype='float64', always_2d=True)
        info = {'path': str(Path(path).resolve()), 'format': source.format, 'subtype': source.subtype,
                'sample_rate_hz': sr, 'channels': channels, 'duration_s': frames / sr}
    if len(data) < 2 or not np.isfinite(data).all():
        raise ValueError('Extrait trop court ou contenant des valeurs non finies.')
    warnings = ['Mesures descriptives, sans écoute. Aucune identification certaine du synthé, du preset ou de la chaîne.',
                'Crêtes d’échantillons uniquement : ni true peak, ni LUFS. Les chiffres portent sur l’extrait sélectionné.']
    levels = np.sqrt(np.mean(data * data, axis=0))
    selected = int(np.argmax(levels))
    x = data[:, selected]
    x_centered = x - np.mean(x)
    if start_frame != 0 or len(data) != frames:
        warnings.append('Analyse partielle du fichier ; sélectionner explicitement une note ou une zone représentative.')
    result = {'source': info,
              'excerpt': {'start_s': start_frame / sr, 'duration_s': len(data) / sr},
              'channels': [{'channel': i + 1, 'sample_peak_dbfs': db(float(np.max(np.abs(data[:, i])))),
                            'rms_dbfs': db(float(levels[i])), 'dc_offset': round(float(np.mean(data[:, i])), 8),
                            'samples_at_or_above_full_scale': int(np.sum(np.abs(data[:, i]) >= 1.0))}
                           for i in range(channels)],
              'analysis_channel': selected + 1,
              'analysis_channel_reason': 'Canal de RMS maximal ; évite une annulation lors de la sommation mono.',
              'warnings': warnings}
    if channels == 2:
        left, right = data[:, 0], data[:, 1]
        lz, rz = left - left.mean(), right - right.mean()
        den = float(np.linalg.norm(lz) * np.linalg.norm(rz))
        corr = float(np.dot(lz, rz)) / den if den > 1e-20 else None
        mid, side = (left + right) / 2, (left - right) / 2
        mr, ss = float(np.sqrt(np.mean(mid * mid))), float(np.sqrt(np.mean(side * side)))
        result['stereo'] = {'correlation': round(float(np.clip(corr, -1, 1)), 6) if corr is not None else None,
                            'mid_rms_dbfs': db(mr), 'side_rms_dbfs': db(ss),
                            'side_to_mid_db': db(ss / mr) if mr > 1e-12 and ss > 0 else None}
        if corr is not None and corr < 0:
            warnings.append('Corrélation globale négative : vérifier la perte en mono à l’écoute ; cela ne suffit pas à diagnostiquer le traitement utilisé.')
    block = max(1, round(sr * 0.01))
    envelope = []
    for pos in range(0, len(data), block):
        part = data[pos:pos + block]
        envelope.append({'time_relative_s': round(pos / sr, 5),
                         'rms_dbfs': db(float(np.sqrt(np.mean(part * part))))})
    result['envelope_10ms'] = envelope
    # Spectre de puissance moyen, fenêtres Hann. La moyenne n’identifie pas une architecture.
    fft_size = min(32768, max(1024, 1 << math.ceil(math.log2(sr * .085))))
    freqs = np.fft.rfftfreq(fft_size, 1 / sr)
    power_sum = np.zeros(len(freqs))
    window = np.hanning(fft_size)
    timeline = []
    hop = fft_size // 2
    positions = range(0, max(1, len(x) - fft_size + 1), hop)
    positions = list(positions)
    last = max(0, len(x) - fft_size)
    if positions[-1] != last:
        positions.append(last)
    for pos in positions:
        chunk = x_centered[pos:pos + fft_size]
        if len(chunk) < fft_size:
            padded = np.zeros(fft_size); padded[:len(chunk)] = chunk; chunk = padded
        spec = np.abs(np.fft.rfft(chunk * window)) ** 2
        power_sum += spec
        total = float(spec.sum())
        centroid = float(np.dot(freqs, spec) / total) if total > 1e-20 else None
        timeline.append({'time_relative_s': round(pos / sr, 5),
                         'power_centroid_hz': round(centroid, 3) if centroid is not None else None})
    total = float(power_sum.sum())
    result['spectrum'] = {'channel': selected + 1, 'fft_size': fft_size, 'window': 'Hann',
                          'bin_spacing_hz': sr / fft_size, 'centroid_weighting': 'power',
                          'centroid_hz': None, 'rolloff_95_hz': None, 'strongest_peaks': []}
    if total > 1e-20:
        norm = power_sum / total
        peaks = [i for i in range(1, len(norm) - 1) if norm[i] > norm[i - 1] and norm[i] >= norm[i + 1]]
        ordered = sorted(peaks, key=lambda i: norm[i], reverse=True)[:12]
        result['spectrum'].update(centroid_hz=round(float(np.dot(freqs, norm)), 3),
                                   rolloff_95_hz=float(freqs[min(int(np.searchsorted(np.cumsum(norm), .95)), len(freqs) - 1)]),
                                   strongest_peaks=[{'bin_frequency_hz': round(float(freqs[i]), 3),
                                                     'relative_power_db': round(10 * math.log10(float(norm[i] / norm.max())), 3)}
                                                    for i in ordered])
    result['spectral_timeline'] = timeline
    result['pitch_hints'] = []
    if mono_note:
        warnings.append('Hauteurs = hypothèses d’une note monophonique périodique, accordée à A=440 Hz. Erreurs d’octave possibles ; périodicité n’est pas une probabilité de justesse.')
        size = round(sr * .25)
        if len(x) < size:
            warnings.append('Extrait inférieur à 250 ms : estimation de hauteur non effectuée.')
        else:
            global_rms = float(np.sqrt(np.mean(x_centered * x_centered)))
            for pos in np.unique(np.linspace(0, len(x) - size, min(12, max(1, int(len(x) / size))), dtype=int)):
                chunk = x_centered[pos:pos + size]
                if float(np.sqrt(np.mean(chunk * chunk))) < max(1e-6, global_rms * .05):
                    continue
                hint = periodicity_hint(chunk, sr, fmin, fmax)
                if hint:
                    result['pitch_hints'].append({'time_relative_s': round(int(pos) / sr, 5), **hint})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('audio', type=Path)
    parser.add_argument('--start', type=float, default=0.0)
    parser.add_argument('--duration', type=float, default=8.0)
    parser.add_argument('--mono-note', action='store_true', help='Demander une estimation de hauteur sous hypothèse monophonique')
    parser.add_argument('--fmin', type=float, default=30.)
    parser.add_argument('--fmax', type=float, default=2000.)
    parser.add_argument('--output', type=Path, help='Nouveau rapport JSON ; aucun écrasement')
    args = parser.parse_args()
    if args.output and args.output.exists():
        parser.error('Le rapport existe déjà ; choisir un nouveau nom.')
    try:
        report = analyze(args.audio, args.start, args.duration, args.mono_note, args.fmin, args.fmax)
        text = json.dumps(report, ensure_ascii=False, allow_nan=False, indent=2)
        if args.output:
            with args.output.open('x', encoding='utf-8') as out:
                out.write(text + '\n')
            print(f'Rapport enregistré : {args.output}')
        else:
            print(text)
    except (ValueError, OSError, RuntimeError) as exc:
        parser.error(str(exc))

if __name__ == '__main__':
    main()
