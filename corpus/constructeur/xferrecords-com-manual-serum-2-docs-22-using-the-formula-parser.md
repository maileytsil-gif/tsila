---
titre: "xferrecords com manual serum 2 docs — Using the Formula Parser (p. 304-311)"
source: constructeur/xferrecords-com-manual-serum-2-docs.pdf
recupere_le: 2026-09-24
mode: texte integral (PDF → texte)
langue: en
axe: documentation constructeur
skills: sound-designer-serum, vst-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

# Using the Formula Parser


<!-- page 304 -->

Serum 2 User Guide
304
Using the Formula Parser
You can use the Formula parser to make a sound using math!
Specifically, the Formula parser field allows you to enter math functions to plot tables in a generative
fashion. This is a fairly advanced feature; don’t worry if you don’t follow all the details. You can still
explore this capability through experimentation.
However if you want to generate waveforms from thin air and enjoy this kind of approach, you’ll be glad
that you paid attention in math class!
The good news is that Serum includes many formula presets, and it’s easy to paste formulas created by
other users.
Basic Functions
The following table lists the basic functions supported by the parser.
Name
Arguments
Description
sin
1
sine function
cos
1
cosine function
tan
1
tangent function
asin
1
arcus sine function
acos
1
arcus cosine function
atan
1
arcus tangent function
sinh
1
hyperbolic sine function
cosh
1
hyperbolic cosine function
tanh
1
hyperbolic tangent function
asinh
1
hyperbolic arcus sine function
acosh
1
hyperbolic arcus cosine function
atanh
1
hyperbolic arcus tangent function
log2
1
logarithm base 2
log10
1
logarithm base 10
log
1
logarithm base 10
ln
1
logarithm base e (2.71828...)
exp
1
e raised to the power of x
sqrt
1
square root of a value

<!-- page 305 -->

﻿
Using the Formula Parser
Serum 2 User Guide
305
Name
Arguments
Description
sign
1
sign function -1 if x<0; 1 if x>0
rint
1
round to nearest integer
abs
1
absolute value
min
var.
minimum of all arguments
max
var.
maximum of all arguments
sum
var.
sum of all arguments
avg
var.
mean values of all arguments
Built-in Binary Operators
The following table lists the default binary operators supported by the parser.
Operator
Meaning
Priority
&&
logical and
1
||
logical or
2
<=
less than or equal
4
>=
greater than or equal
4
!=
not equal
4
==
equal
4
>
greater than
4
<
less than
4
+
addition
5
-
subtraction
5
*
multiplication
6
/
division
6
^
raise x to the power of y
7

<!-- page 306 -->

﻿
Using the Formula Parser
Serum 2 User Guide
306
Constants and Variables
The following table lists the constants and variables supported by the parser.
Note the following:
•	 sel refers to the current (existing) waveform value of the selected table
This does not change for each table when using a multi-table formula. In other words, the formula
contains y or z, and refers only to the selected table when formula processing begins.
•	 rand is a random number from -1.0 to 1.0
This value stays the same for all tables.
Symbol
Description
pi
3.141592658979323846264338
e
2.718281828182818281828
w
The current time-value getting plotted, from 0.0 to 1.0. This is the same as
(x+1)/2.
x
The current time-value being plotted, from -1.0 to 1.0.
y
The current table number, from 0.0 to 1.0.
z
The current table number, from -1.0 to 1.0. This is equivalent to (y\*2)-1.
q
When a q is present in the formula, the function plots to the FFT bins
instead of plotting to the waveform display. Note that q iterates from 1 to
512 for the respective harmonics/bins.
in
The current (old) visible waveform value of the plotting table. This changes
to each old table, if using y or z, which plots all tables.
sel
Similar to in, but only the currently-selected wavetable (does not change to
each table; uses the selected table when formula processing begins).
rand
A random number from -1.0 to 1.0 that stays the same for all tables
(precalculated for every time position).
Note the following:
•	 y and z refer to the current table number. Therefore, when y or z is in the expression, all tables for
the current oscillator are regenerated.
•	 q renders the function to FFT instead of to the waveform display. There is no reason to include x
or y in a formula containing q.

