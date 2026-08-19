---
name: antrag-s05000001287
description: Führt Antragstellende durch „Antrag auf Erteilung einer Fahrschulerlaubnis" (FIM S05000001287 3.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf Erteilung einer Fahrschulerlaubnis

- **FIM-ID:** `S05000001287 3.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 18 FahrlG vom 25.08.1969; § 18 (1a) FahrlG2018DV vom 2.01.2018; § 2 SBGG vom 1.11.2024; TR-03127 des BSI V1.40, S. 17, Datengruppe 8 vom 6.10.2021; § 111 OWiG vom 19.02.1987; § 5 (2) PAuswG vom 1.11.2010; § 3 BMG vom 3.05.2013; Art. 6 (1) VO (EU) 2016/679 vom 27.04.2016; § 14 GewO vom 22.02.1999; Art. 6 (1) DSGVO vom 24.05.2016; § 705 ff. BGB vom 1.01.1900; § 8 ff. HGB vom 1.01.1900; AktG vom 1.01.1966; GmbHG vom. 23.10.2024; HGB vom 1.01.1900; § 22 FahrlG vom 25.08.1969; § 26 FahrlG vom 25.08.1969; § 58 FahrlG vom 25.08.1969; § 12 SBGG vom 1.11.2024
- **Kompiliert:** 2026-08-13T15:39:13Z aus https://fimportal.de/api/v1/schemas/S05000001287/3.0.0/xdf
- **Umfang:** 453 Felder, 187 gesicherte Bedingungen, 47 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet werden (Leistungssteckbrief nicht abrufbar). Zu Fristen, Kosten, Unterlagen und Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle verweisen.

## Felder

### Art der Erteilung (`G05000011579`)

- **Was möchten Sie beantragen?** (`F05000017366`) — Pflicht
  - Rechtsgrundlage: § 17 (2) FahrlG; § 30 FahrlG

### Art der Erteilung › Für welche Fahrlehrerlaubnisklasse(n) stellen Sie den Antrag? (`G05000011580`)

- **A** (`F05000017367`) — optional
  - Rechtsgrundlage: § 17 (2) FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse A berechtigt zur Ausbildung in den Fahrerlaubnisklassen AM, A1, A2 und A.
- **BE** (`F05000017368`) — optional
  - Rechtsgrundlage: § 17 (2) FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse BE berechtigt zur Ausbildung in den Fahrerlaubnisklassen B, BE und L.
- **CE** (`F05000017369`) — optional
  - Rechtsgrundlage: § 17 (2) FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse CE berechtigt zur Ausbildung in den Fahrerlaubnisklassen C1, C1E, C, CE und T.
- **DE** (`F05000017370`) — optional
  - Rechtsgrundlage: § 17 (2) FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse DE berechtigt zur Ausbildung in den Fahrerlaubnisklassen D1, D1E, D und DE.

### Angaben zum Unternehmen › Betriebsangaben (`G05000011753`)

- **Bundeseinheitliche Wirtschaftsnummer** (`F60000000371`) — optional
  - Rechtsgrundlage: § 2 UBRegG; urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Rechtsform** (`F60000000339`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Juristische Person.Rechtsform Version 1.1; verwendet verwendet urn:xoev-de:xunternehmen:codeliste:rechtsformen_2
- **Art der Eintragung oder des Registers** (`F60000000347`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2
  - Hilfe: Geben Sie an, um welche Art von Eintrag es sich handelt.
- **Registergericht** (`F60000000325`) — optional
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Stiftungsverzeichnis (Freitext)** (`F05000018301`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
  - Hilfe: Bei Einträgen im Stiftungsverzeichnis: Angabe des Bundeslandes bzw. der Behörde, in dessen oder deren Stiftungsverzeichnis der Eintrag geführt wird.
- **Ort des Registereintrags** (`F60000000327`) — optional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2
- **Staat** (`F60000000261`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
  - Hilfe: Geben Sie den Namen des Staates bzw. des Landes an, Beispiel Deutschland, Frankreich, ...
- **Nummer des Registereintrages** (`F60000000328`) — optional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Eingetragener Name** (`F60000000319`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Geschäftsbezeichnung** (`F60000000320`) — optional, conditional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.

### Angaben zum Unternehmen › Ansprechperson (`G05000011750`)

- **Geschlecht** (`F60000000332`) — optional
  - Rechtsgrundlage: XPersonenstand:Code.Geschlecht Version 1.7.5; basierend auf DSMeld.Code.Geschlecht urn:de:dsmeld:schluesseltabelle:geschlecht Version 3
  - Hilfe: Geben Sie das Geschlecht an, das auch beim Personenstandsregister oder Standesamt hinterlegt ist.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Angaben zum Unternehmen › Ansprechperson › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Ansprechperson › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Ansprechperson › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zum Unternehmen › Ansprechperson › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Ansprechperson › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Unternehmen › Ansprechperson › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Ansprechperson › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Ansprechperson › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Angaben zum Unternehmen › Ansprechperson › Aufenthaltsgenehmigung (`G05000011749`)

- **Welchen Status hat Ihre Aufenthaltsgenehmigung?** (`F05000017638`) — Pflicht
  - Rechtsgrundlage: xUnternehmen; WiPG NRW; WiPG-DVO
- **Ausstellende Behörde** (`F60000000292`) — optional, conditional
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Ausstellungsdatum** (`F60000000294`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Nachweis** (`F60000000296`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Fügen Sie einen Nachweis bei, der die Angaben bestätigt.

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP (`G05000011754`)

- **Art des gesetzlichen Vertreters** (`F05000017263`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:codeliste:artgesetzlichervertreter

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter (`G05000011751`)

- **Geschlecht** (`F60000000332`) — optional
  - Rechtsgrundlage: XPersonenstand:Code.Geschlecht Version 1.7.5; basierend auf DSMeld.Code.Geschlecht urn:de:dsmeld:schluesseltabelle:geschlecht Version 3
  - Hilfe: Geben Sie das Geschlecht an, das auch beim Personenstandsregister oder Standesamt hinterlegt ist.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Gesetzlicher Vertreter-  Natürliche Person** (`F05000017639`) — optional
  - Rechtsgrundlage: § 8 ff. HGB; § 705 ff. BGB

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Aufenthaltsgenehmigung (`G05000011749`)

- **Welchen Status hat Ihre Aufenthaltsgenehmigung?** (`F05000017638`) — Pflicht
  - Rechtsgrundlage: xUnternehmen; WiPG NRW; WiPG-DVO
- **Ausstellende Behörde** (`F60000000292`) — optional, conditional
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Ausstellungsdatum** (`F60000000294`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Nachweis** (`F60000000296`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Fügen Sie einen Nachweis bei, der die Angaben bestätigt.

### Angaben zum Unternehmen › Nicht Natürliche Person › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Nicht Natürliche Person › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zum Unternehmen › Nicht Natürliche Person › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Unternehmen › Nicht Natürliche Person › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Nicht Natürliche Person › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP (`G05000011756`)

- **Art des gesetzlichen Vertreters** (`F60000000375`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:codeliste:artgesetzlichervertreter

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter (`G05000011751`)

- **Geschlecht** (`F60000000332`) — optional
  - Rechtsgrundlage: XPersonenstand:Code.Geschlecht Version 1.7.5; basierend auf DSMeld.Code.Geschlecht urn:de:dsmeld:schluesseltabelle:geschlecht Version 3
  - Hilfe: Geben Sie das Geschlecht an, das auch beim Personenstandsregister oder Standesamt hinterlegt ist.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Gesetzlicher Vertreter-  Natürliche Person** (`F05000017639`) — optional
  - Rechtsgrundlage: § 8 ff. HGB; § 705 ff. BGB

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Aufenthaltsgenehmigung (`G05000011749`)

- **Welchen Status hat Ihre Aufenthaltsgenehmigung?** (`F05000017638`) — Pflicht
  - Rechtsgrundlage: xUnternehmen; WiPG NRW; WiPG-DVO
- **Ausstellende Behörde** (`F60000000292`) — optional, conditional
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Ausstellungsdatum** (`F60000000294`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Nachweis** (`F60000000296`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Fügen Sie einen Nachweis bei, der die Angaben bestätigt.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter (`G05000011757`)

- **Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?** (`F05000018285`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Gesellschafterart** (`F60000000342`) — optional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Gesellschafter.Art Version 1.1; verwendet urn:xoev-de:xunternehmen:codeliste:artgesellschafterpersonengesellschaft Version 1

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Betriebsangaben (`G05000011753`)

- **Bundeseinheitliche Wirtschaftsnummer** (`F60000000371`) — optional
  - Rechtsgrundlage: § 2 UBRegG; urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Rechtsform** (`F60000000339`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Juristische Person.Rechtsform Version 1.1; verwendet verwendet urn:xoev-de:xunternehmen:codeliste:rechtsformen_2
- **Art der Eintragung oder des Registers** (`F60000000347`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2
  - Hilfe: Geben Sie an, um welche Art von Eintrag es sich handelt.
- **Registergericht** (`F60000000325`) — optional
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Stiftungsverzeichnis (Freitext)** (`F05000018301`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
  - Hilfe: Bei Einträgen im Stiftungsverzeichnis: Angabe des Bundeslandes bzw. der Behörde, in dessen oder deren Stiftungsverzeichnis der Eintrag geführt wird.
- **Ort des Registereintrags** (`F60000000327`) — optional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2
- **Staat** (`F60000000261`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
  - Hilfe: Geben Sie den Namen des Staates bzw. des Landes an, Beispiel Deutschland, Frankreich, ...
- **Nummer des Registereintrages** (`F60000000328`) — optional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Eingetragener Name** (`F60000000319`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Geschäftsbezeichnung** (`F60000000320`) — optional, conditional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter (`G05000011751`)

- **Geschlecht** (`F60000000332`) — optional
  - Rechtsgrundlage: XPersonenstand:Code.Geschlecht Version 1.7.5; basierend auf DSMeld.Code.Geschlecht urn:de:dsmeld:schluesseltabelle:geschlecht Version 3
  - Hilfe: Geben Sie das Geschlecht an, das auch beim Personenstandsregister oder Standesamt hinterlegt ist.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Gesetzlicher Vertreter-  Natürliche Person** (`F05000017639`) — optional
  - Rechtsgrundlage: § 8 ff. HGB; § 705 ff. BGB

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Aufenthaltsgenehmigung (`G05000011749`)

- **Welchen Status hat Ihre Aufenthaltsgenehmigung?** (`F05000017638`) — Pflicht
  - Rechtsgrundlage: xUnternehmen; WiPG NRW; WiPG-DVO
- **Ausstellende Behörde** (`F60000000292`) — optional, conditional
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Ausstellungsdatum** (`F60000000294`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Nachweis** (`F60000000296`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Fügen Sie einen Nachweis bei, der die Angaben bestätigt.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Nicht natürliche Person - Vertreter (`G05000011758`)

- **Gesetzlicher Vertreter JP Freitext** (`F05000017240`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Gesellschafter Freitext** (`F05000017264`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zur Fahrschule (`G05000011578`)

- **Name der Fahrschule** (`F05000017365`) — Pflicht
  - Rechtsgrundlage: § 26 (2) S. 1 Nr. 1 FahrlG
- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1

### Angaben zur Fahrschule › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zur Fahrschule › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zur Fahrschule › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: § 69 GewO
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zur Fahrschule › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zur Fahrschule › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zur Fahrschule › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Vorhergehende Anträge (`G05000011559`)

- **Wurde bereits ein Antrag bei einer anderen Behörde gestellt?** (`F05000017330`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG

### Vorhergehende Anträge › Angaben zur Behörde der bisherigen Antragstellung (`G05000011560`)

- **Name der Behörde** (`F05000017331`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Vorhergehende Anträge › Angaben zu Fahrschulerlaubnis (`G05000011561`)

- **Sind oder waren Sie im Besitz einer Fahrschulerlaubnis?** (`F05000017332`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG

### Vorhergehende Anträge › Angaben zu Fahrschulerlaubnis › Ehemalige Fahrschulerlaubnis (`G05000011562`)

- **Erteilungsdatum ehemaliger Fahrschulerlaubnis** (`F05000017333`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG
- **Art der Erteilung (z.B. Ersterteilung)** (`F05000017334`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG
- **Geben Sie die höchste Klasse Ihrer Fahrschulerlaubnis an:** (`F05000017338`) — Pflicht
  - Rechtsgrundlage: § 17 (2) FahrlG; § 22 (1) S. 2 Nr. 4 FahrlG

### Vorhergehende Anträge › Angaben zu Fahrschulerlaubnis › Ehemalige Fahrschulerlaubnis › Angaben zur ausstellenden Behörde (`G05000011563`)

- **Ausstellende Behörde** (`F60000000292`) — Pflicht
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Vorhergehende Anträge › Angaben zu Fahrschulerlaubnis › Ehemalige Fahrschulerlaubnis › Status Fahrschulerlaubnis (`G05000011566`)

- **Welchen Status hat die Fahrschulerlaubnis?** (`F05000017339`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG; §§ 33-34 FahrlG
- **Datum** (`F60000000030`) — Pflicht
  - Rechtsgrundlage: DIN 5008

### Vorhergehende Anträge › Angaben zu Fahrschulerlaubnis › Aktuelle Fahrschulerlaubnis (`G05000011567`)

- **Erteilungsdatum** (`F05000017340`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG
- **Geben Sie die höchste Klasse Ihrer Fahrschulerlaubnis an:** (`F05000017341`) — Pflicht
  - Rechtsgrundlage: § 17 (2) FahrlG; § 22 (1) S. 2 Nr. 4 FahrlG

### Vorhergehende Anträge › Angaben zu Fahrschulerlaubnis › Aktuelle Fahrschulerlaubnis › Angaben zur ausstellenden Behörde (`G05000011568`)

- **Name der Behörde** (`F05000017342`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 4 FahrlG
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) (`G05000012270`)

- **Geschlecht** (`F60000000332`) — optional
  - Rechtsgrundlage: XPersonenstand:Code.Geschlecht Version 1.7.5; basierend auf DSMeld.Code.Geschlecht urn:de:dsmeld:schluesseltabelle:geschlecht Version 3
  - Hilfe: Geben Sie das Geschlecht an, das auch beim Personenstandsregister oder Standesamt hinterlegt ist.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Aufenthaltsgenehmigung (`G05000011749`)

- **Welchen Status hat Ihre Aufenthaltsgenehmigung?** (`F05000017638`) — Pflicht
  - Rechtsgrundlage: xUnternehmen; WiPG NRW; WiPG-DVO
- **Ausstellende Behörde** (`F60000000292`) — optional, conditional
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Ausstellungsdatum** (`F60000000294`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Nachweis** (`F60000000296`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Fügen Sie einen Nachweis bei, der die Angaben bestätigt.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP (`G05000011754`)

- **Art des gesetzlichen Vertreters** (`F05000017263`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:codeliste:artgesetzlichervertreter

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter (`G05000011751`)

- **Geschlecht** (`F60000000332`) — optional
  - Rechtsgrundlage: XPersonenstand:Code.Geschlecht Version 1.7.5; basierend auf DSMeld.Code.Geschlecht urn:de:dsmeld:schluesseltabelle:geschlecht Version 3
  - Hilfe: Geben Sie das Geschlecht an, das auch beim Personenstandsregister oder Standesamt hinterlegt ist.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — optional
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Gesetzlicher Vertreter-  Natürliche Person** (`F05000017639`) — optional
  - Rechtsgrundlage: § 8 ff. HGB; § 705 ff. BGB

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Kommunikation (`G05000011748`)

- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Telefaxnummer** (`F60000000241`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefaxnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefaxnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Webadresse / Website** (`F60000000321`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; ITU E.123; RFC 5322; RFC 5321 _(geerbt)_

### Verantwortliche Leitung (Fahrschulerlaubnis) › Antragsteller/Anzeigender (nicht geschäftlich) › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Aufenthaltsgenehmigung (`G05000011749`)

- **Welchen Status hat Ihre Aufenthaltsgenehmigung?** (`F05000017638`) — Pflicht
  - Rechtsgrundlage: xUnternehmen; WiPG NRW; WiPG-DVO
- **Ausstellende Behörde** (`F60000000292`) — optional, conditional
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Ausstellungsdatum** (`F60000000294`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Nachweis** (`F60000000296`) — optional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; xUnternehmen; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
  - Hilfe: Fügen Sie einen Nachweis bei, der die Angaben bestätigt.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Erteilte Fahrlehrerlaubnis (`G05000011583`)

- **Hinweis:** (`F05000017372`) — optional
  - Rechtsgrundlage: § 18 (2) FahrlG

### Verantwortliche Leitung (Fahrschulerlaubnis) › Erteilte Fahrlehrerlaubnis › Geben Sie an, welche Fahrlehrerlaubnisklassen Sie besitzen: (`G05000011477`)

- **A** (`F05000017266`) — Pflicht
  - Rechtsgrundlage: § 1 (2) FahrlG; § 4 (1) S. 1 FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse A berechtigt zur Ausbildung in den Fahrerlaubnisklassen AM, A1, A2 und A.
- **BE** (`F05000017269`) — Pflicht
  - Rechtsgrundlage: § 1 (2) FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse BE berechtigt zur Ausbildung in den Fahrerlaubnisklassen B, BE und L.
- **CE** (`F05000017267`) — Pflicht
  - Rechtsgrundlage: § 1 (2) FahrlG; § 4 (1) S. 1 FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse CE berechtigt zur Ausbildung in den Fahrerlaubnisklassen C1, C1E, C, CE und T.
- **DE** (`F05000017268`) — Pflicht
  - Rechtsgrundlage: § 1 (2) FahrlG; § 4 (1) S. 1 FahrlG
  - Hilfe: Die Fahrlehrerlaubnisklasse DE berechtigt zur Ausbildung in den Fahrerlaubnisklassen D1, D1E, D und DE.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Erteilte Fahrlehrerlaubnis › Weitere Angaben zur Fahrlehrerlaubnis (`G05000011478`)

- **Sie haben die Fahrlehrerlaubnis seit:** (`F05000017270`) — Pflicht
  - Rechtsgrundlage: § 4 FahrlG; Anlage 1 S. 7 FahrlG

### Verantwortliche Leitung (Fahrschulerlaubnis) › Erteilte Fahrlehrerlaubnis › Weitere Angaben zur Fahrlehrerlaubnis › Prüfungsausschuss (`G05000011484`)

- **Bei welchem Prüfungsausschuss wurden die Prüfungen abgelegt?** (`F05000017271`) — Pflicht
  - Rechtsgrundlage: § 4 FahrlG; Anlage 1 S. 7 FahrlG _(geerbt)_
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Betriebswirtschaftliches Seminar Fahrschulen (`G05000011584`)

- **Hinweis:** (`F05000017373`) — optional
  - Rechtsgrundlage: § 22 (1) Nr 3 FahrlG
- **Verfügen Sie über eine Teilnahmebescheinigung für ein Fahrschulbetriebswirtschaftsseminar?** (`F05000017374`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 3 FahrlG

### Verantwortliche Leitung (Fahrschulerlaubnis) › Betriebswirtschaftliches Seminar Fahrschulen › Angaben zum Fahrschulbetriebswirtschaftsseminar (`G05000011585`)

- **Geben Sie das Ausstellungsdatum der Teilnahmebescheinigung an** (`F05000017375`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 3 FahrlG
- **Laden Sie hier Ihre Teilnahmebescheinigung am Lehrgang für Fahrschulbetriebswirtschaft hoch** (`F05000017376`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 3 FahrlG

### Verantwortliche Leitung (Fahrschulerlaubnis) › Betriebswirtschaftliches Seminar Fahrschulen › Angaben zum Fahrschulbetriebswirtschaftsseminar › Angaben zum Seminaranbieter (`G05000011556`)

- **Name des Seminaranbieters** (`F05000017323`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 3 FahrlG _(geerbt)_

### Verantwortliche Leitung (Fahrschulerlaubnis) › Betriebswirtschaftliches Seminar Fahrschulen › Angaben zum Fahrschulbetriebswirtschaftsseminar › Angaben zum Seminaranbieter › Anschrift (`G05000011492`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 3 FahrlG _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Betriebswirtschaftliches Seminar Fahrschulen › Angaben zum Fahrschulbetriebswirtschaftsseminar › Angaben zum Seminaranbieter › Anschrift › Anschrift Inland (`G05000011494`)

- **Adresssuche** (`F05000017298`) — optional
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift _(geerbt)_
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Betriebswirtschaftliches Seminar Fahrschulen › Angaben zum Fahrschulbetriebswirtschaftsseminar › Angaben zum Seminaranbieter › Anschrift › Auslandsanschrift (`G60000000091`)

- **Staat** (`F60000000261`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
  - Hilfe: Geben Sie den Namen des Staates bzw. des Landes an, Beispiel Deutschland, Frankreich, ...

### Verantwortliche Leitung (Fahrschulerlaubnis) › Betriebswirtschaftliches Seminar Fahrschulen › Angaben zum Fahrschulbetriebswirtschaftsseminar › Angaben zum Seminaranbieter › Anschrift › Auslandsanschrift › Ausländische Anschrift (`G60000000092`)

- **Anschriftzeile** (`F60000000262`) — optional
  - Rechtsgrundlage: XInneres.Auslandsanschrift.Anschriftzone.zeile.anschrift Version 8
  - Hilfe: Geben Sie die ausländische Anschrift an

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer (`G05000011588`)

- **Hinweis:** (`F05000017377`) — optional
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG
- **Besteht oder bestand ein Beschäftigungsverhältnis über insgesamt mindestens zwei Jahre als Fahrlehrer*in?** (`F05000017378`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG
- **Hinweis:** (`F05000017379`) — optional, conditional
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Zeitraum der Anstellung (`G05000011558`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG _(geerbt)_

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Angaben zur Fahrschule (`G05000011578`)

- **Name der Fahrschule** (`F05000017365`) — Pflicht
  - Rechtsgrundlage: § 26 (2) S. 1 Nr. 1 FahrlG
- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Angaben zur Fahrschule › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoev-de:xunternehmen:standard:basismodul; urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Angaben zur Fahrschule › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Angaben zur Fahrschule › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: § 69 GewO
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Früherer Gemeindename** (`F60000000364`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul_1.1
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Angaben zur Fahrschule › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Angaben zur Fahrschule › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle › Angaben zur Fahrschule › Anschrift › Anschrift Ausland (`G60000000191`)

- **Straße** (`F60000000243`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000382`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul
  - Hilfe: Geben Sie die Postleitzahl des Ortes an.
