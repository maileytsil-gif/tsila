---
titre: "eclab/grains — booker.ino, extrait : en-tête (Leslie, configuration) et listes de registrations de drawbars (Booker T., Jimmy Smith, gospel…)"
source: https://raw.githubusercontent.com/eclab/grains/master/booker/booker.ino
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: orgue Hammond : registrations de drawbars, percussion, Leslie (émulations open source)
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

> Extrait : lignes 1–191 (commentaires, réglages du Leslie, 16 registrations actives et la liste de ~99 registrations commentée) ; les tables de fréquences et le code Mozzi sont omis.

```cpp
// Copyright 2023 Sean Luke
// (sean@cs.gmu.edu)
//
// Released under the Apache 2.0 License


/// BOOKER
///
/// Booker is a Hammond Organ simulator, complete with Leslie.  It is meant to run on the 
/// AE Modular GRAINS, but it could be  adapted to any Arduino.  
///
/// SET GRAINS TO MOZZI MODE.  Sorry, no Grains mode.
///
/// You will need to install the Mozzi Library.  You can do this from the Library Manager
/// in your Arduino IDE.
///
/// ALIASING: At extremely high frequencies, a few of Booker's drawbars will go over Nyquist and
/// you may hear some antialiasing effects.  I can fix this but it puts me over the
/// computational budget of the device, so it's not going to happen.
///
/// THE LESLIE.  Booker comes with a Leslie, which is on by default:

#define LESLIE_ON               // To turn this off, put a // before the #define, as in //#define

// Leslie changes both the amplitude and pitch at a certain rate.
// You can adjust them here

#define LESLIE_FREQUENCY 5.66                           // This is the 450 speed.  The classic slower speed is 0.66, but it's too slow
#define LESLIE_VOLUME 1                                 // Values are 0 (min but not gone), 1, 2, 3, 4, 5, 6 (max).
#define LESLIE_PITCH 128                                 // Values are 1.0 (lots) ... 128.0 or more (little).  Can be floating point.

/// ADJUSTING TUNING AND TRACKING
///
/// Grains's Inputs track 1.3V/octave, not 1V/octave: we'll need to scale them to track properly.  
/// To do this, you can adjust the Pitch CV Scaling on Pot 1.  This GRAINS program is set up to play 
/// the C three octaves below Middle C when it receives 0V.  You should be able to use Pot 1 to scale 
/// the pitch such that high Cs play in tune as well.  Once you have things tracking well, you can 
/// then use the Pitch Tune (Audio In) to tune 0V to some other note.  Note that as GRAINS resistors 
/// warm up, the scaling will change and you will need to adjust the tracking again, at least until 
/// they are fully warmed up.
///
/// By default the note corresponding to 0V is C0, three octaves below middle C, that is MIDI note 24, 
/// or 32.7 Hz.  You can customize the tuning for this Grains program.  This can be done 
/// in two ways.  First, you can add pitch to the tuning with a CV value to Audio In.  Second, you 
/// can transpose the pitch up by changing the TRANSPOSE_OCTAVES and/or TRANSPOSE_SEMITONES #defines 
/// in the code to positive integers.  You can also change TRANSPOSE_BITS: a "bit" is the minimum possible
/// change Grains can do, equal to 1/17 of a semitone.
///

/// CONFIGURATION
///
/// IN 1            Pitch CV
/// IN 2            Volume CV
/// IN 3            [Unused]
/// AUDIO IN (A)    Pitch Tune
/// AUDIO OUT       Out
/// DIGITAL OUT (D) [Unused]
///
/// POT 1           Pitch Scaling  [Set the switch to In1]
///
/// POT 2           Volume
///
/// POT 3           Choice of Organ [Set the switch to MAN]

/// Lastly, here is our present drawbar selection.  Keep this to no more than 31 but feel free
/// to change the selections.  There is a big list of 99 selections below you could swap in.

#define NUM_DRAWBAR_SELECTIONS 16
uint8_t drawbars[NUM_DRAWBAR_SELECTIONS][9] = 
    {
    { 8, 8, 8, 8, 8, 8, 8, 8, 8 },    // 888888888 Full Organ
    { 8, 8, 5, 3, 2, 4, 5, 8, 8 },    // 885324588 Blues
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Booker T. Jones 1
    { 8, 8, 8, 6, 3, 0, 0, 0, 0 },    // 888630000 Booker T. Jones 2
    { 8, 7, 8, 0, 0, 0, 4, 5, 6 },    // 878000456 Bright Comping
    { 8, 4, 3, 0, 0, 0, 0, 0, 0 },    // 843000000 Dark Comping
    { 8, 0, 8, 8, 0, 8, 0, 0, 8 },    // 808808008 Gospel 1
    { 8, 8, 8, 0, 0, 0, 0, 0, 8 },    // 888000008 Gospel 2
    { 8, 6, 8, 6, 6, 6, 5, 6, 8 },    // 868666568 Greg Allman 1
    { 8, 8, 8, 6, 0, 0, 0, 0, 0 },    // 888600000 Greg Allman 2
    { 8, 8, 6, 8, 0, 0, 3, 0, 0 },    // 886800300 Paul Shaffer 1
    { 8, 8, 8, 7, 6, 8, 8, 8, 8 },    // 888768888 Paul Shaffer 2
    { 8, 8, 8, 8, 7, 8, 6, 7, 8 },    // 888878678 Paul Shaffer 3
    { 8, 0, 8, 0, 0, 0, 0, 0, 8 },    // 808000008 Reggae
    { 0, 8, 0, 0, 0, 0, 0, 0, 0 },    // 080000000 Sine
    { 8, 7, 6, 5, 4, 3, 2, 1, 1 },    // 876543211 Strings
    };

/** Here is a collection of Drawbar Selections for you.
    You can find more online.
        
    { 0, 0, 7, 7, 4, 0, 0, 3, 4 },    // 007740034 Alone in the City
    { 8, 8, 7, 7, 2, 4, 1, 1, 0 },    // 887724110 America (Gospel) (U)
    { 0, 0, 6, 6, 0, 6, 0, 0, 0 },    // 006606000 America (Gospel) (L)
    { 8, 8, 5, 3, 2, 4, 5, 8, 8 },    // 885324588 Blues
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Booker T. Jones 1
    { 8, 8, 8, 6, 3, 0, 0, 0, 0 },    // 888630000 Booker T. Jones 2
    { 8, 8, 8, 8, 0, 8, 0, 0, 8 },    // 888808008 Born to B3 (Gospel) (U)
    { 0, 0, 7, 7, 2, 5, 4, 0, 0 },    // 007725400 Born to B3 (Gospel) (L)
    { 8, 8, 8, 1, 1, 0, 0, 0, 0 },    // 888110000 Brian Auger 1
    { 8, 8, 8, 8, 0, 5, 0, 0, 0 },    // 888805000 Brian Auger 2
    { 8, 7, 8, 0, 0, 0, 4, 5, 6 },    // 878000456 Bright Comping
    { 8, 0, 0, 0, 0, 0, 8, 8, 8 },    // 800000888 Brother Jack
    { 8, 4, 3, 0, 0, 0, 0, 0, 0 },    // 843000000 Dark Comping
    { 8, 8, 8, 8, 8, 8, 8, 8, 8 },    // 888888888 Dark Solo A (U)
    { 6, 6, 2, 0, 0, 0, 0, 0, 0 },    // 662000000 Dark Solo A (L)
    { 8, 2, 8, 2, 0, 0, 0, 0, 2 },    // 828200002 Dark Solo B (U)
    { 6, 0, 6, 0, 0, 0, 0, 0, 0 },    // 606000000 Dark Solo B (L)
    { 8, 8, 8, 0, 0, 0, 8, 8, 8 },    // 888000888 Fat
    { 0, 8, 0, 0, 8, 0, 8, 8, 3 },    // 080080883 Fifth Organ (Gospel) (U)
    { 0, 0, 8, 8, 0, 6, 0, 0, 0 },    // 008806000 Fifth Organ (Gospel) (L)
    { 0, 0, 6, 8, 0, 2, 0, 0, 0 },    // 006802000 Flutes
    { 8, 8, 8, 6, 6, 6, 8, 8, 8 },    // 888666888 Full and High
    { 8, 6, 8, 8, 6, 8, 0, 6, 8 },    // 868868068 Full and Sweet
    { 8, 8, 8, 8, 8, 8, 8, 8, 8 },    // 888888888 Full Organ
    { 6, 8, 8, 6, 0, 0, 0, 0, 4 },    // 688600004 Funky Comping
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Gimme Some Loving
    { 8, 0, 8, 8, 0, 8, 0, 0, 8 },    // 808808008 Gospel 1
    { 8, 8, 8, 0, 0, 0, 0, 0, 8 },    // 888000008 Gospel 2
    { 8, 6, 8, 6, 6, 6, 5, 6, 8 },    // 868666568 Greg Allman 1
    { 8, 8, 8, 6, 0, 0, 0, 0, 0 },    // 888600000 Greg Allman 2
    { 8, 8, 6, 0, 0, 0, 0, 4, 0 },    // 886000040 Greg Allman 3
    { 8, 8, 8, 8, 0, 0, 0, 8, 8 },    // 888800088 Greg Rolie 1
    { 8, 8, 6, 4, 0, 0, 0, 0, 0 },    // 886400000 Greg Rolie 2
    { 8, 8, 8, 8, 8, 6, 6, 6, 6 },    // 888886666 Greg Rolie 4
    { 8, 8, 8, 4, 2, 0, 0, 8, 0 },    // 888420080 Groove Holmes (Gospel) (U)
    { 0, 0, 0, 5, 0, 5, 0, 0, 0 },    // 000505000 Groove Holmes (Gospel) (L)
    { 8, 8, 0, 0, 0, 0, 0, 0, 0 },    // 880000000 House Bass (Gospel) (U)
    { 0, 0, 8, 0, 8, 0, 0, 0, 0 },    // 008080000 House Bass (Gospel) (L)
    { 8, 6, 8, 6, 0, 0, 0, 0, 6 },    // 868600006 Jimmy McGriff 1
    { 8, 8, 3, 2, 0, 0, 1, 2, 5 },    // 883200125 Jimmy McGriff 2 (Gospel) (U)
    { 4, 4, 8, 6, 5, 0, 0, 0, 0 },    // 448650000 Jimmy McGriff 2 (Gospel) (L)
    { 8, 8, 8, 8, 8, 8, 8, 8, 8 },    // 888888888 Jimmy Smith 1 (U)
    { 0, 0, 7, 5, 0, 0, 0, 0, 0 },    // 007500000 Jimmy Smith 1 (L)
    { 8, 8, 8, 0, 0, 0, 0, 0, 0 },    // 888000000 Jimmy Smith 2 (U)
    { 8, 3, 8, 0, 0, 0, 0, 0, 0 },    // 838000000 Jimmy Smith 2 (L)
    { 8, 8, 8, 0, 0, 0, 0, 0, 0 },    // 888000000 Jimmy Smith 3 (U)
    { 8, 0, 8, 0, 0, 0, 0, 0, 0 },    // 808000000 Jimmy Smith 3 (L)
    { 8, 8, 8, 4, 0, 0, 0, 8, 0 },    // 888400080 Joey DeFrancesco
    { 8, 8, 4, 4, 0, 0, 0, 0, 0 },    // 884400000 Jon Lord
    { 8, 8, 0, 0, 6, 0, 0, 0, 0 },    // 880060000 Latin (Gospel) (U)
    { 0, 0, 6, 6, 7, 6, 0, 0, 0 },    // 006676000 Latin (Gospel) (L)
    { 8, 0, 0, 8, 0, 8, 0, 0, 0 },    // 800808000 Matthew Fisher
    { 8, 6, 8, 8, 0, 0, 0, 0, 4 },    // 868800004 Melvin Crispel
    { 8, 0, 3, 6, 0, 0, 0, 0, 0 },    // 803600000 Mellow
    { 0, 0, 7, 8, 0, 0, 4, 5, 3 },    // 007800453 Meditation Time (Gospel) (U)
    { 0, 0, 6, 7, 0, 0, 5, 4, 0 },    // 006700540 Meditation Time (Gospel) (L)
    { 8, 8, 6, 8, 0, 0, 3, 0, 0 },    // 886800300 Paul Shaffer 1
    { 8, 8, 8, 7, 6, 8, 8, 8, 8 },    // 888768888 Paul Shaffer 2
    { 8, 8, 8, 8, 7, 8, 6, 7, 8 },    // 888878678 Paul Shaffer 3
    { 8, 5, 0, 0, 0, 5, 0, 0, 0 },    // 850005000 Pink Floyd
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Power Chords
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Progessive (Gospel) (U)
    { 0, 0, 8, 8, 8, 4, 0, 0, 0 },    // 008884000 Progessive (Gospel) (L)
    { 0, 0, 6, 8, 7, 6, 4, 0, 0 },    // 006876400 Ray Charles
    { 8, 0, 8, 0, 0, 0, 0, 0, 8 },    // 808000008 Reggae
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Rock, R&B (U)
    { 8, 4, 8, 0, 0, 0, 0, 0, 0 },    // 848000000 Rock, R&B (L)
    { 8, 0, 0, 3, 8, 8, 8, 8, 8 },    // 800388888 Screaming (Gospel) (U)
    { 0, 0, 7, 0, 3, 3, 3, 3, 3 },    // 007033333 Screaming (Gospel) (L)
    { 0, 0, 8, 8, 8, 8, 8, 0, 0 },    // 008888800 Shirley Scott
    { 8, 3, 0, 0, 0, 0, 3, 7, 8 },    // 830000378 Simmering
    { 0, 8, 0, 0, 0, 0, 0, 0, 0 },    // 080000000 Sine
    { 8, 7, 6, 5, 5, 6, 7, 8, 8 },    // 876556788 Shouting 1
    { 6, 6, 8, 8, 4, 8, 5, 8, 8 },    // 668848588 Shouting 2
    { 8, 7, 8, 6, 4, 5, 4, 6, 6 },    // 878645466 Shouting 3 (Gospel) (U)
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Shouting 3 (Gospel) (L)
    { 0, 0, 8, 4, 0, 0, 0, 0, 0 },    // 008400000 Slow Balllad
    { 0, 6, 8, 8, 4, 0, 0, 0, 3 },    // 068840003 Slowly
    { 8, 8, 8, 7, 0, 0, 0, 0, 0 },    // 888700000 Soft Backing (Gospel) (U)
    { 5, 5, 5, 4, 0, 0, 0, 0, 0 },    // 555400000 Soft Backing (Gospel) (L)
    { 8, 0, 8, 4, 0, 0, 0, 0, 8 },    // 808400008 Soft Chords
    { 6, 7, 8, 4, 0, 4, 2, 3, 1 },    // 678404231 Speaker Talking (Gospel) (U)
    { 0, 0, 6, 6, 0, 2, 0, 2, 4 },    // 006602024 Speaker Talking (Gospel) (L)
    { 8, 8, 8, 6, 4, 3, 2, 0, 0 },    // 888643200 Steppenwolf
    { 8, 8, 8, 8, 7, 6, 7, 8, 8 },    // 888876788 Steve Winwood
    { 8, 7, 6, 5, 4, 3, 2, 1, 1 },    // 876543211 Strings
    { 0, 0, 8, 0, 0, 0, 0, 0, 0 },    // 008000000 Sweet
    { 7, 8, 7, 7, 4, 6, 0, 4, 6 },    // 787746046 Testimony Service  (Gospel) (U)
    { 0, 0, 8, 8, 0, 0, 6, 7, 3 },    // 008800673 Testimony Service  (Gospel) (L)
    { 8, 7, 8, 6, 5, 6, 4, 6, 7 },    // 878656467 Theatre Organ (Gospel) (U)
    { 0, 0, 8, 8, 4, 4, 0, 0, 0 },    // 008844000 Theatre Organ (Gospel) (L)
    { 8, 8, 8, 8, 0, 0, 0, 0, 0 },    // 888800000 Tom Coster
    { 8, 0, 0, 0, 0, 0, 0, 0, 8 },    // 800000008 Whistle 1
    { 8, 8, 8, 0, 0, 0, 0, 0, 8 },    // 888000008 Whistle 2
    { 6, 8, 8, 6, 0, 0, 0, 0, 0 },    // 688600000 Whiter Shade Of Pale 1 (U)
    { 8, 8, 0, 0, 7, 0, 7, 7, 0 },    // 880070770 Whiter Shade Of Pale 1 (L)
    { 8, 8, 8, 8, 0, 8, 0, 0, 6 },    // 888808006 Whiter Shade Of Pale 2 (U)
    { 0, 0, 4, 4, 4, 0, 0, 0, 0 },    // 004440000 Whiter Shade Of Pale 2 (L)
    { 8, 6, 6, 8, 0, 0, 0, 0, 0 },    // 866800000 Wide Leslie
*/
```
