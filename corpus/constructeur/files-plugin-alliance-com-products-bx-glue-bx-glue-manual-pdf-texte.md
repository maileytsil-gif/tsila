---
titre: "bx_glue Manual (texte du PDF, 16 pages)"
source: constructeur/files-plugin-alliance-com-products-bx-glue-bx-glue-manual-pdf.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: 
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---



<!-- page 1 -->

Bx_glue Manual

<!-- page 2 -->

Table of Contents
1. Welcome to bx_glue ...................................................................................................... 1
2. Key features ................................................................................................................ 2
3. Overview ..................................................................................................................... 3
4. Compressor section ...................................................................................................... 4
5. Tone section ................................................................................................................ 5
6. Levels section .............................................................................................................. 6
7. Sidechain section ......................................................................................................... 7
8. Emphasis section ......................................................................................................... 8
9. Stereo section .............................................................................................................. 9
10. Metering .................................................................................................................. 10
Level Metering ......................................................................................................... 10
Spectrum Analyzer .................................................................................................... 10
11. Top toolbar .............................................................................................................. 11
12. Bottom toolbar ......................................................................................................... 12
13. Signal flow ............................................................................................................... 13
14. Additional information ............................................................................................... 14
Modifier keys ........................................................................................................... 14
Online resources ....................................................................................................... 14
Credits .................................................................................................................... 14

<!-- page 3 -->

1. Welcome to bx_glue
Brainworx bx_glue is a versatile dual-band VCA bus compressor plugin. It combines the best of
analog heritage with modern features and tonal flexibility. bx_glue captures the legendary sound
of British bus compressors while incorporating Brainworx’s digital knowledge to deliver a glue
compression workhorse.
Use the plugin to glue together subgroups and stereo buses while maintaining snap and punch in
your sound. Glue compressors are defined by their ability to musically condense subgroups and
define their position in a mix. bx_glue's sophisticated controls make it a great fit for vocals, guitars,
bass, drums, and more.
Download and install your plugin using our Installation Manager: https://www.plugin-
alliance.com/en/installation-manager.html
Thank you for choosing bx_glue. We hope you enjoy it!
WELCOME TO BX_GLUE
1

<!-- page 4 -->

2. Key features
The following list gives you an overview of bx_glue's key features:
•
Ability to match and replicate almost any VCA compressor’s character up to a ratio of 10:1
•
Classic VCA compressor in a modern two-band matrix
•
Stereo compressor with a single set of controls
•
Sophisticated Tilt/Tub Emphasis for dynamic tonal balance
•
Band-Tilt instead of makeup gain to simplify tonal balance
•
Selection of two output transformer models by different manufacturers
•
Inaudible 12 dB/oct two-way crossover
•
Spectral analysis and precise metering
•
“Auto” output level option to easily listen to the compressor's effect at unity gain
•
Stereo Width and Mono Maker
•
Advanced Sidechain Option: Blend external and internal key sources
•
Mono- and Multitrack-Support
KEY FEATURES
2

<!-- page 5 -->

3. Overview
bx_glue consists of the following areas and main controls:
1.
Top Toolbar: Additional global controls relevant to the plugin's processing. For more
information, refer to Top Toolbar
2.
Meter Section: Visible feedback and metering to enhance productivity. For more information,
refer to Metering
3.
Main / Compressor Section : The main compression controls. For more information, refer to
Main / Compressor Section
4.
Tone Section: Unique Brainworx features enabling tonal control of the audio. For more
information, refer to Tone section.
5.
Levels Section: Input and output settings. For more information, refer to Levels section.
6.
Sidechain Section: Advanced sidechain controls enabling surgical compression. For more
information, refer to Sidechain section.
7.
Emphasis Section: Special controls enabling selective compression to low and high-frequency
content. For more information, refer to Emphasis section.
8.
Stereo Section: Controls for adjusting the stereo width of the audio. For more information,
refer to Stereo section.
9.
Bottom Toolbar: Preferences, license information, and documentation. For more information,
refer to Bottom Toolbar.
OVERVIEW
3

<!-- page 6 -->

4. Compressor section
The Compressor section gives access to the main controls of bx_glue. At its core, bx_glue is
a dual-band VCA compressor that uses a single set of parameters. It combines Brainworx’s
experience modeling classic analog audio hardware with modern controls. You can use bx_glue’s
multiband capabilities to compress low and high-frequency content independently, or set Band
Link to 100% to apply broadband compression. The Band Tilt parameter cuts or boosts each band
inversely, helping you to balance their levels post-compression.
This section consists of the following controls:
1.
Ratio: Determines the intensity of compression applied, from gentle (2:1) to heavy (10:1).
2.
Threshold: Sets the level at which gain reduction is applied.
3.
Crossover [Hz]: Sets the crossover frequency of the dual-band compressor, adjusting the
frequency ranges of each band to react independently. At 0%, each band is compressed
independently, while at 100%, gain reduction is applied equally across both bands.
4.
Band Link: Controls the degree to which gain reduction is linked between both frequency
bands.
5.
Band Tilt: Applies an inverse gain boost/attenuation to each band.
6.
Attack: Adjusts the time it takes for a full amount of compression to be applied once the
signal breaches the threshold level.
7.
Release: Adjusts the time it takes for gain reduction to back off a signal when it drops below
the threshold level.
8.
Auto [Release]: When Auto is selected, the release time depends on the duration of program
peaks.
9.
Mix %: Blends between the compressed and uncompressed signal.
COMPRESSOR SECTION
4

