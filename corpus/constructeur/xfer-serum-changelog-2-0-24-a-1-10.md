---
titre: "Xfer Serum — changelog officiel 1.10 → 2.0.24 (copie 0xdevalias, extraction structurée)"
source: https://gist.github.com/0xdevalias/a537a59d1389d5aed3bc63b544c70c8d
recupere_le: 2026-09-24
mode: extraction
langue: en
axe: documentation constructeur ; Serum 2 ; versions
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Le gist (copie du changelog Xfer) n'est pas téléchargeable depuis ce conteneur (gist.githubusercontent.com bloqué) ; contenu obtenu par l'outil de lecture, version par version, chaque entrée paraphrasée brièvement en conservant les noms de fonctions et de paramètres. Pour le texte exact, relire l'URL.

## 2.0.24 (2025-11-13)
- Added VST3 Note ID ignore preference for host compatibility
- Added Pro Tools automatable parameter shortcuts
- Fixed data loss when opening newer version projects
- Fixed help tooltips appearing over Digital Performer window
- Fixed intermittent Digital Performer crashes
- Fixed loading ACIDized WAVs with empty slice chunks on Windows
- Fixed Macro automation in Bitwig Studio Clip Player
- Fixed MPE values persisting after voice stealing
- Fixed piano roll note preview velocity
- Fixed potential crash with invalid process function data
- Fixed preferences UI (broken since 2.0.22)
- Fixed Preset browser unexpectedly selecting after loading session
- Fixed Pro Tools hang at exit on Windows
- Fixed UI sizing in JUCE hosts with non-100% Windows Display Scaling

## 2.0.23 (2025-10-12)
- Added Cubase sustain pedal workaround preference
- Added "Re-import Serum 1 Data" preset browser action
- Added Alt-click exclusion for preset categories/tags
- Added custom preset category import from S1 database
- Fixed Serum 2 FX mono version crash with direct output routing
- Fixed crash resetting mod slot source via Ctrl/Cmd-click
- Fixed envelope sustain level in mono legato with zero release
- Fixed erratic drag export with non-100% UI/Display scaling
- Fixed root note detection for certain Acidized WAVs
- Fixed intermittent AU version crashes
- Fixed Ableton Live session loading crashes
- Fixed LFO sync after Note Latch in FX version
- Fixed multisample loop mode for samples with loop metadata
- Fixed Reverb reset on host transport stop
- Fixed Serum 2 FX default master volume (removed 1.37 dB boost)
- Fixed upside-down GUI in FL Studio 2025 Detached mode on Intel macOS 14 and earlier
- Fixed wavetable prev/next after saving custom table
- Improved GUI performance
- Improved preset ratings import from Serum 1

## 2.0.22 (2025-08-20)
- Added "Lock Module" options for envs, LFOs, note and velocity curves
- Added "Lock Voice Sequencer" option
- Added parameter grouping lock options (osc pitch, unison, porta, etc.)
- Added Preset Browser tag matching toggle (All or Any)
- Added value tooltip for Env Start & End levels
- Changed hybridize procedure for note/velocity curve locking
- Fixed Arp double note on restart under certain conditions
- Fixed Env graph background display
- Fixed modulation intermittently not taking effect
- Fixed preset menu not updating on macOS after save with symlink
- Fixed Logic automation workaround
- Improved Wine compatibility
- Improved piano roll auto-scrolling
- Re-worded audio processing disabled message
- Removed individual parameter locking for oscs (except coarse pitch, pan, level)

## 2.0.21 (2025-08-07)
- Added mono track support to Serum 2 FX AU
- Added Voice Steal Retrigger options to Envelope menu
- Added Live macro name correction workaround
- Added Logic automation data loading workaround
- Added WaveLab compatibility workaround
- Fixed preset browser crash during manual rescan
- Fixed crash importing wavetables exceeding 6996 samples per frame
- Fixed drag & drop preset loading with lowercased extensions
- Fixed excessive RAM with high-count multisamples
- Fixed FM (Noise) quality issue
- Fixed Frequency Response graph for FX on M/S splitter
- Fixed AM/FM/PD/RM warp sound at Ultra quality
- Fixed wavetable warp with S1 compatibility mode and PWM + FM/PD
- Fixed Conv reverb crash with FX additions/removals
- Fixed wavetable interpolation with FolderInfo.txt
- Fixed LFO point modulation loss when removing preceding point
- Fixed LFO point modulation in FX version
- Fixed Porta Scaling
- Fixed potential crash with certain matrix configurations
- Fixed preset pack build detuning at non-44100 sample rates
- Fixed presets sounding different after 2.0.17 envelope fix
- Fixed Serum 2 FX Noise Audio In pan issue
- Removed automatic old Renders deletion

