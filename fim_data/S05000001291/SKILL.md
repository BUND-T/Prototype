---
name: antrag-s05000001291
description: Führt Antragstellende durch „Antrag auf Erlaubnis zum Inverkehrbringen und zur Abgabe bestimmter Stoffe, Gemische und Erzeugnisse (§6 ChemVerbotsV)" (FIM S05000001291 3.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf Erlaubnis zum Inverkehrbringen und zur Abgabe bestimmter Stoffe, Gemische und Erzeugnisse (§6 ChemVerbotsV)

- **FIM-ID:** `S05000001291 3.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 6 (1-4) ChemVerbotsV vom 14.10.1993; § 13 VwVfG vom 8.08.2009; § 2 EGovG vom 1.07.20214; DVO (EU) 2024/197 vom 25.01.2024; § 8 HGB vom 27.12.2024; 11 (1) ChemVerbotsV vom 14.10.1993; § 23 VwVfG vom 8.08.2009; § 9 HGB vom 27.12.2024; § 10 HGB vom 27.12.2024; WiPG NRW vom 30.06.2020; WiPG-DVO vom 1.07.2020; Anlage 2 Eintrag 1 ChemVerbotsV vom 14.10.1993
- **Kompiliert:** 2026-08-13T15:41:38Z aus https://fimportal.de/api/v1/schemas/S05000001291/3.0.0/xdf
- **Umfang:** 66 Felder, 18 gesicherte Bedingungen, 4 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

## Felder

### Art des Antrags (`G05000011615`)

- **Möchten Sie die Erlaubnis uneingeschränkt für alle Produkte ODER eingeschränkt auf gewisse Produkte oder Produktkategorien beantragen?** (`F05000017409`) — Pflicht
  - Rechtsgrundlage: § 6 (4) ChemVerbotsV

### Art des Antrags › Produktangaben (`G05000011616`)

- **Hinweis:** (`F05000017410`) — optional
  - Rechtsgrundlage: Anlage 2 Eintrag 1 ChemVerbotsV
- **Produkte aus folgenden Produktkategorien, die der Anlage 2 Eintrag 1 ChemVerbotsV unterfallen, sollen abgegeben werden:** (`F05000017411`) — Pflicht
  - Rechtsgrundlage: Anlage 2 Eintrag 1 ChemVerbotsV
- **Hinweis:** (`F05000017413`) — optional
  - Rechtsgrundlage: Anlage 2 Eintrag 1 ChemVerbotsV
- **Benennen Sie die einzelnen Produkte:** (`F05000017414`) — Pflicht
  - Rechtsgrundlage: Anlage 2 Eintrag 1 ChemVerbotsV
- **Hinweis:** (`F05000017415`) — optional
  - Rechtsgrundlage: Anlage 2 Eintrag 1 ChemVerbotsV
- **Hier können Sie gerne die genannte Übersicht hochladen.** (`F05000017416`) — Pflicht
  - Rechtsgrundlage: Anlage 2 Eintrag 1 ChemVerbotsV

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Antragsteller › Betriebsangaben (Hauptsitz) (`G05000011544`)

- **Rechtsform** (`F60000000339`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Juristische Person.Rechtsform Version 1.1; verwendet verwendet urn:xoev-de:xunternehmen:codeliste:rechtsformen_2
- **Geschäftsbezeichnung** (`F60000000320`) — optional, conditional
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.
- **Eingetragener Name** (`F60000000319`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.1
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Namen mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Art der Eintragung oder des Registers** (`F60000000347`) — optional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Eintragung.Art der Eintragung Version 1.1; urn:xoev-de:xunternehmen:codeliste:artdereintragung_2
  - Hilfe: Geben Sie an, um welche Art von Eintrag es sich handelt.

### Antragsteller › Anschrift und Vertreter › Straßenanschrift Inland (`G05000012253`)

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

### Antragsteller › Anschrift und Vertreter › Gesetzlicher Vertreter JP (`G05000011770`)

- **Art des gesetzlichen Vertreters** (`F60000000375`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:codeliste:artgesetzlichervertreter

### Antragsteller › Anschrift und Vertreter › Gesetzlicher Vertreter JP › Name der geschäftsführenden / verantwortlichen Person (`G05000011769`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Antragsteller › Anschrift und Vertreter › Gesellschafter (`G05000011771`)

- **Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?** (`F05000018285`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Gesellschafterart** (`F60000000342`) — optional
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Gesellschafter.Art Version 1.1; verwendet urn:xoev-de:xunternehmen:codeliste:artgesellschafterpersonengesellschaft Version 1

### Antragsteller › Anschrift und Vertreter › Gesellschafter › Name der geschäftsführenden / verantwortlichen Person (`G05000011769`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Ansprechperson (`G05000011545`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.

### Ansprechperson › Erreichbarkeit (`G05000011747`)

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

### Betriebsstätte (`G05000011547`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Name der Betriebsstätte** (`F05000018375`) — Pflicht
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.
- **Befindet sich diese Betriebsstätte an anderer Adresse als der Hauptsitz?** (`F05000017315`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Betriebsstätte › Straßenanschrift Inland (`G05000012253`)

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

### Angaben Sachkundige Person (`G05000011617`)

- **Hinweis:** (`F05000017417`) — optional
  - Rechtsgrundlage: § 6 (2) ChemVerbotsV
- **Welcher Betriebsstätte/Filiale ist die sachkundige Person zuzuordnen?** (`F05000017419`) — Pflicht
  - Rechtsgrundlage: § 6 (2) ChemVerbotsV

### Angaben Sachkundige Person › Personenbezogene Angaben Sachkundige Person (`G05000011618`)

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

### Angaben Sachkundige Person › Personenbezogene Angaben Sachkundige Person › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben Sachkundige Person › Sachkundeinhalt (`G05000011622`)

- **Auswahl der Sachkunde** (`F05000017420`) — Pflicht
  - Rechtsgrundlage: § 6 (2) ChemVerbotsV; § 11 (3) ChemVerbotsV
- **Wählen Sie eine anderweitige Qualifikation nach § 11 Absatz 3 ChemVerbotsV aus.** (`F05000017421`) — optional, conditional
  - Rechtsgrundlage: § 11 (3) ChemVerbotsV
- **Spezifizieren Sie die eingeschränkte Sachkunde genauer.** (`F05000017422`) — optional, conditional
  - Rechtsgrundlage: § 11 (2) ChemVerbotsV

### Angaben Sachkundige Person › Nachweise der Sachkundigen Person (`G05000011625`)

- **Laden Sie hier für die genannte sachkundige Person ein Sachkundezeugnis nach §11 Absatz 1 ChemVerbotsV hoch.** (`F05000017423`) — optional, conditional
  - Rechtsgrundlage: § 6 (2) ChemVerbotsV
- **Laden Sie für die genannte sachkundige Person, für die eine Anerkennung bzw. ein Zeugnis nach Pflanzenschutz-Sachkundeverordnung nach §11 Absatz 2 ChemVerbotsV vorliegt, den Nachweis hier hoch.** (`F05000017424`) — optional, conditional
  - Rechtsgrundlage: § 6 (2) ChemVerbotsV
- **Laden Sie für die genannte sachkundige Person, bei der eine anderweitige Qualifikation nach §11 Absatz 3 ChemVerbotsV besteht, den Nachweis hier hoch.** (`F05000017425`) — optional, conditional
  - Rechtsgrundlage: § 6 (2) ChemVerbotsV
- **Laden Sie für die genannte sachkundige Person das aus EU-Staaten anerkannte Sachkundezeugnis / Nachweis über die Qualifikation nach §11 Absatz 4 ChemVerbotsV hoch.** (`F05000017426`) — optional, conditional
  - Rechtsgrundlage: § 6 (2) ChemVerbotsV
- **Laden Sie hier, falls erforderlich, für jede genannte sachkundige Person eine Teilnahmebescheinigung für die zuletzt besuchte vor längstens sechs Jahren durchgeführte eintägige oder vor längstens drei Jahren durchgeführte halbtägige Fortbildungsveranstaltung nach § 11 Abs. 2 ChemVerbotsV hoch.** (`F05000017429`) — Pflicht
  - Rechtsgrundlage: § 11 (2) ChemVerbotsV
- **Gewerbezentralregisterauszug** (`F05000017428`) — optional
  - Rechtsgrundlage: § 6 (2) S. 2 ChemVerbotsV
  - Hilfe: Laden Sie den vollständigen Gewerbezentralregisterauszug hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Gewerbezentralregisterauszug** (`F05000017652`) — optional
  - Rechtsgrundlage: § 6 (2) S. 2 ChemVerbotsV
  - Hilfe: Laden Sie den vollständigen Gewerbezentralregisterauszug hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Angaben Sachkundige Person › Nachweise der Sachkundigen Person › Bundeszentralregisterauszug (erweitertes Führungszeugnis) (`G05000011629`)

- **Hinweis für die juristische Person und Personengesellschaften:** (`F05000017433`) — optional
  - Rechtsgrundlage: § 6 (2) S. 2 ChemVerbotsV
- **Haben Sie einen Bundeszentralregisterauszug, d.h. ein Führungszeugnis zur Vorlage bei einer Behörde 
(Belegart O) beantragt?*** (`F05000017430`) — Pflicht
  - Rechtsgrundlage: § 6 (2) S. 2 ChemVerbotsV
- **Datum der Beantragung*** (`F05000017431`) — Pflicht, conditional
  - Rechtsgrundlage: § 6 (2) S. 2 ChemVerbotsV
- **Hinweis:** (`F05000017432`) — optional, conditional
  - Rechtsgrundlage: § 6 (2) S. 2 ChemVerbotsV

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Auswahl der Sachkunde" gleich einem beliebigen Wert ist | „Laden Sie hier für die genannte sachkundige Person ein Sachkundezeugnis nach §11 Absatz 1 ChemVerbotsV hoch." | muss ausgefüllt werden | — | `R05000012487` |
| wenn „Auswahl der Sachkunde" gleich einem beliebigen Wert ist | „Laden Sie für die genannte sachkundige Person, für die eine Anerkennung bzw. ein Zeugnis nach Pflanzenschutz-Sachkundeverordnung nach §11 Absatz 2 ChemVerbotsV vorliegt, den Nachweis hier hoch." | muss ausgefüllt werden | — | `R05000012488` |
| wenn „Auswahl der Sachkunde" gleich einem beliebigen Wert ist | „Laden Sie für die genannte sachkundige Person, bei der eine anderweitige Qualifikation nach §11 Absatz 3 ChemVerbotsV besteht, den Nachweis hier hoch." | muss ausgefüllt werden | — | `R05000012489` |
| wenn „Auswahl der Sachkunde" gleich einem beliebigen Wert ist | „Laden Sie für die genannte sachkundige Person das aus EU-Staaten anerkannte Sachkundezeugnis / Nachweis über die Qualifikation nach §11 Absatz 4 ChemVerbotsV hoch." | muss ausgefüllt werden | — | `R05000012490` |
| wenn „Möchten Sie die Erlaubnis uneingeschränkt für alle Produkte ODER eingeschränkt auf gewisse Produkte oder Produktkategorien beantragen?" gleich einem beliebigen Wert ist | „Produktangaben" | muss ausgefüllt werden | — | `R05000012316` |
| wenn „Betriebsangaben (Hauptsitz)" gleich einem beliebigen Wert ist | „Anschrift und Vertreter" | muss ausgefüllt werden | — | `R05000013430` |
| wenn „Betriebsangaben (Hauptsitz)" gleich einem beliebigen Wert ist | „Gesellschafter" | entfällt | — | `R05000013430` |
| wenn „Betriebsangaben (Hauptsitz)" gleich einem beliebigen Wert ist | „Anschrift und Vertreter" | muss ausgefüllt werden | — | `R05000013431` |
| wenn „Betriebsangaben (Hauptsitz)" gleich einem beliebigen Wert ist | „Gesetzlicher Vertreter JP" | entfällt | — | `R05000013431` |
| wenn „Eingetragener Name" gesetzt auf einem beliebigen Wert ist | „Geschäftsbezeichnung" | muss ausgefüllt werden | WiPG NRW; WiPG-DVO | `R05000012238` |
| wenn „Befindet sich diese Betriebsstätte an anderer Adresse als der Hauptsitz?" gleich „wahr" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011547` |
| wenn „Art der Niederlassung" ungleich „01" ist | _mehrere Felder_ | wird geprüft | — | `G05000011547` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Auswahl der Sachkunde" gleich „02" ist | „Spezifizieren Sie die eingeschränkte Sachkunde genauer." | muss ausgefüllt werden | — | `G05000011622` |
| wenn „Auswahl der Sachkunde" gleich „06" ist | „Wählen Sie eine anderweitige Qualifikation nach § 11 Absatz 3 ChemVerbotsV aus." | muss ausgefüllt werden | — | `G05000011622` |
| wenn „Haben Sie einen Bundeszentralregisterauszug, d.h. ein Führungszeugnis zur Vorlage bei einer Behörde 
(Belegart O) beantragt?*" gleich „01" ist | „Datum der Beantragung*" | muss ausgefüllt werden | — | `G05000011629` |
| wenn „Haben Sie einen Bundeszentralregisterauszug, d.h. ein Führungszeugnis zur Vorlage bei einer Behörde 
(Belegart O) beantragt?*" gleich „02" ist | „Hinweis:" | muss ausgefüllt werden | — | `G05000011629` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>WENN aus der Eingabe/ Auswahl in G05000011547 "Betriebsstätte (Giftstoffe)" ein oder mehrere Datensätze entstehen, DANN sind diese zusammengefasst als Datenpakete (mit Auswahlmöglichkeit, falls in G05000011547 "Betriebsstätte (Giftstoffe)" mehrere Betriebsstätten angelegt wurden) in F05000017419 'Betriebsstättenauswahl' anzuzeigen.</mark> — Regel `R05000012617`
- <mark>Im Datenfeld F05000018286 "Art des Antragstellers" muss die Auswahl 002=geschäftlich als Vorbefüllung gewählt sein UND diese Datenfeld soll nicht angezeigt werden.</mark> — Regel `R05000013422`
- <mark>WENN in F60000000319 "Eingetragener Name / Organisationsname" ein Eintrag vorgenommen wurde, DANN ist F60000000320 "Geschäftsbezeichnung / Organisationsbezeichnung" ein optionales Feld.</mark> — Regel `R05000012238`
- <mark>Im Datenfeld F05000018285 "Art Person Gesellschafter" muss die Auswahl 001=Natürliche Person als Vorbefüllung gewählt sein UND diese Datenfeld soll nicht angezeigt werden.</mark> — Regel `R05000013424`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000011617_G05000011622_F05000017420["Auswahl der Sachkunde"] ==>|"= ? → required"| G05000011617_G05000011625_F05000017423["Laden Sie hier für die genannte sachku"]
  G05000011617_G05000011622_F05000017420["Auswahl der Sachkunde"] ==>|"= ? → required"| G05000011617_G05000011625_F05000017424["Laden Sie für die genannte sachkundige"]
  G05000011617_G05000011622_F05000017420["Auswahl der Sachkunde"] ==>|"= ? → required"| G05000011617_G05000011625_F05000017425["Laden Sie für die genannte sachkundige"]
  G05000011617_G05000011622_F05000017420["Auswahl der Sachkunde"] ==>|"= ? → required"| G05000011617_G05000011625_F05000017426["Laden Sie für die genannte sachkundige"]
  G05000011615_F05000017409["Möchten Sie die Erlaubnis uneingeschrä"] ==>|"= ? → required"| G05000011615_G05000011616["Produktangaben"]
  G05000011765_G05000011544["Betriebsangaben (Hauptsitz)"] ==>|"= ? → required"| G05000011765_G05000011768["Anschrift und Vertreter"]
  G05000011765_G05000011544["Betriebsangaben (Hauptsitz)"] -.->|"= ? → hide"| G05000011765_G05000011768_G05000011771["Gesellschafter"]
  G05000011765_G05000011544["Betriebsangaben (Hauptsitz)"] ==>|"= ? → required"| G05000011765_G05000011768["Anschrift und Vertreter"]
  G05000011765_G05000011544["Betriebsangaben (Hauptsitz)"] -.->|"= ? → hide"| G05000011765_G05000011768_G05000011770["Gesetzlicher Vertreter JP"]
  G05000011765_G05000011544_F60000000319["Eingetragener Name"] ==>|"? ? → required"| G05000011765_G05000011544_F60000000320["Geschäftsbezeichnung"]
  G05000011547_F05000017315["Befindet sich diese Betriebsstätte an "] ==>|"= wahr → required"| G05000011547_G05000012253["Straßenanschrift Inland"]
  G05000011617_G05000011618_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000011617_G05000011618_G60000000083_F60000000232["Monat"]
  G05000011617_G05000011622_F05000017420["Auswahl der Sachkunde"] ==>|"= 02 → required"| G05000011617_G05000011622_F05000017422["Spezifizieren Sie die eingeschränkte S"]
  G05000011617_G05000011622_F05000017420["Auswahl der Sachkunde"] ==>|"= 06 → required"| G05000011617_G05000011622_F05000017421["Wählen Sie eine anderweitige Qualifika"]
  G05000011617_G05000011625_G05000011629_F05000017430["Haben Sie einen Bundeszentralregistera"] ==>|"= 01 → required"| G05000011617_G05000011625_G05000011629_F05000017431["Datum der Beantragung*"]
  G05000011617_G05000011625_G05000011629_F05000017430["Haben Sie einen Bundeszentralregistera"] ==>|"= 02 → required"| G05000011617_G05000011625_G05000011629_F05000017432["Hinweis:"]
  unclear0["?: WENN aus der Eingabe/ Auswahl in G05000011547 "Betriebsstätt"]:::unclear
  unclear1["?: Im Datenfeld F05000018286 "Art des Antragstellers" muss die "]:::unclear
  unclear2["?: WENN in F60000000319 "Eingetragener Name / Organisationsname"]:::unclear
  unclear3["?: Im Datenfeld F05000018285 "Art Person Gesellschafter" muss d"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