<!-- page 7 -->

5. Tone section
The Tone section allows you to recreate the character of almost any VCA compressor with a ratio
up to 10:1. The XL saturation knob applies light to heavy saturation to your tracks, while the total
harmonic distortion (THD) control lets you choose between a classic or dirty flavor. You also have
the option to activate a nickel or iron input transformer, leading to an open and airy (nickel) or gritty
and aggressive (iron) sound.
This section consists of the following controls:
1.
XL %: Determines the amount of XL Saturation blended into the signal.
2.
THD: The Total Harmonic Distortion (THD) created by the analog VCA model in bx_glue can
be toggled between two modes or switched off. In Classic mode, the exact amount of THD
generated in the analog circuit is added to the signal. Dirty mode hits the VCA’s ceiling harder
to add extra analog glue.
3.
Transformer: A selection of transformers is emulated with Brainworx’s exclusive physical
model of real-world transformers. It can be switched off to avoid magnetic saturation and loss
of transients when needed.
TONE SECTION
5

<!-- page 8 -->

6. Levels section
The Levels section offers input and output settings that you can use to manage the plug-ins signal
levels.
This section consists of the following controls:
1.
Input dB: Adjusts the input level of the processed audio signal.
2.
Headroom dB: Adjusts the volume before processing is applied and adds inverted gain to the
output signal. This feature lets you adjust the level of audio material to work with different
presets.
3.
Output dB: Adjusts the output level of the processed audio signal.
4.
Auto [Output]: Auto analyzes the input and output RMS levels and matches the output RMS
level to the input RMS level. This feature allows for accurate, level-matched A/B comparisons.
LEVELS SECTION
6

<!-- page 9 -->

7. Sidechain section
The Sidechain section consists of controls that let you to apply surgical compression by applying
filtering to the compressor's sidechain signal, or by using an external signal to control the
compression.
This section consists of the following controls:
1.
Listen: Solos the sidechain signal. Use this feature to hear how the filters (SC HPF and
Pre-Emphasis) affect your sidechain signal. You can also adjust the mix between the internal
and external sidechain signals.
2.
HPF Hz: Controls the cutoff frequency of the high-pass filter applied to the sidechain circuit.
3.
Ext.: Enables/disables the external sidechain input.
4.
Int. Gain: When Ext. is enabled, the internal sidechain input signal can be blended in. Int. Gain
controls the level of the internal sidechain input signal, causing bx_glue to respond to both the
external and internal signals.
SIDECHAIN SECTION
7

<!-- page 10 -->

8. Emphasis section
In the Emphasis section you can emphasize frequencies pre-compression while de-emphasizing
frequencies post-compression. Pre-emphasis causes bx_glue to compress the frequency range
you’ve targeted more aggressively, while de-emphasis rebalances the level offset. Use this feature
to tame harsh frequencies while minimally affecting the tonal balance of your subgroups and
stereo bus.
Simpified structure of emphasis in bx_glue
Here are some examples of how you can use emphasis in your productions:
•
Attenuating low frequencies, pre-compression, can reduce the amount of compression applied
to low-end content and help avoid low-frequency distortion.
•
Boosting high-frequency content on the way into the compressor can lead to heavier
compression and reduced top-end harshness.
•
Post-emphasis or de-emphasis is used to rebalance the signal while minimizing common
compression artifacts and is applied automatically.
This section consists of the following controls:
1.
Emphasis: Switches the pre- and de-emphasis filters on/off.
2.
Tilt / Tub: Toggles between a Tilt filter and a Tub filter. The Tilt filter inversely boosts/
attenuates low-end and top-end frequencies, while the Tub filter boosts/attenuates both low-
end and top-end frequencies.
3.
Emphasis dB: Controls the amount of gain applied to the emphasis filter.
4.
Frequency Hz: Adjusts the center frequency of the Tilt or Tub filter. For example, setting the
frequency base at 1kHz results in a low shelf at 100 Hz and a high shelf at 4 kHz. Setting is at
4 kHz results in a low shelf at 400 Hz and a high shelf at 8 khz.
EMPHASIS SECTION
8

<!-- page 11 -->

9. Stereo section
The Stereo section allows you to control the stereo width of your recordings.
This section consists of the following controls:
•
Mono Mkr. Hz: Sweepable from 20 to 666 Hz, this parameter folds the processed sound to
mono starting at the selected frequency.
•
Width: Decrease or increase the stereo width of the processed signal.
STEREO SECTION
9

<!-- page 12 -->

