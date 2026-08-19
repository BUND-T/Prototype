---
name: antrag-s05000001300
description: Führt Antragstellende durch „Antrag auf Erlaubnis für den Betrieb einer Kindertageseinrichtung" (FIM S05000001300 1.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf Erlaubnis für den Betrieb einer Kindertageseinrichtung

- **FIM-ID:** `S05000001300 1.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 45 SGB VIII vom 3.4.2025; § 99 (7) SGB VIII vom 3.4.2025; referenzbasiert
- **Kompiliert:** 2026-08-13T15:44:08Z aus https://fimportal.de/api/v1/schemas/S05000001300/1.0.0/xdf
- **Umfang:** 137 Felder, 45 gesicherte Bedingungen, 1 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Wann soll die Einrichtung in Betrieb genommen werden?** (`F05000017532`) — Pflicht
  - Rechtsgrundlage: DIN 5008
  - Hilfe: Beachten Sie: Eine rückwirkende Datierung ist nicht möglich.

### Angaben zum Träger › Informationen zum Träger (`G05000012393`)

- **Rechtsform** (`F05000017511`) — Pflicht
  - Rechtsgrundlage: § 45 (1) SGB VIII; referenzbasiert _(geerbt)_
- **Eingetragener Name** (`F60000000319`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.

### Angaben zum Träger › Weitere Angaben zum Träger (`G05000012394`)

- **Es handelt sich um einen** (`F05000017571`) — Pflicht
  - Rechtsgrundlage: § 45 (1) SGB VIII; referenzbasiert _(geerbt)_
  - Hilfe: Öffentliche Träger sind z.B. Kommunen. Bei freien Trägern handelt es sich beispielweise um Vereine, Kirchen, Stiftungen, Initiativen oder gemeinnützige GmbHs.

### Angaben zum Träger › Weitere Angaben zum Träger › Anschrift (`G05000011799`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: § 45 (1) SGB VIII; referenzbasiert _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Träger › Weitere Angaben zum Träger › Anschrift › Anschrift in Deutschland (`G05000011790`)

- **Welche Art der Anschrift möchten Sie angeben?** (`F05000017662`) — Pflicht
  - Rechtsgrundlage: § 45 (1) SGB VIII; referenzbasiert _(geerbt)_

### Angaben zum Träger › Weitere Angaben zum Träger › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zum Träger › Weitere Angaben zum Träger › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Träger › Weitere Angaben zum Träger › Anschrift › Anschrift in Deutschland › Anschrift Inland Großempfänger (`G60000000208`)

- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Träger › Weitere Angaben zum Träger › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Träger › Weitere Angaben zum Träger › Anschrift › Anschrift Ausland (`G60000000191`)

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

### Angaben zum Träger › Weitere Angaben zum Träger › Erreichbarkeit (`G05000011747`)

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

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers (`G05000011693`)

- **Art des gesetzlichen Vertreters** (`F60000000375`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:codeliste:artgesetzlichervertreter

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung (`G05000013138`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Weicht die Anschrift von der Trägeranschrift ab?** (`F05000017542`) — Pflicht
  - Rechtsgrundlage: § 45 (1) SGB VIII

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Anschrift (`G05000011799`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: § 45 (1) SGB VIII _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Anschrift › Anschrift in Deutschland (`G05000011790`)

- **Welche Art der Anschrift möchten Sie angeben?** (`F05000017662`) — Pflicht
  - Rechtsgrundlage: § 45 (1) SGB VIII _(geerbt)_

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Anschrift › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Anschrift › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Anschrift › Anschrift in Deutschland › Anschrift Inland Großempfänger (`G60000000208`)

- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Anschrift › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Anschrift › Anschrift Ausland (`G60000000191`)

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

### Angaben zum Träger › Weitere Angaben zum Träger › Vertretung des Trägers › Angaben zur Vertretung › Erreichbarkeit (`G05000011747`)

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

### Angaben zur Kindertageseinrichtung (`G05000011687`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Name der Einrichtung** (`F05000017539`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; referenzbasiert _(geerbt)_
- **Möchten Sie Adressangaben zu Nebengebäuden oder Dependancen machen?** (`F05000017530`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII

### Angaben zur Kindertageseinrichtung › Straßenanschrift Inland (`G05000012253`)

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

### Angaben zur Kindertageseinrichtung › Weitere Adressangabe (`G05000011689`)

- **Gebäudeart** (`F05000017531`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII

### Angaben zur Kindertageseinrichtung › Weitere Adressangabe › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zur Kindertageseinrichtung › Erreichbarkeit (`G05000011747`)

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

### Öffnungszeiten der Einrichtung › Öffnungszeit Montag (`G05000004560`)

- **von** (`F05000007571`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_
- **bis** (`F05000007572`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_

### Öffnungszeiten der Einrichtung › Öffnungszeit Dienstag (`G05000004562`)

- **von** (`F05000007571`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_
- **bis** (`F05000007572`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_

### Öffnungszeiten der Einrichtung › Öffnungszeit Mittwoch (`G05000004563`)

- **von** (`F05000007571`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_
- **bis** (`F05000007572`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_

### Öffnungszeiten der Einrichtung › Öffnungszeit Donnerstag (`G05000004564`)

- **von** (`F05000007571`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_
- **bis** (`F05000007572`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_

### Öffnungszeiten der Einrichtung › Öffnungszeit Freitag (`G05000004565`)

- **von** (`F05000007571`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_
- **bis** (`F05000007572`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_

### Öffnungszeiten der Einrichtung › Öffnungszeit Samstag (`G05000004566`)

- **von** (`F05000007571`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_
- **bis** (`F05000007572`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_

### Öffnungszeiten der Einrichtung › Öffnungszeit Sonntag (`G05000004567`)

- **von** (`F05000007571`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_
- **bis** (`F05000007572`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1f SGB VIII _(geerbt)_

### Nachweise (`G05000011691`)

- **Einrichtungskonzeption (inklusive Gewaltschutzkonzept nach § 45 SGB VIII)** (`F05000017533`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 4 SGB VIII
  - Hilfe: Laden Sie die Einrichtungskonzeption (inklusive Gewaltschutzkonzept nach § 45 SGB VIII) hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Grundrisszeichnung des vorgesehenen Gebäudes und Skizze des Außengeländes** (`F05000017534`) — Pflicht
  - Rechtsgrundlage: § 45 SGB VIII
  - Hilfe: Laden Sie eine Grundrisszeichnung des vorgesehenen Gebäudes und eine Skizze des Außengeländes hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Wirtschaftsplan oder Finanzierungsplan** (`F05000017535`) — optional, conditional
  - Rechtsgrundlage: § 45 SGB VIII
  - Hilfe: Laden Sie den Wirtschaftsplan oder Finanzierungsplan hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: leer, da Referenzkontext
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nutzungsgenehmigung für die beantragten Plätze (`G05000012369`)

- **Liegt eine Nutzungsgenehmigung für die beantragten Plätze vor?** (`F05000017536`) — Pflicht
  - Rechtsgrundlage: § 45 SGB VIII
- **Nutzungsgenehmigung der zuständigen Bauaufsicht** (`F05000017537`) — optional, conditional
  - Rechtsgrundlage: § 45 SGB VIII
  - Hilfe: Laden Sie die Nutzungsgenehmigung der zuständigen Bauaufsicht hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Bescheinigung über eine erfolgte Schlussabnahme** (`F05000017538`) — optional, conditional
  - Rechtsgrundlage: § 45 SGB VIII
  - Hilfe: Laden Sie die Bescheinigung über eine erfolgte Schlussabnahme hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika für Bremen › Alter der Kinder (`G05000011715`)

- **Einheit:** (`F05000018431`) — Pflicht
  - Rechtsgrundlage: § 45 SGB VIII
- **Alter von** (`F05000017581`) — Pflicht
  - Rechtsgrundlage: § 45 SGB VIII; § 99 (7) S. 1 Nr. 1c SGB VIII
- **Alter bis** (`F05000017582`) — Pflicht
  - Rechtsgrundlage: § 45 SGB VIII; § 99 (7) S. 1 Nr. 1c SGB VIII

### Landesspezifika für Bremen (`G05000012375`)

- **Gesamtanzahl der vorhandenen Plätze in der Kindertageseinrichtung** (`F05000017583`) — Pflicht
  - Rechtsgrundlage: § 45 SGB VIII; § 99 (7) S. 1 Nr. 1b SGB VIII
- **Einrichtungsnummer oder EDV-Nummer** (`F05000017584`) — optional
  - Rechtsgrundlage: referenzbasiert

### Landesspezifika für Bremen › Gruppenstruktur (`G05000011716`)

- **Art der Gruppe** (`F05000017585`) — Pflicht
  - Rechtsgrundlage: § 45 SGB VIII; § 99 (7) S. 1 Nr. 1c SGB VIII
- **Anzahl der Gruppen dieser Gruppenart** (`F05000017587`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1c SGB VIII
- **Anzahl der Kinder pro Gruppe** (`F05000017588`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1c SGB VIII
- **Anzahl der Kinder pro Gruppe unter einem Jahr** (`F05000017589`) — optional, conditional
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 1c SGB VIII
- **Gebäudeart** (`F05000017531`) — Pflicht, conditional
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII

### Landesspezifika für Bremen › Räumlichkeit in der Kindertageseinrichtung (`G05000011717`)

- **Hinweis:** (`F05000018432`) — optional
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII
- **Räumlichkeit, die in der Kindertageseinrichtung vorhanden ist:** (`F05000017590`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII
- **Raumgröße in Quadratmetern** (`F05000017591`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII _(geerbt)_

### Landesspezifika für Bremen › Ausstattung der Kindertageseinrichtung (`G05000011719`)

- **Anzahl der Toiletten für Kinder** (`F05000017596`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII
- **Anzahl der Waschbecken für Kinder** (`F05000017597`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII
- **Anzahl Toiletten für Personal** (`F05000017598`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII
- **Ist eine Kochküche vorhanden?** (`F05000017599`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII
- **Ist eine Verteilerküche vorhanden?** (`F05000017600`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII

### Landesspezifika für Bremen › Träger der Jugendhilfe (`G05000011720`)

- **Die Vereinssatzung oder der Nachweis "Träger der Jugendhilfe"** (`F05000017601`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika für Bremen › Vorläufige Adresse / Projektadresse (`G05000012384`)

- **Bei der anzugebenden Adresse der Kindertageseinrichtung handelt es sich um eine Adresse, die noch nicht im Straßenverzeichnis hinterlegt ist, aber in Planung ist.** (`F05000017603`) — Pflicht
  - Rechtsgrundlage: referenzbasiert

### Landesspezifika für Bremen › Vorläufige Adresse / Projektadresse › Vorläufige Adresse / Projektadresse (`G05000012385`)

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

### Landesspezifika für Bremen › Personalmeldung (`G05000012387`)

- **Die Personalmeldung zu dem bei Ihnen beschäftigten Personal** (`F05000017604`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika für Bremen › Personalangaben (`G05000011722`)

- **Hinweis:** (`F05000018433`) — optional
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 2 SGB VIII
- **Funktion in der Kindertageseinrichtung** (`F05000017606`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 2 SGB VIII
- **Anzahl Personen** (`F05000017607`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 2 SGB VIII

### Landesspezifika für Bremen › Personalangaben › Weitere Angaben zum Personal (`G05000012386`)

- **Wöchentliche Arbeitsstunden laut Arbeitsvertrag** (`F05000017608`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 2 SGB VIII
- **Ausbildung / Qualifikation** (`F05000017609`) — Pflicht
  - Rechtsgrundlage: § 45 (2) S. 2 Nr. 2 SGB VIII; § 99 (7) S. 1 Nr. 2 SGB VIII

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Es handelt sich um einen" gleich „freien Träger" ist | „Wirtschaftsplan oder Finanzierungsplan" | muss ausgefüllt werden | — | `R05000013490` |
| wenn „Es handelt sich um einen" ungleich „freien Träger" ist | „Wirtschaftsplan oder Finanzierungsplan" | entfällt | — | `R05000013490` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012599` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `R05000012599` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012600` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012600` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" gleich „002 Postfach" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `R05000012588` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" ungleich „002 Postfach" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `R05000012588` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" gleich „001 Straßenanschrift" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012589` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" ungleich „001 Straßenanschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012589` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" gleich „003 Großempfänger" ist | „Anschrift Inland Großempfänger" | muss ausgefüllt werden | — | `R05000012598` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" ungleich „003 Großempfänger" ist | „Anschrift Inland Großempfänger" | darf nicht ausgefüllt werden | — | `R05000012598` |
| wenn „Weicht die Anschrift von der Trägeranschrift ab?" gleich „wahr" ist | „Anschrift" | muss ausgefüllt werden | — | `R05000012429` |
| wenn „Weicht die Anschrift von der Trägeranschrift ab?" ungleich „wahr" ist | „Anschrift" | entfällt | — | `R05000012429` |
| wenn „Weicht die Anschrift von der Trägeranschrift ab?" gleich „wahr" ist | „Anschrift" | muss ausgefüllt werden | — | `R05000014995` |
| wenn „Weicht die Anschrift von der Trägeranschrift ab?" ungleich „wahr" ist | „Anschrift" | entfällt | — | `R05000014995` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012599` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `R05000012599` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012600` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012600` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" gleich „002 Postfach" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `R05000012588` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" ungleich „002 Postfach" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `R05000012588` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" gleich „001 Straßenanschrift" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012589` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" ungleich „001 Straßenanschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012589` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" gleich „003 Großempfänger" ist | „Anschrift Inland Großempfänger" | muss ausgefüllt werden | — | `R05000012598` |
| wenn „Welche Art der Anschrift möchten Sie angeben?" ungleich „003 Großempfänger" ist | „Anschrift Inland Großempfänger" | darf nicht ausgefüllt werden | — | `R05000012598` |
| wenn „Möchten Sie Adressangaben zu Nebengebäuden oder Dependancen machen?" gleich „wahr" ist | „Weitere Adressangabe" | muss ausgefüllt werden | — | `R05000013516` |
| wenn „Möchten Sie Adressangaben zu Nebengebäuden oder Dependancen machen?" ungleich „wahr" ist | „Weitere Adressangabe" | entfällt | — | `R05000013516` |
| wenn „Liegt eine Nutzungsgenehmigung für die beantragten Plätze vor?" gleich „Ja, Nutzungsgenehmigung liegt schriftlich vor (Schreiben der Bauaufsicht)" ist | „Nutzungsgenehmigung der zuständigen Bauaufsicht" | muss ausgefüllt werden | — | `R05000013488` |
| wenn „Liegt eine Nutzungsgenehmigung für die beantragten Plätze vor?" ungleich „Ja, Nutzungsgenehmigung liegt schriftlich vor (Schreiben der Bauaufsicht)" ist | „Nutzungsgenehmigung der zuständigen Bauaufsicht" | entfällt | — | `R05000013488` |
| wenn „Liegt eine Nutzungsgenehmigung für die beantragten Plätze vor?" gleich „Ja, die Bescheinigung über eine erfolgte Schlussabnahme liegt vor" ist | „Bescheinigung über eine erfolgte Schlussabnahme" | muss ausgefüllt werden | — | `R05000013489` |
| wenn „Liegt eine Nutzungsgenehmigung für die beantragten Plätze vor?" ungleich „Ja, die Bescheinigung über eine erfolgte Schlussabnahme liegt vor" ist | „Bescheinigung über eine erfolgte Schlussabnahme" | entfällt | — | `R05000013489` |
| wenn „Art der Gruppe" gleich „Krippe" ist | „Anzahl der Kinder pro Gruppe unter einem Jahr" | muss ausgefüllt werden | — | `R05000012446` |
| wenn „Art der Gruppe" ungleich „Krippe" ist | „Anzahl der Kinder pro Gruppe unter einem Jahr" | entfällt | — | `R05000012446` |
| wenn „Anzahl der Gruppen dieser Gruppenart" gleich einem beliebigen Wert ist | „Gebäudeart" | muss ausgefüllt werden | — | `R05000013500` |
| wenn „Anzahl der Gruppen dieser Gruppenart" gesetzt auf einem beliebigen Wert ist | „Gebäudeart" | muss ausgefüllt werden | — | `R05000013500` |
| wenn „Die Vereinssatzung oder der Nachweis "Träger der Jugendhilfe"" gleich „wird beigefügt." ist | „Laden Sie den entsprechenden Nachweis hoch." | entfällt und muss ausgefüllt werden | — | `R05000012448` |
| wenn „Bei der anzugebenden Adresse der Kindertageseinrichtung handelt es sich um eine Adresse, die noch nicht im Straßenverzeichnis hinterlegt ist, aber in Planung ist." gleich „wahr" ist | „Vorläufige Adresse / Projektadresse" | muss ausgefüllt werden | — | `R05000013501` |
| wenn „Bei der anzugebenden Adresse der Kindertageseinrichtung handelt es sich um eine Adresse, die noch nicht im Straßenverzeichnis hinterlegt ist, aber in Planung ist." ungleich „wahr" ist | „Vorläufige Adresse / Projektadresse" | entfällt | — | `R05000013501` |
| wenn „Die Personalmeldung zu dem bei Ihnen beschäftigten Personal" gleich „wird beigefügt." ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000013503` |
| wenn „Die Personalmeldung zu dem bei Ihnen beschäftigten Personal" ungleich „wird beigefügt." ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000013503` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Die Angabe in Feld F05000017607 "Anzahl Personen" bestimmt, wie oft die Gruppe G05000012386 "Weitere Angaben Personal" befüllt werden muss.</mark> — Regel `R05000013502`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000011692_G05000012394_F05000017571["Es handelt sich um einen"] ==>|"= freien Träger → required"| G05000011691_F05000017535["Wirtschaftsplan oder Finanzierungsplan"]
  G05000011692_G05000012394_F05000017571["Es handelt sich um einen"] -.->|"<> freien Träger → hide"| G05000011691_F05000017535["Wirtschaftsplan oder Finanzierungsplan"]
  G05000011692_G05000012394_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011692_G05000012394_G05000011799_G05000011790["Anschrift in Deutschland"]
  G05000011692_G05000012394_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → forbidden"| G05000011692_G05000012394_G05000011799_G05000011790["Anschrift in Deutschland"]
  G05000011692_G05000012394_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011692_G05000012394_G05000011799_G60000000191["Anschrift Ausland"]
  G05000011692_G05000012394_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → forbidden"| G05000011692_G05000012394_G05000011799_G60000000191["Anschrift Ausland"]
  G05000011692_G05000012394_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] ==>|"= 002 Postfach → required"| G05000011692_G05000012394_G05000011799_G05000011790_G60000000087["Anschrift Postfach"]
  G05000011692_G05000012394_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] -.->|"<> 002 Postfach → forbidden"| G05000011692_G05000012394_G05000011799_G05000011790_G60000000087["Anschrift Postfach"]
  G05000011692_G05000012394_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] ==>|"= 001 Straßenanschrift → required"| G05000011692_G05000012394_G05000011799_G05000011790_G05000011743["Straßenanschrift Inland"]
  G05000011692_G05000012394_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] -.->|"<> 001 Straßenanschrift → hide"| G05000011692_G05000012394_G05000011799_G05000011790_G05000011743["Straßenanschrift Inland"]
  G05000011692_G05000012394_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] ==>|"= 003 Großempfänger → required"| G05000011692_G05000012394_G05000011799_G05000011790_G60000000208["Anschrift Inland Großempfänger"]
  G05000011692_G05000012394_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] -.->|"<> 003 Großempfänger → forbidden"| G05000011692_G05000012394_G05000011799_G05000011790_G60000000208["Anschrift Inland Großempfänger"]
  G05000011692_G05000012394_G05000011693_G05000013138_F05000017542["Weicht die Anschrift von der Trägerans"] ==>|"= wahr → required"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799["Anschrift"]
  G05000011692_G05000012394_G05000011693_G05000013138_F05000017542["Weicht die Anschrift von der Trägerans"] -.->|"<> wahr → hide"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799["Anschrift"]
  G05000011692_G05000012394_G05000011693_G05000013138_F05000017542["Weicht die Anschrift von der Trägerans"] ==>|"= wahr → required"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799["Anschrift"]
  G05000011692_G05000012394_G05000011693_G05000013138_F05000017542["Weicht die Anschrift von der Trägerans"] -.->|"<> wahr → hide"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799["Anschrift"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790["Anschrift in Deutschland"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → forbidden"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790["Anschrift in Deutschland"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G60000000191["Anschrift Ausland"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → forbidden"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G60000000191["Anschrift Ausland"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] ==>|"= 002 Postfach → required"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_G60000000087["Anschrift Postfach"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] -.->|"<> 002 Postfach → forbidden"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_G60000000087["Anschrift Postfach"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] ==>|"= 001 Straßenanschrift → required"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_G05000011743["Straßenanschrift Inland"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] -.->|"<> 001 Straßenanschrift → hide"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_G05000011743["Straßenanschrift Inland"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] ==>|"= 003 Großempfänger → required"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_G60000000208["Anschrift Inland Großempfänger"]
  G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_F05000017662["Welche Art der Anschrift möchten Sie a"] -.->|"<> 003 Großempfänger → forbidden"| G05000011692_G05000012394_G05000011693_G05000013138_G05000011799_G05000011790_G60000000208["Anschrift Inland Großempfänger"]
  G05000011687_F05000017530["Möchten Sie Adressangaben zu Nebengebä"] ==>|"= wahr → required"| G05000011687_G05000011689["Weitere Adressangabe"]
  G05000011687_F05000017530["Möchten Sie Adressangaben zu Nebengebä"] -.->|"<> wahr → hide"| G05000011687_G05000011689["Weitere Adressangabe"]
  G05000011691_G05000012369_F05000017536["Liegt eine Nutzungsgenehmigung für die"] ==>|"= Ja, Nutzungsgenehmigung lieg → required"| G05000011691_G05000012369_F05000017537["Nutzungsgenehmigung der zuständigen Ba"]
  G05000011691_G05000012369_F05000017536["Liegt eine Nutzungsgenehmigung für die"] -.->|"<> Ja, Nutzungsgenehmigung lieg → hide"| G05000011691_G05000012369_F05000017537["Nutzungsgenehmigung der zuständigen Ba"]
  G05000011691_G05000012369_F05000017536["Liegt eine Nutzungsgenehmigung für die"] ==>|"= Ja, die Bescheinigung über e → required"| G05000011691_G05000012369_F05000017538["Bescheinigung über eine erfolgte Schlu"]
  G05000011691_G05000012369_F05000017536["Liegt eine Nutzungsgenehmigung für die"] -.->|"<> Ja, die Bescheinigung über e → hide"| G05000011691_G05000012369_F05000017538["Bescheinigung über eine erfolgte Schlu"]
  G05000012375_G05000011716_F05000017585["Art der Gruppe"] ==>|"= Krippe → required"| G05000012375_G05000011716_F05000017589["Anzahl der Kinder pro Gruppe unter ein"]
  G05000012375_G05000011716_F05000017585["Art der Gruppe"] -.->|"<> Krippe → hide"| G05000012375_G05000011716_F05000017589["Anzahl der Kinder pro Gruppe unter ein"]
  G05000012375_G05000011716_F05000017587["Anzahl der Gruppen dieser Gruppenart"] ==>|"= ? → required"| G05000012375_G05000011716_F05000017531["Gebäudeart"]
  G05000012375_G05000011716_F05000017587["Anzahl der Gruppen dieser Gruppenart"] ==>|"? ? → required"| G05000012375_G05000011716_F05000017531["Gebäudeart"]
  G05000012375_G05000011720_F05000017601["Die Vereinssatzung oder der Nachweis ""] -.->|"= wird beigefügt. → hide+required"| G05000012375_G05000011720_F05000017676["Laden Sie den entsprechenden Nachweis "]
  G05000012375_G05000012384_F05000017603["Bei der anzugebenden Adresse der Kinde"] ==>|"= wahr → required"| G05000012375_G05000012384_G05000012385["Vorläufige Adresse / Projektadresse"]
  G05000012375_G05000012384_F05000017603["Bei der anzugebenden Adresse der Kinde"] -.->|"<> wahr → hide"| G05000012375_G05000012384_G05000012385["Vorläufige Adresse / Projektadresse"]
  G05000012375_G05000012387_F05000017604["Die Personalmeldung zu dem bei Ihnen b"] ==>|"= wird beigefügt. → required"| G05000012375_G05000012387_F05000017676["Laden Sie den entsprechenden Nachweis "]
  G05000012375_G05000012387_F05000017604["Die Personalmeldung zu dem bei Ihnen b"] ==>|"<> wird beigefügt. → required"| G05000012375_G05000012387_F05000017676["Laden Sie den entsprechenden Nachweis "]
  unclear0["?: Die Angabe in Feld F05000017607 "Anzahl Personen" bestimmt, "]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
