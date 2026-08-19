---
name: antrag-s05000001317
description: Führt Antragstellende durch „Antrag auf Erteilung der Erlaubnis zur gewerbsmäßigen Schaustellung von Personen" (FIM S05000001317 1.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf Erteilung der Erlaubnis zur gewerbsmäßigen Schaustellung von Personen

- **FIM-ID:** `S05000001317 1.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 33a GewO vom 22.02.1999; § 49 GewO vom 22.02.1999; referenzbasiert
- **Kompiliert:** 2026-08-13T15:49:39Z aus https://fimportal.de/api/v1/schemas/S05000001317/1.0.0/xdf
- **Umfang:** 350 Felder, 202 gesicherte Bedingungen, 11 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet werden (Rechtsgrundlage stimmt nicht überein (D99000001901)). Zu Fristen, Kosten, Unterlagen und Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle verweisen.

## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Auswahl Erlaubnis gewerbsmäßigen Schaustellung von Personen (`G05000012036`)

- **Beantragen Sie eine Erlaubnis für eine Veranstaltung von Schaustellungen von Personen?** (`F05000017970`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Beantragen Sie eine Erlaubnis für die Zurverfügungstellung der Räume für Dritte?** (`F05000017971`) — optional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu beschäftigten Veranstaltungsteilnehmenden (`G05000012040`)

- **Geben Sie die Anzahl der Personen an, die zur Schau gestellt werden.** (`F05000017929`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Beschreiben Sie die Art der Schaustellung.** (`F05000017930`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
  - Hilfe: Hinweis: z.B. Striptease-Shop, Tabledance oder Peepshow

### Betriebskonzept des Betreibers › Angaben zum Veranstaltungsort (`G05000012024`)

- **Findet die Veranstaltung an der Geschäftsanschrift statt?** (`F05000017931`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zum Veranstaltungsort › Straßenanschrift Inland (`G05000011743`)

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

### Betriebskonzept des Betreibers (`G05000012023`)

- **Wie häufig wird die Veranstaltung durchgeführt?** (`F05000017932`) — Pflicht, conditional
  - Rechtsgrundlage: § 33a GewO
- **Wie ist die bauliche Sichtabsicherung nach außen hin gestaltet?** (`F05000017945`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen (`G05000012025`)

- **Ist bereits bekannt, wann die erste Schaustellung von Personen stattfindet?** (`F05000017933`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Angaben erste Veranstaltung › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: § 33a GewO _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: § 33a GewO _(geerbt)_

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Angaben erste Veranstaltung (`G05000012026`)

- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — optional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Schaustellungszeiten › Montag (`G05000012043`)

- **Montag** (`F05000017977`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — optional, conditional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Schaustellungszeiten › Dienstag (`G05000012044`)

- **Dienstag** (`F05000017979`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — Pflicht, conditional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Schaustellungszeiten › Mittwoch (`G05000012045`)

- **Mittwoch** (`F05000017980`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — optional, conditional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Schaustellungszeiten › Donnerstag (`G05000012046`)

- **Donnerstag** (`F05000017982`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — optional, conditional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Schaustellungszeiten › Freitag (`G05000012047`)

- **Freitag** (`F05000017984`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — optional, conditional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Schaustellungszeiten › Samstag (`G05000012048`)

- **Samstag** (`F05000017987`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — optional, conditional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zu regelmäßigen Veranstaltungen › Schaustellungszeiten › Sonntag (`G05000012049`)

- **Sonntag** (`F05000017988`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — optional, conditional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Angaben zur einmaligen Veranstaltung (`G05000012028`)

- **von** (`F05000017278`) — optional
  - Rechtsgrundlage: § 33a GewO _(geerbt)_
- **bis** (`F05000017279`) — optional
  - Rechtsgrundlage: § 33a GewO _(geerbt)_
- **Startuhrzeit der ersten Veranstaltung** (`F05000017934`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Enduhrzeit der ersten Veranstaltung** (`F05000017935`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Veranstaltungsräume (`G05000012029`)

- **Raumbezeichnung/-nummerierung** (`F05000017938`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Raumgröße in Quadratmeter** (`F05000017939`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Ergänzende Angaben zum Veranstaltungsraum** (`F05000017940`) — optional
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Veranstaltungsflächen › Angaben Veranstaltungsfläche (`G05000012050`)

- **Wählen Sie die Art der Veranstaltungsfläche.** (`F05000017941`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Beschreibung Sonstige Fläche** (`F05000017942`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Flächengröße in Quadratmeter** (`F05000017943`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Veranstaltungsflächen (`G05000012030`)

- **Wie stellen Sie sicher, dass die Veranstaltungsräume/-flächen oder Umkleiden nicht von Gästen betreten werden?** (`F05000017944`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Maßnahmen zum Schutz von zur Schau gestellten Personen und Dritten (`G05000012031`)

- **Erläutern Sie die Maßnahmen zur Verhinderung der Schaustellung von Minderjährigen sowie der Tätigkeit von Minderjährigen im Betrieb.** (`F05000017946`) — optional
  - Rechtsgrundlage: § 33a GewO
- **Hinweis:** (`F05000017947`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Betriebskonzept des Betreibers › Maßnahmen zur Verhinderung der Prostitution durch Opfer von Menschenhandel (`G05000013298`)

- **Erläutern Sie die Maßnahmen zur Verhinderung der Prostitution durch Opfer von Menschenhandel.** (`F05000017948`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Hinweis** (`F05000017949`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Unternehmensdaten › Identifikation des Unternehmens (`G05000011879`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft (`G05000011870`)

- **Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?** (`F05000018285`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Gesellschafterart** (`F05000019514`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Gesellschafter.Art Version 1.1; verwendet urn:xoev-de:xunternehmen:codeliste:artgesellschafterpersonengesellschaft Version 1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters (`G05000011873`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Identifikation des Unternehmens (`G05000011879`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung (`G05000011868`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Juristische Person als Gesellschafter › Gesetzliche Vertretung der juristischen Person als Gesellschafter › Angaben zur gesetzlichen Vertretung › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters (`G05000011873`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren (`G05000011866`)

- **Hat sich Ihr Hauptwohnsitz in den letzten 5 Jahren geändert?** (`F05000017736`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Zeitraum (`G05000011482`)

- **von** (`F05000017278`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
- **bis** (`F05000017279`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre (`G05000011867`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Straßenanschrift Inland (`G05000013177`)

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

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Personengesellschaft als Gesellschafter › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Änderung des Hauptwohnsitzes in den letzten fünf Jahren › Hauptwohnsitz der letzten fünf Jahre › Anschrift Ausland (`G60000000191`)

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

### Angaben zur Zuverlässigkeit (`G05000012032`)

- **Hinweis:** (`F05000017959`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, anhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftiges abgeschlossenes Strafverfahren gegen Sie?** (`F05000017960`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Gibt oder gab es in den letzten fünf Jahren anhängige oder rechtskräftig abgeschlossene Bußgeldverfahren wegen gewerberechtlicher Verstöße gegen Sie?** (`F05000017961`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
  - Hilfe: Der vorsätzliche oder fahrlässige Verstoß gegen die Erlaubnispflicht oder gegen vollziehbare Auflagen kann als Ordnungswidrigkeit mit einer Geldbuße von bis zu 5.000 Euro geahndet werden.
- **Gibt oder gab es in der Vergangenheit sonstige anhängige oder rechtskräftig abgeschlossene gewerbliche Verfahren gegen Sie?** (`F05000017962`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Haben Sie eine Vermögensauskunft gemäß §802c ZPO abgegeben?** (`F05000017965`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Liegt gegen Sie eine entsprechende Haftanordnung gemäß §802c ZPO vor?** (`F05000017966`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Liegt gegen Sie eine Eintragung im Schuldnerverzeichnis nach 882b ZPO gegen Sie vor?** (`F05000017967`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
  - Hilfe: Sie können über das Vollstreckungsportal der Länder prüfen, ob eine Eintragung im Schuldnerverzeichnis vorliegt. Eintragungen erfolgen, wenn:
- die Schuldnerin, der Schuldner seiner Pflicht zur Abgabe der Vermögensauskunft nicht nachgekommen ist,
- die Vollstreckung nach dem Inhalt der Vermögensauskunft offensichtlich nicht geeignet wäre, zu einer vollständigen Befriedigung der antragstellenden Gläubigerin, des antragstellenden Gläubigers zu führen oder
- die Schuldnerin, der Schuldner der Gerichtsvollzieherin, dem Gerichtsvollzieher nicht innerhalb eines Monats nach Abgabe der Vermögensauskunft die vollständige Befriedigung der antragstellenden Gläubigerin, des antragstellenden Gläubigers nachweist.
- ein Eröffnungsantrag im Insolvenzverfahren mangels Masse abgewiesen worden ist,
Restschuldbefreiung im Insolvenzverfahren versagt worden ist,
- die bereits erteilte Restschuldbefreiung im Insolvenzverfahren widerrufen worden ist.

### Angaben zur Zuverlässigkeit › Insolvenzverfahren (`G05000012034`)

- **Liegt ein Antrag auf Eröffnung eines Insolvenz- oder Vergleichsverfahrens gegen Sie vor?** (`F05000017963`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Liegt eine Ablehnung der Eröffnung eines Insolvenzverfahrens über Ihr Vermögen mangels Masse gegen Sie vor?** (`F05000017964`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Angaben zur Zuverlässigkeit › Angabe Behörden und Justiz (`G05000012035`)

- **Geben Sie die zuständigen Behörden an, die mit dem entsprechenden Verfahren befasst sind.** (`F05000017968`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Geben Sie die entsprechenden Aktenzeichen an.** (`F05000017969`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Angaben zur Zuverlässigkeit › Auszug aus dem Gewerbezentralregister (`G05000011854`)

- **Hinweis zum Gewerbezentralregisterauszug (Belegart 9):** (`F05000017727`) — optional
  - Rechtsgrundlage: § 150 GewO
- **Die Auskunft aus dem Gewerbezentralregister (Belegart 9)** (`F05000017728`) — Pflicht
  - Rechtsgrundlage: § 150 GewO vom 04.02.2026
  - Hilfe: Die Auskunft wird direkt übersandt.
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Angaben zur Zuverlässigkeit › Auszug aus dem Bundeszentralregister / Führungszeugnis (`G05000011878`)

- **Hinweis zum Bundeszentralregisterauszug (Belegart O):** (`F05000017730`) — optional
  - Rechtsgrundlage: § 30 (1) BRZG vom 19.07.2024; § 30a (1) BRZG vom 19.07.2024
- **Die Auskunft aus dem Bundeszentralregister** (`F05000017692`) — Pflicht
  - Rechtsgrundlage: § 30 (1) BRZG vom 19.07.2024; § 30a (1) BRZG vom 19.07.2024
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Nachweise › Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister (`G05000011938`)

- **Ein aktueller Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister** (`F05000017813`) — Pflicht
  - Rechtsgrundlage: § 33a GewO; referenzbasiert _(geerbt)_
- **Fügen Sie einen aktuellen Registerauszug bei.** (`F05000017521`) — optional, conditional
  - Rechtsgrundlage: § 33a GewO; referenzbasiert _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Gesellschaftsvertrag/Satzung (`G05000011883`)

- **Der Gesellschaftsvertrag oder die Satzung** (`F05000017741`) — Pflicht
  - Rechtsgrundlage: § 7 (1) GewO vom 04.02.2026
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Grundrisszeichnung (`G05000012019`)

- **Abfrage  Grundrisszeichnung** (`F05000017902`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Fügen Sie eine Grundrisszeichnung hinzu** (`F05000017903`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Bauliche Sichtabsicherung (`G05000012020`)

- **Eine bauliche Sichtabsicherung** (`F05000017904`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Unterlagen zur baulichen Sichtabsicherung** (`F05000017910`) — Pflicht, conditional
  - Rechtsgrundlage: § 33a GewO
  - Hilfe: Laden Sie die Unterlagen zur baulichen Sichtabsicherung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Bescheinigungen in Steuersachen des Finanzamtes (`G05000012021`)

- **Abfrage Bescheinigung Steuersachen** (`F05000017923`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Bescheinigung in Steuersachen des Finanzamtes** (`F05000017924`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
  - Hilfe: Laden Sie die Bescheinigung in Steuersachen des Finanzamtes hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Hinweis** (`F05000017925`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Nachweise › Bescheinigung der Stadtkasse bzw. Unbedenklichkeitsbescheinigung des Steueramtes (`G05000012022`)

- **Abfrage Bescheinigung Stadtkasse/ Steueramt** (`F05000017926`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
- **Bescheinigung der Stadtkasse bzw. Unbedenklichkeitsbescheinigung des Steueramtes** (`F05000017927`) — Pflicht
  - Rechtsgrundlage: § 33a GewO
  - Hilfe: Laden Sie die Bescheinigung der Stadtkasse bzw. Unbedenklichkeitsbescheinigung des Steueramtes hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Hinweis** (`F05000017928`) — Pflicht
  - Rechtsgrundlage: § 33a GewO

### Nachweise (`G05000012018`)

- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Wie häufig wird die Veranstaltung durchgeführt?" gleich „001 Regelmäßig" ist | „Angaben zu regelmäßigen Veranstaltungen" | wird gezeigt | — | `R05000013017` |
| wenn „Wie häufig wird die Veranstaltung durchgeführt?" ungleich „001 Regelmäßig" ist | „Angaben zu regelmäßigen Veranstaltungen" | entfällt | — | `R05000013017` |
| wenn „Wie häufig wird die Veranstaltung durchgeführt?" gleich „002 Einmalig" ist | „Angaben zur einmaligen Veranstaltung" | wird gezeigt | — | `R05000013018` |
| wenn „Wie häufig wird die Veranstaltung durchgeführt?" ungleich „002 Einmalig" ist | „Angaben zur einmaligen Veranstaltung" | entfällt | — | `R05000013018` |
| wenn „Findet die Veranstaltung an der Geschäftsanschrift statt?" gleich „001 JA" ist | „Wie häufig wird die Veranstaltung durchgeführt?" | wird gezeigt | — | `R05000013031` |
| wenn „Findet die Veranstaltung an der Geschäftsanschrift statt?" ungleich „001 JA" ist | „Wie häufig wird die Veranstaltung durchgeführt?" | entfällt | — | `R05000013031` |
| wenn „Findet die Veranstaltung an der Geschäftsanschrift statt?" ungleich „002 Nein" ist | „Straßenanschrift Inland" | entfällt | — | `R05000013030` |
| wenn „Ist bereits bekannt, wann die erste Schaustellung von Personen stattfindet?" gleich „001 Ja, ein Termin für die erste Veranstaltung ist bekannt." ist | „Angaben erste Veranstaltung" | wird gezeigt | — | `R05000013026` |
| wenn „Ist bereits bekannt, wann die erste Schaustellung von Personen stattfindet?" ungleich „001 Ja, ein Termin für die erste Veranstaltung ist bekannt." ist | „Angaben erste Veranstaltung" | entfällt | — | `R05000013026` |
| wenn „Ist bereits bekannt, wann die erste Schaustellung von Personen stattfindet?" gleich „002 Nein, es wurde noch kein Termin festgelegt." ist | „Schaustellungszeiten" | wird gezeigt | — | `R05000013027` |
| wenn „Ist bereits bekannt, wann die erste Schaustellung von Personen stattfindet?" ungleich „002 Nein, es wurde noch kein Termin festgelegt." ist | „Schaustellungszeiten" | entfällt | — | `R05000013027` |
| wenn „Montag" gleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | wird gezeigt | — | `R05000013019` |
| wenn „Montag" ungleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | entfällt | — | `R05000013019` |
| wenn „Dienstag" gleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | wird gezeigt | — | `R05000013020` |
| wenn „Dienstag" ungleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | entfällt | — | `R05000013020` |
| wenn „Mittwoch" gleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | wird gezeigt | — | `R05000013021` |
| wenn „Mittwoch" ungleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | entfällt | — | `R05000013021` |
| wenn „Donnerstag" gleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | wird gezeigt | — | `R05000013022` |
| wenn „Donnerstag" ungleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | entfällt | — | `R05000013022` |
| wenn „Freitag" gesetzt auf einem beliebigen Wert ist | „Enduhrzeit der ersten Veranstaltung" | wird gezeigt | — | `R05000013023` |
| wenn „Freitag" ungleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | entfällt | — | `R05000013023` |
| wenn „Samstag" gesetzt auf einem beliebigen Wert ist | „Enduhrzeit der ersten Veranstaltung" | wird gezeigt | — | `R05000013024` |
| wenn „Samstag" ungleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | entfällt | — | `R05000013024` |
| wenn „Sonntag" gesetzt auf einem beliebigen Wert ist | „Enduhrzeit der ersten Veranstaltung" | wird gezeigt | — | `R05000013025` |
| wenn „Sonntag" ungleich „WAHR" ist | „Enduhrzeit der ersten Veranstaltung" | entfällt | — | `R05000013025` |
| wenn „Rechtsform" gleich „251000 eG" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012763` |
| wenn „Rechtsform" gleich „252000 SCE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012764` |
| wenn „Rechtsform" gleich „268100 sonst. juristische Person" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012766` |
| wenn „Rechtsform" gleich „138100 sonst. rechtsf. Personengesellschaft" oder „242000 Gebietskörperschaft" oder „540000 Gewerbebetrieb einer KöR" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012767` |
| wenn „Rechtsform" gleich „294000 ausl. juristische Person (EU-Recht)" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012768` |
| wenn „Rechtsform" gleich „211000 e.V." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012769` |
| wenn „Rechtsform" gleich „111100 OHG" oder „111211 GmbH & Co. OHG" oder „111212 UG & Co. OHG" oder „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „411000 e.K.; e.Kfm.; e.Kfr." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012771` |
| wenn „Rechtsform" gleich „230000 rechtsf. Stiftung" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012772` |
| wenn „Rechtsform" gleich „123000 eGbR" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012773` |
| wenn „Rechtsform" gleich „191000 ausl. Personengesellschaft (EU-Recht)" oder „192000 ausl. Personengesellschaft (Nicht-EU-Recht)" oder „491000 ausl. gew. Einzelunternehmen (EU-Recht)" oder „492000 ausl. gew. Einzelunternehmen (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012774` |
| wenn „Rechtsform" gleich „222200 SE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012775` |
| wenn „Rechtsform" gleich „295000 ausl. juristische Person (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012776` |
| wenn „Rechtsform" gleich „213000 VVaG" oder „221100 GmbH" oder „221200 UG" oder „222110 AG" oder „223100 KGaA" oder „223211 GmbH & Co. KGaA" oder „223212 UG & Co. KGaA" oder „223221 AG & Co. KGaA" oder „223222 SE & Co. KGaA" oder „223400 Stiftung & Co. KGaA" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012777` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | muss ausgefüllt werden | — | `R05000014361` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | entfällt | — | `R05000014361` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | muss ausgefüllt werden | — | `R05000014362` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | entfällt | — | `R05000014362` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Staat der Eintragung" | muss ausgefüllt werden | — | `R05000014363` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Staat der Eintragung" | entfällt | — | `R05000014363` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | muss ausgefüllt werden | — | `R05000014364` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | entfällt | — | `R05000014364` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | muss ausgefüllt werden | — | `R05000014365` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | entfällt | — | `R05000014365` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | muss ausgefüllt werden | — | `R05000014366` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | entfällt | — | `R05000014366` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | wird gezeigt | — | `R05000014367` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | entfällt | — | `R05000014367` |
| wenn „Rechtsform" gleich „121000 GbR" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014368` |
| wenn „Rechtsform" ungleich „121000 GbR" ist | „Unternehmensname" | entfällt | — | `R05000014368` |
| wenn „Rechtsform" gleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014369` |
| wenn „Rechtsform" ungleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | entfällt | — | `R05000014369` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | muss ausgefüllt werden | — | `R05000014543` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | entfällt | — | `R05000014543` |
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
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" gleich „001 Natürliche Person" ist | _mehrere Felder_ | entfällt und muss ausgefüllt werden | — | `R05000012744` |
| wenn „Rechtsform" gleich „211000 e.V." oder „221100 GmbH" oder „222110 AG" oder „221200 UG" oder „223400 Stiftung & Co. KGaA" oder „230000 rechtsf. Stiftung" oder „242000 Gebietskörperschaft" oder „251000 eG" ist | „Juristische Person als Gesellschafter" | muss ausgefüllt werden | — | `R05000012745` |
| wenn „Rechtsform" ungleich „211000 e.V." oder „221100 GmbH" oder „222110 AG" oder „221200 UG" oder „223400 Stiftung & Co. KGaA" oder „230000 rechtsf. Stiftung" oder „242000 Gebietskörperschaft" oder „251000 eG" ist | „Juristische Person als Gesellschafter" | entfällt | — | `R05000012745` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" gleich „002 Juristische Person oder Personengesellschaft" ist | „Identifikation des Unternehmens" | muss ausgefüllt werden | — | `R05000012778` |
| wenn „Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?" ungleich „002 Juristische Person oder Personengesellschaft" ist | „Identifikation des Unternehmens" | entfällt | — | `R05000012778` |
| wenn „Rechtsform" gleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Personengesellschaft als Gesellschafter" | muss ausgefüllt werden | — | `R05000012779` |
| wenn „Rechtsform" ungleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Personengesellschaft als Gesellschafter" | entfällt | — | `R05000012779` |
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
| wenn „Rechtsform" gleich „251000 eG" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012763` |
| wenn „Rechtsform" gleich „252000 SCE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012764` |
| wenn „Rechtsform" gleich „268100 sonst. juristische Person" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012766` |
| wenn „Rechtsform" gleich „138100 sonst. rechtsf. Personengesellschaft" oder „242000 Gebietskörperschaft" oder „540000 Gewerbebetrieb einer KöR" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012767` |
| wenn „Rechtsform" gleich „294000 ausl. juristische Person (EU-Recht)" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012768` |
| wenn „Rechtsform" gleich „211000 e.V." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012769` |
| wenn „Rechtsform" gleich „111100 OHG" oder „111211 GmbH & Co. OHG" oder „111212 UG & Co. OHG" oder „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „411000 e.K.; e.Kfm.; e.Kfr." ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012771` |
| wenn „Rechtsform" gleich „230000 rechtsf. Stiftung" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012772` |
| wenn „Rechtsform" gleich „123000 eGbR" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012773` |
| wenn „Rechtsform" gleich „191000 ausl. Personengesellschaft (EU-Recht)" oder „192000 ausl. Personengesellschaft (Nicht-EU-Recht)" oder „491000 ausl. gew. Einzelunternehmen (EU-Recht)" oder „492000 ausl. gew. Einzelunternehmen (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012774` |
| wenn „Rechtsform" gleich „222200 SE" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012775` |
| wenn „Rechtsform" gleich „295000 ausl. juristische Person (Nicht-EU-Recht)" ist | „Art der Eintragung oder des Registers" | wird gezeigt | — | `R05000012776` |
| wenn „Rechtsform" gleich „213000 VVaG" oder „221100 GmbH" oder „221200 UG" oder „222110 AG" oder „223100 KGaA" oder „223211 GmbH & Co. KGaA" oder „223212 UG & Co. KGaA" oder „223221 AG & Co. KGaA" oder „223222 SE & Co. KGaA" oder „223400 Stiftung & Co. KGaA" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000012777` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | muss ausgefüllt werden | — | `R05000014361` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Nummer des Registereintrages" | entfällt | — | `R05000014361` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | muss ausgefüllt werden | — | `R05000014362` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Ort des Registereintrags" | entfällt | — | `R05000014362` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" ist | „Staat der Eintragung" | muss ausgefüllt werden | — | `R05000014363` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" ist | „Staat der Eintragung" | entfällt | — | `R05000014363` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | muss ausgefüllt werden | — | `R05000014364` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Stiftungsverzeichnis (Freitext)" | entfällt | — | `R05000014364` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | muss ausgefüllt werden | — | `R05000014365` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Ausland" oder „Eintragung im Stiftungsverzeichnis" oder „Eintragung im Stiftungsregister" ist | „Registergericht" | entfällt | — | `R05000014365` |
| wenn „Art der Eintragung oder des Registers" gleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | muss ausgefüllt werden | — | `R05000014366` |
| wenn „Art der Eintragung oder des Registers" ungleich „Eintragung im Stiftungsverzeichnis" ist | „Eintragungsnummer" | entfällt | — | `R05000014366` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | wird gezeigt | — | `R05000014367` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Hinweis" | entfällt | — | `R05000014367` |
| wenn „Rechtsform" gleich „121000 GbR" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014368` |
| wenn „Rechtsform" ungleich „121000 GbR" ist | „Unternehmensname" | entfällt | — | `R05000014368` |
| wenn „Rechtsform" gleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014369` |
| wenn „Rechtsform" ungleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | entfällt | — | `R05000014369` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | muss ausgefüllt werden | — | `R05000014543` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | entfällt | — | `R05000014543` |
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
| wenn „Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, anhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftiges abgeschlossenes Strafverfahren gegen Sie?" gleich „Ja" ist | „Angabe Behörden und Justiz" | wird gezeigt | — | `R05000013003` |
| wenn „Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, anhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftiges abgeschlossenes Strafverfahren gegen Sie?" ungleich „JA" ist | „Angabe Behörden und Justiz" | entfällt | — | `R05000013003` |
| wenn „Gibt oder gab es in den letzten fünf Jahren anhängige oder rechtskräftig abgeschlossene Bußgeldverfahren wegen gewerberechtlicher Verstöße gegen Sie?" gleich „Ja" ist | „Angabe Behörden und Justiz" | wird gezeigt | — | `R05000013004` |
| wenn „Gibt oder gab es in den letzten fünf Jahren anhängige oder rechtskräftig abgeschlossene Bußgeldverfahren wegen gewerberechtlicher Verstöße gegen Sie?" ungleich „JA" ist | „Angabe Behörden und Justiz" | entfällt | — | `R05000013004` |
| wenn „Gibt oder gab es in der Vergangenheit sonstige anhängige oder rechtskräftig abgeschlossene gewerbliche Verfahren gegen Sie?" gleich „Ja" ist | „Angabe Behörden und Justiz" | wird gezeigt | — | `R05000013005` |
| wenn „Gibt oder gab es in der Vergangenheit sonstige anhängige oder rechtskräftig abgeschlossene gewerbliche Verfahren gegen Sie?" ungleich „JA" ist | „Angabe Behörden und Justiz" | entfällt | — | `R05000013005` |
| wenn „Liegt ein Antrag auf Eröffnung eines Insolvenz- oder Vergleichsverfahrens gegen Sie vor?" gleich „Ja" ist | „Angabe Behörden und Justiz" | wird gezeigt | — | `R05000013006` |
| wenn „Liegt ein Antrag auf Eröffnung eines Insolvenz- oder Vergleichsverfahrens gegen Sie vor?" ungleich „JA" ist | „Angabe Behörden und Justiz" | entfällt | — | `R05000013006` |
| wenn „Liegt eine Ablehnung der Eröffnung eines Insolvenzverfahrens über Ihr Vermögen mangels Masse gegen Sie vor?" gleich „Ja" ist | „Angabe Behörden und Justiz" | wird gezeigt | — | `R05000013007` |
| wenn „Liegt eine Ablehnung der Eröffnung eines Insolvenzverfahrens über Ihr Vermögen mangels Masse gegen Sie vor?" ungleich „JA" ist | „Angabe Behörden und Justiz" | entfällt | — | `R05000013007` |
| wenn „Haben Sie eine Vermögensauskunft gemäß §802c ZPO abgegeben?" gleich „Ja" ist | „Angabe Behörden und Justiz" | wird gezeigt | — | `R05000013008` |
| wenn „Haben Sie eine Vermögensauskunft gemäß §802c ZPO abgegeben?" ungleich „JA" ist | „Angabe Behörden und Justiz" | entfällt | — | `R05000013008` |
| wenn „Liegt gegen Sie eine entsprechende Haftanordnung gemäß §802c ZPO vor?" gleich „Ja" ist | „Angabe Behörden und Justiz" | wird gezeigt | — | `R05000013009` |
| wenn „Liegt gegen Sie eine entsprechende Haftanordnung gemäß §802c ZPO vor?" ungleich „JA" ist | „Angabe Behörden und Justiz" | entfällt | — | `R05000013009` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" ungleich „001 Ist beantragt" ist | „Datum der Beantragung" | entfällt | — | `R05000012684` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" gleich „002 Ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | muss ausgefüllt werden | — | `R05000012685` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" ungleich „002 Ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | entfällt | — | `R05000012685` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „002 ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | muss ausgefüllt werden | — | `R05000012761` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „002 ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | entfällt | — | `R05000012761` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „001 ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000012762` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „001 ist beantragt" ist | „Datum der Beantragung" | entfällt | — | `R05000012762` |
| wenn „Ein aktueller Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister" gleich „001 liegt vor" ist | „Fügen Sie einen aktuellen Registerauszug bei." | muss ausgefüllt werden | — | `R05000012862` |
| wenn „Ein aktueller Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister" ungleich „001 liegt vor" ist | „Fügen Sie einen aktuellen Registerauszug bei." | entfällt | — | `R05000012862` |
| wenn „Der Gesellschaftsvertrag oder die Satzung" gleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012782` |
| wenn „Der Gesellschaftsvertrag oder die Satzung" ungleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | entfällt | — | `R05000012782` |
| wenn „Eine bauliche Sichtabsicherung" gleich „liegt vor" ist | „Unterlagen zur baulichen Sichtabsicherung" | muss ausgefüllt werden | — | `R05000012998` |
| wenn „Eine bauliche Sichtabsicherung" ungleich „liegt vor" ist | „Unterlagen zur baulichen Sichtabsicherung" | entfällt | — | `R05000012998` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Es muss mindestens eines der Felder F05000017970 "Schaustellung von Personen" oder F05000017971 "Zurverfügungstellung der Räume" = "WAHR" sein.</mark> — Regel `R05000013010`
- <mark>WENN das Feld F05000017931 "Abfrage Veranstaltung an der Geschäftsanschrift" = 002 "Nein", DANN muss die Gruppe G05000011743 "Anschrift Inland Straßenanschrift" ausgefüllt werden.</mark> — Regel `R05000013030`
- <mark>Es muss mindestens eines der Felder G05000012043.F05000017977 "Auswahl Montag" ODER G05000012044.F05000017979 "Auswahl Dienstag" ODER G05000012045.F05000017980 "Auswahl Mittwoch" ODER G05000012046.F05000017982 "Auswahl Donnerstag" ODER G05000012047.F05000017984 "Auswahl Freitag" ODER G05000012048.F05000017987 "Auswahl Samstag" ODER G05000012049.F05000017988 "Auswahl Sonntag" = "WAHR" sein.</mark> — Regel `R05000013028`
- <mark>Wenn F05000017941 "Art der Veranstaltungsfläche" = 004 "Sonstige Fläche", dann muss F05000017942 "Beschreibung Sonstige Fläche" ausgefüllt sein.</mark> — Regel `R05000013029`
- <mark>Wenn F05000017941 "Art der Veranstaltungsfläche"<> 004 "Sonstige Fläche", dann darf F05000017942 "Beschreibung Sonstige Fläche" nicht ausgefüllt sein.</mark> — Regel `R05000013029`
- <mark>Wenn F05000017902 "Abfrage Grundrisszeichnung" = 01, dann muss F05000017903 "Grundrisszeichnung" ausgefüllt sein.</mark> — Regel `R05000012997`
- <mark>Wenn F05000017902 "Abfrage Grundrisszeichnung" <> 01, dann darf F05000017903 "Grundrisszeichnung" nicht ausgefüllt sein.</mark> — Regel `R05000012997`
- <mark>Wenn F05000017923 "Abfrage Bescheinigung Steuersachen" = 01, dann muss F05000017924 "Bescheinigung Steuersachen" ausgefüllt sein.</mark> — Regel `R05000012999`
- <mark>Wenn 05000017923 "Abfrage Bescheinigung Steuersachen" <> 01, dann darf F05000017924 "Bescheinigung Steuersachen" nicht ausgefüllt sein.</mark> — Regel `R05000012999`
- <mark>Wenn F05000017926 "Abfrage Bescheinigung Stadtkasse/ Steueramt" = 01, dann muss F05000017927 "Bescheinigung Stadtkasse/ Steueramt" ausgefüllt sein.</mark> — Regel `R05000013000`
- <mark>WennF05000017926 "Abfrage Bescheinigung Stadtkasse/ Steueramt" <> 01, dann darf F05000017927 "Bescheinigung Stadtkasse/ Steueramt"nicht ausgefüllt sein.</mark> — Regel `R05000013000`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000012023_F05000017932["Wie häufig wird die Veranstaltung durc"] -->|"= 001 Regelmäßig → show"| G05000012023_G05000012025["Angaben zu regelmäßigen Veranstaltunge"]
  G05000012023_F05000017932["Wie häufig wird die Veranstaltung durc"] -.->|"<> 001 Regelmäßig → hide"| G05000012023_G05000012025["Angaben zu regelmäßigen Veranstaltunge"]
  G05000012023_F05000017932["Wie häufig wird die Veranstaltung durc"] -->|"= 002 Einmalig → show"| G05000012023_G05000012028["Angaben zur einmaligen Veranstaltung"]
  G05000012023_F05000017932["Wie häufig wird die Veranstaltung durc"] -.->|"<> 002 Einmalig → hide"| G05000012023_G05000012028["Angaben zur einmaligen Veranstaltung"]
  G05000012023_G05000012024_F05000017931["Findet die Veranstaltung an der Geschä"] -->|"= 001 JA → show"| G05000012023_F05000017932["Wie häufig wird die Veranstaltung durc"]
  G05000012023_G05000012024_F05000017931["Findet die Veranstaltung an der Geschä"] -.->|"<> 001 JA → hide"| G05000012023_F05000017932["Wie häufig wird die Veranstaltung durc"]
  G05000012023_G05000012024_F05000017931["Findet die Veranstaltung an der Geschä"] -.->|"<> 002 Nein → hide"| G05000012023_G05000012024_G05000011743["Straßenanschrift Inland"]
  G05000012023_G05000012025_F05000017933["Ist bereits bekannt, wann die erste Sc"] -->|"= 001 Ja, ein Termin für die e → show"| G05000012023_G05000012025_G05000012026["Angaben erste Veranstaltung"]
  G05000012023_G05000012025_F05000017933["Ist bereits bekannt, wann die erste Sc"] -.->|"<> 001 Ja, ein Termin für die e → hide"| G05000012023_G05000012025_G05000012026["Angaben erste Veranstaltung"]
  G05000012023_G05000012025_F05000017933["Ist bereits bekannt, wann die erste Sc"] -->|"= 002 Nein, es wurde noch kein → show"| G05000012023_G05000012025_G05000012027["Schaustellungszeiten"]
  G05000012023_G05000012025_F05000017933["Ist bereits bekannt, wann die erste Sc"] -.->|"<> 002 Nein, es wurde noch kein → hide"| G05000012023_G05000012025_G05000012027["Schaustellungszeiten"]
  G05000012023_G05000012025_G05000012027_G05000012043_F05000017977["Montag"] -->|"= WAHR → show"| G05000012023_G05000012025_G05000012027_G05000012043_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012043_F05000017977["Montag"] -.->|"<> WAHR → hide"| G05000012023_G05000012025_G05000012027_G05000012043_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012044_F05000017979["Dienstag"] -->|"= WAHR → show"| G05000012023_G05000012025_G05000012027_G05000012044_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012044_F05000017979["Dienstag"] -.->|"<> WAHR → hide"| G05000012023_G05000012025_G05000012027_G05000012044_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012045_F05000017980["Mittwoch"] -->|"= WAHR → show"| G05000012023_G05000012025_G05000012027_G05000012045_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012045_F05000017980["Mittwoch"] -.->|"<> WAHR → hide"| G05000012023_G05000012025_G05000012027_G05000012045_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012046_F05000017982["Donnerstag"] -->|"= WAHR → show"| G05000012023_G05000012025_G05000012027_G05000012046_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012046_F05000017982["Donnerstag"] -.->|"<> WAHR → hide"| G05000012023_G05000012025_G05000012027_G05000012046_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012047_F05000017984["Freitag"] -->|"? ? → show"| G05000012023_G05000012025_G05000012027_G05000012047_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012047_F05000017984["Freitag"] -.->|"<> WAHR → hide"| G05000012023_G05000012025_G05000012027_G05000012047_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012048_F05000017987["Samstag"] -->|"? ? → show"| G05000012023_G05000012025_G05000012027_G05000012048_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012048_F05000017987["Samstag"] -.->|"<> WAHR → hide"| G05000012023_G05000012025_G05000012027_G05000012048_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012049_F05000017988["Sonntag"] -->|"? ? → show"| G05000012023_G05000012025_G05000012027_G05000012049_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012023_G05000012025_G05000012027_G05000012049_F05000017988["Sonntag"] -.->|"<> WAHR → hide"| G05000012023_G05000012025_G05000012027_G05000012049_F05000017935["Enduhrzeit der ersten Veranstaltung"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 251000 eG → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 252000 SCE → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -->|"= 268100 sonst. juristische Pe → show"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -->|"= 138100 sonst. rechtsf. Perso → show"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 294000 ausl. juristische Per → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 211000 e.V. → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 111100 OHG, 111211 GmbH & Co → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 230000 rechtsf. Stiftung → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 123000 eGbR → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -->|"= 191000 ausl. Personengesells → show"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 222200 SE → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -->|"= 295000 ausl. juristische Per → show"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 213000 VVaG, 221100 GmbH, 22 → required"| G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] ==>|"<> Eintragung im Ausland, Eintr → required"| G05000012017_G05000011879_F60000000328["Nummer des Registereintrages"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Ausland, Eintr → hide"| G05000012017_G05000011879_F60000000328["Nummer des Registereintrages"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Ausland → required"| G05000012017_G05000011879_F60000000327["Ort des Registereintrags"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Ausland → hide"| G05000012017_G05000011879_F60000000327["Ort des Registereintrags"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Ausland → required"| G05000012017_G05000011879_F05000017518["Staat der Eintragung"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Ausland → hide"| G05000012017_G05000011879_F05000017518["Staat der Eintragung"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Stiftungsverze → required"| G05000012017_G05000011879_F05000018301["Stiftungsverzeichnis (Freitext)"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Stiftungsverze → hide"| G05000012017_G05000011879_F05000018301["Stiftungsverzeichnis (Freitext)"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] ==>|"<> Eintragung im Ausland, Eintr → required"| G05000012017_G05000011879_F05000017721["Registergericht"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] -.->|"= Eintragung im Ausland, Eintr → hide"| G05000012017_G05000011879_F05000017721["Registergericht"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] ==>|"= Eintragung im Stiftungsverze → required"| G05000012017_G05000011879_F05000017514["Eintragungsnummer"]
  G05000012017_G05000011879_F05000017720["Art der Eintragung oder des Registers"] -.->|"<> Eintragung im Stiftungsverze → hide"| G05000012017_G05000011879_F05000017514["Eintragungsnummer"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -->|"<> 121000 GbR, 340000 GmbH i.G. → show"| G05000012017_G05000011879_F05000017512["Hinweis"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -.->|"= 121000 GbR, 340000 GmbH i.G. → hide"| G05000012017_G05000011879_F05000017512["Hinweis"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 121000 GbR → required"| G05000012017_G05000011879_F05000017734["Unternehmensname"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -.->|"<> 121000 GbR → hide"| G05000012017_G05000011879_F05000017734["Unternehmensname"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"= 412000 nicht eingetr. gew. E → required"| G05000012017_G05000011879_F05000017735["Unternehmensname"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -.->|"<> 412000 nicht eingetr. gew. E → hide"| G05000012017_G05000011879_F05000017735["Unternehmensname"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] ==>|"<> 121000 GbR, 340000 GmbH i.G. → required"| G05000012017_G05000011879_F60000000319["Eingetragener Name"]
  G05000012017_G05000011879_F05000017511["Rechtsform"] -.->|"= 121000 GbR, 340000 GmbH i.G. → hide"| G05000012017_G05000011879_F60000000319["Eingetragener Name"]
  G05000012017_G05000011864_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000012017_G05000011864_G60000000083_F60000000232["Monat"]
  G05000012017_G05000011864_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000012017_G05000011864_G05000011865_G60000000191["Anschrift Ausland"]
  unclear0["?: Es muss mindestens eines der Felder F05000017970 "Schaustell"]:::unclear
  unclear1["?: WENN das Feld F05000017931 "Abfrage Veranstaltung an der Ges"]:::unclear
  unclear2["?: Es muss mindestens eines der Felder G05000012043.F0500001797"]:::unclear
  unclear3["?: Wenn F05000017941 "Art der Veranstaltungsfläche" = 004 "Sons"]:::unclear
  unclear4["?: Wenn F05000017941 "Art der Veranstaltungsfläche"<> 004 "Sons"]:::unclear
  unclear5["?: Wenn F05000017902 "Abfrage Grundrisszeichnung" = 01, dann mu"]:::unclear
  unclear6["?: Wenn F05000017902 "Abfrage Grundrisszeichnung" <> 01, dann d"]:::unclear
  unclear7["?: Wenn F05000017923 "Abfrage Bescheinigung Steuersachen" = 01,"]:::unclear
  unclear8["?: Wenn 05000017923 "Abfrage Bescheinigung Steuersachen" <> 01,"]:::unclear
  unclear9["?: Wenn F05000017926 "Abfrage Bescheinigung Stadtkasse/ Steuera"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