## 2.0.20 (2025-06-24)
- Added warnings if Serum 2 Presets factory content missing
- Fixed S1 preset compatibility with Warp modulation
- Fixed crash closing preset browser while editing notes
- Fixed crash loading invalid MIDI map
- Fixed crash opening website in Check for Updates (Live on Windows)
- Fixed drag & drop preset loading on LFO graph
- Fixed embedded factory multisamples data removal on save
- Fixed envs stuck open if host stops during automation
- Fixed Logic high-precision parameter automation
- Fixed gain/reverse/trim in preset packs from embedded samples
- Fixed mislabeled Cancel button on dialogs
- Fixed Multisample/Sample/Wavetable menus after preset load
- Fixed note killing on transport stop without preference enabled
- Fixed preset modified indicator
- Fixed preset name validation via double-click
- Fixed macOS preset pack error for embedded multisamples
- Fixed Spectral Osc FFT buffer filling
- Improved error messaging for preset database issues
- Improved Windows build performance
- Removed Cubase sustain pedal workaround (fixed in 14.0.30)

## 2.0.19 (2025-05-21)
- Added new Spectral "Pitch Shift" warp mode (renamed old to "Pitch Blend")
- Added preset folder collapse/expand persistence
- Applied double-click reset to Envelope & LFO curves
- Fixed alt-drag from LFO to WT controls
- Fixed automatable params resetting after Pro Tools state load
- Fixed drag from LFO to noise menu/display
- Fixed Filter 2 On button display
- Fixed Granular/Sample/Spectral Osc playhead on loop direction change
- Fixed LFO modulation bus deletion
- Fixed LFO point multiselection via Ctrl/Cmd-drag
- Fixed LFO submenu display when selected
- Fixed LFOs behaving erratically after adding FX
- Fixed MIDI aftertouch/CC/pitch bend pass-through in AU
- Fixed MIDI output in AAX version
- Fixed Noise Osc "Audio Input" in FX version
- Fixed preset pack invalid filename handling
- Fixed Sample Osc clicks on loop direction change
- Fixed Spectral Osc xfade on loop direction change
- Fixed Unison Stereo Width modulation for S1 presets
- Improved FL Studio Serum 2 FX compatibility

## 2.0.18 (2025-04-26)
- Fixed "Revert to Saved" greyed out after session load
- Fixed Conv IRs sounding wrong after parameter adjustment
- Fixed Hybridize crash on some presets
- Fixed modulation inconsistency with per-voice/non-per-voice params
- Fixed Pitch Bend smoothing
- Fixed parameter automation recall offset (2.0.17 issue)