10. Metering
Level Metering
The level metering helps you visualize gain reduction, input levels, and output levels.
1.
Input [PPM]: A sample-peak meter that displays the level of the input signal.
2.
GR: The GR meter displays the overall gain reduction applied by bx_glue, excluding makeup
gain and mix controls.
3.
Output [PPM]: A sample-peak meter that displays the level of the output signal.
Spectrum Analyzer
The spectrum analyzer displays the frequency response of the input and output signals, enabing
you visualize compression effects across the frequency spectrum.
1.
TILT (Gray Readout): The amount of emphasis gain applied is displayed in the upper left and
right corners.
2.
Band-Reduction Readout [GR]: Each band's gain reduction is displayed within a red readout
flag with a hold of 2.0 seconds.
3.
[X-Over Handle]: Adjusts the crossover frequency of the low and high bands and is linked to
the  “Crossover” parameter.
4.
[Headphone Handle]: Solos a narrow band surrounding the crossover's center frequency
when dragged.
METERING
10

<!-- page 13 -->

11. Top toolbar
Additional global controls related to plugin settings and processing are available in the top toolbar.
1.
Power: Bypasses the processor when disengaged.
2.
UI Size: Sets the size of the plugin‘s user interface.
3.
↩ ↪: Undo and redo changes made to controls up to 32 steps.
4.
Bank A B C D: Each preset allows you to switch between four banks (A, B, C, D) of controls.
5.
Copy: Copy the active settings to memory.
6.
Paste: Paste the copied settings to the active bank.
7.
Reset: Reset the current bank.
8.
Ambience: Solos the difference between each band’s input and output to audit what the two
compressors are removing. Unique to  bx_glue, you’ll also hear the effects of Band-Link and
Emphasis applied to the summed ambiences.
9.
View Mode: Toggles between three view modes, with smaller UI views containing fewer
controls. This allows you to hide settings that you’re not using.
10. UI Color: Changes the primary color of controls and meter indicators.
Beneath the top toolbar you can find the Brainworx logo:
1.
Brainworx Logo: Clicking the Brainworx logo or the plugin's title will open a splash screen
containing team credits and allow you to set the default UI color.
TOP TOOLBAR
11

<!-- page 14 -->

12. Bottom toolbar
Preferences, license information, and documentation are available in the bottom toolbar.
1.
Plugin Alliance Logo: If your computer is online, clicking the Plugin Alliance logo will take you
to the Plugin Alliance website via your web browser.
2.
License Info: The toolbar displays information about the type of license you’re running. Trial
licenses are displayed along with the number of days until expiration; there is no note for full
licenses, as these are unlimited.
3.
Dollar Icon: If you are using a demo/trial version of a Brainworx product, you can click
this icon to open a browser that redirects you to the respective product page in the Plugin
Alliance store. Here, you can purchase a product without searching for it on the Plugin Alliance
website.
4.
Key Icon: Clicking on the key icon brings up the activation dialog, allowing you to manually
reauthorize a device in the event of a license upgrade or addition. You can also use this
feature to activate additional computers or USB flash drives.
5.
Help Icon: Clicking the help icon opens a context menu that links to the product manual PDF
and other helpful links, such as checking for product updates online. You must have a PDF
reader installed on your computer to read the manual.
BOTTOM TOOLBAR
12

<!-- page 15 -->

13. Signal flow
The internal signal flow of bx_glue is kept as linear as possible, with each parameter being audible
in almost any setting. However, some specific aspects of the plugin's behavior are useful to keep in
mind for best results.
The signal flow of bx_glue
Emphasis not only has an effect on the amount of compression in the divided bands. The Pre-
Emphasis EQ will also increase the amount of total harmonic distortion in the respective frequency
range. The effect will be audible after the signal passes the de-emphasis stage since it only
removes the tonal emphasis. Additional processing such as harmonics and saturation will also
have an effect on the sound.
Ambience bypasses the band link parameter. Combining tonal shaping while using ambience as a
creative tool can be achieved by using emphasis. Instead of tilting the make-up gains of each band,
emphasis settings will affect the amount of compression in each band by controlling the amount
of gain-reduction, resulting in tonal shaping.
Sidechain listen is a useful tool to audition the Pre-Emphasis EQ pre-compression. It solos and
sums both side-chain signals without passing the following stages and overrides Ambience when
activated.
SIGNAL FLOW
13

<!-- page 16 -->

14. Additional information
Modifier keys
You can use the following keyboard commands to control bx_glue.
Function
AU
VST / VST3
AAX
Fine Control
[shift]
[shift]
•
Mac: [command]
•
Win: [Ctrl]
Jump between default and
last setting
[option]
•
Mac: [command]
•
Win: [Ctrl]
•
Mac: [option]
•
Win: [Alt]
Output Link
[command]
•
Mac: [option]
•
Win: [Alt]
[shift]
Online resources
System requirements & supported platforms:
https://www.plugin-alliance.com/en/systemrequirements.html
Details about your product:
https://www.plugin-alliance.com/en/products/bx_glue.html
Installation, activation, authorisation and FAQ:
https://www.plugin-alliance.com/en/support.html
Credits
Programming and Algorithms: Yunus Proch
UI-Design: Nico Lezim
Product Management: Christoph Tkocz
ADDITIONAL INFORMATION
14