---
titre: "FabFilter — aide Pro-Q 4 : Spectral Dynamics"
source: https://www.fabfilter.com/help/pro-q/using/spectral-dynamics
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: documentation constructeur
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

FabFilter Pro-Q 4 Help - Spectral Dynamics 

 All help files 

### Table of contents

 Go to section 

 About FabFilter Pro-Q 4 
 Quick start 

 Overview 
 Knobs 
 Display and workflow 
 EQ Sketch 
 Band controls 
 Dynamic EQ 
 Spectral dynamics 
 Instance list 
 Solo 
 Full Screen mode, resizing and scaling 
 Piano display 
 Stereo options 
 Surround and Dolby Atmos 
 Processing mode 
 Character mode 
 Spectrum analyzer 
 EQ Match 
 Spectrum Grab 
 Output options 
 MIDI learn 
 Undo, redo, A/B switch 
 Using on iOS 

 Loading presets 
 Saving presets 
 How presets are
 stored 

 Purchasing FabFilter Pro-Q 4 
 Entering your license key 

 Support 
 Upgrading to Pro-Q 4 
 Manual
 installation 
 VST plug-in versions 
 External side
 chaining 
 License agreement 
 Acknowledgements 
 About FabFilter 

 FabFilter Pro-Q 4 Help 

## Introduction

 About FabFilter Pro-Q 4 

 Quick start 

## Using FabFilter Pro-Q 4

 Overview 

 Knobs 

 Display and workflow 

 EQ Sketch 

 Band controls 

 Dynamic EQ 

 Spectral dynamics 

 Instance list 

 Solo 

 Full Screen mode, resizing and scaling 

 Piano display 

 Stereo options 

 Surround and Dolby Atmos 

 Processing mode 

 Character mode 

 Spectrum analyzer 

 EQ Match 

 Spectrum Grab 

 Output options 

 MIDI learn 

 Undo, redo, A/B switch 

 Using on iOS 

## Presets

 Loading presets 

 Saving presets 

 How presets are
 stored 

## Purchasing FabFilter Pro-Q 4

 Purchasing FabFilter Pro-Q 4 

 Entering your license key 

## Support

 Support 

 Upgrading to Pro-Q 4 

 Manual
 installation 

 VST plug-in versions 

 External side
 chaining 

 License agreement 

 Acknowledgements 

 About FabFilter 

# Spectral dynamics

 Pro-Q 4 introduces a new variation on dynamic EQ: Spectral dynamics. With traditional
 dynamic EQ, the gain of an EQ band depends on the level of the input signal. In Spectral
 mode, Pro-Q 4 doesn't change the gain of the whole band, but triggers on specific frequencies
 within that band when it exceeds the threshold, leaving other frequencies untouched.

 Spectral
 dynamic processing is a great way of treating varying problem frequencies in a much more
 subtle manner compared to using traditional dynamic EQing. Typically, you would need a
 separate, dedicated and often complex plug-in for this type of
 processing, but Pro-Q 4 makes the process simple to use and easy to understand, as a
 logical extension of normal dynamic processing.

 You can enable Spectral dynamics by adding a shelving- or bell curve, choosing a
 dynamic range, and then clicking the Spectral icon right at the top of the gain /
 dynamic range knobs.

 You can also create Spectral bands directly in the EQ display 
 via Alt + Shift +click. Otherwise, you can also make a band Spectral by right+clicking
 the curve dot and choosing Make Spectral from the curve menu.

 By default, in Auto mode , the threshold, attack and
 release are set automatically, depending on the incoming audio, but by clicking the expand >> button, you
 can adjust these manually as desired, just as with normal dynamic EQ.

 In Spectral mode, the expanded dynamics section will show a Spectral Density slider. This
 sets how selective the spectral processing is. At lower values, the ranges that are triggered
 for frequencies will be relatively wide, while the areas will be very narrow and specific for higher
 density values.

 The Spectral Tilt button at the right top of the expanded dynamics section sets whether a tilt of 3 dB/oct is applied to the input spectrum before it is used to trigger the spectral dynamics
 processing. This is on by default for new spectral bands. By applying this gentle tilt to the spectrum, higher frequencies will trigger slightly more than lower frequencies. This helps to get more natural sounding results, especially when working on complex, wide-range audio such as a complete mix where the frequency spectrum often matches a pink noise response.

 Spectral EQing requires linear phase processing. Enabling spectral mode on a specific EQ
 band will cause that band to use linear phase processing , while the others will still be processed using
 the current processing mode as set in the bottom bar.

 If you have set any of the bands to use Spectral dynamics, the Processing Resolution 
 control will appear in the bottom bar, also showing a spectral icon if the plug-in is currently set to one of
 the non-linear phase modes. This controls the resolution of 
 linear phase processing of the spectral bands. The best resolution to choose depends
 on the audio you are working with; if you are treating high frequencies only, the Low or
 Medium resolution settings will probably work just fine. The latency introduced by linear phase processing depends on the chosen resolution.

## Tips

 Spectral dynamics is a great way to treat harshness and problem frequencies in
 guitar or vocal recordings.

 The Very High and Maximum linear phase processing resolutions aren't available for
 spectral or dynamic EQ.

 Most of the time, Low or Medium processing resolution settings are perfect for Spectral
 processing, especially when you're treating higher frequencies above 1000 Hz.

 Just like with normal Dynamic EQ, you can use the external side chain of the plug-in
 for triggering instead of the normal input of the plug-in.

 Next: Instance list 

 See Also 

 Overview 

### Table of contents

 Go to section 

 About FabFilter Pro-Q 4 
 Quick start 

 Overview 
 Knobs 
 Display and workflow 
 EQ Sketch 
 Band controls 
 Dynamic EQ 
 Spectral dynamics 
 Instance list 
 Solo 
 Full Screen mode, resizing and scaling 
 Piano display 
 Stereo options 
 Surround and Dolby Atmos 
 Processing mode 
 Character mode 
 Spectrum analyzer 
 EQ Match 
 Spectrum Grab 
 Output options 
 MIDI learn 
 Undo, redo, A/B switch 
 Using on iOS 

 Loading presets 
 Saving presets 
 How presets are
 stored 

 Purchasing FabFilter Pro-Q 4 
 Entering your license key 

 Support 
 Upgrading to Pro-Q 4 
 Manual
 installation 
 VST plug-in versions 
 External side
 chaining 
 License agreement 
 Acknowledgements 
 About FabFilter