## 2.0.17 (2025-04-23)
- Added Key Track option to Filter/Distortion FX frequency menus
- Added Alt/Option + F keyboard shortcut for FX/Matrix toggle
- Added sample filename root note support with 'b' (flat)
- Added text input for Osc Mapping Editor
- Added warning about demo version plug-in state
- Added VST3 note ID workaround for Cubase/Nuendo Windows sustain pedal
- Added VST3 note ID workaround for Reason 12 and below
- Changed Ctrl/Cmd + F shortcut scope
- Changed loop crossfade auto-scaling
- Changed Porta Time readout precision
- Changed sustain pedal note re-trigger behavior
- Fixed Ableton Live automation stopping with FX additions
- Fixed Arp/Clip Player in negative bars
- Fixed Arp missing step on pattern trigger
- Fixed automatable params resetting on Pro Tools playback start
- Fixed sub osc phase modulation clamping
- Fixed clip playback start position with offset marker
- Fixed Conv reverb IR sizing with sample rate mismatch
- Fixed Osc Mapping Editor double-click crash
- Fixed Macro paste crash with deleted FX params
- Fixed preset preview crash
- Fixed sustain pedal mono crash
- Fixed WT Editor Interpolation tool crashes
- Fixed WT import Dynamic Pitch crash
- Fixed Distortion filter frequency adjustments
- Fixed excessive CPU with Conv Size modulation
- Fixed file drag & drop on high DPI scaling (multiple hosts)
- Fixed filter type locking with module locked
- Fixed FX racks delayed audio output
- Fixed global tuning display after preset load
- Fixed Hall reverb sweep on playback restart
- Fixed Arp Rate modulation with non-Pattern shapes
- Fixed Arp pattern editor note labeling
- Fixed Wavetables submenu item checking
- Fixed LFO value jump on voice deallocation with mono
- Fixed LFO phase advance with BPM anchoring
- Fixed S1 LFO .shp file loading
- Fixed S1 preset filter level modulation
- Fixed missing Granular Osc warp controls
- Fixed duplicate mod wheel automation parameter
- Fixed mod wheel smoothing
- Fixed modulation restoration on Undo Cut FX Bus
- Fixed MPE Y to Mod Wheel assignment
- Fixed MPE Y value offset
- Fixed noise draw in Wavetable Editor
- Fixed note expression smoothing
- Fixed note sticking with sustain pedal
- Fixed pitch bend Logic recording duplication
- Fixed pitch changes during loop crossfade
- Fixed Preset Database Missing/Corrupt error after folder relocation
- Fixed Preset Pack creation with text file wavetables
- Fixed osc warp rendering with sync mode
- Fixed env/LFO/noise retriggering with mono or poly count 1
- Fixed Sample Osc FFT buffer direction change
- Fixed chaos free rate modulation scaling from S1
- Fixed FX filter frequency modulation scaling from S1
- Fixed Serum 2 FX FL Studio custom User Data Folder
- Fixed Spectral Osc loop marker modulation
- Fixed unexpected FX bus send with modulated level below 0
- Fixed piano roll velocity marker updates
- Fixed wavetable loading from presets/sessions
- Fixed wavetable saving in hybridized presets
- Fixed WT Remap Warp drawing in slot 2
- Fixed WT Start Phases after Undo to Per Voice mode
- Improved FL Studio 25 Beta compatibility
- Improved Studio One compatibility
- Improved Conv reverb CPU usage
- Improved FX rack right-click menu usability
- SHA256: Multiple installer file hashes provided

## 2.0.16 (2025-03-17)
- Serum 2.0 Release for Windows and macOS
- What's New documentation included: Enhanced UI, Expanded Oscillators, New Oscillator Modes, Wavetable Enhancements, Sample Mode Highlights, Dual Expanded Filters, Improved Serum FX, New Enhanced FX, Signal Splitter Modules, Enhanced Modulation, Enhanced Modulation Matrix, New Serum Mixer, New Clip Sequencer, Advanced Arpeggiator, Enhanced Keyboard, Improved Presets Browser
- SHA256: Multiple installer file hashes provided

## 1.36b8 (October 11 2023)
- Added WT Editor formula rescan in "Rescan Folders on Disk"
- Added incoming MPE Pitch Bend routing to "MPE X" mod source (configurable)
- Added MPE state/tuning/oversample locks to Default preset persistence
- Added preference for MPE Y bi-directional movement
- Added improved preset saving without database rescan
- Fixed MIDI Program Change blank filename "file too small" messages
- Fixed potential first-run crash from very old version updates
- Fixed SerumFX Note Latch visual update on preset load

## 1.36b3 (February 15 2023)
- Added ARM Native support for AAX Apple Silicon (ProTools)
- Added WT Editor formula rescan in "Rescan Folders on Disk"
- Added AllNotesOff MIDI message handling improvements
- Added Clear FX Tails on transport stop without sharp click
- Added Program change improvements for VST3
- Fixed VST3 automation crash with UI closed
- Fixed WT overview redraw on macOS
- Fixed FX delay time typeable values with BPM enabled
- Fixed preset hybridize for some cases with knob/audio mismatch
- Fixed old preset filter type display in VST3
- Fixed missing wavetable search failure on Windows
- Fixed Cubase VST3 Bypass switch illumination
- Fixed Preset Browser delete feature

