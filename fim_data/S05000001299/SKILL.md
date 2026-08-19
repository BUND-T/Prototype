---
name: antrag-s05000001299
description: Führt Antragstellende durch „Antrag auf Erlaubnis zur Kindertagespflege" (FIM S05000001299 1.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf Erlaubnis zur Kindertagespflege

- **FIM-ID:** `S05000001299 1.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 43 SGB VIII vom 03.04.2025; § 43 (2) Nr. 1 SGB VIII vom 03.04.2025; § 43 (2) Nr. 2 SGB VIII vom 03.04.2025; § 20 (8) Nr 1 IfSG vom 03.04.2025; § 33 Nr. 2 IfSG vom 12.12.2023; § 22 SGB VIII vom 03.04.2025; § 20 (8) Nr. 1 IfSG vom 12.12.2023
- **Kompiliert:** 2026-08-13T15:43:49Z aus https://fimportal.de/api/v1/schemas/S05000001299/1.0.0/xdf
- **Umfang:** 82 Felder, 22 gesicherte Bedingungen, 5 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet werden (Rechtsgrundlage stimmt nicht überein (D99000001951)). Zu Fristen, Kosten, Unterlagen und Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle verweisen.

## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Worum handelt es sich bei diesem Antrag?** (`F05000017543`) — Pflicht
  - Rechtsgrundlage: § 43 SGB VIII
- **Planen Sie eine Kindertagespflege mit einer anderen Kindertagespflegeperson?** (`F05000017549`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB VIII; § 22 (1) SGB VIII
- **Ist Ihnen diese Person bereits bekannt?** (`F05000017550`) — Pflicht, conditional
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB; § 22 (1) SGB 8

### Angaben zur Kindertagespflegeperson (`G05000011684`)

- **Geschlecht** (`F60000000332`) — optional
  - Rechtsgrundlage: XPersonenstand:Code.Geschlecht Version 1.7.5; basierend auf DSMeld.Code.Geschlecht urn:de:dsmeld:schluesseltabelle:geschlecht Version 3
  - Hilfe: Geben Sie das Geschlecht an, das auch beim Personenstandsregister oder Standesamt hinterlegt ist.
- **Familienstand** (`F60000000275`) — Pflicht
  - Rechtsgrundlage: urn:de:dsmeld:schluesseltabelle:familienstand_2; XMeld.type.Familienstand Version 2.4.4
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

### Angaben zur Kindertagespflegeperson › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zur Kindertagespflegeperson › Anschrift in Deutschland (`G05000013144`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zur Kindertagespflegeperson › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zur Kindertagespflegeperson › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Angaben zur Kindertagespflegeperson › Erreichbarkeit (`G05000011747`)

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

### Angaben zur Kindertagespflegeperson › Qualifikation (`G05000011703`)

- **Art der Qualifikation** (`F05000017554`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Dies kann bspw. die Grundqualifikation nach dem Qualifizierungshandbuch, staatlich anerkannte Erzieherin oder  staatlich anerkannter Erzieher umfassen.
- **Umfang der Qualifikation** (`F05000017555`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Geben Sie den zeitlichen Umfang (Unterrichtsstunden, Unterrichtseinheiten, Tagen, Wochen) der Qualifikation ein.
- **Höchster allgemeinbildender Schulabschluss** (`F05000017556`) — optional
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
- **Höchster beruflicher Ausbildungs- und Hochschulabschluss** (`F05000017557`) — optional
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII

### Angaben zur Kindertagespflegeperson › Qualifikation › Weitere Qualifikation (`G05000011707`)

- **Art der Qualifikation** (`F05000017554`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Dies kann bspw. die Grundqualifikation nach dem Qualifizierungshandbuch, staatlich anerkannte Erzieherin oder  staatlich anerkannter Erzieher umfassen.
- **Umfang der Qualifikation** (`F05000017555`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Geben Sie den zeitlichen Umfang (Unterrichtsstunden, Unterrichtseinheiten, Tagen, Wochen) der Qualifikation ein.

### Angaben der weiteren Kindertagespflegeperson (`G05000011701`)

- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.

### Angaben der weiteren Kindertagespflegeperson › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben der Kindertagespflegestelle (`G05000011697`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Ist die Adresse der Kindertagespflegestelle identisch zur Wohnanschrift der Kindertagespflegeperson?** (`F05000017544`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB VIII
- **Name der Kindertagestpflege** (`F05000017545`) — Pflicht, conditional
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB VIII

### Angaben der Kindertagespflegestelle › Straßenanschrift Inland (`G05000012613`)

- **Adresssuche** (`F05000017636`) — Pflicht
  - Rechtsgrundlage: referenzbasiert
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — Pflicht
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

### Angaben der Kindertagespflegestelle › Räumlichkeiten (`G05000011700`)

- **Beschreiben Sie die Räumlichkeiten, in denen die Kinderbetreuung stattfinden soll.** (`F05000017546`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB VIII; § 22 (1) SGB VIII
- **Geben Sie den Ort ein, an dem die Kindertagespflege stattfinden soll:** (`F05000017547`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB VIII; § 22 (1) SGB VIII
- **Angabe zur Größe der Räumlichkeiten:** (`F05000017548`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB VIII; § 22 (1) SGB VIII

### Angaben der Kindertagespflegestelle › Kinder und weitere Haushaltangehörige (`G05000011702`)

- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.

### Angaben der Kindertagespflegestelle › Kinder und weitere Haushaltangehörige › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Nachweise (`G05000011696`)

- **Nachweis über die erforderliche Qualifikation als Kindertagespflegeperson** (`F05000017558`) — optional
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Laden Sie an dieser Stelle den Qualifikationsnachweis hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Ärztliche Unbedenklichkeitsbescheinigung** (`F05000017559`) — optional
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Laden Sie an dieser Stelle Ihre ärztliche Unbedenklichkeitsbescheinigung hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Lebenslauf** (`F05000017561`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Laden Sie an dieser Stelle Ihren Lebenslauf hoch, der nachvollziehbar Ihre Befähigung zur Ausübung der Kindertagespflege darlegt.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Nachweise über die erfolgreiche Teilnahme an den Qualifikationskursen des QHB (Zertifikat des Bundesverbands für Kindertagespflege) oder vergleichbare Qualifikation.** (`F05000017562`) — optional
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Laden Sie hier Ihre Bildungsnachweise hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Aktueller Nachweis "Erste Hilfe bei Säuglingen und Kleinkindern"** (`F05000017563`) — Pflicht
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Laden Sie an dieser Stelle Ihren aktuellen Nachweis "Erste Hilfe bei Säuglingen und Kleinkindern" hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Hygieneschulung** (`F05000017564`) — optional
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Laden Sie an dieser Stelle Nachweis über die absolvierten Hygieneschulungen hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Pädagogische Konzeption** (`F05000017565`) — optional
  - Rechtsgrundlage: § 43 (2) Nr. 1 SGB VIII
  - Hilfe: Laden Sie an dieser Stelle Ihre pädagogische Konzeption hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Mietvertrag** (`F05000017566`) — optional, conditional
  - Rechtsgrundlage: § 43 (2) Nr. 2 SGB VIII
  - Hilfe: Laden Sie an dieser Stelle den Mietvertrag oder andere Dokumente, die die Nutzungsberechtigung belegen, hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: leer, da Referenzkontext
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Immunität gegen Masern (`G05000012392`)

- **Hinweis:** (`F05000018445`) — optional
  - Rechtsgrundlage: § 20 (8) Nr 1 IfSG; § 33 Nr 2 IfSG
- **Immunität gegen Masern** (`F05000007322`) — Pflicht
  - Rechtsgrundlage: §43 SGB VIII; §22 KiBiz
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika (`G05000011712`)

- **Aktuelle Haushaltsbescheinigung** (`F05000017577`) — Pflicht, conditional
  - Rechtsgrundlage: § 45 SGB 8
  - Hilfe: Laden Sie eine aktuelle Haushaltsbescheinigung hoch.
- **Sprachzertifikat** (`F05000017578`) — optional
  - Rechtsgrundlage: § 45 SGB VIII
  - Hilfe: Laden Sie bei Bedarf das Sprachzertifikat hoch.
- **Strafverfahren** (`F05000017579`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
  - Hilfe: Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder per Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen Sie oder andere Mitglieder ihres Haushaltes, in dem Sie betreuen werden?
- **Strafverfahren Angabe** (`F05000017580`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
  - Hilfe: Geben Sie das Aktenzeichen des/der Verfahren(s) sowie die zuständige Behörde an.

### Landesspezifika › Bundeszentralregisterauszug der Haushaltsangehörigen über 14 Jahren (erweitertes Führungszeugnis gem. § 30 a BZRG) (`G05000000855`)

- **Haben Sie einen Bundeszentralregisterauszug, d.h. ein erweitertes Führungszeugnis zur Vorlage bei einer Behörde (Belegart OE) beantragt?** (`F05000017616`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
- **Datum der Beantragung** (`F05000017617`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
- **Datum der geplanten Beantragung** (`F05000017618`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
- **Vollständiger Name der haushaltsangehörigen Person** (`F05000017619`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8

### Landesspezifika › Bundeszentralregisterauszug des oder der Antragstellenden (polizeiliches Führungszeugnis) (`G05000000998`)

- **Haben Sie einen Bundeszentralregisterauszug, d.h. ein erweitertes Führungszeugnis zur Vorlage bei einer Behörde (Belegart OE) beantragt?** (`F05000017616`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
- **Datum der Beantragung** (`F05000017617`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
- **Datum der geplanten Beantragung** (`F05000017618`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8
- **Vollständiger Name der haushaltsangehörigen Person** (`F05000017619`) — Pflicht
  - Rechtsgrundlage: § 45 SGB 8

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Geben Sie den Ort ein, an dem die Kindertagespflege stattfinden soll:" gleich einem beliebigen Wert ist | „Mietvertrag" | muss ausgefüllt werden | — | `R05000012460` |
| wenn „Geben Sie den Ort ein, an dem die Kindertagespflege stattfinden soll:" gleich einem beliebigen Wert ist | „Kinder und weitere Haushaltangehörige" | muss ausgefüllt werden | — | `R05000012461` |
| wenn „Geben Sie den Ort ein, an dem die Kindertagespflege stattfinden soll:" gleich einem beliebigen Wert ist | „Aktuelle Haushaltsbescheinigung" | muss ausgefüllt werden | — | `R05000012464` |
| wenn „Geben Sie den Ort ein, an dem die Kindertagespflege stattfinden soll:" gleich einem beliebigen Wert ist | „Bundeszentralregisterauszug der Haushaltsangehörigen über 14 Jahren (erweitertes Führungszeugnis gem. § 30 a BZRG)" | muss ausgefüllt werden | — | `R05000012465` |
| wenn „Planen Sie eine Kindertagespflege mit einer anderen Kindertagespflegeperson?" gleich „wahr" ist | „Ist Ihnen diese Person bereits bekannt?" | muss ausgefüllt werden | — | `R05000013518` |
| wenn „Ist Ihnen diese Person bereits bekannt?" gleich „wahr" ist | „Angaben der weiteren Kindertagespflegeperson" | muss ausgefüllt werden | — | `R05000013519` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000013144` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" ungleich „001" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000013144` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000013144` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" ungleich „002" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000013144` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Ist die Adresse der Kindertagespflegestelle identisch zur Wohnanschrift der Kindertagespflegeperson?" gleich „falsch" ist | „Name der Kindertagestpflege" | muss ausgefüllt werden | — | `R05000012431` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Wenn in F05000017579 "Strafverfahren" = Auswahl 01 "ja, dann erscheint F05000017580 "Strafverfahren Angabe"</mark> — Regel `R05000012442`
- <mark>Wenn in F05000017616 Auswahl = 01 "Ist beantragt", dann erscheint F05000017617 "Datum der Beantragung" und muss befüllt werden</mark> — Regel `R05000012467`
- <mark>Wenn in F05000017616 Auswahl = 02 "Ist noch nicht beantragt", dann erscheint F05000017618 "Datum der geplanten Beantragung" und muss ausgefüllt werden.</mark> — Regel `R05000012468`
- <mark>Wenn in F05000017616 Auswahl = 01 "Ist beantragt", dann erscheint F05000017617 "Datum der Beantragung" und muss befüllt werden</mark> — Regel `R05000012471`
- <mark>Wenn in F05000017616 Auswahl = 02 "Ist noch nicht beantragt", dann erscheint F05000017618 "Datum der geplanten Beantragung" und muss ausgefüllt werden.</mark> — Regel `R05000012472`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000011697_G05000011700_F05000017547["Geben Sie den Ort ein, an dem die Kind"] ==>|"= ? → required"| G05000011696_F05000017566["Mietvertrag"]
  G05000011697_G05000011700_F05000017547["Geben Sie den Ort ein, an dem die Kind"] ==>|"= ? → required"| G05000011697_G05000011702["Kinder und weitere Haushaltangehörige"]
  G05000011697_G05000011700_F05000017547["Geben Sie den Ort ein, an dem die Kind"] ==>|"= ? → required"| G05000011712_F05000017577["Aktuelle Haushaltsbescheinigung"]
  G05000011697_G05000011700_F05000017547["Geben Sie den Ort ein, an dem die Kind"] ==>|"= ? → required"| G05000011712_G05000000855["Bundeszentralregisterauszug der Hausha"]
  F05000017549["Planen Sie eine Kindertagespflege mit "] ==>|"= wahr → required"| F05000017550["Ist Ihnen diese Person bereits bekannt"]
  F05000017550["Ist Ihnen diese Person bereits bekannt"] ==>|"= wahr → required"| G05000011701["Angaben der weiteren Kindertagespflege"]
  G05000011684_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011684_G60000000083_F60000000232["Monat"]
  G05000011684_G05000013144_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000011684_G05000013144_G05000011743["Straßenanschrift Inland"]
  G05000011684_G05000013144_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"<> 001 → forbidden"| G05000011684_G05000013144_G05000011743["Straßenanschrift Inland"]
  G05000011684_G05000013144_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000011684_G05000013144_G60000000087["Anschrift Postfach"]
  G05000011684_G05000013144_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"<> 002 → forbidden"| G05000011684_G05000013144_G60000000087["Anschrift Postfach"]
  G05000011701_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011701_G60000000083_F60000000232["Monat"]
  G05000011697_F05000017544["Ist die Adresse der Kindertagespfleges"] ==>|"= falsch → required"| G05000011697_F05000017545["Name der Kindertagestpflege"]
  G05000011697_G05000011702_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011697_G05000011702_G60000000083_F60000000232["Monat"]
  unclear0["?: Wenn in F05000017579 "Strafverfahren" = Auswahl 01 "ja, dann"]:::unclear
  unclear1["?: Wenn in F05000017616 Auswahl = 01 "Ist beantragt", dann ersc"]:::unclear
  unclear2["?: Wenn in F05000017616 Auswahl = 02 "Ist noch nicht beantragt""]:::unclear
  unclear3["?: Wenn in F05000017616 Auswahl = 01 "Ist beantragt", dann ersc"]:::unclear
  unclear4["?: Wenn in F05000017616 Auswahl = 02 "Ist noch nicht beantragt""]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