<!-- page 307 -->

﻿
Using the Formula Parser
Serum 2 User Guide
307
Exploring the Formula Presets Menu
Serum offers a formula presets menu that you can use to get started with preset examples. This
provides a good way to learn the capabilities, as well as to create your own presets.
Formula Presets Menu
As soon as you select a formula, it appears in the Formula field automatically and the waveform is
calculated.
Menu Item
Description
Singles
These are single-cycle formulas that do not contain y or z variables. When
you select an option, only the currently-selected table is replaced/generated
with the formula.
Multis
These are multi-cycle formulas that contain y or z variables. When you select
an option, the entire wavetable is replaced.
User Singles
These are user-defined single-cycle formulas.
User Multis
These are user-defined multi-cycle formulas.

<!-- page 308 -->

﻿
Using the Formula Parser
Serum 2 User Guide
308
Saving Your Own Formulas
You can save your own formulas for quick access.
1.	Type the formula in the Formula field and press the Enter key.
2.	Click the formula presets menu and choose Save Formula in the menu that appears. A dialog
appears allowing you to save the formula.
Save Formula Dialog
By default, the text box displays the formula.
3.	Type the name of the formula and click the
 button.
The formula is saved in the corresponding formula sub-menu (either User Singles or User Multis,
as appropriate). You can now access your formula using the formula presets menu.
Managing Formula Files Manually (Advanced)
Serum uses two files to store the user formula presets:
•	 FormulaUserMultis.txt
•	 FormulaUserSingles.txt
You can find these files in the Serum 2 Presets/System/ folder. The text files have the following
format:
[formula1][formula1-name]
[formula2][formula2-name]
You can find existing examples in the FormulaFactorySingles.txt or
FormulaFactoryMultis.txt files.

<!-- page 309 -->

﻿
Using the Formula Parser
Serum 2 User Guide
309
If you need to remove a formula preset that you saved earlier, do the following:
1.	Open the appropriate user formula preset file using a text editor.
2.	Delete the line containing the formula you want to remove.
3.	Save the text file.
Important: While you can also edit the FormulaFactorySingles.txt and
FormulaFactoryMultis.txt files, it’s better only to use the user files listed in this section instead.
This prevents your personal formulas from being overwritten when you install a Serum update.
Exploring Formula Parser Examples
This section shows a set of examples of using the q variable in formulas. When you include the q
variable in a formula, Serum processes the formula using the FFT area instead of directly “as audio” in
the wavetable display (time domain).
This means you can do signal generation or processing of a wavetable in the frequency domain. In this
case, the q value represents the bin number in the FFT area at the top of the Wavetable Editor, from 1
to 512.
For example, consider the following formula:
q<17
The formula creates a wavetable frame with only the first 16 harmonics.
Formula as q<17

<!-- page 310 -->

﻿
Using the Formula Parser
Serum 2 User Guide
310
As another example, consider the following formula:
q<z*256
This formula creates an entire table set of 256 frames, with one additional harmonic in each
consecutive frame.
Next consider the following formula:
(1/q)^0.25
This creates a sawtooth wave with higher harmonics than a normal saw (-3 dB/oct). Replace the 0.25
value with a different number to alter the spectral decay (for instance, 0.5 produces a normal saw, 0.75
creates a duller saw).
Alternatively, you could replace 0.25 with z, as shown in the following:
(1/q)^z
This causes Serum to create 256 frames in the wavetable with the harmonic scale.
Finally, consider the following formula:
((q%2)==1)?in:0
This formula removes every second harmonic (even harmonics) from the current wavetable frame,
leaving odd harmonics only (like a square wave).
Formula as ((q%2)==1)?in:0

<!-- page 311 -->

﻿
Using the Formula Parser
Serum 2 User Guide
311
Using this on a (default) sawtooth wave results in a square wave. This is a popular formula, particularly in
Dubstep bass sound design, to make tables sound more “hollow” (taking up less of the spectrum).
Note: This formula appears as an included preset called Proc:Squarify.