## 1.35b7 (November 3 2022)
- Added VST3 Version
- Added pixel dimensions to Zoom Menu items
- Added Drag export for chords
- Added Formula Parser rrnd command
- Fixed WT Editor memory corruption at extreme zoom
- Fixed MemTrig+Mono behavior from 1.351
- Fixed Shape saving from Xshaper menu
- Fixed modulation depth flickering
- Fixed preset change audio loss
- Fixed Render warp 3D waveform display
- Fixed tooltip offsets and macOS Ventura sizing
- Fixed LFO-to-WaveTable render with modulation points
- Fixed MPE pitch bend offset on note start

## 1.35b1 (April 1 2022)
- Fixed MemTrig (rand and phase at 100%) behavior
- Fixed LFO to Wavetable rendering with automation points
- Fixed SerumFX Audio In to Noise Oscillator polyphonic audio quality
- Fixed data corruption error protection for third-party presets
- Fixed WT Editor Bins zoom scaling
- Fixed "Send to noise oscillator" feature crash
- Fixed MIDI config rocker switch control
- Fixed DimExp clicks at 0% size with 48k sample rate
- Added performance improvements

## 1.35b0 (Dec 31 2021)
- Fixed low-level digital noise generation in 1.34b9

## 1.34b9 (Dec 29 2021)
- Added Matrix pulldown "Velo->Amp" quick link menu
- Fixed LFO graph curve point clicking after graph switching
- Fixed knob visual updates with modulation on same panel
- Accelerated wavetable/noise loading
- Fixed FX Delay time label at 0% value
- Fixed filter cutoff Hz entry with key track enabled
- Fixed WT editor thumbnail dragging
- Fixed MIDI CC assignment preset load issue

## 1.34b8 (Dec 16 2021)
- Added Matrix pulldown "Velo->Amp" menu
- Fixed LFO graph curve point clicking
- Fixed knob visual updates with panel modulation
- Accelerated wavetable/noise loading
- Fixed FX Delay time label display
- Fixed filter cutoff Hz with key track
- Fixed WT editor thumbnail dragging
- Fixed MIDI CC assignment loading
- Fixed WT editor vertical nudge mouse events

## 1.34b6 (Oct 29 2021)
- Added .tun tuning file support over 512 characters per line
- Added parameter automation on preset load preference
- Fixed SerumFX audio in to noise osc mono pass-through
- Fixed LFO rate display labels
- Fixed WT editor crash with single table alt-click minus
- Fixed LFO smoothing recall

## 1.34b5 (July 18 2021)
- Fixed Phaser FX clipped/silent signal on preset load
- Fixed .fxp drag and drop acceptance
- Fixed MIDI program changes functionality
- Fixed wavetable morph interpolation rendering on load

## 1.34b4 (June 21 2021)
- Added automatic preset browser ratings backup
- Fixed FX clipped/silent signal on preset load
- Fixed distortion graph saving on FX rack/single
- Fixed UTF8 tuning file support
- Fixed missing presets/ratings in browser
- Fixed "noise missing" false report on preset load

## 1.34b1 (May 7 2021)
- Fixed Render warp menu activation from 1.33b7-9
- Fixed LFO mod source drag interruption
- Fixed Windows AAX Alt key interception by ProTools

## 1.33b9 (May 1 2021)
- Fixed wavetable morph reload on preset load from 1.33b7-8

## 1.33b8 (April 29 2021)
- Fixed "Resample to Osc" crash from 1.336/7

## 1.33b7 (April 28 2021)
- Fixed Macro loading in all cases
- Fixed fast triplet LFO time labeling

## 1.33b6 (April 27 2021)
- Fixed MIDI CC mapping preset recall
- Fixed Macro automation from Serum manual loading
- Fixed filter initialization click in Hyper/Chorus
- Converted Serum.cfg to SerumPrefs.json format
- Added "Ask before preset change on edited presets" preference

