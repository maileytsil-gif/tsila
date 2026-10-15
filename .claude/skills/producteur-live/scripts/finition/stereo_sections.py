"""Largeur stéréo par bande et par section d'un export WAV (16 bits PCM ; convertir avant : afconvert -f WAVE -d LEI16@44100 in.wav out.wav).
Usage : python3 stereo_sections.py master16.wav BPM "INTRO:1-17,GROOVE:17-33,..."   (mesures, fin exclue ; 4/4)
Sortie : corr (1,00 = mono, 0 = décorrélé, <0 = opposition de phase) / S−M dB (côtés moins milieu) pour 20-120, 120-300, 300-1k, 1-3k, 3-8k, 8-16k Hz.
Lecture : grave < 120 Hz doit rester ≈ 1,00 ; aigus 8-16k ≈ 0,4–0,7 = large ; > 0,85 = étroit ; < 0,2 = risque en mono."""
import wave,numpy as np,sys
f=wave.open(sys.argv[1]);sr=f.getframerate();x=np.frombuffer(f.readframes(f.getnframes()),dtype=np.int16).reshape(-1,2).astype(float)
bpm=float(sys.argv[2]);spb=4*60/bpm
secs=[(s.split(':')[0],*map(float,s.split(':')[1].split('-'))) for s in sys.argv[3].split(',')]
bands=[(20,120),(120,300),(300,1000),(1000,3000),(3000,8000),(8000,16000)]
print('section     '+'  '.join(f'{a}-{b}'.rjust(11) for a,b in bands))
N=1<<15;fr=np.fft.rfftfreq(N,1/sr)
for n,a,b in secs:
    l=x[int((a-1)*spb*sr):int((b-1)*spb*sr),0];r=x[int((a-1)*spb*sr):int((b-1)*spb*sr),1];acc={bd:np.zeros(4) for bd in bands}
    for i in range(0,len(l)-N,N):
        Fl=np.fft.rfft(l[i:i+N]*np.hanning(N));Fr=np.fft.rfft(r[i:i+N]*np.hanning(N))
        for bd in bands:
            m=(fr>=bd[0])&(fr<bd[1]);acc[bd]+=[np.sum(abs(Fl[m]+Fr[m])**2/4),np.sum(abs(Fl[m]-Fr[m])**2/4),np.real(np.sum(Fl[m]*np.conj(Fr[m]))),np.sqrt(np.sum(abs(Fl[m])**2)*np.sum(abs(Fr[m])**2))]
    print(n[:11].ljust(11),'  '.join(f'{c/(k+1e-20):+.2f}/{10*np.log10(s/(m_+1e-20)+1e-12):5.1f}'.rjust(11) for m_,s,c,k in (acc[bd] for bd in bands)))
