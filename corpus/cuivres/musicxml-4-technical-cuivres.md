---
titre: "MusicXML 4 (W3C, gh-pages) — éléments technical brass-bend / flip / smear / harmon-mute, types bend, bend-sound, glissando, slide — extrait du schéma"
source: https://raw.githubusercontent.com/w3c/musicxml/gh-pages/schema/musicxml.xsd
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: notation ; articulations de cuivres ; sourdines
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

Complète `musicxml-4-articulations-sourdines.md` (mute, scoop/plop/doit/falloff, shake). Ici : le type `technical` (qui contient brass-bend, flip, smear, harmon-mute, bend…), le groupe d’attributs `bend-sound` (accelerate, beats, first-beat, last-beat), et les types `bend`, `glissando`, `slide`, `harmon-closed`, `harmon-mute`.

```xml
	<xs:attributeGroup name="bend-sound">
		<xs:annotation>
			<xs:documentation>The bend-sound type is used for bend and slide elements, and is similar to the trill-sound attribute group. Here the &lt;beats&gt; element refers to the number of discrete elements (like MIDI pitch bends) used to represent a continuous bend or slide. The first-beat indicates the percentage of the duration for starting a bend; the last-beat the percentage for ending it. The default choices are:

	accelerate = "no"
	beats = "4"
	first-beat = "25"
	last-beat = "75"</xs:documentation>
		</xs:annotation>
		<xs:attribute name="accelerate" type="yes-no">
			<xs:annotation>
				<xs:documentation>Does the bend accelerate during playback? Default is "no".</xs:documentation>
			</xs:annotation>
		</xs:attribute>
		<xs:attribute name="beats" type="trill-beats">
			<xs:annotation>
				<xs:documentation>The number of discrete elements (like MIDI pitch bends) used to represent a continuous bend or slide. Default is 4.</xs:documentation>
			</xs:annotation>
		</xs:attribute>
		<xs:attribute name="first-beat" type="percent">
			<xs:annotation>
				<xs:documentation>The percentage of the duration for starting a bend. Default is 25.</xs:documentation>
			</xs:annotation>
		</xs:attribute>
		<xs:attribute name="last-beat" type="percent">
			<xs:annotation>
				<xs:documentation>The percentage of the duration for ending a bend. Default is 75.</xs:documentation>
			</xs:annotation>
		</xs:attribute>
	</xs:attributeGroup>

	<xs:complexType name="bend">
		<xs:annotation>
			<xs:documentation>The bend type is used in guitar notation and tablature. A single note with a bend and release will contain two bend elements: the first to represent the bend and the second to represent the release. The shape attribute distinguishes between the angled bend symbols commonly used in standard notation and the curved bend symbols commonly used in both tablature and standard notation.</xs:documentation>
		</xs:annotation>
		<xs:sequence>
			<xs:element name="bend-alter" type="semitones">
				<xs:annotation>
					<xs:documentation>The &lt;bend-alter&gt; element indicates the number of semitones in the bend, similar to the &lt;alter&gt; element. As with the &lt;alter&gt; element, numbers like 0.5 can be used to indicate microtones. Negative values indicate pre-bends or releases. The &lt;pre-bend&gt; and &lt;release&gt; elements are used to distinguish what is intended. Because the &lt;bend-alter&gt; element represents the number of steps in the bend, a release after a bend has a negative &lt;bend-alter&gt; value, not a zero value.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:choice minOccurs="0">
				<xs:element name="pre-bend" type="empty">
					<xs:annotation>
						<xs:documentation>The &lt;pre-bend&gt; element indicates that a bend is a pre-bend rather than a normal bend or a release.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="release" type="release">
					<xs:annotation>
						<xs:documentation>The &lt;release&gt; element indicates that a bend is a release rather than a normal bend or pre-bend. The first-beat and last-beat attributes of the parent &lt;bend&gt; element are relative to the original note position, not this offset value.</xs:documentation>
					</xs:annotation>
				</xs:element>
			</xs:choice>
			<xs:element name="with-bar" type="placement-text" minOccurs="0">
				<xs:annotation>
					<xs:documentation>The &lt;with-bar&gt; element indicates that the bend is to be done at the bridge with a whammy or vibrato bar. The content of the element indicates how this should be notated. Content values of &quot;scoop&quot; and &quot;dip&quot; refer to the Standard Music Font Layout (SMuFL) guitarVibratoBarScoop and guitarVibratoBarDip glyphs.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:sequence>
		<xs:attribute name="shape" type="bend-shape">
			<xs:annotation>
				<xs:documentation>Distinguishes between the angled bend symbols commonly used in standard notation and the curved bend symbols commonly used in both tablature and standard notation.</xs:documentation>
			</xs:annotation>
		</xs:attribute>
		<xs:attributeGroup ref="print-style"/>
		<xs:attributeGroup ref="bend-sound"/>
	</xs:complexType>

	<xs:complexType name="glissando">
		<xs:annotation>
			<xs:documentation>Glissando and slide types both indicate rapidly moving from one pitch to the other so that individual notes are not discerned. A glissando sounds the distinct notes in between the two pitches and defaults to a wavy line. The optional text is printed alongside the line.</xs:documentation>
		</xs:annotation>
		<xs:simpleContent>
			<xs:extension base="xs:string">
				<xs:attribute name="type" type="start-stop" use="required">
					<xs:annotation>
						<xs:documentation>Indicates if this is the start or stop of the glissando.</xs:documentation>
					</xs:annotation>
				</xs:attribute>
				<xs:attribute name="number" type="number-level" default="1">
					<xs:annotation>
						<xs:documentation>Distinguishes multiple glissandos when they overlap in MusicXML document order. The default value is 1.</xs:documentation>
					</xs:annotation>
				</xs:attribute>
				<xs:attributeGroup ref="line-type"/>
				<xs:attributeGroup ref="dashed-formatting"/>
				<xs:attributeGroup ref="print-style"/>
				<xs:attributeGroup ref="optional-unique-id"/>
			</xs:extension>
		</xs:simpleContent>
	</xs:complexType>

	<xs:complexType name="slide">
		<xs:annotation>
			<xs:documentation>Glissando and slide types both indicate rapidly moving from one pitch to the other so that individual notes are not discerned. A slide is continuous between the two pitches and defaults to a solid line. The optional text for a is printed alongside the line.</xs:documentation>
		</xs:annotation>
		<xs:simpleContent>
			<xs:extension base="xs:string">
				<xs:attribute name="type" type="start-stop" use="required">
					<xs:annotation>
						<xs:documentation>Indicates if this is the start or stop of the slide.</xs:documentation>
					</xs:annotation>
				</xs:attribute>
				<xs:attribute name="number" type="number-level" default="1">
					<xs:annotation>
						<xs:documentation>Distinguishes multiple slides when they overlap in MusicXML document order. The default value is 1.</xs:documentation>
					</xs:annotation>
				</xs:attribute>
				<xs:attributeGroup ref="line-type"/>
				<xs:attributeGroup ref="dashed-formatting"/>
				<xs:attributeGroup ref="print-style"/>
				<xs:attributeGroup ref="bend-sound"/>
				<xs:attributeGroup ref="optional-unique-id"/>
			</xs:extension>
		</xs:simpleContent>
	</xs:complexType>

	<xs:complexType name="harmon-closed">
		<xs:annotation>
			<xs:documentation>The harmon-closed type represents whether the harmon mute is closed, open, or half-open. The optional location attribute indicates which portion of the symbol is filled in when the element value is half.</xs:documentation>
		</xs:annotation>
		<xs:simpleContent>
			<xs:extension base="harmon-closed-value">
				<xs:attribute name="location" type="harmon-closed-location">
					<xs:annotation>
						<xs:documentation>Indicates which portion of the symbol is filled in when the element value is half.</xs:documentation>
					</xs:annotation>
				</xs:attribute>
			</xs:extension>
		</xs:simpleContent>
	</xs:complexType>

	<xs:complexType name="harmon-mute">
		<xs:annotation>
			<xs:documentation>The harmon-mute type represents the symbols used for harmon mutes in brass notation.</xs:documentation>
		</xs:annotation>
		<xs:sequence>
			<xs:element name="harmon-closed" type="harmon-closed">
				<xs:annotation>
					<xs:documentation>The &lt;harmon-closed&gt; element represents whether the harmon mute is closed, open, or half-open.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:sequence>
		<xs:attributeGroup ref="print-style"/>
		<xs:attributeGroup ref="placement"/>
	</xs:complexType>

	<xs:complexType name="technical">
		<xs:annotation>
			<xs:documentation>Technical indications give performance information for individual instruments.</xs:documentation>
		</xs:annotation>
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="up-bow" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;up-bow&gt; element represents the symbol that is used both for up-bowing on bowed instruments, and up-stroke on plucked instruments.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="down-bow" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;down-bow&gt; element represents the symbol that is used both for down-bowing on bowed instruments, and down-stroke on plucked instruments.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="harmonic" type="harmonic">
				<xs:annotation>
					<xs:documentation>The &lt;harmonic&gt; element indicates natural and artificial harmonics. Allowing the type of pitch to be specified, combined with controls for appearance/playback differences, allows both the notation and the sound to be represented. Artificial harmonics can add a notated touching pitch; artificial pinch harmonics will usually not notate a touching pitch. The attributes for the &lt;harmonic&gt; element refer to the use of the circular harmonic symbol, typically but not always used with natural harmonics.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="open-string" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;open-string&gt; element represents the zero-shaped open string symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="thumb-position" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;thumb-position&gt; element represents the thumb position symbol. This is a circle with a line, where the line does not come within the circle. It is distinct from the &lt;snap-pizzicato&gt; symbol, where the line comes inside the circle.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="fingering" type="fingering">
				<xs:annotation>
					<xs:documentation>Fingering is typically indicated 1,2,3,4,5. Multiple fingerings may be given, typically to substitute fingerings in the middle of a note. For guitar and other fretted instruments, the &lt;fingering&gt; element represents the fretting finger; the &lt;pluck&gt; element represents the plucking finger.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="pluck" type="placement-text">
				<xs:annotation>
					<xs:documentation>The &lt;pluck&gt; element is used to specify the plucking fingering on a fretted instrument, where the fingering element refers to the fretting fingering. Typical values are p, i, m, a for pulgar/thumb, indicio/index, medio/middle, and anular/ring fingers.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="double-tongue" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;double-tongue&gt; element represents the double tongue symbol (two dots arranged horizontally).</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="triple-tongue" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;triple-tongue&gt; element represents the triple tongue symbol (three dots arranged horizontally).</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="stopped" type="empty-placement-smufl">
				<xs:annotation>
					<xs:documentation>The &lt;stopped&gt; element represents the stopped symbol, which looks like a plus sign. The smufl attribute distinguishes different Standard Music Font Layout (SMuFL) glyphs that have a similar appearance such as handbellsMalletBellSuspended and guitarClosePedal. If not present, the default glyph is brassMuteClosed.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="snap-pizzicato" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;snap-pizzicato&gt; element represents the snap pizzicato symbol. This is a circle with a line, where the line comes inside the circle. It is distinct from the &lt;thumb-position&gt; symbol, where the line does not come inside the circle.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="fret" type="fret">
				<xs:annotation>
					<xs:documentation>The &lt;fret&gt; element is used with tablature notation and chord diagrams. Fret numbers start with 0 for an open string and 1 for the first fret.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="string" type="string">
				<xs:annotation>
					<xs:documentation>The &lt;string&gt; element is used with tablature notation, regular notation (where it is often circled), and chord diagrams. String numbers start with 1 for the highest pitched full-length string.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="hammer-on" type="hammer-on">
				<xs:annotation>
					<xs:documentation>The &lt;hammer-on&gt; element is used in guitar and fretted instrument notation. Since a single slur can be marked over many notes, the &lt;hammer-on&gt; element is separate so the individual pair of notes can be specified. The element content can be used to specify how the &lt;hammer-on&gt; should be notated. An empty element leaves this choice up to the application.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="pull-off" type="pull-off">
				<xs:annotation>
					<xs:documentation>The &lt;pull-off&gt; element is used in guitar and fretted instrument notation. Since a single slur can be marked over many notes, the &lt;pull-off&gt; element is separate so the individual pair of notes can be specified. The element content can be used to specify how the &lt;pull-off&gt; should be notated. An empty element leaves this choice up to the application.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="bend" type="bend">
				<xs:annotation>
					<xs:documentation>The &lt;bend&gt; element is used in guitar notation and tablature. A single note with a bend and release will contain two &lt;bend&gt; elements: the first to represent the bend and the second to represent the release.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="tap" type="tap">
				<xs:annotation>
					<xs:documentation>The &lt;tap&gt; element indicates a tap on the fretboard. The element content allows specification of the notation; + and T are common choices.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="heel" type="heel-toe">
				<xs:annotation>
					<xs:documentation>The &lt;heel&gt; element is used with organ pedals.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="toe" type="heel-toe">
				<xs:annotation>
					<xs:documentation>The &lt;toe&gt; element is used with organ pedals.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="fingernails" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;fingernails&gt; element is used in notation for harp and other plucked string instruments.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="hole" type="hole">
				<xs:annotation>
					<xs:documentation>The &lt;hole&gt; element represents the symbols used for woodwind and brass fingerings as well as other notations.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="arrow" type="arrow">
				<xs:annotation>
					<xs:documentation>The &lt;arrow&gt; element represents an arrow used for a musical technical indication. It can represent both Unicode and Standard Music Font Layout (SMuFL) arrows. The smufl attribute distinguishes different SMuFL glyphs that have an arrow appearance such as arrowBlackUp, guitarStrumUp, or handbellsSwingUp. The specified glyph should match the descriptive representation.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="handbell" type="handbell">
				<xs:annotation>
					<xs:documentation>The &lt;handbell&gt; element represents notation for various techniques used in handbell and handchime music.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="brass-bend" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;brass-bend&gt; element represents the u-shaped bend symbol used in brass notation, distinct from the &lt;bend&gt; element used in guitar music.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="flip" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;flip&gt; element represents the flip symbol used in brass notation.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="smear" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;smear&gt; element represents the tilde-shaped smear symbol used in brass notation.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="open" type="empty-placement-smufl">
				<xs:annotation>
					<xs:documentation>The &lt;open&gt; element represents the open symbol, which looks like a circle. The smufl attribute can be used to distinguish different Standard Music Font Layout (SMuFL) glyphs that have a similar appearance such as brassMuteOpen and guitarOpenPedal. If not present, the default glyph is brassMuteOpen.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="half-muted" type="empty-placement-smufl">
				<xs:annotation>
					<xs:documentation>The &lt;half-muted&gt; element represents the half-muted symbol, which looks like a circle with a plus sign inside. The smufl attribute can be used to distinguish different SMuFL glyphs that have a similar appearance such as brassMuteHalfClosed and guitarHalfOpenPedal. If not present, the default glyph is brassMuteHalfClosed.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="harmon-mute" type="harmon-mute">
				<xs:annotation>
					<xs:documentation>The &lt;harmon-mute&gt; element represents the symbols used for harmon mutes in brass notation.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="golpe" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The &lt;golpe&gt; element represents the golpe symbol that is used for tapping the pick guard in guitar music.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="other-technical" type="other-placement-text">
				<xs:annotation>
					<xs:documentation>The &lt;other-technical&gt; element is used to define any technical indications not yet in the MusicXML format. The smufl attribute can be used to specify a particular glyph, allowing application interoperability without requiring every Standard Music Font Layout (SMuFL) technical indication to have a MusicXML element equivalent. Using the &lt;other-technical&gt; element without the smufl attribute allows for extended representation, though without application interoperability.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:choice>
		<xs:attributeGroup ref="optional-unique-id"/>
	</xs:complexType>
```