## 1.33b4 (March 12 2021)
- Fixed default noise file silence on init
- Fixed bipolar modulator text control clipping display
- Fixed preference text font scaling
- Added overlapping LFO point selection on right edge

## 1.33b3 (March 6 2021)
- Fixed FX level trims functionality from 1.33b versions

## 1.33b2 (March 5 2021)
- Fixed crash from Default preset during DAW plugin scan
- Fixed macOS SerumFX version removal on 1.331 install
- Fixed non-retina display resizing corruption/crash

## 1.33b1 (March 4 2021)
- Added preset deletion without database rescan
- Fixed preset ratings/categories assignment on some systems

## 1.32b9 (March 2 2021)
- Fixed wavetables appearing as imported from menus

## 1.32b8 (March 1 2021)
- Fixed preset hybridize error messaging
- Fixed unnecessary database rescan on plugin start
- Fixed macOS Serum 1.322 update prevention

## 1.32b6 (February 26 2021)
- Fixed older versioned plugin updates on macOS

## 1.32b5 (February 25 2021)
- Improved directory scan times
- Improved graphics redraw
- Fixed Distortion Downsample sound difference in 1.32x

## 1.32b2 (February 4 2021)
- Fixed windowing issues (Cubase rare situations)
- Re-introduced macOS 10.9-10.11 legacy support
- Re-introduced ProTools 11-12.5 legacy support
- Fixed Delay effect time updates from 1.319-1.320

## 1.32b0 (January 30 2021)
- Fixed incorrect version display on first window open with zoom
- Added MIDI note name to drag-exported WAV filenames

## 1.31b9 (January 27 2021)
- Fixed macOS versioning showing 1.318 as older to OS

## 1.31b8 (January 27 2021)
- Fixed Apple security bug preventing macOS 10.9-10.11 loading

## 1.31b7 (January 23 2021)
- Fixed "WT to LFO" accidental activation from FX preset loading
- Fixed audio engine initialization crash causing garbled audio

## 1.31b6 (January 23 2021)
- Fixed display redraw delay with advance arrows

## 1.31b5 (January 22 2021)
- Synced incorrect version number

## 1.31b3 (January 18 2021)
- Added macOS ARM (M1) native support
- Added "Wavetable to LFO Shape" in LFO Shape load menu
- Added macOS 10.8-10.11 support variants
- Added unicode folder/filename support on Windows
- Fixed preset loading improvements
- Fixed graphics redraw improvements
- Fixed parameter mod depth halting Bitwig automation
- Fixed cc64 MIDI channel limitation
- Fixed foreign language character directory names

## 1.30b9 (November 11 2020)
- Added DSP phase state persistence for modulation effects
- Fixed AAX ProTools All Notes Off stuck note issue
- Fixed mod assignment to OSC coarse pitch above 16 assignments

## 1.30b8 (October 14 2020)
- Fixed dB display value crash

## 1.30b7 (August 21 2020)
- Fixed AudioUnit automation parameter reloading in Logic

## 1.30b6 (August 1 2020)
- Added SerumFX oscillator state persistence
- Added WT Editor Sort Random
- Added Envelope zoom lock persistence
- Added FX Level trim smoothing
- Fixed wavetable saving memory leak
- Fixed skin missing resources sizing
- Fixed FFT bar shift-click fine tuning
- Fixed wavetable import scaling
- Fixed Logic X song/preset reload issue

## 1.30b4 (June 7 2020)
- Fixed drag to matrix mod source audio disabling
- Fixed Cubase Media Bay XML drag import
- Fixed OSC A/B unison setting drag indicators
- Fixed legato portamento continuation when disabled
- Fixed LFO curve scaling at 100% negative
- Added Logic 24-bit WAV render export
- Added Logic Project folder drag-import support
- Added "Send to Noise Oscillator" in WT Editor
- Added LFO to noise osc drag for waveform render

## 1.30b3 (May 30 2020)
- Added Shift-drag preset .fxp export from logo
- Added preset name to WAV render export filename
- Added comma as decimal indicator for typeable values
- Added drag mod sources to matrix menus
- Added realtime FFT updates in WT Editor
- Fixed zoom scaling cosmetics
- Fixed DAW transport hang/crash from 1.301-1.302
- Fixed Preset Browser content filter clearing

