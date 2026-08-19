---
name: antrag-s05000001294
description: Führt Antragstellende durch „Gewerbeabmeldung" (FIM S05000001294 2.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Gewerbeabmeldung

- **FIM-ID:** `S05000001294 2.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** Anlage 3 Nr. 1 GewAnzV vom 11.12.2024; Anlage 3 Nr. 2 GewAnzV vom 11.12.2024; § 14 GewO vom 27.12.2024; § 15 GewO vom 27.12.2024; § 11 GewO vom 27.12.2024; Anlage 3 GewAnzV vom 11.12.2024; § 8a HGB; § 8b HGB
- **Kompiliert:** 2026-08-13T15:41:58Z aus https://fimportal.de/api/v1/schemas/S05000001294/2.0.0/xdf
- **Umfang:** 180 Felder, 66 gesicherte Bedingungen, 4 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet werden (Rechtsgrundlage stimmt nicht überein (D99000001878)). Zu Fristen, Kosten, Unterlagen und Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle verweisen.

## Felder

### Umfang der Anzeige (`G05000011640`)

- **Grund für die Gewerbeabmeldung** (`F05000017437`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 25 GewAnzV; Anlage 3 Nr. 26 GewAnzV
- **Gründe für die Betriebsaufgabe** (`F05000017438`) — Pflicht, conditional
  - Rechtsgrundlage: Anlage 3 Nr. 28 GewAnzV
  - Hilfe: z.B. Alter, wirtschaftliche Schwierigkeiten, Insolvenzverfahren etc.
Hinweis: Die Wiederaufnahme der Tätigkeit ist erneut anzeigepflichtig.
- **Wurde die aufgegebene Tätigkeit (zuletzt) im Nebenerwerb betrieben?** (`F05000017450`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 19 GewAnzV
- **Datum der Betriebsaufgabe:** (`F05000017451`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 20 GewAnzV
  - Hilfe: Beachten Sie, dass das angegebene Datum nicht mehr als 4 Wochen in der Vergangenheit liegen darf.

### Umfang der Anzeige › Abgemeldete Tätigkeit (`G05000011728`)

- **Hinweis** (`F05000017612`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 18 GewAnzV
- **Welche Tätigkeit wurde zum Zeitpunkt vor der Änderung ausgeübt?** (`F05000017440`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 18 GewAnzV; Anlage 2 Nr. 18 GewAnzV
- **Beschreiben Sie die Tätigkeit möglichst umfassend:** (`F05000017488`) — Pflicht
  - Rechtsgrundlage: Anlage 1 Nr. 18 GewAnzV; Anlage 3 Nr. 18 GewAnzV

### Umfang der Anzeige › Abgemeldete Tätigkeit › Weitere Tätigkeit (`G05000011729`)

- **Welche weitere Tätigkeit haben Sie ausgeübt?** (`F05000017614`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 18 GewAnzV
- **Beschreiben Sie die Tätigkeit möglichst umfassend:** (`F05000017488`) — Pflicht
  - Rechtsgrundlage: Anlage 1 Nr. 18 GewAnzV; Anlage 3 Nr. 18 GewAnzV

### Umfang der Anzeige › Art des abgemeldeten Betriebs › Welche Art des Betriebes möchten Sie für Ihr Gewerbe abmelden? (`G05000011730`)

- **Handel** (`F05000017592`) — optional
  - Rechtsgrundlage: Anlage 1 Nr. 21 GewAnzV; Anlage 3 Nr. 21 GewAnzV
- **Handwerk** (`F05000017593`) — optional
  - Rechtsgrundlage: Anlage 1 Nr. 21 GewAnzV; Anlage 3 Nr. 21 GewAnzV
- **Industrie** (`F05000017594`) — optional
  - Rechtsgrundlage: Anlage 1 Nr. 21 GewAnzV; Anlage 3 Nr. 21 GewAnzV
- **Sonstiges** (`F05000017595`) — optional
  - Rechtsgrundlage: Anlage 1 Nr. 21 GewAnzV; Anlage 3 Nr. 21 GewAnzV
- **Die Abmeldung wird erstattet für:** (`F05000017445`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 23 GewAnzV; Anlage 3 Nr. 24 GewAnzV

### Umfang der Anzeige › Art des abgemeldeten Betriebs › Beschäftigte Personen (`G05000011731`)

- **Beschäftigten Sie Personen in Vollzeit?** (`F05000017446`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 22 GewAnzV
  - Hilfe: Zahl der bei der Geschäftsaufgabe / Geschäftsübergabe tätigen Personen (einschließlich Aushilfen, Ehe- oder Lebenspartner des Inhabers); ohne Inhaber
- **Anzahl der Personen in Vollzeit** (`F05000017499`) — optional, conditional
  - Rechtsgrundlage: Anlage 1 Nr. 22 GewAnzV; Anlage 3 Nr. 22 GewAnzV
- **Beschäftigten Sie Personen in Teilzeit?** (`F05000017448`) — Pflicht
  - Rechtsgrundlage: Anlage 3 Nr. 22 GewAnzV
  - Hilfe: Zahl der bei der Geschäftsaufgabe / Geschäftsübergabe tätigen Personen (einschließlich Aushilfen, Ehe- oder Lebenspartner des Inhabers); ohne Inhaber
- **Anzahl der Personen in Teilzeit** (`F05000017501`) — optional, conditional
  - Rechtsgrundlage: Anlage 1 Nr. 22 GewAnzV; Anlage 3 Nr. 22 GewAnzV

### Angaben zum Betrieb (`G05000011678`)

- **Hinweis** (`F05000017510`) — Pflicht
  - Rechtsgrundlage: § 14 GewO
- **Rechtsform** (`F05000017511`) — Pflicht
  - Rechtsgrundlage: Anlage 1 Nr. 1 GewAnzV; Anlage 2 Nr. 1 GewAnzV; Anlage 3 Nr. 1 GewAnzV; Anlage 1 Nr. 2 GewAnzV; Anlage 2 Nr. 2 GewAnzV; Anlage 3 Nr. 2 GewAnzV; § 14 GewO; Anlage 1 GewAnzV Nr.1; Anlage 3 GewAnzV Nr. 3; Anlage 3 GewAnzV Nr. 13 _(geerbt)_

### Angaben zum Betrieb › Register- und Verzeichniseintrag (`G05000011679`)

- **Hinweis** (`F05000017512`) — optional
  - Rechtsgrundlage: Anlage 1 Nr. 1 GewAnzV; Anlage 2 Nr. 1 GewAnzV; Anlage 3 Nr. 1 GewAnzV; Anlage 1 Nr. 2 GewAnzV; Anlage 2 Nr. 2 GewAnzV; Anlage 3 Nr. 2 GewAnzV; § 14 GewO; Anlage 1 GewAnzV Nr.1; Anlage 3 GewAnzV Nr. 3; Anlage 3 GewAnzV Nr. 13 _(geerbt)_
- **Art der Eintragung oder des Registers** (`F05000017720`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2
  - Hilfe: Geben Sie an, um welche Art von Eintrag es sich handelt.
- **Eintragungsnummer** (`F05000017514`) — optional, conditional
  - Rechtsgrundlage: Anlage 1 Nr. 1 GewAnzV; Anlage 2 Nr. 1 GewAnzV; Anlage 3 Nr. 1 GewAnzV; Anlage 1 Nr. 2 GewAnzV; Anlage 2 Nr. 2 GewAnzV; Anlage 3 Nr. 2 GewAnzV; § 14 GewO; Anlage 1 GewAnzV Nr.1; Anlage 3 GewAnzV Nr. 3; Anlage 3 GewAnzV Nr. 13 _(geerbt)_
- **Bundesland des Stiftungsregistereintrags** (`F60000000374`) — optional, conditional
  - Rechtsgrundlage: GewAnzV vom 03.07.2019, Nr. 2; angelehnt an XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; basierend auf Codeliste urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:bundesland_2010-04-01; urn:xoev-de:xunternehmen:standard:basismodul_1.1
  - Hilfe: Bei Einträgen im Stiftungsverzeichnis: Angabe des Bundeslandes bzw. der Behörde, indessen oder deren Stiftungsverzeichnis der Eintrag geführt wird.
- **Nummer des Registereintrages** (`F60000000328`) — optional, conditional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Registergericht** (`F05000017721`) — optional, conditional
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Staat der Eintragung** (`F05000017518`) — optional, conditional
  - Rechtsgrundlage: Anlage 1 Nr. 1 GewAnzV; Anlage 2 Nr. 1 GewAnzV; Anlage 3 Nr. 1 GewAnzV; Anlage 1 Nr. 2 GewAnzV; Anlage 2 Nr. 2 GewAnzV; Anlage 3 Nr. 2 GewAnzV; § 14 GewO; Anlage 1 GewAnzV Nr.1; Anlage 3 GewAnzV Nr. 3; Anlage 3 GewAnzV Nr. 13 _(geerbt)_
- **Ort des Registereintrags** (`F60000000327`) — optional, conditional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2
- **Eingetragener Name** (`F60000000319`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.

### Angaben zum Betrieb › Angaben zum Unternehmen (`G05000011647`)

- **Geschäftsbezeichnung** (`F60000000320`) — optional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.
- **Liegt eine Beteiligung der öffentlichen Hand vor?** (`F05000017462`) — Pflicht
  - Rechtsgrundlage: Anlage 1 Nr. 13 GewAnzV; Anlage 2 Nr. 13 GewAnzV; Anlage 3 Nr. 13 GewAnzV

### Einzelunternehmen - Angaben der anzeigenden Person (`G05000011594`)

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
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Einzelunternehmen - Angaben der anzeigenden Person › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Einzelunternehmen - Angaben der anzeigenden Person › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.Meldeanschrift.postleitzahl Version 8; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Einzelunternehmen - Angaben der anzeigenden Person › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Einzelunternehmen - Angaben der anzeigenden Person › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

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

### Einzelunternehmen - Angaben der anzeigenden Person › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Einzelunternehmen - Angaben der anzeigenden Person › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Einzelunternehmen - Angaben der anzeigenden Person › Anschrift › Anschrift Ausland (`G60000000191`)

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

### Einzelunternehmen - Angaben der anzeigenden Person › Erreichbarkeit (`G05000011747`)

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

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) (`G05000011596`)

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
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Existieren weitere gesetzlich Vertretende?** (`F05000017394`) — Pflicht
  - Rechtsgrundlage: § 8 ff. HGB; § 11 GewO; § 14 GewO

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.Meldeanschrift.postleitzahl Version 8; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

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

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Anschrift › Anschrift Ausland (`G60000000191`)

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

### Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand) › Erreichbarkeit (`G05000011747`)

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

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters (`G05000011650`)

- **Sind Sie als anzeigestellende Gesellschafterin oder anzeigestellender Gesellschafter eine natürliche oder eine juristische Person?** (`F05000017395`) — Pflicht
  - Rechtsgrundlage: § 14 GewO; § 11 GewO; § 8 ff. HGB

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben zur juristischen Person (`G05000011601`)

- **Rechtsform** (`F05000017511`) — Pflicht
  - Rechtsgrundlage: § 11 (1) GewO; § 14 GewO; § 8 ff. HGB _(geerbt)_
- **Art der Eintragung oder des Registers** (`F60000000347`) — optional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2
  - Hilfe: Geben Sie an, um welche Art von Eintrag es sich handelt.
- **Land der Eintragung** (`F05000017400`) — optional, conditional
  - Rechtsgrundlage: § 11 GewO; § 14 GewO; § 20 (1) S.2 GwG
  - Hilfe: Geben Sie den Namen des Staates bzw. des Landes an, (Beispiel Deutschland, Frankreich,...), in dem sich die registerführende Stelle befindet, die ihren Handels-, Genossenschafts- oder Vereinsregistereintrag vorgenommen hat.

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben zur juristischen Person › Eintragung im Stiftungsverzeichnis (Gewerbemeldung) (`G05000011602`)

- **Nummer des Registereintrages** (`F60000000328`) — Pflicht
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Stiftungsverzeichnis** (`F05000017515`) — Pflicht
  - Rechtsgrundlage: § 11 (1) GewO; § 14 GewO; § 8 (2b) BGB _(geerbt)_
- **Eingetragener Name** (`F60000000319`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben zur juristischen Person › Eintragung in einem Inland- Register (`G05000011603`)

- **Nummer des Registereintrages** (`F60000000328`) — Pflicht
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Registergericht** (`F60000000325`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Ort des Registereintrags** (`F60000000327`) — Pflicht
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2
- **Eingetragener Name** (`F60000000319`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters (`G05000011599`)

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
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staat der Geburt** (`F60000000235`) — Pflicht
  - Rechtsgrundlage: XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat)
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Existieren weitere gesetzlich Vertretende?** (`F05000017397`) — Pflicht
  - Rechtsgrundlage: § 8 ff. HGB; § 705 ff. BGB

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.Meldeanschrift.postleitzahl Version 8; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1 _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Anschrift › Anschrift in Deutschland (`G05000011745`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

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

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Anschrift › Anschrift Ausland (`G60000000191`)

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

### Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters › Erreichbarkeit (`G05000011747`)

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

### Angaben zur vertretungsberechtigten Person (`G05000011605`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Angaben zur Hauptniederlassung › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zur Hauptniederlassung › Erreichbarkeit (`G05000011747`)

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

### Angaben zur künftigen Betriebsstätte (`G05000011607`)

- **Geschäftsbezeichnung** (`F60000000320`) — optional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.

### Angaben zur künftigen Betriebsstätte › Anschrift Inland (`G05000011494`)

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

### Angaben zur künftigen Betriebsstätte › Erreichbarkeit (`G05000011747`)

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

### Angaben zur aktuellen Betriebsstätte › Anschrift Inland (`G05000011494`)

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

### Angaben zur aktuellen Betriebsstätte › Erreichbarkeit (`G05000011747`)

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

### Nachweise (`G05000011648`)

- **Fügen Sie einen aktuellen Registerauszug bei.** (`F05000017521`) — optional
  - Rechtsgrundlage: Anlage 3 Nr. 2 GewAnzV; Anlage 3 Nr. 29 GewAnzV; referenzbasiert _(geerbt)_
  - Hilfe: Bitte beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Vorherige Gewerbeanzeige** (`F05000017464`) — Pflicht
  - Rechtsgrundlage: Anlage 1 Nr. 29 GewAnzV
  - Hilfe: Fügen Sie die bisherige Gewerbeanzeige bei.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: Anlage 3 Nr. 2 GewAnzV; Anlage 3 Nr. 29 GewAnzV; referenzbasiert _(geerbt)_
  - Hilfe: Bitte laden Sie weitere Unterlagen hoch, falls nötig. Bitte beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Existieren weitere gesetzlich Vertretende?" gleich „ja" ist | „Juristische Person - Persönliche Angaben der gesetzlichen Vertretung (Geschäftsführende, Vorstand)" | muss ausgefüllt werden | — | `R05000012288` |
| wenn „Grund für die Gewerbeabmeldung" gleich „Vollständige Aufgabe" ist | „Gründe für die Betriebsaufgabe" | muss ausgefüllt werden | — | `R05000012353` |
| wenn „Beschäftigten Sie Personen in Teilzeit?" gleich „Wahr" ist | „Anzahl der Personen in Teilzeit" | muss ausgefüllt werden | — | `R05000012462` |
| wenn „Beschäftigten Sie Personen in Teilzeit?" ungleich „Wahr" ist | „Anzahl der Personen in Teilzeit" | darf nicht ausgefüllt werden | — | `R05000012462` |
| wenn „Beschäftigten Sie Personen in Vollzeit?" gleich „wahr" ist | „Anzahl der Personen in Vollzeit" | muss ausgefüllt werden | — | `R05000012463` |
| wenn „Beschäftigten Sie Personen in Vollzeit?" ungleich „wahr" ist | „Anzahl der Personen in Vollzeit" | darf nicht ausgefüllt werden | — | `R05000012463` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | muss ausgefüllt werden | — | `R05000012386` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | entfällt | — | `R05000012386` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | muss ausgefüllt werden | — | `R05000012387` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | darf nicht ausgefüllt werden | — | `R05000012387` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Staat der Eintragung" | muss ausgefüllt werden | — | `R05000012389` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Staat der Eintragung" | entfällt | — | `R05000012389` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | muss ausgefüllt werden | — | `R05000012454` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | darf nicht ausgefüllt werden | — | `R05000012454` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Bundesland des Stiftungsregistereintrags" | darf nicht ausgefüllt werden und muss ausgefüllt werden | — | `R05000012699` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | muss ausgefüllt werden | — | `R05000012700` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | darf nicht ausgefüllt werden | — | `R05000012700` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Sind Sie als anzeigestellende Gesellschafterin oder anzeigestellender Gesellschafter eine natürliche oder eine juristische Person?" gleich „Natürliche Person" ist | „Personengesellschaft - Angaben zur juristischen Person" | entfällt | — | `R05000012368` |
| wenn „Sind Sie als anzeigestellende Gesellschafterin oder anzeigestellender Gesellschafter eine natürliche oder eine juristische Person?" gleich „Natürliche Person" ist | „Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters" | muss ausgefüllt werden | — | `R05000012368` |
| wenn „Existieren weitere gesetzlich Vertretende?" gleich „ja" ist | „Personengesellschaft - Angaben der anzeigestellenden Gesellschafterin oder des anzeigestellenden Gesellschafters" | muss ausgefüllt werden | — | `R05000012369` |
| wenn „Art der Eintragung oder des Registers" gleich einem beliebigen Wert ist | „Eintragung im Stiftungsverzeichnis (Gewerbemeldung)" | muss ausgefüllt werden | — | `R05000012295` |
| wenn „Art der Eintragung oder des Registers" gleich einem beliebigen Wert ist | „Eintragung in einem Inland- Register" | entfällt | — | `R05000012295` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Ausland" ist | „Eintragung in einem Inland- Register" | muss ausgefüllt werden | — | `R05000012296` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Ausland" ist | „Eintragung im Stiftungsverzeichnis (Gewerbemeldung)" | entfällt | — | `R05000012296` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Land der Eintragung" | muss ausgefüllt werden | — | `R05000012297` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Eintragung im Stiftungsverzeichnis (Gewerbemeldung)" | entfällt | — | `R05000012297` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Wenn in Datenfeld F05000017394 'Abfrage weitere gesetzlich Vertretende' Auswahl gleich = 'nein', dann ist Datenfeldgruppe G05000011596 'Juristische Person - Angaben der gesetzlichen Vertretung (Gewerbemeldung)' nicht ein weiteres Mal anzuzeigen.</mark> — Regel `R05000012288`
- <mark>Wenn im Datenfeld F05000017445 "Art Niederlassung (Gewerbeabmeldung)" Auswahl = 01 "eine Hauptniederlassung ODER 03 "eine unselbstständige Zweigstelle", dann erscheint die Gruppe G05000011606 Angaben zur Hauptniederlassung (Gewerbemeldung) und die Gruppe G05000011605 "Angaben zur vertretungsberechtigten Person (Gewerbemeldung)" und muss ausgefüllt werden</mark> — Regel `R05000013032`
- <mark>Wenn im Datenfeld F05000017437 "Grund Gewerbeabmeldung" Auswahl = 03 "Gesellschafteraustritt", dann erscheint Gruppe G05000011605 "Angaben zur vertretungsberechtigten Person (Gewerbemeldung)" und muss ausgefüllt werden</mark> — Regel `R05000013033`
- <mark>Im Datenfeld F05000017511 "Rechtsform (XUnternehmen) Verwendung-in-XGewO" sind in der Codeliste nur die Einträge folgender Codes zur Auswahl anzuzeigen: 211000, 213000-213200, 221000-223400, 230000-232000, 242000, 242400, 251000, 252000, 290000, 294000-298100, 340000, 350000.</mark> — Regel `R05000012294`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000011596_F05000017394["Existieren weitere gesetzlich Vertrete"] ==>|"= ja → required"| G05000011596["Juristische Person - Persönliche Angab"]
  G05000011640_F05000017437["Grund für die Gewerbeabmeldung"] ==>|"= Vollständige Aufgabe → required"| G05000011640_F05000017438["Gründe für die Betriebsaufgabe"]
  G05000011640_G05000011644_G05000011731_F05000017448["Beschäftigten Sie Personen in Teilzeit"] ==>|"= Wahr → required"| G05000011640_G05000011644_G05000011731_F05000017501["Anzahl der Personen in Teilzeit"]
  G05000011640_G05000011644_G05000011731_F05000017448["Beschäftigten Sie Personen in Teilzeit"] -.->|"<> Wahr → forbidden"| G05000011640_G05000011644_G05000011731_F05000017501["Anzahl der Personen in Teilzeit"]
  G05000011640_G05000011644_G05000011731_F05000017446["Beschäftigten Sie Personen in Vollzeit"] ==>|"= wahr → required"| G05000011640_G05000011644_G05000011731_F05000017499["Anzahl der Personen in Vollzeit"]
  G05000011640_G05000011644_G05000011731_F05000017446["Beschäftigten Sie Personen in Vollzeit"] -.->|"<> wahr → forbidden"| G05000011640_G05000011644_G05000011731_F05000017499["Anzahl der Personen in Vollzeit"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Stiftungsverze → required"| G05000011678_G05000011679_F05000017514["Eintragungsnummer"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Stiftungsverze → hide"| G05000011678_G05000011679_F05000017514["Eintragungsnummer"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] ==>|"<> Eintragung im Ausland, Eintr → required"| G05000011678_G05000011679_F60000000328["Nummer des Registereintrages"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Ausland, Eintr → forbidden"| G05000011678_G05000011679_F60000000328["Nummer des Registereintrages"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Ausland → required"| G05000011678_G05000011679_F05000017518["Staat der Eintragung"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Ausland → hide"| G05000011678_G05000011679_F05000017518["Staat der Eintragung"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Ausland → required"| G05000011678_G05000011679_F60000000327["Ort des Registereintrags"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Ausland → forbidden"| G05000011678_G05000011679_F60000000327["Ort des Registereintrags"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Stiftungsverze → forbidden+required"| G05000011678_G05000011679_F60000000374["Bundesland des Stiftungsregistereintra"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] ==>|"<> Eintragung im Ausland, Eintr → required"| G05000011678_G05000011679_F05000017721["Registergericht"]
  G05000011678_G05000011679_F05000017720["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Ausland, Eintr → forbidden"| G05000011678_G05000011679_F05000017721["Registergericht"]
  G05000011594_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011594_G60000000083_F60000000232["Monat"]
  G05000011594_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011594_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011594_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000011594_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011594_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011594_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011594_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000011594_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011594_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000011594_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011594_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 001 → forbidden"| G05000011594_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011594_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000011594_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011594_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 002 → forbidden"| G05000011594_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011596_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011596_G60000000083_F60000000232["Monat"]
  G05000011596_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011596_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011596_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000011596_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011596_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011596_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011596_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000011596_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011596_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000011596_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011596_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 001 → forbidden"| G05000011596_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011596_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000011596_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011596_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 002 → forbidden"| G05000011596_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011650_F05000017395["Sind Sie als anzeigestellende Gesellsc"] -.->|"= Natürliche Person → hide"| G05000011650_G05000011601["Personengesellschaft - Angaben zur jur"]
  G05000011650_F05000017395["Sind Sie als anzeigestellende Gesellsc"] ==>|"= Natürliche Person → required"| G05000011650_G05000011599["Personengesellschaft - Angaben der anz"]
  G05000011650_G05000011599_F05000017397["Existieren weitere gesetzlich Vertrete"] ==>|"= ja → required"| G05000011650_G05000011599["Personengesellschaft - Angaben der anz"]
  G05000011650_G05000011601_F60000000347["Art der Eintragung oder des Registers"] ==>|"= ? → required"| G05000011650_G05000011601_G05000011602["Eintragung im Stiftungsverzeichnis (Ge"]
  G05000011650_G05000011601_F60000000347["Art der Eintragung oder des Registers"] -.->|"= ? → hide"| G05000011650_G05000011601_G05000011603["Eintragung in einem Inland- Register"]
  G05000011650_G05000011601_F60000000347["Art der Eintragung oder des Registers"] ==>|"<> Eintragung im Stiftungsverze → required"| G05000011650_G05000011601_G05000011603["Eintragung in einem Inland- Register"]
  G05000011650_G05000011601_F60000000347["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Stiftungsverze → hide"| G05000011650_G05000011601_G05000011602["Eintragung im Stiftungsverzeichnis (Ge"]
  G05000011650_G05000011601_F60000000347["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Ausland → required"| G05000011650_G05000011601_F05000017400["Land der Eintragung"]
  G05000011650_G05000011601_F60000000347["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Ausland → hide"| G05000011650_G05000011601_G05000011602["Eintragung im Stiftungsverzeichnis (Ge"]
  G05000011650_G05000011599_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011650_G05000011599_G60000000083_F60000000232["Monat"]
  G05000011650_G05000011599_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011650_G05000011599_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011650_G05000011599_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000011650_G05000011599_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000011650_G05000011599_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011650_G05000011599_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011650_G05000011599_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000011650_G05000011599_G05000011746_G60000000191["Anschrift Ausland"]
  G05000011650_G05000011599_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000011650_G05000011599_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000011650_G05000011599_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 001 → forbidden"| G05000011650_G05000011599_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011650_G05000011599_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000011650_G05000011599_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000011650_G05000011599_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 002 → forbidden"| G05000011650_G05000011599_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  unclear0["?: Wenn in Datenfeld F05000017394 'Abfrage weitere gesetzlich V"]:::unclear
  unclear1["?: Wenn im Datenfeld F05000017445 "Art Niederlassung (Gewerbeab"]:::unclear
  unclear2["?: Wenn im Datenfeld F05000017437 "Grund Gewerbeabmeldung" Ausw"]:::unclear
  unclear3["?: Im Datenfeld F05000017511 "Rechtsform (XUnternehmen) Verwend"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
