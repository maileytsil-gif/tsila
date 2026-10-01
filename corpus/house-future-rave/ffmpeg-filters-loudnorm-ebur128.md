---
titre: "FFmpeg doc/filters.texi — filtres loudnorm (normalisation EBU R128 : I, LRA, TP) et ebur128 (mesure LUFS M/S/I, LRA, sample peak, true peak)"
source: https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/doc/filters.texi
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: mixage et mastering (future rave, bass house, house)
skills: house-future-rave-bass-house-production
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Extrait de `doc/filters.texi` du dépôt FFmpeg (format Texinfo conservé) : sections `loudnorm` (normalisation EBU R128, cibles I/LRA/TP) et `ebur128` (analyse M/S/I/LRA, sample peak et true peak). Commande d'analyse : `ffmpeg -nostats -i input.wav -filter_complex ebur128=peak=true -f null -`.

## loudnorm

@section loudnorm

EBU R128 loudness normalization. Includes both dynamic and linear normalization modes.
Support for both single pass (livestreams, files) and double pass (files) modes.
This algorithm can target IL, LRA, and maximum true peak. In dynamic mode, to accurately
detect true peaks, the audio stream will be upsampled to 192 kHz.
Use the @code{-ar} option or @code{aresample} filter to explicitly set an output sample rate.

The filter accepts the following options:

@table @option
@item I, i
Set integrated loudness target.
Range is -70.0 - -5.0. Default value is -24.0.

@item LRA, lra
Set loudness range target.
Range is 1.0 - 50.0. Default value is 7.0.

@item TP, tp
Set maximum true peak.
Range is -9.0 - +0.0. Default value is -2.0.

@item measured_I, measured_i
Measured IL of input file.
Range is -99.0 - +0.0.

@item measured_LRA, measured_lra
Measured LRA of input file.
Range is  0.0 - 99.0.

@item measured_TP, measured_tp
Measured true peak of input file.
Range is  -99.0 - +99.0.

@item measured_thresh
Measured threshold of input file.
Range is -99.0 - +0.0.

@item offset
Set offset gain. Gain is applied before the true-peak limiter.
Range is  -99.0 - +99.0. Default is +0.0.

@item linear
Normalize by linearly scaling the source audio.
@code{measured_I}, @code{measured_LRA}, @code{measured_TP},
and @code{measured_thresh} must all be specified. Target LRA shouldn't
be lower than source LRA and the change in integrated loudness shouldn't
result in a true peak which exceeds the target TP. If any of these
conditions aren't met, normalization mode will revert to @var{dynamic}.
Options are @code{true} or @code{false}. Default is @code{true}.

@item dual_mono
Treat mono input files as "dual-mono". If a mono file is intended for playback
on a stereo system, its EBU R128 measurement will be perceptually incorrect.
If set to @code{true}, this option will compensate for this effect.
Multi-channel input files are not affected by this option.
Options are true or false. Default is false.

@item print_format
Set print format for stats. Options are summary, json, or none.
Default value is none.

@item stats_file
Write stats to specified file. Format is controlled by @option{print_format},
which must be set. Specify @code{-} to write to standard output.
Default is unset.
@end table



## ebur128

@section ebur128

EBU R128 scanner filter. This filter takes an audio stream and analyzes its loudness
level. By default, it logs a message at a frequency of 10Hz with the
Momentary loudness (identified by @code{M}), Short-term loudness (@code{S}),
Integrated loudness (@code{I}) and Loudness Range (@code{LRA}).

The filter can only analyze streams which have
sample format is double-precision floating point. The input stream will be converted to
this specification, if needed. Users may need to insert aformat and/or aresample filters
after this filter to obtain the original parameters.

The filter also has a video output (see the @var{video} option) with a real
time graph to observe the loudness evolution. The graphic contains the logged
message mentioned above, so it is not printed anymore when this option is set,
unless the verbose logging is set. The main graphing area contains the
short-term loudness (3 seconds of analysis), and the gauge on the right is for
the momentary loudness (400 milliseconds), but can optionally be configured
to instead display short-term loudness (see @var{gauge}).

