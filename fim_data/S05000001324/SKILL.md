---
name: antrag-s05000001324
description: Führt Antragstellende durch „Anzeige von Tätigkeiten mit Krankheitserregern" (FIM S05000001324 1.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Anzeige von Tätigkeiten mit Krankheitserregern

- **FIM-ID:** `S05000001324 1.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 28 IfSG vom 12.12.2023; § 44 IfSG vom 12.12.2023; § 45 IfSG vom 12.12.2023; § 49 IfSG vom 12.12.2023; § 50 IfSG vom 12.12.2023; § 9 BioStoffV vom 2.12.2024; referenzbasiert
- **Kompiliert:** 2026-08-13T15:51:10Z aus https://fimportal.de/api/v1/schemas/S05000001324/1.0.0/xdf
- **Umfang:** 116 Felder, 71 gesicherte Bedingungen, 1 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Anzeigeumfang (`G05000012249`)

- **Es handelt sich um eine** (`F05000018264`) — Pflicht
  - Rechtsgrundlage: § 49 IfSG; § 50 IfSG

### Anzeigeumfang › Art der Änderung (`G05000012252`)

- **Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern** (`F05000018265`) — Pflicht
  - Rechtsgrundlage: § 49 IfSG; § 50 IfSG
- **Angaben zur Beschaffenheit der Räume und Einrichtungen** (`F05000018266`) — Pflicht
  - Rechtsgrundlage: § 49 IfSG; § 50 IfSG
- **Angaben zur Erlaubnisfreiheit** (`F05000018267`) — optional
  - Rechtsgrundlage: § 49 IfSG; § 50 IfSG
- **Veränderungen zu § 45 Abs. 2 IfSG** (`F05000018367`) — optional
  - Rechtsgrundlage: § 49 IfSG; § 50 IfSG

### Angaben zum Unternehmen › Betriebsangaben (`G05000013429`)

- **Rechtsform** (`F60000000339`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Juristische Person.Rechtsform Version 1.1; verwendet verwendet urn:xoev-de:xunternehmen:codeliste:rechtsformen_2
- **Eingetragener Name** (`F60000000319`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.

### Angaben zum Unternehmen › Ansprechperson (`G05000013430`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Angaben zum Unternehmen › Ansprechperson › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1; referenzbasiert; § 69 GewO; XInneres.Meldeanschrift.postleitzahl Version 8 _(geerbt)_
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

### Angaben zum Unternehmen › Nicht Natürliche Person › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1; referenzbasiert; § 69 GewO; XInneres.Meldeanschrift.postleitzahl Version 8 _(geerbt)_
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

### Tätigkeit mit Krankheitserregern - Erstanzeige (`G05000012257`)

- **Es handelt sich um eine Tätigkeit, die** (`F05000018275`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 1 IfSG; § 45 IfSG

### Tätigkeit mit Krankheitserregern - Erstanzeige › Angaben zur erlaubnisinnehabenden Person (`G05000012260`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Tätigkeit mit Krankheitserregern - Erstanzeige › Angaben zur erlaubnisinnehabenden Person › Erreichbarkeit (`G05000011747`)

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

### Tätigkeit mit Krankheitserregern - Erstanzeige › Angaben zur antragstellenden Person (`G05000012341`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Tätigkeit mit Krankheitserregern - Erstanzeige › Angaben zur antragstellenden Person › Erreichbarkeit (`G05000011747`)

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

### Tätigkeit mit Krankheitserregern - Erstanzeige › Erlaubnisfreiheit (`G05000012261`)

- **Beschreibung der Erlaubnisfreiheit** (`F05000018276`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 1 IfSG; § 45 IfSG
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 1 IfSG; § 45 IfSG _(geerbt)_

### Tätigkeit mit Krankheitserregern - Erstanzeige › Art und Umfang der Tätigkeit (`G05000012263`)

- **Hinweis zur Beschreibung:** (`F05000018280`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
- **Beschreibung der Tätigkeit** (`F05000018278`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG _(geerbt)_
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG _(geerbt)_

### Tätigkeit mit Krankheitserregern - Erstanzeige › Beschreibung der Räume und Einrichtungen (`G05000012264`)

- **Hinweis zur Beschreibung:** (`F05000018281`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
- **Beschreibung der Räume und Einrichtungen** (`F05000018282`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG _(geerbt)_

### Tätigkeit mit Krankheitserregern - Erstanzeige › Entsorgungswege und Entsorgungsverfahren für infektiösen Abfall (`G05000012265`)

- **Beschreibung der Entsorgungswege und -verfahren** (`F05000018283`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG _(geerbt)_

### Tätigkeit Krankheitserreger - Veränderungsanzeige › Angaben zur erlaubnisinnehabenden Person (`G05000012260`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Tätigkeit Krankheitserreger - Veränderungsanzeige › Angaben zur erlaubnisinnehabenden Person › Erreichbarkeit (`G05000011747`)

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

### Tätigkeit Krankheitserreger - Veränderungsanzeige › Erlaubnisfreiheit (`G05000012269`)

- **Beschreibung der Erlaubnisfreiheit** (`F05000018276`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 1 IfSG; § 45 IfSG
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 45 IfSG; § 49 (1) S. 2 Nr. 1 IfSG; § 50 IfSG _(geerbt)_
- **Zu welchem Zeitpunkt soll die Änderung erfolgen?** (`F05000018284`) — Pflicht
  - Rechtsgrundlage: § 45 IfSG; § 49 (1) S. 2 Nr. 1 IfSG; § 50 IfSG _(geerbt)_

### Tätigkeit Krankheitserreger - Veränderungsanzeige › Art und Umfang der Tätigkeit (`G05000012263`)

- **Hinweis zur Beschreibung:** (`F05000018280`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
- **Beschreibung der Tätigkeit** (`F05000018278`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG _(geerbt)_
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG _(geerbt)_

### Tätigkeit Krankheitserreger - Veränderungsanzeige › Beschreibung der Räume und Einrichtungen (`G05000012268`)

- **Hinweis zur Beschreibung:** (`F05000018281`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
- **Beschreibung der Räume und Einrichtungen** (`F05000018282`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG; § 50 IfSG _(geerbt)_
- **Zu welchem Zeitpunkt soll die Änderung erfolgen?** (`F05000018284`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG; § 50 IfSG _(geerbt)_

### Tätigkeit Krankheitserreger - Veränderungsanzeige › Entsorgungswege und Entsorgungsverfahren für infektiösen Abfall (`G05000012267`)

- **Beschreibung der Entsorgungswege und -verfahren** (`F05000018283`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
- **Möchten Sie zusätzlich zur Beschreibung ein Dokument hochladen?** (`F05000018277`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG; § 50 IfSG _(geerbt)_
- **Zu welchem Zeitpunkt soll die Änderung erfolgen?** (`F05000018284`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG; § 50 IfSG _(geerbt)_

### Nachweise Tätigkeiten mit Krankheitserregern › Nachweis Erlaubnis nach § 44 IfSG (`G05000012315`)

- **Hinweis:** (`F05000018324`) — optional
  - Rechtsgrundlage: § 44 IfSG; § 45 IfSG
- **Erlaubnis nach § 44 IfSG bzw. Erlaubnisfreiheit nach § 45 IfSG** (`F05000018326`) — optional
  - Rechtsgrundlage: § 44 IfSG; § 45 IfSG
  - Hilfe: Laden Sie die Erlaubnis nach § 44 IfSG bzw. die Erlaubnisfreiheit nach § 45 IfSG hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise Tätigkeiten mit Krankheitserregern › Nachweis Auflistung und Einstufung der Erreger in Risikogruppen (`G05000012316`)

- **Hinweis:** (`F05000018376`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
- **Auflistung und Einstufung der Erreger in Risikogruppen** (`F05000018377`) — Pflicht
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
  - Hilfe: Laden Sie Auflistung und Einstufung der Erreger in Risikogruppen hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise Tätigkeiten mit Krankheitserregern › Darstellung der Entsorgungswege und der Entsorgungsverfahren für infektiöses Entsorgungsgut (`G05000012317`)

- **Hinweis:** (`F05000018328`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
- **Darstellung der Entsorgungswege und das Entsorgungsverfahren für infektiöses Entsorgungsgut** (`F05000018329`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
  - Hilfe: Laden Sie die Darstellung der Entsorgungswege und das Entsorgungsverfahren für infektiöses Entsorgungsgut hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise Tätigkeiten mit Krankheitserregern (`G05000012314`)

- **Darstellung der Ver- und Entsorgungsbereiche, der Nebenräume, der eventuellen Tierställe und der technischen Ausstattung** (`F05000018334`) — optional, conditional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
  - Hilfe: Laden Sie eine Darstellung der Ver- und Entsorgungsbereiche, der Nebenräume, der eventuellen Tierställe und der technischen Ausstattung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Grundrissplan mit Funktionsausweisung der Räume** (`F05000018335`) — optional, conditional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
  - Hilfe: Laden Sie den Grundrissplan mit Funktionsausweisung der Räume hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Dokument zu Art und Umfang der beabsichtigten Tätigkeit** (`F05000018358`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
  - Hilfe: Laden Sie das Dokument zu Art und Umfang der beabsichtigten Tätigkeit hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Dokument zur Beschreibung der Räume und Einrichtungen** (`F05000018359`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
  - Hilfe: Laden Sie das Dokument zur Beschreibung der Räume und Einrichtungen hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Dokument zur Darstellung der Entsorgungswege und der Entsorgungsverfahren für infektiösen Abfall** (`F05000018373`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 2 IfSG
  - Hilfe: Laden Sie das Dokument zur Darstellung der Entsorgungswege und der Entsorgungsverfahren für infektiösen Abfall hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Dokument zur Beschreibung der Erlaubnisfreiheit** (`F05000018361`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 1 IfSG; § 45 IfSG
  - Hilfe: Laden Sie das Dokument zur Beschreibung der Erlaubnisfreiheit hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise Tätigkeiten mit Krankheitserregern › Darstellung der Raumausstattung und der Raumaufteilung (`G05000012323`)

- **Hinweis:** (`F05000018337`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
- **Darstellung der Raumausstattung und der Raumaufteilung** (`F05000018339`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
  - Hilfe: Laden Sie eine Darstellung der Raumausstattung und der Raumaufteilung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise Tätigkeiten mit Krankheitserregern › Nachweis Liste der sicherheitsrelevanten Geräte und Anlagen (`G05000012326`)

- **Hinweis:** (`F05000018342`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
- **Liste der Laborgeräte** (`F05000018345`) — optional
  - Rechtsgrundlage: § 49 (1) S. 2 Nr. 3 IfSG
  - Hilfe: Laden Sie eine Liste der Laborgeräte hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise Tätigkeiten mit Krankheitserregern › Nachweis zu Schutzmaßnahmen (`G05000012328`)

- **Hinweis:** (`F05000018349`) — optional
  - Rechtsgrundlage: § 28 IfSG; § 9 BioStoffV
- **Nachweis zu Schutzmaßnahmen** (`F05000018352`) — optional
  - Rechtsgrundlage: § 28 IfSG; § 9 BioStoffV
  - Hilfe: Laden Sie den Nachweis zu Schutzmaßnahmen hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise Tätigkeiten mit Krankheitserregern › Nachweis Hygieneplan (`G05000012330`)

- **Hinweis:** (`F05000018354`) — optional
  - Rechtsgrundlage: § 9 BioStoffV
- **Hygieneplan** (`F05000018355`) — Pflicht
  - Rechtsgrundlage: § 9 BioStoffV
  - Hilfe: Laden Sie den Hygieneplan hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika (`G05000012334`)

- **Angaben zum Vorhandensein eines Tierstalls** (`F05000018372`) — optional
  - Rechtsgrundlage: Referenzbasiert
  - Hilfe: Laden Sie die Angaben zum Vorhandensein eines Tierstalls hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Es handelt sich um eine" gleich „Erstanzeige" ist | „Tätigkeit mit Krankheitserregern - Erstanzeige" | muss ausgefüllt werden | — | `R05000013373` |
| wenn „Es handelt sich um eine" ungleich „Erstanzeige" ist | „Tätigkeit mit Krankheitserregern - Erstanzeige" | entfällt | — | `R05000013373` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" gleich „wahr" ist | _mehrere Felder_ | muss ausgefüllt werden | — | `R05000013375` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" ungleich „wahr" ist | _mehrere Felder_ | entfällt | — | `R05000013375` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" gleich „wahr" ist | „Beschreibung der Räume und Einrichtungen" | muss ausgefüllt werden | — | `R05000013376` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" ungleich „wahr" ist | „Beschreibung der Räume und Einrichtungen" | entfällt | — | `R05000013376` |
| wenn „Angaben zur Erlaubnisfreiheit" gleich „wahr" oder „Veränderungen zu § 45 (2) IfSG" oder „wahr" ist | „Erlaubnisfreiheit" | muss ausgefüllt werden | — | `R05000013377` |
| wenn „Angaben zur Erlaubnisfreiheit" ungleich „wahr" oder „Veränderungen zu § 45 (2) IfSG" oder „wahr" ist | „Erlaubnisfreiheit" | entfällt | — | `R05000013377` |
| wenn „Es handelt sich um eine" gleich „Erstanzeige" ist | „Nachweis Erlaubnis nach § 44 IfSG" | muss ausgefüllt werden | — | `R05000013412` |
| wenn „Es handelt sich um eine" ungleich „Erstanzeige" ist | „Nachweis Erlaubnis nach § 44 IfSG" | entfällt | — | `R05000013412` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" gleich „wahr" ist | „Darstellung der Ver- und Entsorgungsbereiche, der Nebenräume, der eventuellen Tierställe und der technischen Ausstattung" | muss ausgefüllt werden | — | `R05000013413` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" ungleich „wahr" ist | „Darstellung der Ver- und Entsorgungsbereiche, der Nebenräume, der eventuellen Tierställe und der technischen Ausstattung" | entfällt | — | `R05000013413` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" gleich „wahr" ist | „Grundrissplan mit Funktionsausweisung der Räume" | muss ausgefüllt werden | — | `R05000013414` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" ungleich „wahr" ist | „Grundrissplan mit Funktionsausweisung der Räume" | entfällt | — | `R05000013414` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" gleich „wahr" ist | „Darstellung der Raumausstattung und der Raumaufteilung" | muss ausgefüllt werden | — | `R05000013415` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" ungleich „wahr" ist | „Darstellung der Raumausstattung und der Raumaufteilung" | entfällt | — | `R05000013415` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" gleich „wahr" ist | „Nachweis Liste der sicherheitsrelevanten Geräte und Anlagen" | muss ausgefüllt werden | — | `R05000013416` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" ungleich „wahr" ist | „Nachweis Liste der sicherheitsrelevanten Geräte und Anlagen" | entfällt | — | `R05000013416` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" gleich „wahr" ist | „Nachweis zu Schutzmaßnahmen" | muss ausgefüllt werden | — | `R05000013417` |
| wenn „Angaben zur Beschaffenheit der Räume und Einrichtungen" ungleich „wahr" ist | „Nachweis zu Schutzmaßnahmen" | entfällt | — | `R05000013417` |
| wenn „Es handelt sich um eine" gleich „Veränderungsanzeige" ist | „Tätigkeit Krankheitserreger - Veränderungsanzeige" | muss ausgefüllt werden | — | `R05000013428` |
| wenn „Es handelt sich um eine" ungleich „Veränderungsanzeige" ist | „Tätigkeit Krankheitserreger - Veränderungsanzeige" | entfällt | — | `R05000013428` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" gleich „wahr" ist | „Entsorgungswege und Entsorgungsverfahren für infektiösen Abfall" | muss ausgefüllt werden | — | `R05000013429` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" ungleich „wahr" ist | „Entsorgungswege und Entsorgungsverfahren für infektiösen Abfall" | entfällt | — | `R05000013429` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" gleich „wahr" ist | „Darstellung der Entsorgungswege und der Entsorgungsverfahren für infektiöses Entsorgungsgut" | muss ausgefüllt werden | — | `R05000013433` |
| wenn „Angaben zur Art und Umfang der beabsichtigten Tätigkeiten, Entsorgungsmaßnahmen oder Änderungen bei den Erregern" ungleich „wahr" ist | „Darstellung der Entsorgungswege und der Entsorgungsverfahren für infektiöses Entsorgungsgut" | entfällt | — | `R05000013433` |
| wenn „Es handelt sich um eine" gleich „02" ist | „Art der Änderung" | muss ausgefüllt werden | — | `G05000012249` |
| wenn „Es handelt sich um eine" ungleich „02" ist | „Art der Änderung" | darf nicht ausgefüllt werden | — | `G05000012249` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Ansprechperson" | muss ausgefüllt werden | — | `R05000015800` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | entfällt | — | `R05000015800` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | muss ausgefüllt werden | — | `R05000015801` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Ansprechperson" | entfällt | — | `R05000015801` |
| wenn „Wo befindet sich die Anschrift?" gleich „001" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" gleich „002" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wo befindet sich die Anschrift?" gleich „001" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" gleich „002" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Es handelt sich um eine Tätigkeit, die" gleich „01" ist | „Angaben zur erlaubnisinnehabenden Person" | muss ausgefüllt werden | — | `G05000012257` |
| wenn „Es handelt sich um eine Tätigkeit, die" ungleich „01" ist | „Angaben zur erlaubnisinnehabenden Person" | darf nicht ausgefüllt werden | — | `G05000012257` |
| wenn „Es handelt sich um eine Tätigkeit, die" gleich „02" ist | „Erlaubnisfreiheit" | muss ausgefüllt werden | — | `G05000012257` |
| wenn „Es handelt sich um eine Tätigkeit, die" ungleich „02" ist | „Erlaubnisfreiheit" | darf nicht ausgefüllt werden | — | `G05000012257` |
| wenn „Es handelt sich um eine Tätigkeit, die" gleich „02" ist | „Angaben zur antragstellenden Person" | muss ausgefüllt werden | — | `G05000012257` |
| wenn „Es handelt sich um eine Tätigkeit, die" ungleich „02" ist | „Angaben zur antragstellenden Person" | darf nicht ausgefüllt werden | — | `G05000012257` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Mindestens eins der Felder F05000018265 "Abfrage Änderung Tätigkeiten (Anzeige Krankheitserreger)", F05000018266 "Abfrage Änderung Räume (Anzeige Krankheitserreger)", F05000018267 "Abfrage Änderung Erlaubnisfreiheit (Anzeige Krankheitserreger)" oder F05000018367 "Veränderungen zu § 45 (2) IfSG" muss den Wert "wahr" haben.</mark> — Regel `R05000013346`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000012249_F05000018264["Es handelt sich um eine"] ==>|"= Erstanzeige → required"| G05000012257["Tätigkeit mit Krankheitserregern - Ers"]
  G05000012249_F05000018264["Es handelt sich um eine"] -.->|"<> Erstanzeige → hide"| G05000012257["Tätigkeit mit Krankheitserregern - Ers"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] ==>|"= wahr → required"| G05000012266_G05000012268["Beschreibung der Räume und Einrichtung"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] -.->|"<> wahr → hide"| G05000012266_G05000012268["Beschreibung der Räume und Einrichtung"]
  G05000012249_G05000012252_F05000018267["Angaben zur Erlaubnisfreiheit"] ==>|"= wahr, Veränderungen zu § 45  → required"| G05000012266_G05000012269["Erlaubnisfreiheit"]
  G05000012249_G05000012252_F05000018267["Angaben zur Erlaubnisfreiheit"] -.->|"<> wahr, Veränderungen zu § 45  → hide"| G05000012266_G05000012269["Erlaubnisfreiheit"]
  G05000012249_F05000018264["Es handelt sich um eine"] ==>|"= Erstanzeige → required"| G05000012314_G05000012315["Nachweis Erlaubnis nach § 44 IfSG"]
  G05000012249_F05000018264["Es handelt sich um eine"] -.->|"<> Erstanzeige → hide"| G05000012314_G05000012315["Nachweis Erlaubnis nach § 44 IfSG"]
  G05000012249_G05000012252_F05000018265["Angaben zur Art und Umfang der beabsic"] ==>|"= wahr → required"| G05000012314_F05000018334["Darstellung der Ver- und Entsorgungsbe"]
  G05000012249_G05000012252_F05000018265["Angaben zur Art und Umfang der beabsic"] -.->|"<> wahr → hide"| G05000012314_F05000018334["Darstellung der Ver- und Entsorgungsbe"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] ==>|"= wahr → required"| G05000012314_F05000018335["Grundrissplan mit Funktionsausweisung "]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] -.->|"<> wahr → hide"| G05000012314_F05000018335["Grundrissplan mit Funktionsausweisung "]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] ==>|"= wahr → required"| G05000012314_G05000012323["Darstellung der Raumausstattung und de"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] -.->|"<> wahr → hide"| G05000012314_G05000012323["Darstellung der Raumausstattung und de"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] ==>|"= wahr → required"| G05000012314_G05000012326["Nachweis Liste der sicherheitsrelevant"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] -.->|"<> wahr → hide"| G05000012314_G05000012326["Nachweis Liste der sicherheitsrelevant"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] ==>|"= wahr → required"| G05000012314_G05000012328["Nachweis zu Schutzmaßnahmen"]
  G05000012249_G05000012252_F05000018266["Angaben zur Beschaffenheit der Räume u"] -.->|"<> wahr → hide"| G05000012314_G05000012328["Nachweis zu Schutzmaßnahmen"]
  G05000012249_F05000018264["Es handelt sich um eine"] ==>|"= Veränderungsanzeige → required"| G05000012266["Tätigkeit Krankheitserreger - Veränder"]
  G05000012249_F05000018264["Es handelt sich um eine"] -.->|"<> Veränderungsanzeige → hide"| G05000012266["Tätigkeit Krankheitserreger - Veränder"]
  G05000012249_G05000012252_F05000018265["Angaben zur Art und Umfang der beabsic"] ==>|"= wahr → required"| G05000012266_G05000012267["Entsorgungswege und Entsorgungsverfahr"]
  G05000012249_G05000012252_F05000018265["Angaben zur Art und Umfang der beabsic"] -.->|"<> wahr → hide"| G05000012266_G05000012267["Entsorgungswege und Entsorgungsverfahr"]
  G05000012249_G05000012252_F05000018265["Angaben zur Art und Umfang der beabsic"] ==>|"= wahr → required"| G05000012314_G05000012317["Darstellung der Entsorgungswege und de"]
  G05000012249_G05000012252_F05000018265["Angaben zur Art und Umfang der beabsic"] -.->|"<> wahr → hide"| G05000012314_G05000012317["Darstellung der Entsorgungswege und de"]
  G05000012249_F05000018264["Es handelt sich um eine"] ==>|"= 02 → required"| G05000012249_G05000012252["Art der Änderung"]
  G05000012249_F05000018264["Es handelt sich um eine"] -.->|"<> 02 → forbidden"| G05000012249_G05000012252["Art der Änderung"]
  G05000013428_G05000013429["Betriebsangaben"] ==>|"= ? → required"| G05000013428_G05000013430["Ansprechperson"]
  G05000013428_G05000013429["Betriebsangaben"] -.->|"= ? → hide"| G05000013428_G05000013431["Nicht Natürliche Person"]
  G05000013428_G05000013429["Betriebsangaben"] ==>|"= ? → required"| G05000013428_G05000013431["Nicht Natürliche Person"]
  G05000013428_G05000013429["Betriebsangaben"] -.->|"= ? → hide"| G05000013428_G05000013430["Ansprechperson"]
  G05000013428_G05000013430_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 → required"| G05000013428_G05000013430_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013428_G05000013430_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 → forbidden"| G05000013428_G05000013430_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013428_G05000013430_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 → required"| G05000013428_G05000013430_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013428_G05000013430_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 → forbidden"| G05000013428_G05000013430_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013428_G05000013430_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000013428_G05000013430_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013428_G05000013430_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 001 → forbidden"| G05000013428_G05000013430_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013428_G05000013430_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000013428_G05000013430_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013428_G05000013430_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 002 → forbidden"| G05000013428_G05000013430_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013428_G05000013431_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 → required"| G05000013428_G05000013431_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013428_G05000013431_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 → forbidden"| G05000013428_G05000013431_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013428_G05000013431_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 → required"| G05000013428_G05000013431_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013428_G05000013431_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 → forbidden"| G05000013428_G05000013431_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013428_G05000013431_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000013428_G05000013431_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013428_G05000013431_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 001 → forbidden"| G05000013428_G05000013431_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013428_G05000013431_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000013428_G05000013431_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013428_G05000013431_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 002 → forbidden"| G05000013428_G05000013431_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000012257_F05000018275["Es handelt sich um eine Tätigkeit, die"] ==>|"= 01 → required"| G05000012257_G05000012260["Angaben zur erlaubnisinnehabenden Pers"]
  G05000012257_F05000018275["Es handelt sich um eine Tätigkeit, die"] -.->|"<> 01 → forbidden"| G05000012257_G05000012260["Angaben zur erlaubnisinnehabenden Pers"]
  G05000012257_F05000018275["Es handelt sich um eine Tätigkeit, die"] ==>|"= 02 → required"| G05000012257_G05000012261["Erlaubnisfreiheit"]
  G05000012257_F05000018275["Es handelt sich um eine Tätigkeit, die"] -.->|"<> 02 → forbidden"| G05000012257_G05000012261["Erlaubnisfreiheit"]
  G05000012257_F05000018275["Es handelt sich um eine Tätigkeit, die"] ==>|"= 02 → required"| G05000012257_G05000012341["Angaben zur antragstellenden Person"]
  G05000012257_F05000018275["Es handelt sich um eine Tätigkeit, die"] -.->|"<> 02 → forbidden"| G05000012257_G05000012341["Angaben zur antragstellenden Person"]
  unclear0["?: Mindestens eins der Felder F05000018265 "Abfrage Änderung Tä"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
