---
titre: "Faust physmodels.lib — section cuivres (brassLipsTable, brassLips, brassModel, wBell) — extrait"
source: https://raw.githubusercontent.com/grame-cncm/faustlibraries/master/physmodels.lib
recupere_le: 2026-09-24
mode: texte integral (extrait de fichier)
langue: en
axe: modèle physique ; extrait de la bibliothèque
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

```
 `maxLength`: the maximum length of the tube in meters (should be static)
// * `length`: the length of the tube in meters
//
// #### Test
// ```
// pm = library("physmodels.lib");
// openTube_test = 0.25, -0.15, 0.05 : pm.openTube(pm.maxLength, 0.9);
// ```
//----------------------------------
openTube = stringSegment;


//-------`(pm.)reedTable`----------
// Extremely basic reed table that can be used to implement a wide range of
// single reed types for many different instruments (saxophone, clarinet, etc.).
//
// #### Usage
//
// ```
// excitation : reedTable(offset,slope) : _
// ```
//
// Where:
//
// * `excitation`: an excitation signal
// * `offset`: table offset
// * `slope`: table slope
//
// #### Test
// ```
// pm = library("physmodels.lib");
// os = library("oscillators.lib");
// reedTable_test = os.osc(220) : pm.reedTable(0.4, 0.2);
// ```
//----------------------------------
reedTable(offset,slope) = reedTable : min(1) : max(-1)
with {
    reedTable = *(slope) + offset;
};


//-------`(pm.)fluteJetTable`----------
// Extremely basic flute jet table.
//
// #### Usage
//
// ```
// excitation : fluteJetTable : _
// ```
//
// Where:
//
// * `excitation`: an excitation signal
//
// #### Test
// ```
// pm = library("physmodels.lib");
// os = library("oscillators.lib");
// fluteJetTable_test = os.osc(220) : pm.fluteJetTable;
// ```
//----------------------------------
fluteJetTable = _ <: *(* : -(1)) : clipping
with {
    clipping = min(1) : max(-1);
};


//-------`(pm.)brassLipsTable`----------
// Simple brass lips/mouthpiece table. Since this implementation is very basic
// and that the lips and tube of the instrument are coupled to each other, the
// length of that tube must be provided here.
//
// #### Usage
//
// ```
// excitation : brassLipsTable(tubeLength,lipsTension) : _
// ```
//
// Where:
//
// * `excitation`: an excitation signal (can be DC)
// * `tubeLength`: length in meters of the tube connected to the mouthpiece
// * `lipsTension`: tension of the lips (0-1) (default: 0.5)
//
// #### Test
// ```
// pm = library("physmodels.lib");
// os = library("oscillators.lib");
// brassLipsTable_test = os.osc(220) : pm.brassLipsTable(0.3, 0.2);
// ```
//----------------------------------
brassLipsTable(tubeLength,lipsTension) = *(0.03) : lipFilter <: * : clipping
with {
    clipping = min(1) : max(-1);
    freq = (tubeLength : l2f)*pow(4,(2*lipsTension)-1);
    filterR = 0.997;
    a1 = -2*filterR*cos(ma.PI*2*freq/ma.SR);
    lipFilter = fi.tf2(1,0,0,a1,pow(filterR,2)); // resonance with same freq as tube
};


//-------`(pm.)clarinetReed`----------
// Clarinet reed based on [`reedTable`](#reedtable) with controllable
// stiffness.
//
// #### Usage
//
// ```
// excitation : clarinetReed(stiffness) : _
// ```
//
// Where:
//
// * `excitation`: an excitation signal
// * `stiffness`: reed stiffness (0-1)
//
// #### Test
// ```
// pm = library("physmodels.lib");
// os = library("oscillators.lib");
// clarinetReed_test = os.osc(440) : pm.clarinetReed(0.6);
// ```
//----------------------------------
clarinetReed(stiffness) = reedTable(0.7,tableSlope)
with {
    tableSlope = -0.44 + 0.26*stiffness;
};


