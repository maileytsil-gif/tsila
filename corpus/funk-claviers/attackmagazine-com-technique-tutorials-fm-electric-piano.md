---
titre: "attackmagazine.com — fm electric piano"
source: https://www.attackmagazine.com/technique/tutorials/fm-electric-piano/
recupere_le: 2026-09-24
mode: texte integral
langue: en
axe: claviers électromécaniques
skills: studio-grade-funk-keys-synth-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

FM Electric Piano - Attack Magazine 

## Technique » Tutorials » FM Electric Piano 

# FM Electric Piano

#### Share

 Facebook 

 Twitter 
 
 WhatsApp 

 Moving forward with our examination of FM synthesis, we show how to create a classic electric piano patch in NI’s FM8. This is the basis of countless classic sounds in just about every genre of dance music.

 In our Introduction to FM Synthesis we looked at how to create a simple percussive synth bass sound using one operator to modulate another. This time we’re going to employ some more involved programming to create another classic FM sound, a DX7-like digital electric piano that’s perfect for capturing that smooth 80s vibe  but can also be tweaked to create much more modern sounds.

 We’ll be using NI’s FM8 plugin for this walkthrough (you can download a demo from here ), but the same principles apply to any good FM synth plugin. Starting with the default patch in FM8, click the Expert tab on the left-hand side of the screen to bring up the modulation matrix.

 In the matrix, right-click Operator E to activate it, then left click it to bring up its parameters. Drag up on the box in the matrix below Operator E and to the left of Operator F like until the modulation amount reaches 100. This adds harmonics and gives the sound a sawtooth-like timbre.

 http://www.attackmagazine.com/wp-content/uploads/2014/08/Audio-13.mp3 
 We can change the timbre of this frequency modulation by adjusting Operator E’s Ratio setting. If you play a note and drag up on this parameter you’ll hear how the timbre becomes sharper and brighter, eventually beginning to alias and create all kinds of unusual tones.

 http://www.attackmagazine.com/wp-content/uploads/2014/08/Audio-21.mp3 
 To create our digital piano we want to use a fairly high ratio to simulate the harmonics created by the electric piano’s tine being struck. We’ll set the Ratio to 18.00, giving us a harsh, sustained tone.

 http://www.attackmagazine.com/wp-content/uploads/2014/08/Audio-31.mp3 
 Let’s use an envelope to make this sound more percussive. When we created our bass sound we used the modulating operator’s envelope to alter the timbre of the sound over time. Here we want the timbre to stay consistent, and the volume to drop instead. This means we need to modify the envelope of the carrier, Operator F. Click Operator F in the modulation matrix to bring up its parameters. Drag down on the square at the top right-hand corner of the envelope to turn down its sustain level.

 If we play our patch now it sounds like something metallic being tapped lightly. Not terribly impressive on its own, but it forms a fundamental part of our electric piano patch.

 http://www.attackmagazine.com/wp-content/uploads/2014/08/Audio-41.mp3 

### Related 

 21st August, 2014 

 Previous 
 Tutorials - Grime Synth Basics 

 Next 
 Tutorials - Reese Bass Redux 

### Leave a Reply
 Your email address will not be published. Required fields are marked * 
 Comment * 
 Name * 

 Email * 

 Δ 

### A WEEKLY SELECTION OF OUR BEST ARTICLES DELIVERED TO YOUR INBOX

 Δ 

#### You currently have an ad blocker installed

 Attack Magazine is funded by advertising revenue. To help support our original content, please consider whitelisting Attack in your ad blocker software.

 Find out how 
 x