The green area marks a  +/- 1LU target range around the target loudness
(-23LUFS by default, unless modified through @var{target}).

More information about the Loudness Recommendation EBU R128 on
@url{http://tech.ebu.ch/loudness}.

The filter accepts the following options:

@table @option

@item video
Activate the video output. The audio stream is passed unchanged whether this
option is set or no. The video stream will be the first output stream if
activated. Default is @code{0}.

@item size
Set the video size. This option is for video only. For the syntax of this
option, check the
@ref{video size syntax,,"Video size" section in the ffmpeg-utils manual,ffmpeg-utils}.
Default and minimum resolution is @code{640x480}.

@item meter
Set the EBU scale meter. Default is @code{9}. Common values are @code{9} and
@code{18}, respectively for EBU scale meter +9 and EBU scale meter +18. Any
other integer value between this range is allowed.

@item metadata
Set metadata injection. If set to @code{1}, the audio input will be segmented
into 100ms output frames, each of them containing various loudness information
in metadata.  All the metadata keys are prefixed with @code{lavfi.r128.}.

Default is @code{0}.

@item framelog
Force the frame logging level.

Available values are:
@table @samp
@item quiet
logging disabled
@item info
information logging level
@item verbose
verbose logging level
@end table

By default, the logging level is set to @var{info}. If the @option{video} or
the @option{metadata} options are set, it switches to @var{verbose}.

@item peak
Set peak mode(s).

Available modes can be cumulated (the option is a @code{flag} type). Possible
values are:
@table @samp
@item none
Disable any peak mode (default).
@item sample
Enable sample-peak mode.

Simple peak mode looking for the higher sample value. It logs a message
for sample-peak (identified by @code{SPK}).
@item true
Enable true-peak mode.

If enabled, the peak lookup is done on an over-sampled version of the input
stream for better peak accuracy. It logs a message for true-peak.
(identified by @code{TPK}) and true-peak per frame (identified by @code{FTPK}).
This mode requires a build with @code{libswresample}.
@end table

@item dualmono
Treat mono input files as "dual mono". If a mono file is intended for playback
on a stereo system, its EBU R128 measurement will be perceptually incorrect.
If set to @code{true}, this option will compensate for this effect.
Multi-channel input files are not affected by this option.

@item panlaw
Set a specific pan law to be used for the measurement of dual mono files.
This parameter is optional, and has a default value of -3.01dB.

@item target
Set a specific target level (in LUFS) used as relative zero in the visualization.
This parameter is optional and has a default value of -23LUFS as specified
by EBU R128. However, material published online may prefer a level of -16LUFS
(e.g. for use with podcasts or video platforms).

@item gauge
Set the value displayed by the gauge. Valid values are @code{momentary} and s
@code{shortterm}. By default the momentary value will be used, but in certain
scenarios it may be more useful to observe the short term value instead (e.g.
live mixing).

@item scale
Sets the display scale for the loudness. Valid parameters are @code{absolute}
(in LUFS) or @code{relative} (LU) relative to the target. This only affects the
video output, not the summary or continuous log output.

@item integrated
Read-only exported value for measured integrated loudness, in LUFS.

@item range
Read-only exported value for measured loudness range, in LU.

@item lra_low
Read-only exported value for measured LRA low, in LUFS.

@item lra_high
Read-only exported value for measured LRA high, in LUFS.

@item sample_peak
Read-only exported value for measured sample peak, in dBFS.

@item true_peak
Read-only exported value for measured true peak, in dBFS.
@end table

@subsection Examples

@itemize
@item
Real-time graph using @command{ffplay}, with a EBU scale meter +18:
@example
ffplay -f lavfi -i "amovie=input.mp3,ebur128=video=1:meter=18 [out0][out1]"
@end example

@item
Run an analysis with @command{ffmpeg}:
@example
ffmpeg -nostats -i input.mp3 -filter_complex ebur128 -f null -
@end example
@end itemize