//-------`(pm.)clarinetMouthPiece`----------
// Bidirectional block implementing a clarinet mouthpiece as well as the various
// interactions happening with traveling waves. This element is ready to be
// plugged to a tube...
//
// #### Usage
//
// ```
// chain(clarinetMouthPiece(reedStiffness,pressure) : tube : etc.)
// ```
//
// Where:
//
// * `pressure`: the pressure of the air flow (DC) created by the virtual performer (0-1).
// This can also be any kind of signal that will directly injected in the mouthpiece
// (e.g., breath noise, etc.).
// * `reedStiffness`: reed stiffness (0-1)
//
// #### Test
// ```
// pm = library("physmodels.lib");
// clarinetMouthPiece_test = 0.25, -0.15, 0.05 : pm.clarinetMouthPiece(0.6, 0.4);
// ```
//----------------------------------
clarinetMouthPiece(reedStiffness,pressure) = lTermination(reedInteraction,in(pressure))
with {
    reedInteraction = *(-1) <: *(clarinetReed(reedStiffness));
};


//-------`(pm.)brassLips`----------
// Bidirectional block implementing a brass mouthpiece as well as the various
// interactions happening with traveling waves. This element is ready to be
// plugged to a tube...
//
// #### Usage
//
// ```
// chain(brassLips(tubeLength,lipsTension,pressure) : tube : etc.)
// ```
//
// Where:
//
// * `tubeLength`: length in meters of the tube connected to the mouthpiece
// * `lipsTension`: tension of the lips (0-1) (default: 0.5)
// * `pressure`: the pressure of the air flow (DC) created by the virtual performer (0-1).
// This can also be any kind of signal that will directly injected in the mouthpiece
// (e.g., breath noise, etc.).
//
// #### Test
// ```
// pm = library("physmodels.lib");
// brassLips_test = 0.25, -0.15, 0.05 : pm.brassLips(0.3, 0.2, 0.1);
// ```
//----------------------------------
brassLips(tubeLength,lipsTension,pressure) = lTermination(mpInteraction,basicBlock)
with {
    absorption = *(0.85); // absorption coefficient
    p = pressure*0.3; // scaling pressure
    mpInteraction = absorption <:
    (p-_ : brassLipsTable(tubeLength,lipsTension) <: *(p),1-_),_ : _,* : + : fi.dcblocker;
};


//-------`(pm.)fluteEmbouchure`----------
// Bidirectional block implementing a flute embouchure as well as the various
// interactions happening with traveling waves. This element is ready to be
// plugged between tubes segments...
//
// #### Usage
//
// ```
// chain(... : tube : fluteEmbouchure(pressure) : tube : etc.)
// ```
//
// Where:
//
// * `pressure`: the pressure of the air flow (DC) created by the virtual
// performer (0-1).
// This can also be any kind of signal that will directly injected in the
// mouthpiece (e.g., breath noise, etc.).
//
// #### Test
// ```
// pm = library("physmodels.lib");
// fluteEmbouchure_test = 0.25, -0.15, 0.05 : pm.fluteEmbouchure(0.5);
// ```
//----------------------------------
fluteEmbouchure(pressure) =
(_ <: _,_),_,_ : _,*(0.5)+(pressure-_*0.5 : fluteJetTable),_;


//-------`(pm.)wBell`----------
// Generic wind instrument bell bidirectional block that should be placed at
// the end of a [`chain`](#chain).
//
// #### Usage
//
// ```
// chain(... : wBell(opening))
// ```
//
// Where:
//
// * `opening`: the "opening" of bell (0-1)
//
// #### Test
// ```
// pm = library("physmodels.lib");
// wBell_test = 0.25, -0.15, 0.05 : pm.wBell(0.4);
// ```
//----------------------------------
wBell(opening) = rTermination(basicBlock,si.smooth(opening));