- **Ort** (`F60000000247`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Angaben zur Arbeitsstelle (`G05000011589`)

- **Anstellungsvertrag** (`F05000017326`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG _(geerbt)_
  - Hilfe: Bitte laden Sie den Anstellungsvertrag hoch. 
Bitte beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Nachweis einer mindestens zweijährigen hauptberuflichen Fahrlehrertätigkeit** (`F05000007068`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 4; § 22 (1) S. 2 Nr. 2 FahrlG
  - Hilfe: Laden Sie den Nachweis einer mindestens zweijährigen hauptberuflichen Fahrlehrertätigkeit hoch.  Dieser Nachweis kann zum Beispiel eine schriftliche Bestätigung der Inhaberin oder des Inhabers der Fahrschulen sein, bei denen bisher Beschäftigungsverhältnisse bestanden.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Verantwortliche Leitung (Fahrschulerlaubnis) › Berufserfahrung Fahrlehrer › Nachweise  Fahrschulleitung (`G05000011590`)

- **Ausweisdokument** (`F05000017328`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG _(geerbt)_
  - Hilfe: Bitte laden Sie ein Foto des Personalausweises, des Nationalpasses oder eines anderen (amtlichen) Ausweisdokuments hoch. Bitte beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Führerschein** (`F05000017292`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 4 FahrlG _(geerbt)_
  - Hilfe: Laden Sie die Bescheinigungen der Fahrlehrerausbildungsstätte und der Ausbildungsfahrschule über die Teilnahme an der Einführungsphase hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Fahrlehrerschein** (`F05000007067`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 1 FahrlG
  - Hilfe: Laden Sie den Fahrlehrerschein hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Erklärung zu den beruflichen Verpflichtungen der Fahrschulleitung** (`F05000017380`) — Pflicht
  - Rechtsgrundlage: § 18 (2) FahrlG
  - Hilfe: Laden Sie eine Erklärung zu den beruflichen Verpflichtungen der Fahrschulleitung hoch. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Angaben zu den Räumlichkeiten der Fahrschule › Eigentumsform der Räumlichkeiten (`G05000011570`)

- **Geben Sie die Eigentumsform der Räumlichkeiten an:** (`F05000017343`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
- **Mietvertrag** (`F05000017344`) — optional, conditional
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
  - Hilfe: Laden Sie den Mietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Eigentumsnachweis** (`F05000017345`) — optional, conditional
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
  - Hilfe: Laden Sie den Kauf- bzw. Pachtvertrag hoch. Legen Sie außerdem, wenn vorliegend, den aktuellen Grundbuchauszug vor. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Angaben zu den Räumlichkeiten der Fahrschule › Gemeinsame Raumnutzung (`G05000011571`)

- **Nutzen Sie die Räumlichkeiten gemeinsam mit einer anderen Fahrschule bzw. einem anderen Betrieb?** (`F05000017346`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG

### Angaben zu den Räumlichkeiten der Fahrschule › Gemeinsame Raumnutzung › Angaben zum anderen Betrieb oder zur anderen Fahrschule (`G05000011572`)

- **Name der Fahrschule oder des anderen Betriebs** (`F05000017347`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
- **Name des Inhabers / der Inhaberin oder der verantwortlichen Leitung** (`F05000017348`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
- **Nutzungsvertrag** (`F05000017349`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
  - Hilfe: Laden Sie hier den Nutzungsvertrag hoch. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Angaben zu den Räumlichkeiten der Fahrschule (`G05000011569`)

- **Maßstabsgerechter Plan der Unterrrichtsräume mit Angaben über deren Ausstattung und die Raummaße** (`F05000017350`) — Pflicht
  - Rechtsgrundlage: § 22 (1) S. 2 Nr. 5 FahrlG
  - Hilfe: Laden Sie einen maßstabsgerechten Plan der Unterrichtsräume mit Angaben über deren Ausstattung (Mobiliar, Art der Visualisierung) und die Raummaße (Länge, Breite, Höhe) hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Betretungsbefugnis** (`F05000017351`) — Pflicht
  - Rechtsgrundlage: § 51 (4) S. 1 Nr. 1 FahrlG
  - Hilfe: Laden Sie die Betretungsbefugnis hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Lehrfahrzeuge › Allgemeine Informationen zum Lehrfahrzeug (`G05000011574`)

- **Hinweis Lehrfahrzeuge Klasse B** (`F05000017352`) — optional
  - Rechtsgrundlage: § 5 FahrlG2018DV
- **Hinweis Lehrfahrzeuge Klasse A** (`F05000017353`) — optional
  - Rechtsgrundlage: § 5 FahrlG2018DV
- **Hinweis Lehrfahrzeuge Klasse C und D** (`F05000017354`) — optional
  - Rechtsgrundlage: § 5 FahrlG2018DV
- **Allgemeiner Hinweis zu Lehrfahrzeugen** (`F05000017355`) — optional
  - Rechtsgrundlage: § 5 FahrlG2018DV

### Lehrfahrzeuge › Angaben zu den Lehrfahrzeugen (`G05000011575`)

- **Anzahl der Lehrfahrzeuge** (`F05000017356`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG; § 22 (1) S. 2 Nr. 7 FahrlG

### Lehrfahrzeuge › Angaben zu den Lehrfahrzeugen › Lehrfahrzeug (`G05000011576`)

- **Fahrzeugtyp** (`F05000017357`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG; § 22 (1) S. 2 Nr. 7 FahrlG
- **Es handelt sich um ein:** (`F05000017358`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG; § 22 (1) S. 2 Nr. 7 FahrlG
- **Eigentumsnachweis** (`F05000017359`) — optional, conditional
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
  - Hilfe: Laden Sie den Eigentumsnachweis hoch. Als Eigentumsnachweis ist der aktuelle Grundbuchauszug vorzulegen. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Mietvertrag** (`F05000017360`) — optional, conditional
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
  - Hilfe: Laden Sie den Mietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Leasingvertrag** (`F05000017361`) — optional, conditional
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
  - Hilfe: Laden Sie den Leasingvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Ohne Gruppe

- **Soll der Bescheid an eine andere Adresse oder an eine andere Person geschickt werden?** (`F05000018430`) — Pflicht
  - Rechtsgrundlage: § 18 FahrlG vom 25.08.1969; § 18 (1a) FahrlG2018DV vom 2.01.2018; § 2 SBGG vom 1.11.2024; TR-03127 des BSI V1.40, S. 17, Datengruppe 8 vom 6.10.2021; § 111 OWiG vom 19.02.1987; § 5 (2) PAuswG vom 1.11.2010; § 3 BMG vom 3.05.2013; Art. 6 (1) VO (EU) 2016/679 vom 27.04.2016; § 14 GewO vom 22.02.1999; Art. 6 (1) DSGVO vom 24.05.2016; § 705 ff. BGB vom 1.01.1900; § 8 ff. HGB vom 1.01.1900; AktG vom 1.01.1966; GmbHG vom. 23.10.2024; HGB vom 1.01.1900; § 22 FahrlG vom 25.08.1969; § 26 FahrlG vom 25.08.1969; § 58 FahrlG vom 25.08.1969; § 12 SBGG vom 1.11.2024 _(geerbt)_

### Abweichender Bescheidempfänger (`G05000012376`)

- **Art des Bescheides** (`F05000017257`) — Pflicht, conditional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Abweichender Bescheidempfänger › Ansprechperson (`G05000012377`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Abweichender Bescheidempfänger › Ansprechperson › Anschrift Inland (`G05000011494`)

- **Adresssuche** (`F05000017298`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift _(geerbt)_
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Adresszusatz** (`F60000000248`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an. Beispiele: Hinterhaus, Gartenhaus.

### Angaben zu Lehrmitteln (`G05000011577`)

- **Hinweis Lehrmittel** (`F05000017362`) — optional
  - Rechtsgrundlage: § 4 FahrlG2018DV; § 22 (1) S. 2 Nr. 6 FahrlG
- **Schriftliche Erklärung zu Lehrmitteln** (`F05000017363`) — Pflicht
  - Rechtsgrundlage: §§ 18 (1) S. 1 Nr. 6, 22 (1) S. 2 Nr. 6 FahrlG
  - Hilfe: Laden sie eine schriftliche Erklärung hoch, dass die nach § 4 FahrlG2018DV  (Durchführungsverordnung zum Fahrlehrergesetz) vorgeschriebenen Lehrmittel zur Verfügung stehen und in welcher Art der Visualisierung diese vorliegen.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF."
- **Verfügungsnachweis** (`F05000017364`) — Pflicht
  - Rechtsgrundlage: § 18 (1) S. 1 Nr. 6 FahrlG
  - Hilfe: Laden Sie einen Verfügungsnachweis hoch, zum Beispiel einen Kaufvertrag oder einen Bestellschein. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise antragstellende Person (`G05000011591`)

- **Erklärung Fahrlehrerlaubnisse** (`F05000017381`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 3 FahrlG
  - Hilfe: Laden Sie hier die Erklärung für alle beantragten FE-Klassen und Erlaubnisse (Ausbildungsfahrlehrerlaubnis, ASF-Seminarerlaubnis, FES-Seminarerlaubnis) hoch.
- **Handelsregister** (`F05000017383`) — Pflicht
  - Rechtsgrundlage: § 22 (2) FahrlG
- **Gesellschaftsregister** (`F05000017384`) — Pflicht
  - Rechtsgrundlage: § 22 (2) FahrlG
  - Hilfe: Fügen Sie einen Auszug aus dem Gesellschaftsregister bei. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Vereinsregister** (`F05000017385`) — Pflicht
  - Rechtsgrundlage: § 22 (2) FahrlG
  - Hilfe: Fügen Sie einen Auszug aus dem Vereinsregister bei. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise antragstellende Person › Nachweise zur Zuverlässigkeit (`G05000011592`)

- **Hinweis:** (`F05000017386`) — optional
  - Rechtsgrundlage: § 18 (1) Nr 1 FahrlG
- **Strafverfahren** (`F05000017387`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 1 FahrlG
  - Hilfe: Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, anhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen Sie, die Geschäftsführung, die Betriebsleitung oder die Leitung einer Zweigstelle Ihres Unternehmens?
- **Nachweise zur Zuverlässigkeit** (`F05000017391`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 1 FahrlG

### Nachweise antragstellende Person › Bescheinigung in Steuersachen des Finanzamtes (`G05000011593`)

- **Hinweis:** (`F05000017388`) — optional
  - Rechtsgrundlage: § 18 (1) Nr 1 FahrlG; § 22 (1) Nr 9 FahrlG
- **Ist eine Bescheinigung in Steuersachen des Finanzamtes beigefügt?** (`F05000017389`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 1 FahrlG; § 22 (1) Nr 9 FahrlG
- **Bescheinigung Steuersachen Finanzamtes** (`F05000017390`) — Pflicht
  - Rechtsgrundlage: § 18 (1) Nr 1 FahrlG; § 22 (1) Nr 9 FahrlG
  - Hilfe: Hinweis für Juristische Personen: Beachten Sie, dass der Nachweis für die juristische Person zu erbringen ist
Laden Sie alle vollständigen Unterlagen hoch

### Nachweise antragstellende Person › Haben Sie bereits eine Auskunft aus dem Gewerbezentralregister (Belegart 9) beantragt?* (`G05000011612`)

- **Hinweis:** (`F05000017403`) — optional
  - Rechtsgrundlage: § 22 (1) Nr 8 FahrlG
- **Haben Sie bereits eine Auskunft aus dem Gewerbezentralregister (Belegart 9) beantragt?*** (`F05000017404`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 8 FahrlG
- **Datum der geplanten Beantragung** (`F05000017407`) — Pflicht, conditional
  - Rechtsgrundlage: § 22 (1) Nr 8 FahrlG

### Nachweise antragstellende Person › Haben Sie bereits eine Auskunft aus dem Gewerbezentralregister (Belegart 9) beantragt?* › Datum der Beantragung (`G05000011613`)

- **Datum der Beantragung** (`F05000017405`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 8 FahrlG
- **Laden Sie hier einen Nachweis der Beantragung hoch.** (`F05000017406`) — Pflicht
  - Rechtsgrundlage: § 22 (1) Nr 8 FahrlG

### Nachweise antragstellende Person › Landesspezifika › Angaben zum Aufenthaltstitel (`G05000012350`)

- **Status der Aufenthaltsgenehmigung** (`F05000014710`) — Pflicht
  - Rechtsgrundlage: ProstSchG
- **Ausstellungsdatum** (`F60000000294`) — Pflicht
  - Rechtsgrundlage: § 14 Gewerbeordnung (GewO) _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Ausstellende Behörde** (`F60000000292`) — Pflicht
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
  - Hilfe: Geben Sie den Namen der ausstellenden Behörde an.
- **Kopie Aufenthaltstitel** (`F05000002604`) — optional
  - Rechtsgrundlage: PassG
  - Hilfe: Beide Seiten einreichen.

### Nachweise antragstellende Person › Landesspezifika (`G05000012349`)

- **Gewünschter Gültigkeitsbeginn der Betriebserlaubnis** (`F05000018380`) — Pflicht
  - Rechtsgrundlage: § 17 Gesetz über das Fahrlehrerwesen (Fahrlehrergesetz - FahrlG) vom 30.06.2017
- **Laden Sie hier die Baugenehmigung durch die Bauaufsichtsbehörde hoch.** (`F05000018381`) — Pflicht
  - Rechtsgrundlage: § 17 Fahrlehrergesetz - FahrlG
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie hier eine Kopie Ihrer Fahrschuleraubnis hoch.** (`F05000018382`) — Pflicht
  - Rechtsgrundlage: § 17 Fahrlehrergesetz - FahrlG
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Bußgeldverfahren** (`F05000018383`) — Pflicht
  - Rechtsgrundlage: § 17 (1) Fahrlehrergesetz - FahrlG
  - Hilfe: Gibt oder gab es in den letzten fünf Jahren anhängige oder rechtskräftig abgeschlossene Bußgeldverfahren wegen gewerberechtlicher Verstöße gegen Sie bzw. eine von Ihnen vertretene Firma oder gegen die Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?

Der vorsätzliche oder fahrlässige Verstoß gegen die Erlaubnispflicht oder gegen vollziehbare Auflagen kann als Ordnungswidrigkeit mit einer Geldbuße von bis zu 5.000 Euro geahndet werden.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Soll der Bescheid an eine andere Adresse oder an eine andere Person geschickt werden?" gleich „wahr" ist | „Art des Bescheides" | entfällt | — | `R05000013562` |
| wenn „Soll der Bescheid an eine andere Adresse oder an eine andere Person geschickt werden?" ungleich „wahr" ist | „Art des Bescheides" | entfällt | — | `R05000013562` |
| wenn „Soll der Bescheid an eine andere Adresse oder an eine andere Person geschickt werden?" gleich „wahr" ist | „Ansprechperson" | muss ausgefüllt werden | — | `R05000013564` |
| wenn „Soll der Bescheid an eine andere Adresse oder an eine andere Person geschickt werden?" ungleich „wahr" ist | „Ansprechperson" | entfällt | — | `R05000013564` |
| wenn „Eingetragener Name" gesetzt auf einem beliebigen Wert ist | „Geschäftsbezeichnung" | muss ausgefüllt werden | — | `R05000012499` |
| wenn „Rechtsform" gleich „Personenhandelsgesellschaft" oder „Partenreederei (§ 489 HGB a. F.)" oder „ oder 411100=" oder „ oder 411200 " ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012513` |
| wenn „Rechtsform" gleich „ oder 230000=" oder „ bis 232000=" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012519` |
| wenn „Rechtsform" gleich „Genossenschaft" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012520` |
| wenn „Rechtsform" gleich „121000 nicht eingetragene Gesellschaft des bürgerlichen Rechts" oder „ oder 214000 " oder „ oder 261000=" oder „ oder 310000=" oder „ bis 381000=" oder „ oder 412000=" oder „ bis 412200=" oder „ oder 421000=" oder „ oder 423000=" oder „ bis 424000=" oder „ oder 510000=" oder „ bis 530000=" oder „ oder 550000=" oder „ bis 560000=" oder „ oder 590000=" oder „ bis 610000=" oder „ oder 691000=" ist | „Art der Eintragung oder des Registers" | entfällt | — | `R05000012522` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | muss ausgefüllt werden | — | `R05000012512` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | entfällt | — | `R05000012512` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | muss ausgefüllt werden | — | `R05000012512` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | entfällt | — | `R05000012512` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" gleich einem beliebigen Wert ist | „Natürliche Person - Vertreter" | muss ausgefüllt werden | — | `R05000012533` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" gleich einem beliebigen Wert ist | „Betriebsangaben" | entfällt | — | `R05000012533` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" gleich einem beliebigen Wert ist | „Betriebsangaben" | muss ausgefüllt werden | — | `R05000013378` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Natürliche Person - Vertreter" | muss ausgefüllt werden | — | `R05000013393` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht natürliche Person - Vertreter" | entfällt | — | `R05000013393` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht natürliche Person - Vertreter" | muss ausgefüllt werden | — | `R05000013394` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Natürliche Person - Vertreter" | entfällt | — | `R05000013394` |
| wenn „Eingetragener Name" gesetzt auf einem beliebigen Wert ist | „Geschäftsbezeichnung" | muss ausgefüllt werden | — | `R05000012499` |
| wenn „Rechtsform" gleich „Personenhandelsgesellschaft" oder „Partenreederei (§ 489 HGB a. F.)" oder „ oder 411100=" oder „ oder 411200 " ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012513` |
| wenn „Rechtsform" gleich „ oder 230000=" oder „ bis 232000=" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012519` |
| wenn „Rechtsform" gleich „Genossenschaft" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012520` |
| wenn „Rechtsform" gleich „121000 nicht eingetragene Gesellschaft des bürgerlichen Rechts" oder „ oder 214000 " oder „ oder 261000=" oder „ oder 310000=" oder „ bis 381000=" oder „ oder 412000=" oder „ bis 412200=" oder „ oder 421000=" oder „ oder 423000=" oder „ bis 424000=" oder „ oder 510000=" oder „ bis 530000=" oder „ oder 550000=" oder „ bis 560000=" oder „ oder 590000=" oder „ bis 610000=" oder „ oder 691000=" ist | „Art der Eintragung oder des Registers" | entfällt | — | `R05000012522` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | muss ausgefüllt werden | — | `R05000012512` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | entfällt | — | `R05000012512` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Wurde bereits ein Antrag bei einer anderen Behörde gestellt?" gleich „wahr" ist | „Angaben zur Behörde der bisherigen Antragstellung" | muss ausgefüllt werden | — | `R05000012250` |
| wenn „Wurde bereits ein Antrag bei einer anderen Behörde gestellt?" ungleich „wahr" ist | „Angaben zur Behörde der bisherigen Antragstellung" | darf nicht ausgefüllt werden | — | `R05000012250` |
| wenn „Wurde bereits ein Antrag bei einer anderen Behörde gestellt?" gleich „falsch" ist | „Aktuelle Fahrschulerlaubnis" | muss ausgefüllt werden | — | `R05000012254` |
| wenn „Wurde bereits ein Antrag bei einer anderen Behörde gestellt?" ungleich „falsch" ist | „Aktuelle Fahrschulerlaubnis" | darf nicht ausgefüllt werden | — | `R05000012254` |
| wenn „Sind oder waren Sie im Besitz einer Fahrschulerlaubnis?" gleich „Ja, ich war im Besitz" ist | „Ehemalige Fahrschulerlaubnis" | muss ausgefüllt werden | — | `R05000013484` |
| wenn „Sind oder waren Sie im Besitz einer Fahrschulerlaubnis?" ungleich „Ja, ich war im Besitz" ist | „Ehemalige Fahrschulerlaubnis" | darf nicht ausgefüllt werden | — | `R05000013484` |
| wenn „Sind oder waren Sie im Besitz einer Fahrschulerlaubnis?" gleich „Ja, ich bin im Besitz" ist | „Aktuelle Fahrschulerlaubnis" | muss ausgefüllt werden | — | `R05000013485` |
| wenn „Sind oder waren Sie im Besitz einer Fahrschulerlaubnis?" ungleich „Ja, ich bin im Besitz" ist | „Aktuelle Fahrschulerlaubnis" | darf nicht ausgefüllt werden | — | `R05000013485` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | muss ausgefüllt werden | — | `R05000012512` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | entfällt | — | `R05000012512` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Verfügen Sie über eine Teilnahmebescheinigung für ein Fahrschulbetriebswirtschaftsseminar?" gleich „wahr" ist | „Angaben zum Fahrschulbetriebswirtschaftsseminar" | muss ausgefüllt werden | — | `R05000012271` |
| wenn „Verfügen Sie über eine Teilnahmebescheinigung für ein Fahrschulbetriebswirtschaftsseminar?" gleich einem beliebigen Wert ist | „Angaben zum Fahrschulbetriebswirtschaftsseminar" | entfällt | — | `R05000012271` |
| wenn „Wo befindet sich die Anschrift?" gleich „001" ist | „Anschrift Inland" | muss ausgefüllt werden | — | `G05000011492` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001" ist | „Anschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011492` |
| wenn „Wo befindet sich die Anschrift?" gleich „002" ist | „Auslandsanschrift" | muss ausgefüllt werden | — | `G05000011492` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002" ist | „Auslandsanschrift" | darf nicht ausgefüllt werden | — | `G05000011492` |
| wenn „Besteht oder bestand ein Beschäftigungsverhältnis über insgesamt mindestens zwei Jahre als Fahrlehrer*in?" gleich „wahr" ist | „Angaben zur Arbeitsstelle" | muss ausgefüllt werden | — | `R05000012275` |
| wenn „Besteht oder bestand ein Beschäftigungsverhältnis über insgesamt mindestens zwei Jahre als Fahrlehrer*in?" gleich einem beliebigen Wert ist | „Angaben zur Arbeitsstelle" | darf nicht ausgefüllt werden und muss ausgefüllt werden | — | `R05000012275` |
| wenn „Besteht oder bestand ein Beschäftigungsverhältnis über insgesamt mindestens zwei Jahre als Fahrlehrer*in?" gleich „wahr" ist | „Hinweis:" | wird gezeigt | — | `R05000012276` |
| wenn „Besteht oder bestand ein Beschäftigungsverhältnis über insgesamt mindestens zwei Jahre als Fahrlehrer*in?" gleich einem beliebigen Wert ist | „Hinweis:" | entfällt | — | `R05000012276` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000012492` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012492` |
| wenn „Geben Sie die Eigentumsform der Räumlichkeiten an:" gleich „01 Miete" ist | „Mietvertrag" | muss ausgefüllt werden | — | `G05000011570` |
| wenn „Geben Sie die Eigentumsform der Räumlichkeiten an:" ungleich „01 Miete" ist | „Mietvertrag" | darf nicht ausgefüllt werden | — | `G05000011570` |
| wenn „Geben Sie die Eigentumsform der Räumlichkeiten an:" gleich „02 Eigentum" ist | „Eigentumsnachweis" | muss ausgefüllt werden | — | `G05000011570` |
| wenn „Geben Sie die Eigentumsform der Räumlichkeiten an:" ungleich „02 Eigentum" ist | „Eigentumsnachweis" | darf nicht ausgefüllt werden | — | `G05000011570` |
| wenn „Nutzen Sie die Räumlichkeiten gemeinsam mit einer anderen Fahrschule bzw. einem anderen Betrieb?" gleich „wahr" ist | „Angaben zum anderen Betrieb oder zur anderen Fahrschule" | muss ausgefüllt werden | — | `G05000011571` |
| wenn „Nutzen Sie die Räumlichkeiten gemeinsam mit einer anderen Fahrschule bzw. einem anderen Betrieb?" ungleich „wahr" ist | „Angaben zum anderen Betrieb oder zur anderen Fahrschule" | darf nicht ausgefüllt werden | — | `G05000011571` |
| wenn „Es handelt sich um ein:" gleich „01 eigenes Fahrzeug" ist | „Eigentumsnachweis" | muss ausgefüllt werden | — | `G05000011576` |
| wenn „Es handelt sich um ein:" ungleich „01 eigenes Fahrzeug" ist | „Eigentumsnachweis" | darf nicht ausgefüllt werden | — | `G05000011576` |
| wenn „Es handelt sich um ein:" gleich „02 Mietfahrzeug" ist | „Mietvertrag" | muss ausgefüllt werden | — | `G05000011576` |
| wenn „Es handelt sich um ein:" ungleich „02 Mietfahrzeug" ist | „Mietvertrag" | darf nicht ausgefüllt werden | — | `G05000011576` |
| wenn „Es handelt sich um ein:" gleich „03 Leasingfahrzeug" ist | „Leasingvertrag" | muss ausgefüllt werden | — | `G05000011576` |
| wenn „Es handelt sich um ein:" ungleich „03 Leasingfahrzeug" ist | „Leasingvertrag" | darf nicht ausgefüllt werden | — | `G05000011576` |
| wenn „Haben Sie bereits eine Auskunft aus dem Gewerbezentralregister (Belegart 9) beantragt?*" gleich „wahr" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000012311` |
| wenn „Haben Sie bereits eine Auskunft aus dem Gewerbezentralregister (Belegart 9) beantragt?*" gleich einem beliebigen Wert ist | „Datum der geplanten Beantragung" | muss ausgefüllt werden | — | `R05000012312` |
| wenn „Haben Sie bereits eine Auskunft aus dem Gewerbezentralregister (Belegart 9) beantragt?*" ungleich einem beliebigen Wert ist | „Datum der geplanten Beantragung" | entfällt | — | `R05000012312` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Es muss mindestens eines der Felder F05000017367 "Fahrlehrerlaubnisklasse A, F05000017368 "Fahrlehrerlaubnisklasse BE", F05000017369 "Fahrlehrerlaubnisklasse CE", F05000017370 "Fahrlehrerlaubnisklasse DE" der Wert = "wahr" sein.</mark> — Regel `R05000012268`
- <mark>WENN in F60000000319 "Eingetragener Name / Organisationsname" ein Eintrag vorgenommen wurde, DANN ist F60000000320 "Geschäftsbezeichnung / Organisationsbezeichnung" ein optionales Feld.</mark> — Regel `R05000012499`
- <mark>WENN im Feld F6000000339 "Rechtsform (XUnternehmen)" Auswahl = 120000="Gesellschaft des bürgerlichen Rechts (BGB-Gesellschaft) ; auch eingetragene Gesellschaft des bürgerlichen Rechts" oder 123000="eingetragene Gesellschaft des bürgerlichen Rechts", DANN darf in Feld F6000000347 "Art Eintragung / Register" nur der Code GesR "Gesellschaftsregister" ausgewählt sein.</mark> — Regel `R05000012514`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 138000="Auffangtatbestände (Personengesellschaft)", 138100="sonstige rechtsfähige Personengesellschaft (Auffangstatbestand)", 212000="Wirtschaftlicher Verein", 240000="Körperschaft des öffentlichen Rechts (KöR)" bis 243000="öffentlich-rechtliche Religionsgesellschaft", 262000="rechtsfähige Anstalt des öffentlichen Rechts (rechtsf. AöR)", 268400="sonstige juristische Person, die im Handelsregister Abteilung A eingetragen ist (Auffangtatbestand Justiz)", 410000="gewerbliches Einzelunternehmen (ohne Hausgewerbe)", 411000="eingetragenes gewerbliches Einzelunternehmen (e.K.; e.Kfm.; e.Kfr.)", 420000="sonstige wirtschaftliche Tätigkeit einer natürlichen Person", 422000="Land-/Forstwirt", 428000="Auffangtatbestände (wirtschaftliche Tätigkeit einer natürlichen Person)", 428100="sonstige wirtschaftliche Tätigkeit einer natürlichen Person (Auffangstatbestand)", 540000="Gewerbebetrieb einer Körperschaft des öffentlichen Rechts", 580000="Auffangtatbestände (wirtschaftliche Tätigkeit einer nicht-natürlichen Person)" oder 581000="sonstige wirtschaftliche Tätigkeit einer nicht-natürlichen Person (Auffangtatbestand)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code A "Eintragung im Handelsregister A" ausgewählt sein.</mark> — Regel `R05000012516`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 221100="Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH" bis 221200="Unternehmergesellschaft (haftungsbeschränkt)" oder 222100="Aktiengesellschaft (AG); auch Investmentaktiengesellschaft (InvAG)" bis 222120="Investmentaktiengesellschaft (InvAG)" oder 223000="Kommanditgesellschaft auf Aktien (KGaA); auch & Co. KGaA" bis 224810="sonstige Kapitalgesellschaft (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000012517`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 213000 "Versicherungsverein auf Gegenseitigkeit; auch Pensionsfondsverein auf Gegenseitigkeit", 213100="Versicherungsverein auf Gegenseitigkeit", 213200="Pensionsfondsverein auf Gegenseitigkeit" oder 221000 "Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH ; auch Unternehmergesellschaft (haftungsbeschränkt)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000012518`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 220000="Kapitalgesellschaft", 222000="Aktiengesellschaft (AG); auch Europäische Aktiengesellschaft (SE); Investmentaktiengesellschaft (Investment-AG)", 222200="Europäische Aktiengesellschaft (SE)", 293000="ausländische Kapitalgesellschaft" oder 293100="Limited Company (unspezifisch)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012521`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 190000="ausländische Personengesellschaft" bis 192000="ausländische Personengesellschaft (Nicht-EU-Recht)" oder 291000="ausländische Körperschaft des öffentlichen Rechts" oder 490000="ausländische wirtschaftliche Tätigkeit einer natürlichen Person" bis 492000="ausländisches gewerbliches Einzelunternehmen (Nicht-EU-Recht)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012523`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 294000="ausländische juristische Person (EU-Recht)" oder 295000="ausländische juristische Person (Nicht-EU-Recht)" bis 298100="sonstige ausländische juristische Person des privaten Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012524`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 260000="sonstige juristische Person" oder 268000="Auffangtatbestände (juristische Person)" bis 268200="sonstige juristische Person des Privatrechts (Auffangtatbestand Steuer)" oder 268300="sonstige juristische Person des öffentlichen Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000012525`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 290000="ausländische juristische Person" oder 681000="Freitext (Auffangtatbestand)" oder 683000="Ersatzwert (Auffangtatbestand Steuer)" bis 690000="ausländische Rechtsform" oder 698000="Auffangtatbestände (ausländische Rechtsform)" oder 680000="Auffangtatbestände (ohne Rechtsform-Typ)" oder 698100="sonstige ausländische Rechtsform (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012526`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 252000="Europäische Genossenschaft (SCE)" oder 292000="ausländische Genossenschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes G "Eintragung im Genossenschaftsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012527`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 130000="sonstige rechtsfähige Personengesellschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000012528`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 131000="Partnerschaftsgesellschaft (PartG)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000012529`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 210000="rechtsfähiger Verein", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000012530`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 211000="eingetragener Verein (e.V.)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000012531`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 682000="Freitext (Auffangtatbestand Justiz)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012532`
- <mark>Die Mitgliedstaaten der Europäischen Union (Stand 2025) sind alphabetisch sortiert: 124 Belgien, 125 Bulgarien, 126 Dänemark, 0 Deutschland, 127 Estland, 128 Finnland, 129 Frankreich, 134 Griechenland, 135 Irland, 137 Italien, 130 Kroatien, 139 Lettland, 142 Litauen, 143 Luxemburg, 145 Malta, 148 Niederlande, 151 Österreich, 152 Polen, 153 Portugal, 154 Rumänien, 157 Schweden, 155 Slowakei, 131 Slowenien, 161 Spanien, 164 Tschechien, 165 Ungarn und 181 Zypern.</mark> — Regel `R05000012511`
- <mark>WENN im Feld F05000017638 "Status der Aufenthaltsgenehmigung" Auswahl <> 001="liegt vor", DANN sind Felder F60000000292 "Ausstellende Behörde Name", F60000000294 "Ausstellungsdatum" und F60000000296 "Nachweis" nicht anzuzeigen.</mark> — Regel `R05000012496`
- <mark>Die Mitgliedstaaten der Europäischen Union (Stand 2025) sind alphabetisch sortiert: 124 Belgien, 125 Bulgarien, 126 Dänemark, 0 Deutschland, 127 Estland, 128 Finnland, 129 Frankreich, 134 Griechenland, 135 Irland, 137 Italien, 130 Kroatien, 139 Lettland, 142 Litauen, 143 Luxemburg, 145 Malta, 148 Niederlande, 151 Österreich, 152 Polen, 153 Portugal, 154 Rumänien, 157 Schweden, 155 Slowakei, 131 Slowenien, 161 Spanien, 164 Tschechien, 165 Ungarn und 181 Zypern.</mark> — Regel `R05000012512`
- <mark>WENN im Feld F05000017638 "Status der Aufenthaltsgenehmigung" Auswahl <> 001="liegt vor", DANN sind Felder F60000000292 "Ausstellende Behörde Name", F60000000294 "Ausstellungsdatum" und F60000000296 "Nachweis" nicht anzuzeigen.</mark> — Regel `R05000012496`
- <mark>Die Mitgliedstaaten der Europäischen Union (Stand 2025) sind alphabetisch sortiert: 124 Belgien, 125 Bulgarien, 126 Dänemark, 0 Deutschland, 127 Estland, 128 Finnland, 129 Frankreich, 134 Griechenland, 135 Irland, 137 Italien, 130 Kroatien, 139 Lettland, 142 Litauen, 143 Luxemburg, 145 Malta, 148 Niederlande, 151 Österreich, 152 Polen, 153 Portugal, 154 Rumänien, 157 Schweden, 155 Slowakei, 131 Slowenien, 161 Spanien, 164 Tschechien, 165 Ungarn und 181 Zypern.</mark> — Regel `R05000012512`
- <mark>WENN im Feld F05000017638 "Status der Aufenthaltsgenehmigung" Auswahl <> 001="liegt vor", DANN sind Felder F60000000292 "Ausstellende Behörde Name", F60000000294 "Ausstellungsdatum" und F60000000296 "Nachweis" nicht anzuzeigen.</mark> — Regel `R05000012496`
- <mark>WENN in F60000000319 "Eingetragener Name / Organisationsname" ein Eintrag vorgenommen wurde, DANN ist F60000000320 "Geschäftsbezeichnung / Organisationsbezeichnung" ein optionales Feld.</mark> — Regel `R05000012499`
- <mark>WENN im Feld F6000000339 "Rechtsform (XUnternehmen)" Auswahl = 120000="Gesellschaft des bürgerlichen Rechts (BGB-Gesellschaft) ; auch eingetragene Gesellschaft des bürgerlichen Rechts" oder 123000="eingetragene Gesellschaft des bürgerlichen Rechts", DANN darf in Feld F6000000347 "Art Eintragung / Register" nur der Code GesR "Gesellschaftsregister" ausgewählt sein.</mark> — Regel `R05000012514`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 138000="Auffangtatbestände (Personengesellschaft)", 138100="sonstige rechtsfähige Personengesellschaft (Auffangstatbestand)", 212000="Wirtschaftlicher Verein", 240000="Körperschaft des öffentlichen Rechts (KöR)" bis 243000="öffentlich-rechtliche Religionsgesellschaft", 262000="rechtsfähige Anstalt des öffentlichen Rechts (rechtsf. AöR)", 268400="sonstige juristische Person, die im Handelsregister Abteilung A eingetragen ist (Auffangtatbestand Justiz)", 410000="gewerbliches Einzelunternehmen (ohne Hausgewerbe)", 411000="eingetragenes gewerbliches Einzelunternehmen (e.K.; e.Kfm.; e.Kfr.)", 420000="sonstige wirtschaftliche Tätigkeit einer natürlichen Person", 422000="Land-/Forstwirt", 428000="Auffangtatbestände (wirtschaftliche Tätigkeit einer natürlichen Person)", 428100="sonstige wirtschaftliche Tätigkeit einer natürlichen Person (Auffangstatbestand)", 540000="Gewerbebetrieb einer Körperschaft des öffentlichen Rechts", 580000="Auffangtatbestände (wirtschaftliche Tätigkeit einer nicht-natürlichen Person)" oder 581000="sonstige wirtschaftliche Tätigkeit einer nicht-natürlichen Person (Auffangtatbestand)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code A "Eintragung im Handelsregister A" ausgewählt sein.</mark> — Regel `R05000012516`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 221100="Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH" bis 221200="Unternehmergesellschaft (haftungsbeschränkt)" oder 222100="Aktiengesellschaft (AG); auch Investmentaktiengesellschaft (InvAG)" bis 222120="Investmentaktiengesellschaft (InvAG)" oder 223000="Kommanditgesellschaft auf Aktien (KGaA); auch & Co. KGaA" bis 224810="sonstige Kapitalgesellschaft (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000012517`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 213000 "Versicherungsverein auf Gegenseitigkeit; auch Pensionsfondsverein auf Gegenseitigkeit", 213100="Versicherungsverein auf Gegenseitigkeit", 213200="Pensionsfondsverein auf Gegenseitigkeit" oder 221000 "Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH ; auch Unternehmergesellschaft (haftungsbeschränkt)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000012518`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 220000="Kapitalgesellschaft", 222000="Aktiengesellschaft (AG); auch Europäische Aktiengesellschaft (SE); Investmentaktiengesellschaft (Investment-AG)", 222200="Europäische Aktiengesellschaft (SE)", 293000="ausländische Kapitalgesellschaft" oder 293100="Limited Company (unspezifisch)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012521`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 190000="ausländische Personengesellschaft" bis 192000="ausländische Personengesellschaft (Nicht-EU-Recht)" oder 291000="ausländische Körperschaft des öffentlichen Rechts" oder 490000="ausländische wirtschaftliche Tätigkeit einer natürlichen Person" bis 492000="ausländisches gewerbliches Einzelunternehmen (Nicht-EU-Recht)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012523`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 294000="ausländische juristische Person (EU-Recht)" oder 295000="ausländische juristische Person (Nicht-EU-Recht)" bis 298100="sonstige ausländische juristische Person des privaten Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012524`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 260000="sonstige juristische Person" oder 268000="Auffangtatbestände (juristische Person)" bis 268200="sonstige juristische Person des Privatrechts (Auffangtatbestand Steuer)" oder 268300="sonstige juristische Person des öffentlichen Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000012525`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 290000="ausländische juristische Person" oder 681000="Freitext (Auffangtatbestand)" oder 683000="Ersatzwert (Auffangtatbestand Steuer)" bis 690000="ausländische Rechtsform" oder 698000="Auffangtatbestände (ausländische Rechtsform)" oder 680000="Auffangtatbestände (ohne Rechtsform-Typ)" oder 698100="sonstige ausländische Rechtsform (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012526`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 252000="Europäische Genossenschaft (SCE)" oder 292000="ausländische Genossenschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes G "Eintragung im Genossenschaftsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012527`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 130000="sonstige rechtsfähige Personengesellschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000012528`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 131000="Partnerschaftsgesellschaft (PartG)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000012529`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 210000="rechtsfähiger Verein", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000012530`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 211000="eingetragener Verein (e.V.)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000012531`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 682000="Freitext (Auffangtatbestand Justiz)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000012532`
- <mark>Die Mitgliedstaaten der Europäischen Union (Stand 2025) sind alphabetisch sortiert: 124 Belgien, 125 Bulgarien, 126 Dänemark, 0 Deutschland, 127 Estland, 128 Finnland, 129 Frankreich, 134 Griechenland, 135 Irland, 137 Italien, 130 Kroatien, 139 Lettland, 142 Litauen, 143 Luxemburg, 145 Malta, 148 Niederlande, 151 Österreich, 152 Polen, 153 Portugal, 154 Rumänien, 157 Schweden, 155 Slowakei, 131 Slowenien, 161 Spanien, 164 Tschechien, 165 Ungarn und 181 Zypern.</mark> — Regel `R05000012512`
- <mark>WENN im Feld F05000017638 "Status der Aufenthaltsgenehmigung" Auswahl <> 001="liegt vor", DANN sind Felder F60000000292 "Ausstellende Behörde Name", F60000000294 "Ausstellungsdatum" und F60000000296 "Nachweis" nicht anzuzeigen.</mark> — Regel `R05000012496`
- <mark>Die Mitgliedstaaten der Europäischen Union (Stand 2025) sind alphabetisch sortiert: 124 Belgien, 125 Bulgarien, 126 Dänemark, 0 Deutschland, 127 Estland, 128 Finnland, 129 Frankreich, 134 Griechenland, 135 Irland, 137 Italien, 130 Kroatien, 139 Lettland, 142 Litauen, 143 Luxemburg, 145 Malta, 148 Niederlande, 151 Österreich, 152 Polen, 153 Portugal, 154 Rumänien, 157 Schweden, 155 Slowakei, 131 Slowenien, 161 Spanien, 164 Tschechien, 165 Ungarn und 181 Zypern.</mark> — Regel `R05000013381`
- <mark>WENN im Feld F05000017638 "Status der Aufenthaltsgenehmigung" Auswahl <> 001="liegt vor", DANN sind Felder F60000000292 "Ausstellende Behörde Name", F60000000294 "Ausstellungsdatum" und F60000000296 "Nachweis" nicht anzuzeigen.</mark> — Regel `R05000012496`
- <mark>Die Mitgliedstaaten der Europäischen Union (Stand 2025) sind alphabetisch sortiert: 124 Belgien, 125 Bulgarien, 126 Dänemark, 0 Deutschland, 127 Estland, 128 Finnland, 129 Frankreich, 134 Griechenland, 135 Irland, 137 Italien, 130 Kroatien, 139 Lettland, 142 Litauen, 143 Luxemburg, 145 Malta, 148 Niederlande, 151 Österreich, 152 Polen, 153 Portugal, 154 Rumänien, 157 Schweden, 155 Slowakei, 131 Slowenien, 161 Spanien, 164 Tschechien, 165 Ungarn und 181 Zypern.</mark> — Regel `R05000012512`
- <mark>WENN im Feld F05000017638 "Status der Aufenthaltsgenehmigung" Auswahl <> 001="liegt vor", DANN sind Felder F60000000292 "Ausstellende Behörde Name", F60000000294 "Ausstellungsdatum" und F60000000296 "Nachweis" nicht anzuzeigen.</mark> — Regel `R05000012496`
- <mark>Es muss mindestens eines der Felder F05000017266 "Fahrlehrerlaubnisklasse A", F05000017269 "Fahrlehrerlaubnisklasse BE", F05000017267 "Fahrlehrerlaubnisklasse CE" oder F05000017268 "Fahrlehrerlaubnisklasse DE" den Wert "wahr" haben.</mark> — Regel `R05000012151`
- <mark>Der Wert in F05000017356 "Anzahl der Lehrfahrzeuge" gibt an, wie oft die Gruppe G05000011576 "Lehrfahrzeug" befüllt sein muss.</mark> — Regel `R05000013486`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  F05000018430["Soll der Bescheid an eine andere Adres"] -.->|"= wahr → hide"| G05000012376_F05000017257["Art des Bescheides"]
  F05000018430["Soll der Bescheid an eine andere Adres"] -.->|"<> wahr → hide"| G05000012376_F05000017257["Art des Bescheides"]
  F05000018430["Soll der Bescheid an eine andere Adres"] ==>|"= wahr → required"| G05000012376_G05000012377["Ansprechperson"]
  F05000018430["Soll der Bescheid an eine andere Adres"] -.->|"<> wahr → hide"| G05000012376_G05000012377["Ansprechperson"]
  G05000011762_G05000011753_F60000000319["Eingetragener Name"] ==>|"? ? → required"| G05000011762_G05000011753_F60000000320["Geschäftsbezeichnung"]
  G05000011762_G05000011753_F60000000339["Rechtsform"] ==>|"= Personenhandelsgesellschaft, → required"| G05000011762_G05000011753_F60000000347["Art der Eintragung oder des Registers"]
  G05000011762_G05000011753_F60000000339["Rechtsform"] ==>|"=  oder 230000=,  bis 232000= → required"| G05000011762_G05000011753_F60000000347["Art der Eintragung oder des Registers"]
  G05000011762_G05000011753_F60000000339["Rechtsform"] ==>|"= Genossenschaft → required"| G05000011762_G05000011753_F60000000347["Art der Eintragung oder des Registers"]
  G05000011762_G05000011753_F60000000339["Rechtsform"] -.->|"= 121000 nicht eingetragene Ge → hide"| G05000011762_G05000011753_F60000000347["Art der Eintragung oder des Registers"]
  G05000011762_G05000011750_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011762_G05000011750_G60000000083_F60000000232["Monat"]
  G05000011762_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011762_G05000011750_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000011762_G05000011750_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011762_G05000011750_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000011762_G05000011750_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Straßenanschrift Inland → required+show"| G05000011762_G05000011750_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Straßenanschrift Inland → hide"| G05000011762_G05000011750_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Postfach- oder Großempfänger → required+show"| G05000011762_G05000011750_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Postfach- oder Großempfänger → hide"| G05000011762_G05000011750_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011750_G05000011749_F05000017638["Welchen Status hat Ihre Aufenthaltsgen"] ==>|"= liegt vor → required"| G05000011762_G05000011750_G05000011749_F60000000292["Ausstellende Behörde"]
  G05000011762_G05000011750_G05000011754_G05000011751_F60000000236["Staatsangehörigkeit"] ==>|"? ? → required"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000011762_G05000011750_G05000011754_G05000011751_F60000000236["Staatsangehörigkeit"] -.->|"? ? → hide"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000011762_G05000011750_G05000011754_G05000011751_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011762_G05000011750_G05000011754_G05000011751_G60000000083_F60000000232["Monat"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Straßenanschrift Inland → required+show"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Straßenanschrift Inland → hide"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Postfach- oder Großempfänger → required+show"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Postfach- oder Großempfänger → hide"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011750_G05000011754_G05000011751_G05000011749_F05000017638["Welchen Status hat Ihre Aufenthaltsgen"] ==>|"= liegt vor → required"| G05000011762_G05000011750_G05000011754_G05000011751_G05000011749_F60000000292["Ausstellende Behörde"]
  G05000011762_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011762_G05000011759_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000011762_G05000011759_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011762_G05000011759_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000011762_G05000011759_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Straßenanschrift Inland → required+show"| G05000011762_G05000011759_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Straßenanschrift Inland → hide"| G05000011762_G05000011759_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Postfach- oder Großempfänger → required+show"| G05000011762_G05000011759_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Postfach- oder Großempfänger → hide"| G05000011762_G05000011759_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011759_G05000011756_G05000011751_F60000000236["Staatsangehörigkeit"] ==>|"? ? → required"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000011762_G05000011759_G05000011756_G05000011751_F60000000236["Staatsangehörigkeit"] -.->|"? ? → hide"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000011762_G05000011759_G05000011756_G05000011751_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011762_G05000011759_G05000011756_G05000011751_G60000000083_F60000000232["Monat"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Straßenanschrift Inland → required+show"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Straßenanschrift Inland → hide"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Postfach- oder Großempfänger → required+show"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Postfach- oder Großempfänger → hide"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011762_G05000011759_G05000011756_G05000011751_G05000011749_F05000017638["Welchen Status hat Ihre Aufenthaltsgen"] ==>|"= liegt vor → required"| G05000011762_G05000011759_G05000011756_G05000011751_G05000011749_F60000000292["Ausstellende Behörde"]
  G05000011762_G05000011759_G05000011757_F05000018285["Ist der Gesellschafter eine Natürliche"] ==>|"= ? → required"| G05000011762_G05000011759_G05000011757_G05000011751["Natürliche Person - Vertreter"]
  G05000011762_G05000011759_G05000011757_F05000018285["Ist der Gesellschafter eine Natürliche"] -.->|"= ? → hide"| G05000011762_G05000011759_G05000011757_G05000011753["Betriebsangaben"]
  G05000011762_G05000011759_G05000011757_F05000018285["Ist der Gesellschafter eine Natürliche"] ==>|"= ? → required"| G05000011762_G05000011759_G05000011757_G05000011753["Betriebsangaben"]
  G05000011762_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000011762_G05000011759_G05000011757_G05000011751["Natürliche Person - Vertreter"]
  G05000011762_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000011762_G05000011759_G05000011757_G05000011758["Nicht natürliche Person - Vertreter"]
  G05000011762_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000011762_G05000011759_G05000011757_G05000011758["Nicht natürliche Person - Vertreter"]
  G05000011762_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000011762_G05000011759_G05000011757_G05000011751["Natürliche Person - Vertreter"]
  G05000011762_G05000011759_G05000011757_G05000011753_F60000000319["Eingetragener Name"] ==>|"? ? → required"| G05000011762_G05000011759_G05000011757_G05000011753_F60000000320["Geschäftsbezeichnung"]
  G05000011762_G05000011759_G05000011757_G05000011753_F60000000339["Rechtsform"] ==>|"= Personenhandelsgesellschaft, → required"| G05000011762_G05000011759_G05000011757_G05000011753_F60000000347["Art der Eintragung oder des Registers"]
  unclear0["?: Es muss mindestens eines der Felder F05000017367 "Fahrlehrer"]:::unclear
  unclear1["?: WENN in F60000000319 "Eingetragener Name / Organisationsname"]:::unclear
  unclear2["?: WENN im Feld F6000000339 "Rechtsform (XUnternehmen)" Auswahl"]:::unclear
  unclear3["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear4["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear5["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear6["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear7["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear8["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear9["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
