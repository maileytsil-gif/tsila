---
titre: "Dexed — site du synthé DX7 logiciel"
source: https://asb2m10.github.io/dexed/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: synth brass vintage et cuivres FM
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Dexed 

# 
 dexed - FM Plugin Synth

 Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7 . Dexed is also a midi cartridge librarian/manager for the DX7.

 Minimal documentation is available on Dexed Wiki .

 Examples from One Synth Challenge :

 Dexed is free software and is licensed on the GPL v3.

## 
 Features

 Multi platform (OS X, Windows or Linux) and multi format (VST, AU, LV2)

 The sound engine music-synthesizer-for-android is closely modeled on the original DX7 characteristics

 144 DAW automatable DX7 parameters available from one single panel

 Fully supports DX7 input and output Sysex messages; including controller change. This means that you can use this with a native DX7/TX7 as a patch editor and sysex manager

 Each operator have a realtime VU meter to know which one is active

 Can load/save any DX7/TX7 sysex programs. It is also possible to save a single program into a different sysex file.

## 
 Credits & thanks

 DX Synth engine : Raph Levien and the msfa team 

 Graphical design : AZur Studio 

 Surge Synthesizer Team for substantial contributions like microtuning and MPE support.

 LP Filter : Filatov Vadim (2DaT); taken from the excellent Obxd project

 PPPlay : Great OPL3 implementation, with documented code :D

 DX7 program compilation : Jean-Marc Desprez (author of SynprezFM ) 

 DX7 programs : Dave Benson, Frank Carvalho, Tim Conrardy, Jack Deckard, Chris Dodunski, Tim Garrett, Hitaye, Stephan Ibsen, Christian Jezreel, Narfman, Godric Wilkie

## 
 Cartridge Manager

 Any .syx file in the Cartridges directory will be available from the "CART" window. Find this directory by using the "CART" button and then the "SHOW DIR" button.

 You can drag and drop any DX7 program from what is loaded in dexed and/or what you have loaded in the cartridge browser.

 Double-clicking on a program will load the currently selected program in the plugin.

 Use the context (right-click) menu to send the program/cartridge the DX7 or open your OS file browser from the directory context.

 Hint: BlackWinny from kvraudio did a great DX7 compilation named Dexed_cart_1.0.zip . Simply unzip the content of this zipfile to your Cartridges directory.

## 
 Engine Type

 Dexed can be configured to use some of the original math limitation of a DX synthesizer. This does not
only apply to the DAC, it also involves the bit resolution of the sine waves and the way that the 
amplitude is applied to each operator. Since all of this is experimental, multiple engines will be 
available to be able to compare them easily.

 Dexed comes with 3 engine types :

 Modern : this is the original 24-bit music-synthesizer-for-android implementation.

 Mark I : Based on the OPL Series but at a higher resolution (LUT are 10-bits). The target of this engine is to be closest to the real DX7.

 OPL Series : this is an experimental implementation of the reversed engineered OPL family chips . 8-bit. Keep in mind that the envelopes stills needs tuning.