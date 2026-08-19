---
name: antrag-s05000001382
description: Führt Antragstellende durch „Antrag auf Zertifizierung von Betrieben für die klimaschutzgerechte Installation, Wartung und Instandhaltung von Anlagen" (FIM S05000001382 1.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf Zertifizierung von Betrieben für die klimaschutzgerechte Installation, Wartung und Instandhaltung von Anlagen

- **FIM-ID:** `S05000001382 1.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 5 ChemKlimaschutzV vom 19.06.2020; § 6 ChemKlimaschutzV vom 19.06.2020; Art. 3 (4) S. 2 VO (EU) Nr. 517/2014 vom 16.04.2014; Art. 4 (7) S. 2 VO (EU) 2024/573 vom 07.02.2024; Art. 6 DVO (EU) 2024/2215 vom 06.09.2024; referenzbasiert
- **Kompiliert:** 2026-08-13T15:54:30Z aus https://fimportal.de/api/v1/schemas/S05000001382/1.0.0/xdf
- **Umfang:** 109 Felder, 61 gesicherte Bedingungen, 6 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet werden (Rechtsgrundlage stimmt nicht überein (D99000002132)). Zu Fristen, Kosten, Unterlagen und Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle verweisen.

## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Antragsumfang (`G05000013225`)

- **Hinweis:** (`F05000019540`) — optional
  - Rechtsgrundlage: § 6 (2) ChemKlimaschutzV; Art. 4 (7) S. 2 VO (EU) 2024/573; Art. 6 DVO (EU) 2024/2215
- **Hinweis:** (`F05000019544`) — optional
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Umfirmierung (`G05000013286`)

- **Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?** (`F05000019620`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Zertifikatsnummer** (`F05000019621`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert _(geerbt)_

### Antragsumfang › Angaben zu einer bereits erfolgten Zertifizierung (`G05000013297`)

- **War Ihr Unternehmen schon einmal gemäß § 6 ChemKlimaschutzV zertifiziert?** (`F05000019626`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Aktenzeichen der vorangegangenen Zertifizierung** (`F05000019629`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
- **Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?** (`F05000019630`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert

### Antragsumfang › Angabe der Tätigkeiten › Ortsfeste Kälteanlagen, Klimaanlagen und Wärmepumpen (`G05000013289`)

- **Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Ortsfeste Kälteanlagen, Klimaanlagen und Wärmepumpen" beantragt?** (`F05000019545`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Angabe der Tätigkeiten › Ortsfeste Kälteanlagen, Klimaanlagen und Wärmepumpen › Folgende Kältemittel sind enthalten: (`G05000013231`)

- **Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)** (`F05000019548`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:** (`F05000019551`) — optional, conditional
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Kohlendioxid (CO2) Zertifikat B** (`F05000019549`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Ammoniak (NH3) Zertifikat C** (`F05000019550`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Angabe der Tätigkeiten › Ortsfeste Organic-Rankine-Kreisläufe (`G05000013291`)

- **Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Ortsfeste Organic-Rankine-Kreisläufe" beantragt?** (`F05000019546`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Angabe der Tätigkeiten › Ortsfeste Organic-Rankine-Kreisläufe › Folgende Kältemittel sind enthalten: (`G05000013231`)

- **Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)** (`F05000019548`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:** (`F05000019551`) — optional, conditional
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Kohlendioxid (CO2) Zertifikat B** (`F05000019549`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Ammoniak (NH3) Zertifikat C** (`F05000019550`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Angabe der Tätigkeiten › Kälteanlagen in Kühllastkraftfahrzeugen und Kühlanhängern und Kälteanlagen in leichten Kühlfahrzeugen, intermodalen Containern und Eisenbahnwaggons (`G05000013292`)

- **Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Kälteanlagen in Kühllastkraftfahrzeugen und Kühlanhängern und Kälteanlagen in leichten Kühlfahrzeugen, intermodalen Containern und Eisenbahnwaggons" beantragt?** (`F05000019547`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Angabe der Tätigkeiten › Kälteanlagen in Kühllastkraftfahrzeugen und Kühlanhängern und Kälteanlagen in leichten Kühlfahrzeugen, intermodalen Containern und Eisenbahnwaggons › Folgende Kältemittel sind enthalten: (`G05000013231`)

- **Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)** (`F05000019548`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:** (`F05000019551`) — optional, conditional
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Kohlendioxid (CO2) Zertifikat B** (`F05000019549`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Ammoniak (NH3) Zertifikat C** (`F05000019550`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Angaben zur sachkundigen Person mit Zertifikat (`G05000013233`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Zu Ihrer Orientierung:** (`F05000019543`) — optional
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Geschätztes Tätigkeitsvolumen (in Stunden pro Jahr)** (`F05000019556`) — Pflicht
  - Rechtsgrundlage: § 5 ChemKlimaschutzV

### Antragsumfang › Angaben zur sachkundigen Person mit Zertifikat › Die Mitarbeiterin oder der Mitarbeiter hat ein: (`G05000013236`)

- **Zertifikat A1** (`F05000019552`) — Pflicht
  - Rechtsgrundlage: § 5 ChemKlimaschutzV
- **Zertifikat A2** (`F05000019553`) — Pflicht
  - Rechtsgrundlage: § 5 ChemKlimaschutzV
- **Zertifikat B** (`F05000019554`) — Pflicht
  - Rechtsgrundlage: § 5 ChemKlimaschutzV
- **Zertifikat C** (`F05000019555`) — Pflicht
  - Rechtsgrundlage: § 5 ChemKlimaschutzV

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Absauggerät/-station (`G05000013272`)

- **Gerätetyp** (`F05000019591`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_
- **Anzahl** (`F05000019590`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Multifunktionsmessgerät (`G05000013273`)

- **Gerätetyp** (`F05000019591`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_
- **Anzahl** (`F05000019590`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Absolutdruckmessgerät (`G05000013274`)

- **Gerätetyp** (`F05000019591`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_
- **Anzahl** (`F05000019590`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Vakuumpumpe (`G05000013275`)

- **Gerätetyp** (`F05000019591`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_
- **Anzahl** (`F05000019590`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Lötgerät, Löte (Hartlöteinrichtung) (`G05000013276`)

- **Gerätetyp** (`F05000019591`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_
- **Anzahl** (`F05000019590`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Waage (`G05000013277`)

- **Gerätetyp** (`F05000019591`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_
- **Anzahl** (`F05000019590`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Elektronisches Lecksuchgerät (`G05000013278`)

- **Gerätetyp** (`F05000019591`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_
- **Anzahl** (`F05000019590`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV _(geerbt)_

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: › Übrige Unternehmensausrüstung (`G05000013285`)

- **Anlagen-/Maschinenflaschen (gereinigt und evakuiert)** (`F05000019596`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Aufweitzange** (`F05000019597`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Biegewerkzeug** (`F05000019598`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Bördelwerkzeug** (`F05000019599`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Digitale Zangenmessgeräte** (`F05000019600`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Drehmomentschlüssel** (`F05000019601`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Druckminderer für Trockenstickstoff oder einem anderen nicht brennbaren, nicht reaktiven Trockengas** (`F05000019602`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Einstechvorrichtung mit Ventil** (`F05000019603`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Flasche gefüllt mit Trockenstickstoff oder einem anderen nicht brennbaren, nicht reaktiven Trockengas** (`F05000019604`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Flaschenanschlussstücke** (`F05000019605`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Kältemaschinenöl** (`F05000019606`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Kugelventile** (`F05000019607`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Lamellenkamm** (`F05000019608`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Lecksuchspray** (`F05000019609`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Manometerbatterie mit Schläuchen** (`F05000019610`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Montage-Füll- und Prüfeinheiten** (`F05000019611`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Plombierzange mit Plomben** (`F05000019612`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Rohrabschneider/Entgrader/Schälbohrer** (`F05000019613`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Rollgabelschlüssel** (`F05000019614`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Säuretester** (`F05000019616`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Schraderventilschrauben inkl. Ventileinsätze** (`F05000019617`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Thermometer digital (Oberfläche, Einsteckthermometer)** (`F05000019618`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Ventilratsche** (`F05000019619`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV

### Antragsumfang › Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist: (`G05000013270`)

- **Folgende Werkzeuge sind für die Kategorie I als zwingend vorhanden vorausgesetzt:** (`F05000019588`) — optional
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV
- **Hiermit bestätige ich, dass die  aufgelisteten Werkzeuge vorhanden und den sachkundigen Personen zugänglich sind.** (`F05000019589`) — Pflicht
  - Rechtsgrundlage: § 5 (1) Nr. 2 ChemKlimaschutzV

### Unternehmensdaten › Identifikation des Unternehmens (`G05000012938`)

- **Rechtsform** (`F05000017511`) — Pflicht
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1; XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1; XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1 _(geerbt)_
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

### Unternehmensdaten › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers (`G05000013383`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Unternehmensdaten › Weitere Angaben zum Unternehmen › Inländische Geschäftsanschrift oder Anschrift des Verwaltungssitzes (`G05000013419`)

- **Es handelt sich um die:** (`F05000019734`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert _(geerbt)_
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

### Antragstellende Person › Angaben zur antragstellenden Person (`G05000012734`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Zertifizierung eines Standorts (`G05000013226`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Geschäftsbezeichnung** (`F60000000320`) — Pflicht
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.
- **Ist der Standort ein eingetragener EMAS-Standort?** (`F05000019541`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Zu Ihrer Orientierung:** (`F05000019543`) — optional
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV
- **Erwartetes gesamtes Tätigkeitsvolumen Ihres Standortes (in Stunden pro Jahr)** (`F05000019542`) — Pflicht
  - Rechtsgrundlage: § 6 (1) ChemKlimaschutzV; § 6 (2) Nr. 2 ChemKlimaschutzV

### Zertifizierung eines Standorts › Straßenanschrift Inland (`G05000012253`)

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

### Nachweise (`G05000013237`)

- **Laden Sie das EU-Öko-Audit oder einen Bericht über die Umweltbetriebsprüfung (EMAS) gemäß § 6 Absatz 3 ChemKlimaschutzV hoch.** (`F05000019583`) — optional, conditional
  - Rechtsgrundlage: § 6 (3) ChemKlimaschutzV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie die Zertifikate aller genannten sachkundigen Personen hoch.** (`F05000019584`) — optional, conditional
  - Rechtsgrundlage: § 5 ChemKlimaschutzV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Nachweis zur Umfirmierung** (`F05000019585`) — optional, conditional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Laden Sie den Nachweis zur Umfirmierung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Aktueller Auszug aus dem Handelsregister** (`F05000019587`) — optional, conditional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Laden Sie einen aktuellen Auszug aus dem Handelsregister hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Aktuelle Gewerbeanmeldung** (`F05000019586`) — optional, conditional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Laden Sie die aktuelle Gewerbeanmeldung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Ist der Standort ein eingetragener EMAS-Standort?" gleich „wahr" ist | „Laden Sie das EU-Öko-Audit oder einen Bericht über die Umweltbetriebsprüfung (EMAS) gemäß § 6 Absatz 3 ChemKlimaschutzV hoch." | muss ausgefüllt werden | — | `R05000015443` |
| wenn „Antragsumfang" gleich „wahr" ist | „Nachweis zur Umfirmierung" | muss ausgefüllt werden | — | `R05000015446` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist | „Nachweis zur Umfirmierung" | entfällt | — | `R05000015446` |
| wenn „Rechtsform" gleich „412000 nicht eingetr. gew. Einzelunternehmen" oder „121000 GbR" ist _(nur SL)_ | „Aktuelle Gewerbeanmeldung" | muss ausgefüllt werden | — | `R05000015453` |
| wenn „Rechtsform" ungleich „412000 nicht eingetr. gew. Einzelunternehmen" oder „121000 GbR" ist _(nur SL)_ | „Aktuelle Gewerbeanmeldung" | entfällt | — | `R05000015453` |
| wenn „Rechtsform" gleich „211000 e.V." oder „221100 GmbH" oder „222110 AG" oder „221200 UG" oder „223400 Stiftung & Co. KGaA" oder „230000 rechtsf. Stiftung" oder „242000 Gebietskörperschaft" oder „251000 eG" ist _(nur SL)_ | „Aktueller Auszug aus dem Handelsregister" | muss ausgefüllt werden | — | `R05000015454` |
| wenn „Rechtsform" ungleich „211000 e.V." oder „221100 GmbH" oder „222110 AG" oder „221200 UG" oder „223400 Stiftung & Co. KGaA" oder „230000 rechtsf. Stiftung" oder „242000 Gebietskörperschaft" oder „251000 eG" ist _(nur SL)_ | „Aktueller Auszug aus dem Handelsregister" | entfällt | — | `R05000015454` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist _(nur TH)_ | „Laden Sie die Zertifikate aller genannten sachkundigen Personen hoch." | muss ausgefüllt werden | — | `R05000015455` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist _(nur TH)_ | „Laden Sie die Zertifikate aller genannten sachkundigen Personen hoch." | entfällt | — | `R05000015455` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist _(nur SL, RP)_ | „Laden Sie die Zertifikate aller genannten sachkundigen Personen hoch." | muss ausgefüllt werden | — | `R05000015455` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist _(nur SL, RP)_ | „Laden Sie die Zertifikate aller genannten sachkundigen Personen hoch." | entfällt | — | `R05000015455` |
| wenn „Rechtsform" ungleich „411000 e.K., e.Kfm., e.Kfr." oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Antragstellende Person" | muss ausgefüllt werden | — | `R05000015785` |
| wenn „Rechtsform" gleich „411000 e.K., e.Kfm., e.Kfr." oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Antragstellende Person" | entfällt | — | `R05000015785` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist | „Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist:" | muss ausgefüllt werden | — | `R05000015445` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist | „Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist:" | entfällt | — | `R05000015445` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist _(nur TH)_ | „Angabe der Tätigkeiten" | muss ausgefüllt werden | — | `R05000015450` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist _(nur TH)_ | „Angabe der Tätigkeiten" | entfällt | — | `R05000015450` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist _(nur SL, RP)_ | „Angabe der Tätigkeiten" | muss ausgefüllt werden | — | `R05000015450` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist _(nur SL, RP)_ | „Angabe der Tätigkeiten" | entfällt | — | `R05000015450` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist _(nur TH)_ | „Angaben zur sachkundigen Person mit Zertifikat" | muss ausgefüllt werden | — | `R05000015451` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist _(nur TH)_ | „Angaben zur sachkundigen Person mit Zertifikat" | entfällt | — | `R05000015451` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist _(nur SL, RP)_ | „Angaben zur sachkundigen Person mit Zertifikat" | muss ausgefüllt werden | — | `R05000015451` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist _(nur SL, RP)_ | „Angaben zur sachkundigen Person mit Zertifikat" | entfällt | — | `R05000015451` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist _(nur SL, RP)_ | „Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist:" | muss ausgefüllt werden | — | `R05000015452` |
| wenn „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist _(nur SL, RP)_ | „Ausrüstung des Unternehmens, welche den zertifizierungspflichtige Tätigkeiten ausübenden natürlichen Personen zugänglich ist:" | entfällt | — | `R05000015452` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" gleich „wahr" ist | „Zertifikatsnummer" | muss ausgefüllt werden | — | `R05000015435` |
| wenn „Erfolgte innerhalb der letzten drei Jahren bereits eine reguläre Zertifizierung (Zertifikat A1, A2, B, C) des Unternehmens und soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" ungleich „wahr" ist | „Zertifikatsnummer" | entfällt | — | `R05000015435` |
| wenn „War Ihr Unternehmen schon einmal gemäß § 6 ChemKlimaschutzV zertifiziert?" gleich „wahr" ist | „Aktenzeichen der vorangegangenen Zertifizierung" | muss ausgefüllt werden | — | `R05000015447` |
| wenn „War Ihr Unternehmen schon einmal gemäß § 6 ChemKlimaschutzV zertifiziert?" ungleich „wahr" ist | „Aktenzeichen der vorangegangenen Zertifizierung" | entfällt | — | `R05000015447` |
| wenn „War Ihr Unternehmen schon einmal gemäß § 6 ChemKlimaschutzV zertifiziert?" gleich „wahr" ist | „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" | muss ausgefüllt werden | — | `R05000015448` |
| wenn „War Ihr Unternehmen schon einmal gemäß § 6 ChemKlimaschutzV zertifiziert?" ungleich „wahr" ist | „Soll nur eine Umfirmierung (Adresse, Name) des Unternehmens erfolgen?" | entfällt | — | `R05000015448` |
| wenn „Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Ortsfeste Kälteanlagen, Klimaanlagen und Wärmepumpen" beantragt?" gleich „wahr" ist | „Folgende Kältemittel sind enthalten:" | muss ausgefüllt werden | — | `R05000015438` |
| wenn „Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Ortsfeste Kälteanlagen, Klimaanlagen und Wärmepumpen" beantragt?" ungleich „wahr" ist | „Folgende Kältemittel sind enthalten:" | entfällt | — | `R05000015438` |
| wenn „Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)" gleich „wahr" ist | „Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:" | muss ausgefüllt werden | — | `R05000015439` |
| wenn „Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)" ungleich „wahr" ist | „Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:" | entfällt | — | `R05000015439` |
| wenn „Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Ortsfeste Organic-Rankine-Kreisläufe" beantragt?" gleich „wahr" ist | „Folgende Kältemittel sind enthalten:" | muss ausgefüllt werden | — | `R05000015440` |
| wenn „Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Ortsfeste Organic-Rankine-Kreisläufe" beantragt?" ungleich „wahr" ist | „Folgende Kältemittel sind enthalten:" | entfällt | — | `R05000015440` |
| wenn „Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)" gleich „wahr" ist | „Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:" | muss ausgefüllt werden | — | `R05000015439` |
| wenn „Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)" ungleich „wahr" ist | „Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:" | entfällt | — | `R05000015439` |
| wenn „Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Kälteanlagen in Kühllastkraftfahrzeugen und Kühlanhängern und Kälteanlagen in leichten Kühlfahrzeugen, intermodalen Containern und Eisenbahnwaggons" beantragt?" gleich „wahr" ist | „Folgende Kältemittel sind enthalten:" | muss ausgefüllt werden | — | `R05000015441` |
| wenn „Wird die Unternehmenszertifizierung für die Installation, Reparatur, Instandhaltung oder Wartung sowie Außerbetriebnahme für "Kälteanlagen in Kühllastkraftfahrzeugen und Kühlanhängern und Kälteanlagen in leichten Kühlfahrzeugen, intermodalen Containern und Eisenbahnwaggons" beantragt?" ungleich „wahr" ist | „Folgende Kältemittel sind enthalten:" | entfällt | — | `R05000015441` |
| wenn „Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)" gleich „wahr" ist | „Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:" | muss ausgefüllt werden | — | `R05000015439` |
| wenn „Fluorierte Treibhausgase oder Kohlenwasserstoffe (Zertifikat A1 bzw. A2)" ungleich „wahr" ist | „Die fluorierten Treibhausgase oder Kohlenwasserstoffe haben:" | entfällt | — | `R05000015439` |
| wenn „Rechtsform" gleich „411000 e.K., e.Kfm., e.Kfr." oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers" | muss ausgefüllt werden | — | `R05000015784` |
| wenn „Rechtsform" ungleich „411000 e.K., e.Kfm., e.Kfr." oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers" | entfällt | — | `R05000015784` |
| wenn „Rechtsform" gleich „121000 GbR" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014642` |
| wenn „Rechtsform" ungleich „121000 GbR" ist | „Unternehmensname" | entfällt | — | `R05000014642` |
| wenn „Rechtsform" gleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014643` |
| wenn „Rechtsform" ungleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | entfällt | — | `R05000014643` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | muss ausgefüllt werden | — | `R05000014650` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | entfällt | — | `R05000014650` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Mindestens eines der Datenfelder G05000013289.F05000019545 "Ortsfeste Kälteanlagen", G05000013291.F05000019546 "Ortsfeste Organic-Rankine-Kreisläufe" oder G05000013292.F05000019547 "Kälteanlagen in Kühllastkraftfahrzeugen" muss den Wert "wahr" haben.</mark> — Regel `R05000015442`
- <mark>Mindestens eines der Datenfelder F05000019548 "Fluorierte Treibhausgase", F05000019549 "Kohlendioxid" oder F05000019550 "Ammoniak" muss den Wert "wahr" haben.</mark> — Regel `R05000015323`
- <mark>Mindestens eines der Datenfelder F05000019548 "Fluorierte Treibhausgase", F05000019549 "Kohlendioxid" oder F05000019550 "Ammoniak" muss den Wert "wahr" haben.</mark> — Regel `R05000015323`
- <mark>Mindestens eines der Datenfelder F05000019548 "Fluorierte Treibhausgase", F05000019549 "Kohlendioxid" oder F05000019550 "Ammoniak" muss den Wert "wahr" haben.</mark> — Regel `R05000015323`
- <mark>Mindestens eines der Datenfelder F05000019552 "Zertifikat A1", F05000019553 "Zertifikat A2", F05000019554 "Zertifikat B" oder F05000019555 "Zertifikat C" muss den Wert "wahr" haben.</mark> — Regel `R05000015324`
- <mark>Mindestens ein Datenfeld der Datenfeldgruppe muss den Wert "wahr" haben.</mark> — Regel `R05000015434`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000013226_F05000019541["Ist der Standort ein eingetragener EMA"] ==>|"= wahr → required"| G05000013237_F05000019583["Laden Sie das EU-Öko-Audit oder einen "]
  G05000013225["Antragsumfang"] ==>|"= wahr → required"| G05000013237_F05000019585["Nachweis zur Umfirmierung"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] -.->|"<> wahr → hide"| G05000013237_F05000019585["Nachweis zur Umfirmierung"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] ==>|"= 412000 nicht eingetr. gew. E → required [SL]"| G05000013237_F05000019586["Aktuelle Gewerbeanmeldung"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] -.->|"<> 412000 nicht eingetr. gew. E → hide [SL]"| G05000013237_F05000019586["Aktuelle Gewerbeanmeldung"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] ==>|"= 211000 e.V., 221100 GmbH, 22 → required [SL]"| G05000013237_F05000019587["Aktueller Auszug aus dem Handelsregist"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] -.->|"<> 211000 e.V., 221100 GmbH, 22 → hide [SL]"| G05000013237_F05000019587["Aktueller Auszug aus dem Handelsregist"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] ==>|"<> wahr → required [TH]"| G05000013237_F05000019584["Laden Sie die Zertifikate aller genann"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] -.->|"= wahr → hide [TH]"| G05000013237_F05000019584["Laden Sie die Zertifikate aller genann"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] ==>|"<> wahr → required [SL,RP]"| G05000013237_F05000019584["Laden Sie die Zertifikate aller genann"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] -.->|"= wahr → hide [SL,RP]"| G05000013237_F05000019584["Laden Sie die Zertifikate aller genann"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] ==>|"<> 411000 e.K., e.Kfm., e.Kfr., → required"| G05000013216["Antragstellende Person"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] -.->|"= 411000 e.K., e.Kfm., e.Kfr., → hide"| G05000013216["Antragstellende Person"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] ==>|"<> wahr → required"| G05000013225_G05000013271["Ausrüstung des Unternehmens, welche de"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] -.->|"= wahr → hide"| G05000013225_G05000013271["Ausrüstung des Unternehmens, welche de"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] ==>|"<> wahr → required [TH]"| G05000013225_G05000013227["Angabe der Tätigkeiten"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] -.->|"= wahr → hide [TH]"| G05000013225_G05000013227["Angabe der Tätigkeiten"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] ==>|"<> wahr → required [SL,RP]"| G05000013225_G05000013227["Angabe der Tätigkeiten"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] -.->|"= wahr → hide [SL,RP]"| G05000013225_G05000013227["Angabe der Tätigkeiten"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] ==>|"<> wahr → required [TH]"| G05000013225_G05000013233["Angaben zur sachkundigen Person mit Ze"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] -.->|"= wahr → hide [TH]"| G05000013225_G05000013233["Angaben zur sachkundigen Person mit Ze"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] ==>|"<> wahr → required [SL,RP]"| G05000013225_G05000013233["Angaben zur sachkundigen Person mit Ze"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] -.->|"= wahr → hide [SL,RP]"| G05000013225_G05000013233["Angaben zur sachkundigen Person mit Ze"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] ==>|"<> wahr → required [SL,RP]"| G05000013225_G05000013270["Ausrüstung des Unternehmens, welche de"]
  G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"] -.->|"= wahr → hide [SL,RP]"| G05000013225_G05000013270["Ausrüstung des Unternehmens, welche de"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] ==>|"= wahr → required"| G05000013225_G05000013286_F05000019621["Zertifikatsnummer"]
  G05000013225_G05000013286_F05000019620["Erfolgte innerhalb der letzten drei Ja"] -.->|"<> wahr → hide"| G05000013225_G05000013286_F05000019621["Zertifikatsnummer"]
  G05000013225_G05000013297_F05000019626["War Ihr Unternehmen schon einmal gemäß"] ==>|"= wahr → required"| G05000013225_G05000013297_F05000019629["Aktenzeichen der vorangegangenen Zerti"]
  G05000013225_G05000013297_F05000019626["War Ihr Unternehmen schon einmal gemäß"] -.->|"<> wahr → hide"| G05000013225_G05000013297_F05000019629["Aktenzeichen der vorangegangenen Zerti"]
  G05000013225_G05000013297_F05000019626["War Ihr Unternehmen schon einmal gemäß"] ==>|"= wahr → required"| G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"]
  G05000013225_G05000013297_F05000019626["War Ihr Unternehmen schon einmal gemäß"] -.->|"<> wahr → hide"| G05000013225_G05000013297_F05000019630["Soll nur eine Umfirmierung (Adresse, N"]
  G05000013225_G05000013227_G05000013289_F05000019545["Wird die Unternehmenszertifizierung fü"] ==>|"= wahr → required"| G05000013225_G05000013227_G05000013289_G05000013231["Folgende Kältemittel sind enthalten:"]
  G05000013225_G05000013227_G05000013289_F05000019545["Wird die Unternehmenszertifizierung fü"] -.->|"<> wahr → hide"| G05000013225_G05000013227_G05000013289_G05000013231["Folgende Kältemittel sind enthalten:"]
  G05000013225_G05000013227_G05000013289_G05000013231_F05000019548["Fluorierte Treibhausgase oder Kohlenwa"] ==>|"= wahr → required"| G05000013225_G05000013227_G05000013289_G05000013231_F05000019551["Die fluorierten Treibhausgase oder Koh"]
  G05000013225_G05000013227_G05000013289_G05000013231_F05000019548["Fluorierte Treibhausgase oder Kohlenwa"] -.->|"<> wahr → hide"| G05000013225_G05000013227_G05000013289_G05000013231_F05000019551["Die fluorierten Treibhausgase oder Koh"]
  G05000013225_G05000013227_G05000013291_F05000019546["Wird die Unternehmenszertifizierung fü"] ==>|"= wahr → required"| G05000013225_G05000013227_G05000013291_G05000013231["Folgende Kältemittel sind enthalten:"]
  G05000013225_G05000013227_G05000013291_F05000019546["Wird die Unternehmenszertifizierung fü"] -.->|"<> wahr → hide"| G05000013225_G05000013227_G05000013291_G05000013231["Folgende Kältemittel sind enthalten:"]
  G05000013225_G05000013227_G05000013291_G05000013231_F05000019548["Fluorierte Treibhausgase oder Kohlenwa"] ==>|"= wahr → required"| G05000013225_G05000013227_G05000013291_G05000013231_F05000019551["Die fluorierten Treibhausgase oder Koh"]
  G05000013225_G05000013227_G05000013291_G05000013231_F05000019548["Fluorierte Treibhausgase oder Kohlenwa"] -.->|"<> wahr → hide"| G05000013225_G05000013227_G05000013291_G05000013231_F05000019551["Die fluorierten Treibhausgase oder Koh"]
  G05000013225_G05000013227_G05000013292_F05000019547["Wird die Unternehmenszertifizierung fü"] ==>|"= wahr → required"| G05000013225_G05000013227_G05000013292_G05000013231["Folgende Kältemittel sind enthalten:"]
  G05000013225_G05000013227_G05000013292_F05000019547["Wird die Unternehmenszertifizierung fü"] -.->|"<> wahr → hide"| G05000013225_G05000013227_G05000013292_G05000013231["Folgende Kältemittel sind enthalten:"]
  G05000013225_G05000013227_G05000013292_G05000013231_F05000019548["Fluorierte Treibhausgase oder Kohlenwa"] ==>|"= wahr → required"| G05000013225_G05000013227_G05000013292_G05000013231_F05000019551["Die fluorierten Treibhausgase oder Koh"]
  G05000013225_G05000013227_G05000013292_G05000013231_F05000019548["Fluorierte Treibhausgase oder Kohlenwa"] -.->|"<> wahr → hide"| G05000013225_G05000013227_G05000013292_G05000013231_F05000019551["Die fluorierten Treibhausgase oder Koh"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] ==>|"= 411000 e.K., e.Kfm., e.Kfr., → required"| G05000012939_G05000013383["Einzelunternehmen - Persönliche Angabe"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] -.->|"<> 411000 e.K., e.Kfm., e.Kfr., → hide"| G05000012939_G05000013383["Einzelunternehmen - Persönliche Angabe"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] ==>|"= 121000 GbR → required"| G05000012939_G05000012938_F05000017734["Unternehmensname"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] -.->|"<> 121000 GbR → hide"| G05000012939_G05000012938_F05000017734["Unternehmensname"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] ==>|"= 412000 nicht eingetr. gew. E → required"| G05000012939_G05000012938_F05000017735["Unternehmensname"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] -.->|"<> 412000 nicht eingetr. gew. E → hide"| G05000012939_G05000012938_F05000017735["Unternehmensname"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] ==>|"<> 121000 GbR, 340000 GmbH i.G. → required"| G05000012939_G05000012938_F60000000319["Eingetragener Name"]
  G05000012939_G05000012938_F05000017511["Rechtsform"] -.->|"= 121000 GbR, 340000 GmbH i.G. → hide"| G05000012939_G05000012938_F60000000319["Eingetragener Name"]
  unclear0["?: Mindestens eines der Datenfelder G05000013289.F05000019545 ""]:::unclear
  unclear1["?: Mindestens eines der Datenfelder F05000019548 "Fluorierte Tr"]:::unclear
  unclear2["?: Mindestens eines der Datenfelder F05000019548 "Fluorierte Tr"]:::unclear
  unclear3["?: Mindestens eines der Datenfelder F05000019548 "Fluorierte Tr"]:::unclear
  unclear4["?: Mindestens eines der Datenfelder F05000019552 "Zertifikat A1"]:::unclear
  unclear5["?: Mindestens ein Datenfeld der Datenfeldgruppe muss den Wert ""]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
