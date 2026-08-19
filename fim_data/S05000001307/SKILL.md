---
name: antrag-s05000001307
description: Führt Antragstellende durch „Antrag auf Erlaubnis für Immobilienmakler, Darlehensvermittler, Bauträger, Baubetreuer und Wohnimmobilienverwalter" (FIM S05000001307 1.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf Erlaubnis für Immobilienmakler, Darlehensvermittler, Bauträger, Baubetreuer und Wohnimmobilienverwalter

- **FIM-ID:** `S05000001307 1.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 34c GewO vom 27.12.2024; § 802 ZPO vom 01.01.20213
- **Kompiliert:** 2026-08-13T15:44:37Z aus https://fimportal.de/api/v1/schemas/S05000001307/1.0.0/xdf
- **Umfang:** 358 Felder, 203 gesicherte Bedingungen, 1 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet werden (Rechtsgrundlage stimmt nicht überein (D99000001400)). Zu Fristen, Kosten, Unterlagen und Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle verweisen.

## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Art der Erlaubnis (`G05000011789`)

- **Hinweis:** (`F05000017661`) — Pflicht
  - Rechtsgrundlage: 34c GewO

### Art der Erlaubnis › Erlaubnis Immobilienmakler (`G05000011842`)

- **Hinweis:** (`F05000017665`) — Pflicht
  - Rechtsgrundlage: § 34c (1) S. 1 Nr. 1 GewO
- **Beantragen Sie eine Erlaubnis für die Tätigkeit als Immobilienmaklerin oder Immobilienmakler nach § 34c Abs. 1 Satz 1 Nummer 1 GewO?** (`F05000017664`) — Pflicht
  - Rechtsgrundlage: § 34c (1) S. 1 Nr. 1 GewO

### Art der Erlaubnis › Erlaubnis Darlehensvermittler (`G05000011846`)

- **Hinweis:** (`F05000017667`) — optional
  - Rechtsgrundlage: § 34c (1) S. 1 Nr. 2 GewO
- **Beantragen Sie eine Erlaubnis für die Tätigkeit als Darlehensvermittlerin oder Darlehensvermittler nach § 34c Abs. 1 Satz 1 Nummer 2 GewO?** (`F05000017666`) — Pflicht
  - Rechtsgrundlage: § 34c (1) S. 1 Nr. 2 GewO

### Art der Erlaubnis › Erlaubnis Bauträger (`G05000011847`)

- **Hinweis:** (`F05000017669`) — optional
  - Rechtsgrundlage: § 34c (1) S. 2 Nr. 3a GewO
- **Beantragen Sie eine Erlaubnis für die Tätigkeit als Bauträgerin oder Bauträger nach § 34c Absatz 1 Satz 2 Nr. 3a GewO?** (`F05000017668`) — Pflicht
  - Rechtsgrundlage: § 34c (1) S. 2 Nr. 3a GewO

### Art der Erlaubnis › Erlaubnis Baubetreuer (`G05000011848`)

- **Hinweis:** (`F05000017671`) — optional
  - Rechtsgrundlage: § 34c (1) S. 2 Nr. 3b GewO
- **Beantragen Sie eine Erlaubnis für die Tätigkeit als Baubetreuerin oder Baubetreuer nach § 34c Absatz 1 Satz 2 Nummer 3b GewO?** (`F05000017670`) — Pflicht
  - Rechtsgrundlage: § 34c (1) S. 2 Nr. 3b GewO

### Art der Erlaubnis › Erlaubnis Wohnimmobilienverwalter (`G05000011849`)

- **Hinweis:** (`F05000017673`) — optional
  - Rechtsgrundlage: § 34c (1) S. 1 Nr. 4 GewO
- **Beantragen Sie eine Erlaubnis für die Tätigkeit als Wohnimmobilienverwalterin oder Wohnimmobilienverwalter nach § 34c Absatz 1 Seite 2 Nummer 4 GewO?** (`F05000017672`) — Pflicht
  - Rechtsgrundlage: § 34c (1) S. 1 Nr. 4 GewO

### Unternehmensdaten › Identifikation des Unternehmens (`G05000013336`)

- **Rechtsform** (`F05000017511`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Hinweis** (`F05000017512`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Art der Eintragung oder des Registers** (`F05000017720`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2
  - Hilfe: Geben Sie an, um welche Art von Eintrag es sich handelt.
- **Eintragungsnummer** (`F05000017514`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Stiftungsverzeichnis (Freitext)** (`F05000018301`) — optional, conditional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
  - Hilfe: Bei Einträgen im Stiftungsverzeichnis: Angabe des Bundeslandes bzw. der Behörde, in dessen oder deren Stiftungsverzeichnis der Eintrag geführt wird.
- **Nummer des Registereintrages** (`F60000000328`) — optional, conditional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Registergericht** (`F05000017721`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Staat der Eintragung** (`F05000017518`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Ort des Registereintrags** (`F60000000327`) — optional, conditional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2
- **Eingetragener Name** (`F60000000319`) — optional, conditional
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Unternehmensname** (`F05000017734`) — optional, conditional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Der Name besteht aus dem Vor- und Familiennamen aller Gesellschafterinnen oder Gesellschafter mit Zusatz GbR.
- **Unternehmensname** (`F05000017735`) — optional, conditional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Der Name entspricht dem Vor- und Familiennamen der Inhaberin oder des Inhabers.
- **Geschäftsbezeichnung** (`F60000000320`) — optional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers (`G05000011864`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Inländische Geschäftsanschrift (`G05000011862`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Verwaltungssitz (`G05000011861`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Erreichbarkeit (`G05000011747`)

- **Telefonnummer** (`F60000000240`) — Pflicht
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
  - Rechtsgrundlage: Art. 6 Abs. 1 VO (EU) 2016/679 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung (`G05000011868`)

- **Hinweis:** (`F05000017737`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020; § 5 (2) Nr. 2 PAuswG vom 21.6.2019; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020; § 5 (2) Nr. 4 PAuswG vom 21.6.2019; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit); § 5 (2) PAuswG vom 21.6.2019 _(geerbt)_
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Gesetzliche Vertretung des Unternehmens › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft (`G05000013338`)

- **Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?** (`F05000018285`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Gesellschafterart** (`F05000019514`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Gesellschafter.Art Version 1.1; verwendet urn:xoev-de:xunternehmen:codeliste:artgesellschafterpersonengesellschaft Version 1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters (`G05000011873`)

- **Hinweis:** (`F05000017739`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020; § 5 (2) Nr. 2 PAuswG vom 21.6.2019; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020; § 5 (2) Nr. 4 PAuswG vom 21.6.2019; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit); § 5 (2) PAuswG vom 21.6.2019 _(geerbt)_
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Identifikation des Unternehmens (`G05000013336`)

- **Rechtsform** (`F05000017511`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Hinweis** (`F05000017512`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Art der Eintragung oder des Registers** (`F05000017720`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2
  - Hilfe: Geben Sie an, um welche Art von Eintrag es sich handelt.
- **Eintragungsnummer** (`F05000017514`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Stiftungsverzeichnis (Freitext)** (`F05000018301`) — optional, conditional
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
  - Hilfe: Bei Einträgen im Stiftungsverzeichnis: Angabe des Bundeslandes bzw. der Behörde, in dessen oder deren Stiftungsverzeichnis der Eintrag geführt wird.
- **Nummer des Registereintrages** (`F60000000328`) — optional, conditional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Registergericht** (`F05000017721`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Staat der Eintragung** (`F05000017518`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2; XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
- **Ort des Registereintrags** (`F60000000327`) — optional, conditional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2
- **Eingetragener Name** (`F60000000319`) — optional, conditional
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Unternehmensname** (`F05000017734`) — optional, conditional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Der Name besteht aus dem Vor- und Familiennamen aller Gesellschafterinnen oder Gesellschafter mit Zusatz GbR.
- **Unternehmensname** (`F05000017735`) — optional, conditional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Der Name entspricht dem Vor- und Familiennamen der Inhaberin oder des Inhabers.
- **Geschäftsbezeichnung** (`F60000000320`) — optional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung (`G05000011868`)

- **Hinweis:** (`F05000017737`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020; § 5 (2) Nr. 2 PAuswG vom 21.6.2019; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020; § 5 (2) Nr. 4 PAuswG vom 21.6.2019; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit); § 5 (2) PAuswG vom 21.6.2019 _(geerbt)_
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters (`G05000011873`)

- **Hinweis:** (`F05000017739`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020; § 5 (2) Nr. 2 PAuswG vom 21.6.2019; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020; § 5 (2) Nr. 4 PAuswG vom 21.6.2019; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit); § 5 (2) PAuswG vom 21.6.2019 _(geerbt)_
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Betriebsleitung (`G05000013333`)

- **Stellen Sie eine Betriebsleitung ein oder wird eine Zweigniederlassung Ihres Betriebes von einer beauftragten Person geleitet?** (`F05000017706`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020; § 5 (2) Nr. 2 PAuswG vom 21.6.2019; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020; § 5 (2) Nr. 4 PAuswG vom 21.6.2019; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; § 5 (2) PAuswG vom 21.6.2019 _(geerbt)_

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters (`G05000013334`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Betriebsleitung › Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Nachweise › Auszug aus dem Handelsregister oder aus dem Genossenschaftsregister (`G05000011882`)

- **Ein aktueller Auszug aus dem Handelsregister oder Genossenschaftsregister** (`F05000017740`) — Pflicht
  - Rechtsgrundlage: § 34c GewO _(geerbt)_
- **Fügen Sie einen aktuellen Registerauszug bei.** (`F05000017521`) — optional, conditional
  - Rechtsgrundlage: § 34c GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Gesellschaftsvertrag/Satzung (`G05000011883`)

- **Der Gesellschaftsvertrag oder die Satzung** (`F05000017741`) — Pflicht
  - Rechtsgrundlage: § 34c GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Berufshaftpflichtversicherung (`G05000011824`)

- **Hinweis:** (`F05000017731`) — optional
  - Rechtsgrundlage: § 34c (2) S. 1 Nr. 3 GewO
- **Eine Berufshaftpflicht** (`F05000017713`) — Pflicht
  - Rechtsgrundlage: § 34c (2) S. 1 Nr. 3 GewO
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) S. 1 Nr. 3 GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit (`G05000011794`)

- **Hinweis:** (`F05000017674`) — optional
  - Rechtsgrundlage: § 34c (2) GewO

### Nachweise › Nachweise zur Zuverlässigkeit › Strafverfahren (`G05000011795`)

- **Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen Sie, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?** (`F05000017675`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Bußgeldverfahren (`G05000011800`)

- **Gibt oder gab es in den letzten fünf Jahren abhängige oder rechtskräftig abgeschlossene Bußgeldverfahren wegen gewerberechtlicher Verstöße gegen Sie oder von Ihnen vertretene Firma, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?** (`F05000017677`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Sonstige gewerbliche Verfahren (`G05000011801`)

- **Gibt oder gab es in der Vergangenheit sonstige abhängige oder rechtskräftig abgeschlossene gewerbliche Verfahren gegen Sie oder eine von Ihnen vertretene Firma, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?** (`F05000017679`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Insolvenzverfahren › Eröffnung Insolvenzverfahren (`G05000011851`)

- **Liegt ein Antrag auf Eröffnung eines Insolvenz- oder Vergleichsverfahrens gegen Sie vor?** (`F05000017681`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Insolvenzverfahren › Ablehnung Insolvenzverfahren (`G05000011852`)

- **Liegt eine Ablehnung der Eröffnung eines Insolvenzverfahrens über Ihr Vermögen mangels Masse gegen Sie vor?** (`F05000017683`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Vermögensauskunft (`G05000011803`)

- **Haben Sie eine Vermögensauskunft gemäß § 802c ZPO abgegeben?** (`F05000017685`) — Pflicht
  - Rechtsgrundlage: § 802c ZPO
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 802c ZPO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Haftanordnung (`G05000011804`)

- **Liegt gegen Sie eine entsprechende Haftanforderung gemäß 802g ZPO vor?** (`F05000017688`) — Pflicht
  - Rechtsgrundlage: § 802g ZPO
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 802g ZPO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Schuldnerverzeichnis (`G05000011807`)

- **Liegt eine Eintragung im Schuldnerverzeichnis nach 882b ZPO gegen Sie vor?** (`F05000017689`) — Pflicht
  - Rechtsgrundlage: § 882b ZPO
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 882b ZPO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Gewerbezentralregister (`G05000011808`)

- **Hinweis:** (`F05000017691`) — optional
  - Rechtsgrundlage: § 150 GewO

### Nachweise › Nachweise zur Zuverlässigkeit › Gewerbezentralregister › Geschäftsführung oder gesetzliche Vertretung (`G05000011853`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Nachweise › Nachweise zur Zuverlässigkeit › Gewerbezentralregister › Auszug aus dem Gewerbezentralregister (`G05000011854`)

- **Hinweis zum Gewerbezentralregisterauszug (Belegart 9):** (`F05000017727`) — optional
  - Rechtsgrundlage: § 150 GewO
- **Die Auskunft aus dem Gewerbezentralregister (Belegart 9)** (`F05000017728`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Die Auskunft wird direkt übersandt.
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Nachweise › Nachweise zur Zuverlässigkeit › Bescheinigung in Steuersachen des Finanzamtes (`G05000011809`)

- **Liegt Ihnen eine Bescheinigung in Steuersachen des Finanzamtes vor, die Ihre Unbedenklichkeit bestätigt?** (`F05000017696`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Bescheinigung in Steuersachen des kommunalen Steueramtes (`G05000011810`)

- **Liegt Ihnen eine Bescheinigung in Steuersachen des kommunalen Steueramtes vor?** (`F05000017697`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur Zuverlässigkeit › Bundeszentralregisterauszug (Führungszeugnis) (`G05000011877`)

- **Hinweis:** (`F05000017729`) — optional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_

### Nachweise › Nachweise zur Zuverlässigkeit › Bundeszentralregisterauszug (Führungszeugnis) › Geschäftsführung oder gesetzliche Vertretung (`G05000011853`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Nachweise › Nachweise zur Zuverlässigkeit › Bundeszentralregisterauszug (Führungszeugnis) › Auszug aus dem Bundeszentralregister / Führungszeugnis (`G05000011878`)

- **Hinweis zum Bundeszentralregisterauszug (Belegart O):** (`F05000017730`) — optional
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Die Auskunft aus dem Bundeszentralregister** (`F05000017692`) — Pflicht
  - Rechtsgrundlage: § 34c (2) GewO _(geerbt)_
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Nachweise (`G05000011857`)

- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: leer, da Referenzkontext
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Beantragen Sie eine Erlaubnis für die Tätigkeit als Wohnimmobilienverwalterin oder Wohnimmobilienverwalter nach § 34c Absatz 1 Seite 2 Nummer 4 GewO?" gleich „wahr" ist | „Berufshaftpflichtversicherung" | muss ausgefüllt werden | — | `R05000012654` |
| wenn „Beantragen Sie eine Erlaubnis für die Tätigkeit als Wohnimmobilienverwalterin oder Wohnimmobilienverwalter nach § 34c Absatz 1 Seite 2 Nummer 4 GewO?" ungleich „wahr" ist | „Berufshaftpflichtversicherung" | entfällt | — | `R05000012654` |
| wenn „Rechtsform" gleich „121000 GbR" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000015508` |
| wenn „Rechtsform" ungleich „121000 GbR" ist | „Unternehmensname" | entfällt | — | `R05000015508` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | muss ausgefüllt werden | — | `R05000015509` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | entfällt | — | `R05000015509` |
| wenn „Rechtsform" gleich „222200 SE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015510` |
| wenn „Rechtsform" gleich „251000 eG" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015511` |
| wenn „Rechtsform" gleich „213000 VVaG" oder „221100 GmbH" oder „221200 UG" oder „222110 AG" oder „223100 KGaA" oder „223211 GmbH & Co. KGaA" oder „223212 UG & Co. KGaA" oder „223221 AG & Co. KGaA" oder „223222 SE & Co. KGaA" oder „223400 Stiftung & Co. KGaA" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015512` |
| wenn „Rechtsform" gleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000015513` |
| wenn „Rechtsform" ungleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | entfällt | — | `R05000015513` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | muss ausgefüllt werden | — | `R05000015514` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | entfällt | — | `R05000015514` |
| wenn „Rechtsform" gleich „111100 OHG" oder „111211 GmbH & Co. OHG" oder „111212 UG & Co. OHG" oder „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „411000 e.K.; e.Kfm.; e.Kfr." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015515` |
| wenn „Rechtsform" gleich „294000 ausl. juristische Person (EU-Recht)" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015516` |
| wenn „Rechtsform" gleich „268100 sonst. juristische Person" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015517` |
| wenn „Rechtsform" gleich „295000 ausl. juristische Person (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015518` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | muss ausgefüllt werden | — | `R05000015519` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | entfällt | — | `R05000015519` |
| wenn „Rechtsform" gleich „191000 ausl. Personengesellschaft (EU-Recht)" oder „192000 ausl. Personengesellschaft (Nicht-EU-Recht)" oder „491000 ausl. gew. Einzelunternehmen (EU-Recht)" oder „492000 ausl. gew. Einzelunternehmen (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015520` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | wird gezeigt | — | `R05000015521` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | entfällt | — | `R05000015521` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | muss ausgefüllt werden | — | `R05000015522` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | entfällt | — | `R05000015522` |
| wenn „Rechtsform" gleich „211000 e.V." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015523` |
| wenn „Rechtsform" gleich „230000 rechtsf. Stiftung" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015524` |
| wenn „Rechtsform" gleich „252000 SCE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015525` |
| wenn „Rechtsform" gleich „123000 eGbR" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015526` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Staat der Eintragung" | muss ausgefüllt werden | — | `R05000015527` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Staat der Eintragung" | entfällt | — | `R05000015527` |
| wenn „Rechtsform" gleich „138100 sonst. rechtsf. Personengesellschaft" oder „242000 Gebietskörperschaft" oder „540000 Gewerbebetrieb einer KöR" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015528` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | muss ausgefüllt werden | — | `R05000015529` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | entfällt | — | `R05000015529` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | muss ausgefüllt werden | — | `R05000015530` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | entfällt | — | `R05000015530` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" gleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | muss ausgefüllt werden | — | `R05000012722` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" ungleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | darf nicht ausgefüllt werden | — | `R05000012722` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012721` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012721` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" gleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | muss ausgefüllt werden | — | `R05000012722` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" ungleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | darf nicht ausgefüllt werden | — | `R05000012722` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012721` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012721` |
| wenn „Rechtsform" gleich „211000 e.V." oder „221100 GmbH" oder „222110 AG" oder „221200 UG" oder „223400 Stiftung & Co. KGaA" oder „230000 rechtsf. Stiftung" oder „242000 Gebietskörperschaft" oder „251000 eG" ist | „Juristische Person als Gesellschafter" | muss ausgefüllt werden | — | `R05000015533` |
| wenn „Rechtsform" ungleich „211000 e.V." oder „221100 GmbH" oder „222110 AG" oder „221200 UG" oder „223400 Stiftung & Co. KGaA" oder „230000 rechtsf. Stiftung" oder „242000 Gebietskörperschaft" oder „251000 eG" ist | „Juristische Person als Gesellschafter" | entfällt | — | `R05000015533` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" gleich „002 Juristische Person oder Personengesellschaft" ist | „Identifikation des Unternehmens" | muss ausgefüllt werden | — | `R05000015535` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" ungleich „002 Juristische Person oder Personengesellschaft" ist | „Identifikation des Unternehmens" | entfällt | — | `R05000015535` |
| wenn „Rechtsform" gleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Personengesellschaft als Gesellschafter" | muss ausgefüllt werden | — | `R05000015536` |
| wenn „Rechtsform" ungleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Personengesellschaft als Gesellschafter" | entfällt | — | `R05000015536` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" gleich „001 Natürliche Person" ist | _mehrere Felder_ | entfällt und muss ausgefüllt werden | — | `R05000015537` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" gleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | muss ausgefüllt werden | — | `R05000012722` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" ungleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | darf nicht ausgefüllt werden | — | `R05000012722` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012721` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012721` |
| wenn „Rechtsform" gleich „121000 GbR" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000015508` |
| wenn „Rechtsform" ungleich „121000 GbR" ist | „Unternehmensname" | entfällt | — | `R05000015508` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | muss ausgefüllt werden | — | `R05000015509` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | entfällt | — | `R05000015509` |
| wenn „Rechtsform" gleich „222200 SE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015510` |
| wenn „Rechtsform" gleich „251000 eG" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015511` |
| wenn „Rechtsform" gleich „213000 VVaG" oder „221100 GmbH" oder „221200 UG" oder „222110 AG" oder „223100 KGaA" oder „223211 GmbH & Co. KGaA" oder „223212 UG & Co. KGaA" oder „223221 AG & Co. KGaA" oder „223222 SE & Co. KGaA" oder „223400 Stiftung & Co. KGaA" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015512` |
| wenn „Rechtsform" gleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000015513` |
| wenn „Rechtsform" ungleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | entfällt | — | `R05000015513` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | muss ausgefüllt werden | — | `R05000015514` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | entfällt | — | `R05000015514` |
| wenn „Rechtsform" gleich „111100 OHG" oder „111211 GmbH & Co. OHG" oder „111212 UG & Co. OHG" oder „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „411000 e.K.; e.Kfm.; e.Kfr." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015515` |
| wenn „Rechtsform" gleich „294000 ausl. juristische Person (EU-Recht)" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015516` |
| wenn „Rechtsform" gleich „268100 sonst. juristische Person" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015517` |
| wenn „Rechtsform" gleich „295000 ausl. juristische Person (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015518` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | muss ausgefüllt werden | — | `R05000015519` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | entfällt | — | `R05000015519` |
| wenn „Rechtsform" gleich „191000 ausl. Personengesellschaft (EU-Recht)" oder „192000 ausl. Personengesellschaft (Nicht-EU-Recht)" oder „491000 ausl. gew. Einzelunternehmen (EU-Recht)" oder „492000 ausl. gew. Einzelunternehmen (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015520` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | wird gezeigt | — | `R05000015521` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | entfällt | — | `R05000015521` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | muss ausgefüllt werden | — | `R05000015522` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | entfällt | — | `R05000015522` |
| wenn „Rechtsform" gleich „211000 e.V." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015523` |
| wenn „Rechtsform" gleich „230000 rechtsf. Stiftung" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015524` |
| wenn „Rechtsform" gleich „252000 SCE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015525` |
| wenn „Rechtsform" gleich „123000 eGbR" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015526` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Staat der Eintragung" | muss ausgefüllt werden | — | `R05000015527` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Staat der Eintragung" | entfällt | — | `R05000015527` |
| wenn „Rechtsform" gleich „138100 sonst. rechtsf. Personengesellschaft" oder „242000 Gebietskörperschaft" oder „540000 Gewerbebetrieb einer KöR" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000015528` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | muss ausgefüllt werden | — | `R05000015529` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | entfällt | — | `R05000015529` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | muss ausgefüllt werden | — | `R05000015530` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | entfällt | — | `R05000015530` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" gleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | muss ausgefüllt werden | — | `R05000012722` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" ungleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | darf nicht ausgefüllt werden | — | `R05000012722` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012721` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012721` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" gleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | muss ausgefüllt werden | — | `R05000012722` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" ungleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | darf nicht ausgefüllt werden | — | `R05000012722` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012721` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012721` |
| wenn „Stellen Sie eine Betriebsleitung ein oder wird eine Zweigniederlassung Ihres Betriebes von einer beauftragten Person geleitet?" gleich „wahr" ist | „Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters" | muss ausgefüllt werden | — | `R05000015500` |
| wenn „Stellen Sie eine Betriebsleitung ein oder wird eine Zweigniederlassung Ihres Betriebes von einer beauftragten Person geleitet?" ungleich „wahr" ist | „Persönliche Angaben der Betriebsleiterin oder des Betriebsleiters" | entfällt | — | `R05000015500` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" gleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | muss ausgefüllt werden | — | `R05000012722` |
| wenn „Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?" ungleich „wahr" ist | „Hauptwohnsitz der letzten fünf Jahre" | darf nicht ausgefüllt werden | — | `R05000012722` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt | — | `R05000012720` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012721` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012721` |
| wenn „Ein aktueller Auszug aus dem Handelsregister oder Genossenschaftsregister" gleich „001 liegt vor" ist | „Fügen Sie einen aktuellen Registerauszug bei." | muss ausgefüllt werden | — | `R05000012781` |
| wenn „Ein aktueller Auszug aus dem Handelsregister oder Genossenschaftsregister" ungleich „001 liegt vor" ist | „Fügen Sie einen aktuellen Registerauszug bei." | entfällt | — | `R05000012781` |
| wenn „Der Gesellschaftsvertrag oder die Satzung" gleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012782` |
| wenn „Der Gesellschaftsvertrag oder die Satzung" ungleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | entfällt | — | `R05000012782` |
| wenn „Eine Berufshaftpflicht" gleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012624` |
| wenn „Eine Berufshaftpflicht" ungleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012624` |
| wenn „Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen Sie, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012601` |
| wenn „Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen Sie, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012601` |
| wenn „Gibt oder gab es in den letzten fünf Jahren abhängige oder rechtskräftig abgeschlossene Bußgeldverfahren wegen gewerberechtlicher Verstöße gegen Sie oder von Ihnen vertretene Firma, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012602` |
| wenn „Gibt oder gab es in den letzten fünf Jahren abhängige oder rechtskräftig abgeschlossene Bußgeldverfahren wegen gewerberechtlicher Verstöße gegen Sie oder von Ihnen vertretene Firma, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012602` |
| wenn „Gibt oder gab es in der Vergangenheit sonstige abhängige oder rechtskräftig abgeschlossene gewerbliche Verfahren gegen Sie oder eine von Ihnen vertretene Firma, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012603` |
| wenn „Gibt oder gab es in der Vergangenheit sonstige abhängige oder rechtskräftig abgeschlossene gewerbliche Verfahren gegen Sie oder eine von Ihnen vertretene Firma, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012603` |
| wenn „Liegt ein Antrag auf Eröffnung eines Insolvenz- oder Vergleichsverfahrens gegen Sie vor?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012680` |
| wenn „Liegt ein Antrag auf Eröffnung eines Insolvenz- oder Vergleichsverfahrens gegen Sie vor?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012680` |
| wenn „Liegt eine Ablehnung der Eröffnung eines Insolvenzverfahrens über Ihr Vermögen mangels Masse gegen Sie vor?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012681` |
| wenn „Liegt eine Ablehnung der Eröffnung eines Insolvenzverfahrens über Ihr Vermögen mangels Masse gegen Sie vor?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012681` |
| wenn „Haben Sie eine Vermögensauskunft gemäß § 802c ZPO abgegeben?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012604` |
| wenn „Haben Sie eine Vermögensauskunft gemäß § 802c ZPO abgegeben?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012604` |
| wenn „Liegt gegen Sie eine entsprechende Haftanforderung gemäß 802g ZPO vor?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012607` |
| wenn „Liegt gegen Sie eine entsprechende Haftanforderung gemäß 802g ZPO vor?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012607` |
| wenn „Liegt eine Eintragung im Schuldnerverzeichnis nach 882b ZPO gegen Sie vor?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012608` |
| wenn „Liegt eine Eintragung im Schuldnerverzeichnis nach 882b ZPO gegen Sie vor?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012608` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" gleich „001 Ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000012684` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" ungleich „001 Ist beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | — | `R05000012684` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" gleich „002 Ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | muss ausgefüllt werden | — | `R05000012685` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" ungleich „002 Ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | darf nicht ausgefüllt werden | — | `R05000012685` |
| wenn „Liegt Ihnen eine Bescheinigung in Steuersachen des Finanzamtes vor, die Ihre Unbedenklichkeit bestätigt?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012682` |
| wenn „Liegt Ihnen eine Bescheinigung in Steuersachen des Finanzamtes vor, die Ihre Unbedenklichkeit bestätigt?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012682` |
| wenn „Liegt Ihnen eine Bescheinigung in Steuersachen des kommunalen Steueramtes vor?" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012683` |
| wenn „Liegt Ihnen eine Bescheinigung in Steuersachen des kommunalen Steueramtes vor?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012683` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „002 ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | muss ausgefüllt werden | — | `R05000012761` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „002 ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | darf nicht ausgefüllt werden | — | `R05000012761` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „001 ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000012762` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „001 ist beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | — | `R05000012762` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Es muss mindestens eines der Felder F05000017664 "Immobilienmakler", F05000017666 "Darlehensvermittler", F05000017668 "Bauträger", F05000017670 "Baubetreuer" oder F05000017672 "Wohnimmobilienverwalter" = "wahr" sein.</mark> — Regel `R05000012679`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000011789_G05000011849_F05000017672["Beantragen Sie eine Erlaubnis für die "] ==>|"= wahr → required"| G05000011857_G05000011824["Berufshaftpflichtversicherung"]
  G05000011789_G05000011849_F05000017672["Beantragen Sie eine Erlaubnis für die "] -.->|"<> wahr → hide"| G05000011857_G05000011824["Berufshaftpflichtversicherung"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 121000 GbR → required"| G05000013335_G05000013336_F05000017734["Unternehmensname"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -.->|"<> 121000 GbR → hide"| G05000013335_G05000013336_F05000017734["Unternehmensname"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Stiftungsverze → required"| G05000013335_G05000013336_F05000017514["Eintragungsnummer"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Stiftungsverze → hide"| G05000013335_G05000013336_F05000017514["Eintragungsnummer"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 222200 SE → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 251000 eG → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 213000 VVaG, 221100 GmbH, 22 → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 412000 nicht eingetr. gew. E → required"| G05000013335_G05000013336_F05000017735["Unternehmensname"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -.->|"<> 412000 nicht eingetr. gew. E → hide"| G05000013335_G05000013336_F05000017735["Unternehmensname"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] ==>|"<> Eintragung im Ausland, Eintr → required"| G05000013335_G05000013336_F60000000328["Nummer des Registereintrages"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Ausland, Eintr → hide"| G05000013335_G05000013336_F60000000328["Nummer des Registereintrages"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 111100 OHG, 111211 GmbH & Co → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 294000 ausl. juristische Per → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -->|"= 268100 sonst. juristische Pe → show"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -->|"= 295000 ausl. juristische Per → show"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Stiftungsverze → required"| G05000013335_G05000013336_F05000018301["Stiftungsverzeichnis (Freitext)"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Stiftungsverze → hide"| G05000013335_G05000013336_F05000018301["Stiftungsverzeichnis (Freitext)"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -->|"= 191000 ausl. Personengesells → show"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -->|"<> 121000 GbR, 340000 GmbH i.G. → show"| G05000013335_G05000013336_F05000017512["Hinweis"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -.->|"= 121000 GbR, 340000 GmbH i.G. → hide"| G05000013335_G05000013336_F05000017512["Hinweis"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"<> 121000 GbR, 340000 GmbH i.G. → required"| G05000013335_G05000013336_F60000000319["Eingetragener Name"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -.->|"= 121000 GbR, 340000 GmbH i.G. → hide"| G05000013335_G05000013336_F60000000319["Eingetragener Name"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 211000 e.V. → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 230000 rechtsf. Stiftung → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 252000 SCE → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] ==>|"= 123000 eGbR → required"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Ausland → required"| G05000013335_G05000013336_F05000017518["Staat der Eintragung"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Ausland → hide"| G05000013335_G05000013336_F05000017518["Staat der Eintragung"]
  G05000013335_G05000013336_F05000017511["Rechtsform"] -->|"= 138100 sonst. rechtsf. Perso → show"| G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Ausland → required"| G05000013335_G05000013336_F60000000327["Ort des Registereintrags"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Ausland → hide"| G05000013335_G05000013336_F60000000327["Ort des Registereintrags"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] ==>|"<> Eintragung im Ausland, Eintr → required"| G05000013335_G05000013336_F05000017721["Registergericht"]
  G05000013335_G05000013336_F05000017720["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Ausland, Eintr → hide"| G05000013335_G05000013336_F05000017721["Registergericht"]
  G05000013335_G05000011864_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000013335_G05000011864_G60000000083_F60000000232["Monat"]
  G05000013335_G05000011864_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013335_G05000011864_G05000011865_G60000000191["Anschrift Ausland"]
  G05000013335_G05000011864_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → forbidden"| G05000013335_G05000011864_G05000011865_G60000000191["Anschrift Ausland"]
  G05000013335_G05000011864_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013335_G05000011864_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000011864_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide"| G05000013335_G05000011864_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000011864_G05000011866_F05000017736["Hat sich Ihr Hauptwohnsitz in den letz"] ==>|"= wahr → required"| G05000013335_G05000011864_G05000011866_G05000011867["Hauptwohnsitz der letzten fünf Jahre"]
  G05000013335_G05000011864_G05000011866_F05000017736["Hat sich Ihr Hauptwohnsitz in den letz"] -.->|"<> wahr → forbidden"| G05000013335_G05000011864_G05000011866_G05000011867["Hauptwohnsitz der letzten fünf Jahre"]
  G05000013335_G05000011864_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013335_G05000011864_G05000011866_G05000011867_G60000000191["Anschrift Ausland"]
  G05000013335_G05000011864_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide"| G05000013335_G05000011864_G05000011866_G05000011867_G60000000191["Anschrift Ausland"]
  G05000013335_G05000011864_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013335_G05000011864_G05000011866_G05000011867_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000011864_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide"| G05000013335_G05000011864_G05000011866_G05000011867_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000013335_G05000013337_G05000013065_G05000011868_G60000000083_F60000000232["Monat"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_G60000000191["Anschrift Ausland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → forbidden"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_G60000000191["Anschrift Ausland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_F05000017736["Hat sich Ihr Hauptwohnsitz in den letz"] ==>|"= wahr → required"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867["Hauptwohnsitz der letzten fünf Jahre"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_F05000017736["Hat sich Ihr Hauptwohnsitz in den letz"] -.->|"<> wahr → forbidden"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867["Hauptwohnsitz der letzten fünf Jahre"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_G60000000191["Anschrift Ausland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_G60000000191["Anschrift Ausland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide"| G05000013335_G05000013337_G05000013065_G05000011868_G05000011866_G05000011867_G05000013177["Straßenanschrift Inland"]
  G05000013335_G05000013337_G05000013338_G05000013336_F05000017511["Rechtsform"] ==>|"= 211000 e.V., 221100 GmbH, 22 → required"| G05000013335_G05000013337_G05000013338_G05000012703["Juristische Person als Gesellschafter"]
  G05000013335_G05000013337_G05000013338_G05000013336_F05000017511["Rechtsform"] -.->|"<> 211000 e.V., 221100 GmbH, 22 → hide"| G05000013335_G05000013337_G05000013338_G05000012703["Juristische Person als Gesellschafter"]
  G05000013335_G05000013337_G05000013338_F05000018285["Ist der Gesellschafter eine Natürliche"] ==>|"= 002 Juristische Person oder  → required"| G05000013335_G05000013337_G05000013338_G05000013336["Identifikation des Unternehmens"]
  unclear0["?: Es muss mindestens eines der Felder F05000017664 "Immobilien"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