## 1.30b2 (May 28 2020)
- Fixed Spectral blur in WT Editor Process
- Fixed LFO point modulation clearing
- Fixed Flip Horizontal point modulation offset
- Fixed LFO playback on DAW transport cycle
- Fixed skin Mix/Level switches
- Fixed pop-up menu crash with multiple LFO bus unassignment
- Fixed modulating LFO points crash
- Fixed .fxp visible in preset name after save
- Fixed negative value prevention on controls
- Fixed LFO sync on transport loopback/play start
- Fixed Spectral blur phases with adjacent frames
- Added Spectral blur adjacent frames in WT Editor
- Fixed mouseover help tooltip display

## 1.30b1 (May 25 2020)
- Fixed Limit Polyphony filter click on note steal
- Fixed SerumFX latching on stop
- Fixed help tooltips wrong information
- Fixed Flip Vertical LFO Bus assignment
- Fixed Remove Modulations context menu on Windows
- Fixed AAX Windows Alt key response
- Fixed X-Shaper/Remap graph curve drawing from 1.29b9
- Fixed LFO 5-8 rate adjustment with notes playing
- Updated Mix/Level artwork

## 1.29b9 (May 23 2020)
- Fixed FX level knobs typing entry percentage issue
- Fixed modulator drag to LFO graph flickering
- Fixed drag to exact LFO point assignment
- Fixed negative LFO rate Hz entry acceptance
- Fixed preset browser filter/search row selection
- Fixed modulated icon greying on numeric controls
- Added LFO drag to point improvements
- Added LFO point bus removal check
- Fixed compressor circuit preset load memory leak
- Fixed "(no category)" preset browser filter display
- Fixed single LFO curve right-click assignment on Windows
- Added SerumFX oscillator state song reload

## 1.29b8 (May 20 2020)
- Fixed blank Preset Browser in some situations
- Fixed alt-drag LFO to wavetable

## 1.29b7 (May 18 2020)
- Added LFO Point modulation via right-click
- Added drag-export last played note as WAV file
- Added high-resolution skin bitmap resampling on Windows
- Added LFO Rise/Delay automation parameters
- Added FX Level Trim controls
- Added velocity to onscreen piano keyboard clicking
- Added "init all LFOs" to main menu
- Fixed tooltip overlap at 110% zoom
- Fixed distortion Q negative value crash
- Fixed browser nested folder support
- Fixed polyphony limit held note priority
- Fixed excessive LFO point generation on drag

## 1.28b6 (Jan 22 2020)
- Fixed AAX deactivated track/instance setting restoration
- Fixed LFO point stream generation on shift-click drag
- Fixed alt-drag LFO to wavetable
- Fixed WT Editor drawing update

## 1.28b5 (Jan 17 2020)
- Fixed piano key visibility preset menu response
- Fixed SerumFX "Audio In" error/no pass-through

## 1.28b4 (Jan 9 2020)
- Fixed Copy Osc interpolated table preservation
- Fixed Windows version numbering display
- Added automatic authorization for secondary accounts

## 1.28b2 (Dec 26 2019)
- Fixed UI resize crash during playback

## 1.28b1 (Dec 24 2019)
- Fixed FFT editing/WT-to-FFT audio playback halt from 1.27b7

## 1.27b9 (Dec 23 2019)
- Fixed WT Editor wave drawing processing

## 1.27b8 (Dec 21 2019)
- Fixed Windows drag resize crash from 1.27b7

## 1.27b7 (Dec 20 2019)
- Added Stomp Box and Tape Sat distortion types
- Fixed short noise samples memory issue
- Fixed window resize crash on macOS
- Fixed switch control window redraw
- Fixed mono legato FM depth clicks
- Improved preset changing

## 1.27b6 (Dec 14 2019)
- Added preliminary spectrum view on filter click
- Added Check for Updates to Menu
- Added embedded tuning files without names display as (special)
- Fixed DSP noise osc high pitch issue
- Fixed chaos osc invalid output
- Fixed parameter display cosmetics
- Improved UI redraw performance
- Fixed SerumAAX Windows backup/file saving crash
- Fixed custom font loading on all systems
- Fixed "(none)" named tuning file loading in presets
- Fixed MW->WT Pos modulation on WT Editor open
- Fixed compressor crossover filter stability