//-------`(pm.)fluteHead`----------
// Simple flute head implementing waves reflexion.
//
// #### Usage
//
// ```
// _,_,_ : fluteHead
// ```
// Typical use: `chain(fluteHead : tube : ...)`
//
// #### Test
// ```
// pm = library("physmodels.lib");
// fluteHead_test = 0.25, -0.15, 0.05 : pm.fluteHead;
// ```
//----------------------------------
fluteHead = lTermination(*(absorption),basicBlock)
with {
    absorption = 0.95; // same as for foot
};


//-------`(pm.)fluteFoot`----------
// Simple flute foot implementing waves reflexion and dispersion.
//
// #### Usage
//
// ```
// chain(... : tube : fluteFoot)
// ```
//
// #### Test
// ```
// pm = library("physmodels.lib");
// fluteFoot_test = 0.25, -0.15, 0.05 : pm.fluteFoot;
// ```
//----------------------------------
fluteFoot = rTermination(basicBlock,*(absorption) : dispersion)
with {
    dispersion = si.smooth(0.7); // just a simple lowpass
    absorption = 0.95;           // same as for head
};


//-------`(pm.)clarinetModel`----------
// A simple clarinet physical model without tone holes (pitch is changed by
// changing the length of the tube of the instrument).
//
// #### Usage
//
// ```
// clarinetModel(tubeLength,pressure,reedStiffness,bellOpening) : _
// ```
//
// Where:
//
// * `tubeLength`: the length of the tube in meters
// * `pressure`: the pressure of the air flow created by the virtual performer (0-1).
// This can also be any kind of signal that will directly injected in the mouthpiece
// (e.g., breath noise, etc.).
// * `reedStiffness`: reed stiffness (0-1)
// * `bellOpening`: the opening of bell (0-1)
//
// #### Test
// ```
// pm = library("physmodels.lib");
// clarinetModel_test = pm.clarinetModel(0.9, 0.4, 0.3, 0.2);
// ```
//----------------------------------
clarinetModel(tubeLength,pressure,reedStiffness,bellOpening) = endChain(modelChain)
with {
    lengthTuning = 0.05; // empirical adjustment of the tuning of the tube
    maxTubeLength = maxLength;
    tunedLength = tubeLength/2-lengthTuning; // not really sure why we had to shift octave here
    modelChain =
        chain(
            clarinetMouthPiece(reedStiffness,pressure) :
            openTube(maxTubeLength,tunedLength) :
            wBell(bellOpening) : out
        );
};


//-------`(pm.)clarinetModel_ui`----------
// Same as [`clarinetModel`](#clarinetModel) but with a built-in UI. This function
// doesn't implement a virtual "blower", thus `pressure` remains an argument here.
//
// #### Usage
//
// ```
// clarinetModel_ui(pressure) : _
// ```
//
// Where:
//
// * `pressure`: the pressure of the air flow created by the virtual performer (0-1).
// This can also be any kind of signal that will be directly injected in the mouthpiece
// (e.g., breath noise, etc.).
//
// #### Test
// ```
// pm = library("physmodels.lib");
// clarinetModel_ui_test = pm.clarinetModel_ui(0.4);
// ```
//----------------------------------
clarinetModel_ui(pressure) = clarinetModel(tubeLength,pressure,reedStiffness,bellOpening)*outGain
with {
    tubeLength = hslider("v:clarinetModel/[0]tubeLength",0.8,0.01,3,0.01) : si.smoo;
    reedStiffness = hslider("v:clarinetModel/[1]reedStiffness",0.5,0,1,0.01);
    bellOpening = hslider("v:clarinetModel/[2]bellOpening",0.5,0,1,0.01);
    outGain = hslider("v:clarinetModel/[3]outGain",0.5,0,1,0.01);
};


