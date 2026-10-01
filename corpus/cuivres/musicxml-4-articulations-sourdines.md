---
titre: "MusicXML 4.0 (W3C) — définitions des sourdines (mute) et des articulations scoop/plop/doit/falloff/shake — extrait du schéma"
source: https://raw.githubusercontent.com/w3c/musicxml/v4.0/schema/musicxml.xsd
recupere_le: 2026-09-24
mode: texte integral (extrait)
langue: en
axe: articulations ; norme
skills: studio-grade-brass-sound-design
usage: copie personnelle pour recherche locale (Ollama) ; droits des auteurs cités
---

```xml
<xs:simpleType name="mute">
		<xs:annotation>
			<xs:documentation>The mute type represents muting for different instruments, including brass, winds, and strings. The on and off values are used for undifferentiated mutes. The remaining values represent specific mutes.</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:enumeration value="on"/>
			<xs:enumeration value="off"/>
			<xs:enumeration value="straight"/>
			<xs:enumeration value="cup"/>
			<xs:enumeration value="harmon-no-stem"/>
			<xs:enumeration value="harmon-stem"/>
			<xs:enumeration value="bucket"/>
			<xs:enumeration value="plunger"/>
			<xs:enumeration value="hat"/>
			<xs:enumeration value="solotone"/>
			<xs:enumeration value="practice"/>
			<xs:enumeration value="stop-mute"/>
			<xs:enumeration value="stop-hand"/>
			<xs:enumeration value="echo"/>
			<xs:enumeration value="palm"/>
		</xs:restriction>
	</xs:simpleType>

	<

<xs:complexType name="articulations">
		<xs:annotation>
			<xs:documentation>Articulations and accents are grouped together here.</xs:documentation>
		</xs:annotation>
		<xs:choice minOccurs="0" maxOccurs="unbounded">
			<xs:element name="accent" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The accent element indicates a regular horizontal accent mark.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="strong-accent" type="strong-accent">
				<xs:annotation>
					<xs:documentation>The strong-accent element indicates a vertical accent mark.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="staccato" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The staccato element is used for a dot articulation, as opposed to a stroke or a wedge.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="tenuto" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The tenuto element indicates a tenuto line symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="detached-legato" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The detached-legato element indicates the combination of a tenuto line and staccato dot symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="staccatissimo" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The staccatissimo element is used for a wedge articulation, as opposed to a dot or a stroke.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="spiccato" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The spiccato element is used for a stroke articulation, as opposed to a dot or a wedge.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="scoop" type="empty-line">
				<xs:annotation>
					<xs:documentation>The scoop element is an indeterminate slide attached to a single note. The scoop appears before the main note and comes from below the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="plop" type="empty-line">
				<xs:annotation>
					<xs:documentation>The plop element is an indeterminate slide attached to a single note. The plop appears before the main note and comes from above the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="doit" type="empty-line">
				<xs:annotation>
					<xs:documentation>The doit element is an indeterminate slide attached to a single note. The doit appears after the main note and goes above the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="falloff" type="empty-line">
				<xs:annotation>
					<xs:documentation>The falloff element is an indeterminate slide attached to a single note. The falloff appears after the main note and goes below the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="breath-mark" type="breath-mark"/>
			<xs:element name="caesura" type="caesura"/>
			<xs:element name="stress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The stress element indicates a stressed note.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="unstress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The unstress element indicates an unstressed note. It is often notated using a u-shaped symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="soft-accent" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The soft-accent element indicates a soft accent that is not as heavy as a normal accent. It is often notated as &lt;&gt;. It can be combined with other articulations to implement the first eight symbols in the SMuFL Articulation supplement range.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="other-articulation" type="other-placement-text">
				<xs:annotation>
					<xs:documentation>The other-articulation element is used to define any articulations not yet in the MusicXML format. The smufl attribute can be used to specify a particular articulation, allowing application interoperability without requiring every SMuFL articulation to have a MusicXML element equivalent. Using the other-articulation element without the smufl attribute allows for extended representation, though without application interoperability.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:choice>
		<xs:attributeGroup ref="optional-unique-id"/>
	</xs:complexType>

	

<xs:element name="scoop" type="empty-line">
				<xs:annotation>
					<xs:documentation>The scoop element is an indeterminate slide attached to a single note. The scoop appears before the main note and comes from below the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="plop" type="empty-line">
				<xs:annotation>
					<xs:documentation>The plop element is an indeterminate slide attached to a single note. The plop appears before the main note and comes from above the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="doit" type="empty-line">
				<xs:annotation>
					<xs:documentation>The doit element is an indeterminate slide attached to a single note. The doit appears after the main note and goes above the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="falloff" type="empty-line">
				<xs:annotation>
					<xs:documentation>The falloff element is an indeterminate slide attached to a single note. The falloff appears after the main note and goes below the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="breath-mark" type="breath-mark"/>
			<xs:element name="caesura" type="caesura"/>
			<xs:element name="stress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The stress element indicates a stressed note.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="unstress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The unstress element indicates an unstressed note. It is often notated using a u-shaped symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="soft-accent" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The soft-accent element indicates a soft accent that is not as heavy as a normal accent. It is often notated as &lt;&gt;. It can be combined with other articulations to implement the first eight symbols in the SMuFL Articulation supplement range.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="other-articulation" type="other-placement-text">
				<xs:annotation>
					<xs:documentation>The other-articulation element is used to define any articulations not yet in the MusicXML format. The smufl attribute can be used to specify a particular articulation, allowing application interoperability without requiring every SMuFL articulation to have a MusicXML element equivalent. Using the other-articulation element without the smufl attribute allows for extended representation, though without application interoperability.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:choice>
		<xs:attributeGroup ref="optional-unique-id"/>
	</xs:complexType>

	

<xs:element name="plop" type="empty-line">
				<xs:annotation>
					<xs:documentation>The plop element is an indeterminate slide attached to a single note. The plop appears before the main note and comes from above the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="doit" type="empty-line">
				<xs:annotation>
					<xs:documentation>The doit element is an indeterminate slide attached to a single note. The doit appears after the main note and goes above the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="falloff" type="empty-line">
				<xs:annotation>
					<xs:documentation>The falloff element is an indeterminate slide attached to a single note. The falloff appears after the main note and goes below the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="breath-mark" type="breath-mark"/>
			<xs:element name="caesura" type="caesura"/>
			<xs:element name="stress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The stress element indicates a stressed note.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="unstress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The unstress element indicates an unstressed note. It is often notated using a u-shaped symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="soft-accent" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The soft-accent element indicates a soft accent that is not as heavy as a normal accent. It is often notated as &lt;&gt;. It can be combined with other articulations to implement the first eight symbols in the SMuFL Articulation supplement range.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="other-articulation" type="other-placement-text">
				<xs:annotation>
					<xs:documentation>The other-articulation element is used to define any articulations not yet in the MusicXML format. The smufl attribute can be used to specify a particular articulation, allowing application interoperability without requiring every SMuFL articulation to have a MusicXML element equivalent. Using the other-articulation element without the smufl attribute allows for extended representation, though without application interoperability.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:choice>
		<xs:attributeGroup ref="optional-unique-id"/>
	</xs:complexType>

	

<xs:element name="doit" type="empty-line">
				<xs:annotation>
					<xs:documentation>The doit element is an indeterminate slide attached to a single note. The doit appears after the main note and goes above the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="falloff" type="empty-line">
				<xs:annotation>
					<xs:documentation>The falloff element is an indeterminate slide attached to a single note. The falloff appears after the main note and goes below the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="breath-mark" type="breath-mark"/>
			<xs:element name="caesura" type="caesura"/>
			<xs:element name="stress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The stress element indicates a stressed note.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="unstress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The unstress element indicates an unstressed note. It is often notated using a u-shaped symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="soft-accent" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The soft-accent element indicates a soft accent that is not as heavy as a normal accent. It is often notated as &lt;&gt;. It can be combined with other articulations to implement the first eight symbols in the SMuFL Articulation supplement range.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="other-articulation" type="other-placement-text">
				<xs:annotation>
					<xs:documentation>The other-articulation element is used to define any articulations not yet in the MusicXML format. The smufl attribute can be used to specify a particular articulation, allowing application interoperability without requiring every SMuFL articulation to have a MusicXML element equivalent. Using the other-articulation element without the smufl attribute allows for extended representation, though without application interoperability.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:choice>
		<xs:attributeGroup ref="optional-unique-id"/>
	</xs:complexType>

	

<xs:element name="falloff" type="empty-line">
				<xs:annotation>
					<xs:documentation>The falloff element is an indeterminate slide attached to a single note. The falloff appears after the main note and goes below the main pitch.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="breath-mark" type="breath-mark"/>
			<xs:element name="caesura" type="caesura"/>
			<xs:element name="stress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The stress element indicates a stressed note.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="unstress" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The unstress element indicates an unstressed note. It is often notated using a u-shaped symbol.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="soft-accent" type="empty-placement">
				<xs:annotation>
					<xs:documentation>The soft-accent element indicates a soft accent that is not as heavy as a normal accent. It is often notated as &lt;&gt;. It can be combined with other articulations to implement the first eight symbols in the SMuFL Articulation supplement range.</xs:documentation>
				</xs:annotation>
			</xs:element>
			<xs:element name="other-articulation" type="other-placement-text">
				<xs:annotation>
					<xs:documentation>The other-articulation element is used to define any articulations not yet in the MusicXML format. The smufl attribute can be used to specify a particular articulation, allowing application interoperability without requiring every SMuFL articulation to have a MusicXML element equivalent. Using the other-articulation element without the smufl attribute allows for extended representation, though without application interoperability.</xs:documentation>
				</xs:annotation>
			</xs:element>
		</xs:choice>
		<xs:attributeGroup ref="optional-unique-id"/>
	</xs:complexType>

	

<xs:element name="shake" type="empty-trill-sound">
					<xs:annotation>
						<xs:documentation>The shake element has a similar appearance to an inverted-mordent element.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="wavy-line" type="wavy-line"/>
				<xs:element name="mordent" type="mordent">
					<xs:annotation>
						<xs:documentation>The mordent element represents the sign with the vertical line. The choice of which mordent sign is inverted differs between MusicXML and SMuFL. The long attribute is "no" by default.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="inverted-mordent" type="mordent">
					<xs:annotation>
						<xs:documentation>The inverted-mordent element represents the sign without the vertical line. The choice of which mordent is inverted differs between MusicXML and SMuFL. The long attribute is "no" by default.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="schleifer" type="empty-placement">
					<xs:annotation>
						<xs:documentation>The name for this ornament is based on the German, to avoid confusion with the more common slide element defined earlier.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="tremolo" type="tremolo"/>
				<xs:element name="haydn" type="empty-trill-sound">
					<xs:annotation>
						<xs:documentation>The haydn element represents the Haydn ornament. This is defined in SMuFL as ornamentHaydn.</xs:documentation>
					</xs:annotation>
				</xs:element>
				<xs:element name="other-ornament" type="other-placement-text">
					<xs:annotation>
					<xs:documentation>The other-ornament element is used to define any ornaments not yet in the MusicXML format. The smufl attribute can be used to specify a particular ornament, allowing application interoperability without requiring every SMuFL ornament to have a MusicXML element equivalent. Using the other-ornament element without the smufl attribute allows for extended representation, though without application interoperability.</xs:documentation>
					</xs:annotation>
				</xs:element>
			</xs:choice>
			<xs:element name="accidental-mark" type="accidental-mark" minOccurs="0" maxOccurs="unbounded"/>
		</xs:sequence>
		<xs:attributeGroup ref="optional-unique-id"/>
	</xs:complexType>

	

<xs:simpleType name="harmon-closed-value">
		<xs:annotation>
			<xs:documentation>The harmon-closed-value type represents whether the harmon mute is closed, open, or half-open.</xs:documentation>
		</xs:annotation>
		<xs:restriction base="xs:string">
			<xs:enumeration value="yes"/>
			<xs:enumeration value="no"/>
			<xs:enumeration value="half"/>
		</xs:restriction>
	</xs:simpleType>

	<
```