## 1.27b1 (July 28 2019)
- Fixed noise pitch at maximum with high notes range
- Fixed S&H on chaos osc state issue
- Fixed portamento "Always" mode first note
- Fixed short looping samples high pitch issue

## 1.26b9 (July 24 2019)
- Fixed UTF-8 foreign language Serum Presets directory
- Fixed font blurriness on menu titles

## 1.26b8 (July 15 2019)
- Fixed MPE Bend range MIDI message GUI crash
- Fixed Prune Database feature from 1.26b4

## 1.26b7 (July 12 2019)
- Fixed preset browser access violation during rebuild

## 1.26b6 (July 11 2019)
- Fixed preset browser scan memory leak
- Fixed SerumFX audio clipping above 0 dB
- Fixed folder name apostrophe support

## 1.26b5 (July 10 2019)
- Fixed preset save browser instability from 1.26b4
- Changed macOS skin bitmap loading

## 1.26b4 (July 9 2019)
- Rewrote preset database scanning/thread handling from 1.257-1.26b3

## 1.26b2/3 (July 5 2019)
- Fixed potential preset load crashes from 1.25b9 changes

## 1.26b0/1 (July 3 2019)
- Added potential crash fix
- Fixed Windows folder sorting from 1.257

## 1.25b7/8/9 (July 2 2019)
- Added potential crash fixes
- Improved preset changing

## 1.25b6 (July 1 2019)
- Improved preset changing
- Fixed preset database rescanning
- Fixed custom font memory leaks
- Fixed polyphony voice stealing from held notes
- Added "Prune Duplicates and Missing Presets" browser menu

## 1.25b5 (June 29 2019)
- Fixed preset database rescanning on window open
- Fixed custom font memory leaks
- Fixed polyphony voice stealing from held notes
- Fixed Windows 10 portamento/matrix curve redraw
- Added "Prune Duplicates and Missing Presets" feature

## 1.25b4b (June 22 2019)
- Fixed very old MacOS compatibility

## 1.25b4 (June 21 2019)
- Fixed potential crash with MPE Sysex messages when UI closed

## 1.25b3d (June 3 2019)
- Fixed VST version compatibility for older processors

## 1.25b2 (May 27 2019)
- Fixed note offs on MIDI channels > 1 with Mono enabled

## 1.25b1 (May 27 2019)
- Faster preset database scanning
- Fixed GUI open thread sync issue from 1.24x
- Fixed crash with config MIDI CC/note when UI closed
- Fixed compressor first peak catching
- Fixed MPE channel 16 expression response
- Fixed MPE discrete note off handling per-channel

## 1.24b9e (May 15 2019)
- Fixed FX modules Dry level amount quietness

## 1.24b8 (April 19 2019)
- Fixed French filter from 1.24x builds

## 1.24b5-6-7 (March 29 2019)
- Updated Delay filter to improved/updated filter (matching EQ)

## 1.24b4 (March 28 2019)
- Fixed Noise menu checkmarks in sub-sub folders
- Fixed macOS older processor/macOS init crash

## 1.24b3 (March 27 2019)
- Improved EQ and Hall reverb filters
- Fixed Macro4 FX crackle in 1.24b2
- Added preset ratings preservation through database rebuild

## 1.24b2 (March 21 2019)
- Fixed MIDI Program Change multiple trigger
- Fixed Windows Serum Presets folder missing prompt
- Fixed MPE->Macros incorrect depth with multiple destinations
- Fixed wavetable text file interpolation recognition

## 1.24b1 (March 18 2019)
- Fixed Matrix curve value tips display
- Fixed Windows non-English username support
- Fixed "noises missing" message path display
- Fixed macOS SerumFX AU aval on older Macs
- Fixed alt-drag mini halo mousing
- Fixed WT Editor grid size highlight with zero grid
- Fixed WT Editor multiselection zoom traces
- Fixed MPE disabled by default