//-------`(pm.)clarinet_ui`----------
// Ready-to-use clarinet physical model with built-in UI based on
// [`clarinetModel`](#clarinetmodel).
//
// #### Usage
//
// ```
// clarinet_ui : _
// ```
//
// #### Test
// ```
// pm = library("physmodels.lib");
// clarinet_ui_test = pm.clarinet_ui;
// ```
//----------------------------------
clarinet_ui = hgroup("clarinet",blower_ui : clarinetModel_ui);


//-------`(pm.)clarinet_ui_MIDI`----------
// Ready-to-use MIDI compliant clarinet physical model with built-in UI.
//
// #### Usage
//
// ```
// clarinet_ui_MIDI : _
// ```
//
// #### Test
// ```
// pm = library("physmodels.lib");
// clarinet_ui_MIDI_test = pm.clarinet_ui_MIDI;
// ```
//----------------------------------
clarinet_ui_MIDI =
clarinetModel(tubeLength,blow,reedStiffness,bellOpening)*outGain
with {
    f = hslider("v:clarinet/h:[0]midi/[0]freq[style:knob]",440,50,1000,0.01);
    bend = ba.semi2ratio(hslider("v:clarinet/h:[0]midi/[1]bend[hidden:1][midi:pitchwheel]
    [style:knob]",0,-2,2,0.01)) : si.polySmooth(gate,0.999,1);
    gain = hslider("v:clarinet/h:[0]midi/[2]gain[style:knob]
    ",0.6,0,1,0.01);
    envAttack = hslider("v:clarinet/h:[0]midi/[3]envAttack[style:knob]
    ",1,0,30,0.01)*0.001;
    s = hslider("v:clarinet/h:[0]midi/[4]sustain[hidden:1][midi:ctrl 64]
    [style:knob]",0,0,1,1);
    reedStiffness = hslider("v:clarinet/h:[1]otherParams/[0]reedStiffness
    [midi:ctrl 1][style:knob]",0.5,0,1,0.01);
    bellOpening = hslider("v:clarinet/h:[1]otherParams/[1]bellOpening
    [midi:ctrl 3][style:knob]",0.5,0,1,0.01);
    vibratoFreq = hslider("v:clarinet/h:[1]otherParams/[2]vibratoFreq
    [style:knob]",5,1,10,0.01);
    vibratoGain = hslider("v:clarinet/h:[1]otherParams/[3]vibratoGain
    [style:knob]",0.25,0,1,0.01)*0.01;
    outGain = hslider("v:clarinet/h:[1]otherParams/[4]outGain[style:knob]
    ",0.5,0,1,0.01);
    t = button("v:clarinet/[2]gate");

    gate = t+s : min(1);
    vibrato = 1+os.osc(vibratoFreq)*vibratoGain*envelope;
    freq = f*bend*vibrato;
    envelope = gate*gain : si.smooth(ba.tau2pole(envAttack));

    tubeLength = freq : f2l;
    pressure = envelope; // TODO: double vibrato here!!
    blow = blower(pressure,0.05,2000,vibratoFreq,vibratoGain);
};


//-------`(pm.)brassModel`----------
// A simple generic brass instrument physical model without pistons
// (pitch is changed by changing the length of the tube of the instrument).
// This model is kind of hard to control and might not sound very good if
// bad parameters are given to it...
//
// #### Usage
//
// ```
// brassModel(tubeLength,lipsTension,mute,pressure) : _
// ```
//
// Where:
//
// * `tubeLength`: the length of the tube in meters
// * `lipsTension`: tension of the lips (0-1) (default: 0.5)
// * `mute`: mute opening at the end of the instrument (0-1) (default: 0.5)
// * `pressure`: the pressure of the air flow created by the virtual performer (0-1).
// This can also be any kind of signal that will directly injected in the mouthpiece
// (e.g., breath noise, etc.).
//
// #### Test
// ```
// pm = library("physmodels.lib");
// brassModel_test = pm.brassModel(0.9, 0.4, 0.2, 0.6);
// ```
//----------------------------------
brassModel(tubeLength,lipsTension,mute,pressure) = endChain(brassChain)
with {
    maxTubeLength = maxLength;
    lengthTuning = 0; // Not that important for that one because of lips tension
    tunedLength = tubeLength + lengthTuning;
    brassChain = chain(brassLips(tunedLength,lipsTension,pressure) : openTube(maxTubeLength,tunedLength) : wBell(mute) : out);
};


//-------`(pm.)brassModel_ui`----------
// Same as [`brassModel`](#brassModel) but with a built-in UI. This function
// doesn't implement a virtual "blower", thus `pressure` remains an argument here.
//
// #### Usage
//
// ```
// brassModel_ui(pressure) : _
// ```
//
// Where:
//
// * `pressure`: the pressure of the air flow created by the virtual performer (0-1).
// This can also be any kind of signal that will be directly injected in the mouthpiece
// (e.g., breath noise, etc.).
//
// #### Test
// ```
// pm = library("physmodels.lib");
// brassModel_ui_test = pm.brassModel_ui(0.4);
// ```
//----------------------------------
brassModel_ui(pressure) = brassModel(tubeLength,lipsTension,mute,pressure)
with {
    tubeLength = hslider("v:brassModel/[1]tubeLength",0.5,0.01,2.5,0.01) : si.smoo;
    lipsTension = hslider("v:brassModel/[2]lipsTension",0.5,0,1,0.01) : si.smoo;
    mute = hslider("v:brassModel/[3]mute",0.5,0,1,0.01) : si.smoo;
};


//-------`(pm.)brass_ui`----------
// Ready-to-use brass instrument physical model with built-in UI based on
// [`brassModel`](#brassmodel).
//
// #### Usage
//
// ```
// brass_ui : _
// ```
//
// #### Test
// ```
// pm = library("physmodels.lib");
// brass_ui_test = pm.brass_ui;
// ```
//----------------------------------
brass_ui = hgroup("brass",blower_ui : brassModel_ui);


//-------`(pm.)brass_ui_MIDI`----------
// Ready-to-use MIDI-controllable brass instrument physical model with built-in UI.
//
// #### Usage
//
// ```
// brass_ui_MIDI : _
// ```
//
// #### Test
// ```
// pm = library("physmodels.lib");
// brass_ui_MIDI_test = pm.brass_ui_MIDI;
// ```
//----------------------------------
brass_ui_MIDI = brassModel(tubeLength,lipsTension,mute,pressure)*outGain
with {
    f = hslider("v:brass/h:[0]midi/[0]freq[style:knob]",440,50,1000,0.01);
    bend = ba.semi2ratio(hslider("v:brass/h:[0]midi/[1]bend[hidden:1][midi:pitchwheel]
    [style:knob]",0,-2,2,0.01)) : si.polySmooth(gate,0.999,1);
    gain = hslider("v:brass/h:[0]midi/[2]gain[style:knob]
    ",0.5,0,1,0.01);
    envAttack = hslider("v:brass/h:[0]midi/[3]envAttack[style:knob]
    ",1,0,30,0.01)*0.001;
    s = hslider("v:brass/h:[0]midi/[4]sustain[hidden:1][midi:ctrl 64]
    [style:knob]",0,0,1,1);
    lipsTension = hslider("v:brass/h:[1]otherParams/[0]lipsTension[style:knob]
    [midi:ctrl 1]",0.5,0,1,0.01) : si.smoo;
    mute = hslider("v:brass/h:[1]otherParams/[1]mute[style:knob]
    ",0.5,0,1,0.01) : si.smoo;
    vibratoFreq = hslider("v:brass/h:[1]otherParams/[2]vibratoFreq[style:knob]
    ",5,1,10,0.01);
    vibratoGain = hslider("v:brass/h:[1]otherParams/[3]vibratoGain[style:knob]
    ",0.5,0,1,0.01)*0.04;
    outGain = hslider("v:brass/h:[1]otherPa
```