## 1.23b9 (March 14 2019)
- Fixed control non-response when value tips disabled
- Fixed WT Editor scrollbar visibility
- Fixed formula parser NaN handling
- Added WT Editor zoom size persistence

## 1.23b8 (March 12 2019)
- Fixed multiple instances memory issue
- Fixed Multiband Comp warmup time on first playback

## 1.23b7 (March 9 2019)
- Fixed SN# entry requiring Return in some DAWs
- Fixed WT Editor formula NaN value handling

## 1.23b5 (March 8 2019)
- Fixed multiple MIDI sysex events buffer crash
- Fixed clicks with Mono and overlapping notes

## 1.23b3 (March 6 2019)
- Fixed SN# acceptance without Return
- Fixed Maschine plugin window size storage
- Fixed oversampling default config loading

## 1.23b2 (Mar 6 2019)
- Added default oversampling level in Serum.cfg
- Added WT Editor Reduce submenu for frame thinning
- Added separate LFO vertical grid size text entry
- Added preset browser secondary sort method
- Added alt-drag LFO to WT official support/Windows
- Added preset name rescan on Serum instance opening
- Added resizable interface (lower-right corner)
- Added zoom menu in top-left with default size preference
- Added Oversampling lock enable with non-2x config
- Added "Export All as Single-Cycle Waves" to WT export
- Added skin support with zoom menu selection
- Added custom TTF font support for skins
- Added Scream Filter, Dist.Comb 1 and 2 filter types
- Improved Ringmod Filter warm-up time
- Added Ringmod/S&H custom filter display
- Added preliminary MPE support
- Added Preset Hybridize feature
- Added Promethium Skin by Lance Thackeray
- Added automation smoothing rate preference
- Added custom user category in preset browser
- Added WT Editor FFT bins quarter snap to right-click
- Added "Scale Freq Values by Bin Index" to right-click
- Added unison phase memory trigger (MemTrig) at 100% Rand/Phase
- Added WT Editor Process "Set Spectra same for all Frames"
- Added "Set Phases same for all Frames"
- Added "Subtract Spectra from other Osc"
- Added Retina/HiDPI support with skin scaling
- Added noise osc direct out switch
- Added default preset loading from User/default.fxp
- Added Matrix quick vibrato assignment menu
- Reduced CPU when modulating WT Pos significantly

## 1.11b3 (Aug 10 2016)
- Fixed Splice lease user issue
- Fixed noise oscillator loop click

## 1.11b2 (Aug 8 2016)
- Fixed preset browser arrow key functionality
- Fixed "render osc warp" 3D display update
- Fixed Splice lease compatibility

## 1.10b9b (Aug 1 2016)
- Fixed incorrect tuning on old preset load (A=430)
- Fixed Reverb parameter label display

## 1.10b8 (July 30 2016)
- Fixed presets > 4 MB size loading
- Fixed Env3 AHDSR mod source drag tooltip
- Added Multiband Compressor individual band threshold control
- Added Compressor mix control
- Added FX Filter "pan" (cutoff offset) knob
- Added stereo WAV to OSC B right channel import
- Added "Resample to A+B (Stereo)" in main menu

## 1.10b7 (Jun 30 2016)
- Added polyphony count lock option
- Fixed oversampling lock visual update on preset load
- Fixed noise sample loop point mangling
- Fixed AAX ProTools 12 first run
- Fixed potential project close crash

## 1.10b6 (Jun 19 2016)
- Fixed byte alignment incompatibility between 32/64-bit presets
- Fixed alt-drag LFO 5-8 copy
- Fixed LFO 5-8 free rate Hz display

## 1.10b5f (Jun 17 2016)
- Fixed ProTools AAX plugin detection and bypass
- Fixed Noise folder navigation buttons
- Fixed modulator tile drawing

## 1.10b5 (Jun 16 2016)
- Added 8 LFOs (hidden until LFO4 use)
- Added Noise drag and drop with preset/song embedding
- Added noise pitch track fine tune skip
- Added alt-click MOD matrix toggle (normal/active modulation)

*(Extraction interrompue à la version 1.10b5 ; les versions antérieures, 1.10b3 à 1.07b4, existent dans le gist d'origine avec peu de détail.)*
