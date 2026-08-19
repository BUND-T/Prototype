---
name: antrag-s05000001310
description: Führt Antragstellende durch „Antrag auf eine Gemeinschaftslizenz oder Erlaubnisurkunde für den gewerblichen Güterkraftverkehr" (FIM S05000001310 2.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf eine Gemeinschaftslizenz oder Erlaubnisurkunde für den gewerblichen Güterkraftverkehr

- **FIM-ID:** `S05000001310 2.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 3 GBZugV vom 11.4.2024; § 5 (7) GBZugV vom 11.4.2024; § 10 GBZugV vom 11.4.2024; § 3 GüKG vom 15.7.2024; Nr. 17 GüKVwV vom 09.11.2012; Art. 5 VO (EG) 1071/2009; Art. 4 VO (EG) NR. 1072/2009; Art. 4 (3) VO (EG) Nr. 1072/2009; Art. 4 (2c) VO (EG) Nr. 1071/2009; § 26 (2) InsO; § 882b ZPO
- **Kompiliert:** 2026-08-13T15:46:07Z aus https://fimportal.de/api/v1/schemas/S05000001310/2.0.0/xdf
- **Umfang:** 291 Felder, 159 gesicherte Bedingungen, 44 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

## Antworten zur Leistung

_Quelle: LeiKa 99055031012000, bundesweiter Stammtext · Zuordnung geprüft über § 10, 3, 5 · gbzugv, gükg._


## Felder

### Art der Transportgenehmigung › Art der Transportgenehmigung (`G05000012015`)

- **Beantragen Sie eine Gemeinschaftslizenz nach Art. 4 VO (EG) NR. 1072/2009?** (`F05000017742`) — optional
  - Rechtsgrundlage: § 3 (3) GüKG; Art. 4 VO (EG) NR. 1072/2009
- **Beantragen Sie eine Erlaubnis für den gewerblichen Güterkraftverkehr nach § 3 Abs. 1 GüKG?** (`F05000017743`) — optional
  - Rechtsgrundlage: § 3 (1) GüKG

### Art der Transportgenehmigung › Anzahl der Fahrzeuge (`G05000011890`)

- **Anzahl der Fahrzeuge mit einer zulässigen Gesamtmasse zwischen 2,5 t und 3,5 t, die im gewerblichen Güterkraftverkehr eingesetzt werden.** (`F05000017745`) — Pflicht
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 8 GBZugV
- **Anzahl der Fahrzeuge mit einer zulässigen Gesamtmasse über 3,5 t, die im gewerblichen Güterkraftverkehr eingesetzt werden.** (`F05000017746`) — Pflicht
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 8 GBZugV

### Art der Transportgenehmigung (`G05000011888`)

- **Haben Sie ein bestehendes Gewerbe?** (`F05000017747`) — Pflicht
  - Rechtsgrundlage: § 3 GüKG; Art. 4 VO (EG) NR. 1072/2009; § 10 (1) GBZugV _(geerbt)_
- **Anzahl der beglaubigten Kopien / Ausfertigungen, die beantragt werden** (`F05000017748`) — Pflicht
  - Rechtsgrundlage: § 3 (3) GüKG; § 10 (1) S. 1 Nr. 7 GBZugV

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Wollen Sie eine weitere Niederlassungen angeben?** (`F05000017753`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV vom 11.4.2024; § 5 (7) GBZugV vom 11.4.2024; § 10 GBZugV vom 11.4.2024; § 3 GüKG vom 15.7.2024; Nr. 17 GüKVwV vom 09.11.2012; Art. 5 VO (EG) 1071/2009; Art. 4 VO (EG) NR. 1072/2009; Art. 4 (3) VO (EG) Nr. 1072/2009; Art. 4 (2c) VO (EG) Nr. 1071/2009; § 26 (2) InsO; § 882b ZPO _(geerbt)_

### Angaben zum Unternehmen › Betriebsangaben (`G05000013185`)

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

### Angaben zum Unternehmen › Ansprechperson (`G05000013186`)

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
  - Rechtsgrundlage: § 8a HGB; § 705 BGB; § 8b HGB; § 706 BGB; § 707 BGB

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesetzlicher Vertreter JP › Natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1; referenzbasiert; § 69 GewO; XInneres.Meldeanschrift.postleitzahl Version 8 _(geerbt)_
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
  - Rechtsgrundlage: § 8a HGB; § 705 BGB; § 8b HGB; § 706 BGB; § 707 BGB

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Nicht Natürliche Person › Gesellschafter › Natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1; referenzbasiert; § 69 GewO; XInneres.Meldeanschrift.postleitzahl Version 8 _(geerbt)_
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
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1; referenzbasiert; § 69 GewO; XInneres.Meldeanschrift.postleitzahl Version 8 _(geerbt)_
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

### Verkehrsleitung (`G05000011906`)

- **Ist eine zuvor erfasste Person Verkehrsleitung?** (`F05000017755`) — Pflicht
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 6 GBZugV
- **Welche Person ist als Verkehrsleiterin oder Verkehrsleiter tätig?** (`F05000017809`) — optional, conditional
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 6 GBZugV

### Verkehrsleitung › Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters (`G05000011908`)

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

### Verkehrsleitung › Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Verkehrsleitung › Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Verkehrsleitung › Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Verkehrsleitung › Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Verkehrsleitung › Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Verkehrsleitung › Kommunikation (`G05000011748`)

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

### Verkehrsleitung › Angaben zur Beschäftigung › Angaben zur fachlichen Eignung (`G05000011939`)

- **Nummer der Bescheinigung der fachlichen Eignung** (`F05000017757`) — Pflicht
  - Rechtsgrundlage: § 5 (7) GBZugV; § 10 GBZugV; § 4 VO (EG) Nr. 1071/2009 _(geerbt)_
- **Ausstellender Staat** (`F05000017758`) — Pflicht
  - Rechtsgrundlage: § 5 (7) GBZugV; § 10 GBZugV; § 4 VO (EG) Nr. 1071/2009 _(geerbt)_
- **Ausstellungsdatum** (`F60000000294`) — Pflicht
  - Rechtsgrundlage: § 5 (7) GBZugV; § 10 GBZugV; § 4 VO (EG) Nr. 1071/2009 _(geerbt)_
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.

### Verkehrsleitung › Angaben zur Beschäftigung › Angaben zur Beschäftigung im Unternehmen (`G05000011940`)

- **Stellung im Unternehmen** (`F05000017759`) — Pflicht
  - Rechtsgrundlage: § 10 GBZugV; § 4 (1) VO (EG) Nr. 1071/2009; § 4 (2) VO (EG) Nr. 1071/2009 _(geerbt)_
- **Die Verkehrsleitung ist** (`F05000017760`) — Pflicht
  - Rechtsgrundlage: § 10 GBZugV; § 4 (1) VO (EG) Nr. 1071/2009; § 4 (2) VO (EG) Nr. 1071/2009

### Verkehrsleitung › Angaben zur Beschäftigung › Tätigkeit in weiteren Unternehmen (`G05000011941`)

- **Ist die Verkehrsleitung in weiteren Unternehmen als Verkehrsleiterin oder Verkehrsleiter tätig?** (`F05000017761`) — Pflicht
  - Rechtsgrundlage: § 10 (2) S. 1, Nr. 2e GBZugV
- **Regelmäßige wöchentliche Arbeitszeit in Stunden** (`F05000017766`) — optional, conditional
  - Rechtsgrundlage: § 10 (2) S. 1 Nr. 2e GBZugV _(geerbt)_

### Verkehrsleitung › Angaben zur Beschäftigung › Tätigkeit in weiteren Unternehmen › Angaben zur Tätigkeit in weiteren Unternehmen (`G05000011942`)

- **Name des Unternehmens** (`F05000017763`) — Pflicht
  - Rechtsgrundlage: § 10 (2) S. 1 Nr. 2e GBZugV _(geerbt)_
- **Anzahl der Fahrzeuge oder Abschriften** (`F05000017764`) — Pflicht
  - Rechtsgrundlage: § 10 (2) S. 1 Nr. 2e GBZugV

### Angaben zur Niederlassung (`G05000011895`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Hinweis:** (`F05000017750`) — optional
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 5 GBZugV; Art. 5 VO (EG) 1071/2009
- **Haben Sie eine Niederlassung im Sinne von Art. 5 (EG) Nr. 1071/2009?** (`F05000017751`) — Pflicht
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 5 GBZugV; Art. 5 VO (EG) 1071/2009
- **Entspricht die Niederlassung der vorher erfassten Geschäftsanschrift?** (`F05000017752`) — optional
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 5 GBZugV; Art. 5 VO (EG) 1071/2009 _(geerbt)_

### Angaben zur Niederlassung › Anschrift in Deutschland (`G05000013423`)

- **Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?** (`F05000017637`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zur Niederlassung › Anschrift in Deutschland › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zur Niederlassung › Anschrift in Deutschland › Anschrift Postfach (`G60000000087`)

- **Postfach** (`F60000000249`) — optional
  - Rechtsgrundlage: XInneres.PostalischeInlandsanschrift.postfach Version 8
  - Hilfe: Geben Sie die Nummer oder Zeichenkette des Postfachs an. Das wird manchmal Postfachnummer genannt.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.

### Nachweise › Gewerbeanmeldung (`G05000011911`)

- **Die Gewerbeanmeldung** (`F05000017767`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Laden Sie die Gewerbeanmeldung hoch.** (`F05000017768`) — optional, conditional
  - Rechtsgrundlage: § 3 GBZugV; § 10 GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister (`G05000011938`)

- **Ein aktueller Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister** (`F05000017813`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Fügen Sie einen aktuellen Registerauszug bei.** (`F05000017521`) — optional, conditional
  - Rechtsgrundlage: § 3 GBZugV; § 10 GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Gesellschaftsvertrag/Satzung (`G05000011883`)

- **Der Gesellschaftsvertrag oder die Satzung** (`F05000017741`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 3 GBZugV; § 10 GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise (`G05000011910`)

- **Laden Sie eine Kopie des Personalausweises oder eine Kopie des Aufenthaltstitels (für Personen, die keine EU-Staatsangehörigkeit besitzen) hoch. Dieser Nachweis ist für alle verantwortlichen Personen zu erbringen.** (`F05000017769`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie eine Fahrzeugliste hoch.** (`F05000017770`) — optional
  - Rechtsgrundlage: § 10 (1) S. 1 Nr. 8 GBZugV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: leer, da Referenzkontext
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Verkehrsleitung (`G05000011912`)

- **Hinweis:** (`F05000017811`) — optional
  - Rechtsgrundlage: § 10 (2) GBZugV; § 10 (5) GBZugV
- **Laden Sie einen Nachweis über die fachliche Eignung (IHK-Bescheinigung) oder einen Nachweis über eine gleichwertige, anerkannte Abschlussprüfung hoch. Alternativ können Sie auch einen Nachweis über eine leitende Tätigkeit in einem Güterkraftverkehrsunternehmen von mindestens zehn Jahren hochladen.** (`F05000017771`) — Pflicht
  - Rechtsgrundlage: § 10 (2) S. 1 Nr. 2c GBZugV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie eine Kopie des Personalausweises oder eine Kopie des Aufenthaltstitels (für Personen, die keine EU-Staatsangehörigkeit besitzen) hoch. Dieser Nachweis ist für alle verantwortlichen Personen zu erbringen.** (`F05000017812`) — Pflicht
  - Rechtsgrundlage: § 10 (2) S. 1 Nr. 2 GBZugV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Arbeitsvertrag oder Geschäftsbesorgungsvertrag** (`F05000017772`) — optional, conditional
  - Rechtsgrundlage: § 10 (2) Nr. 2d GBZugV; Art. 4 (1) VO (EG) Nr. 1071/2009
  - Hilfe: Laden Sie den Arbeitsvertrag oder den Geschäftsbesorgungsvertrag hoch. Dieser dient als Nachweis der arbeitsvertraglichen oder gesellschaftsrechtlichen Bindung. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Geschäftsbesorgungsvertrag** (`F05000017773`) — optional, conditional
  - Rechtsgrundlage: § 10 (2) Nr. 2e GBZugV; Art. 4 (2) VO (EG) Nr. 1071/2009
  - Hilfe: Laden Sie den Geschäftsbesorgungsvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Gewerbeanmeldung der externen Verkehrsleitung** (`F05000017774`) — optional, conditional
  - Rechtsgrundlage: § 10 (2) Nr. 2e GBZugV; Art. 4 (2) VO (EG) Nr. 1071/2009
  - Hilfe: Laden Sie die Gewerbeanmeldung der externen Verkehrsleitung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Zuverlässigkeit (`G05000011913`)

- **Hinweis:** (`F05000017775`) — optional
  - Rechtsgrundlage: § 10 (2) Nr. 1c GBZugV; § 10 (2) Nr. 2a GBZugV; § 10 (2) Nr. 2b GBZugV; § 10 (5) GBZugV; § 26 (2) InsO; § 882b ZPO

### Nachweise › Angaben zur Zuverlässigkeit › Auskunft Fahreignungsregister (`G05000011914`)

- **Die Auskunft aus dem Fahreignungsregister wird** (`F05000017776`) — Pflicht
  - Rechtsgrundlage: § 10 (2) S. 1 Nr. 1b GBZugV; § 10 (2) S. 1 Nr. 2b GBZugV; § 10 (2) S. 2-3 GBZugV
- **Laden Sie eine Auskunft aus dem Fahreignungsregister des Kraftfahrt-Bundesamtes (KBA) Flensburg hoch. Diese darf nicht älter als drei Monate sein.** (`F05000017777`) — optional, conditional
  - Rechtsgrundlage: § 10 (2) S. 1 Nr. 1b GBZugV; § 10 (2) S. 1 Nr. 2b GBZugV; § 10 (2) S. 2-3 GBZugV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Zuverlässigkeit › Auskunft Fahreignungsregister › Name der zu überprüfenden Person (`G05000011944`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Nachweise › Angaben zur Zuverlässigkeit › Bundeszentralregisterauszug › Name der zu überprüfenden Person (`G05000011944`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Nachweise › Angaben zur Zuverlässigkeit › Bundeszentralregisterauszug › Auszug aus dem Bundeszentralregister / Führungszeugnis (`G05000011878`)

- **Hinweis zum Bundeszentralregisterauszug (Belegart O):** (`F05000017730`) — optional
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Die Auskunft aus dem Bundeszentralregister** (`F05000017692`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Nachweise › Angaben zur Zuverlässigkeit › Eigenkapitalbescheinigung (`G05000011917`)

- **Hinweis:** (`F05000017778`) — optional
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Das Dokument** (`F05000017780`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Zuverlässigkeit › Zusatzbescheinigung zum Nachweis der finanziellen Leistungsfähigkeit (`G05000011921`)

- **Hinweis:** (`F05000017783`) — optional
  - Rechtsgrundlage: Art. 4 (3) Verordnung (EG) Nr. 1072/2009; Nr. 17 GüKVwV; § 3 Abs 3 GüKG
- **Das Dokument** (`F05000017780`) — Pflicht
  - Rechtsgrundlage: § 3 (3) GüKG; Art. 4 (3) Verordnung (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 3 (3) GüKG; Art. 4 (3) Verordnung (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Zuverlässigkeit › Bescheinigung in Steuersachen des Finanzamtes (`G05000011945`)

- **Liegt Ihnen eine Bescheinigung in Steuersachen des Finanzamtes vor, die Ihre Unbedenklichkeit bestätigt? Diese darf nicht älter als drei Monate sein.** (`F05000017814`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Zuverlässigkeit › Unbedenklichkeitsbescheinigung der Krankenkasse (`G05000011923`)

- **Hinweis:** (`F05000017798`) — optional
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Eine Unbedenklichkeitsbescheinigung der Krankenkasse** (`F05000017799`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
- **Laden Sie die Unbedenklichkeitsbescheinigung der Krankenkasse hoch. Diese darf nicht älter als drei Monate sein.** (`F05000017800`) — optional, conditional
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV; § 3 (3) GüKG; Art. 4 (3) VO (EG) Nr. 1072/2009; Nr. 17 GüKVwV _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Zuverlässigkeit › Unbedenklichkeitsbescheinigung Berufsgenossenschaft (`G05000011924`)

- **Eine Unbedenklichkeitsbescheinigung der Berufsgenossenschaft** (`F05000017801`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV _(geerbt)_
- **Laden Sie die Unbedenklichkeitsbescheinigung der Berufsgenossenschaft Verkehrswirtschaft, Post-Logistik, Telekommunikation (BG Verkehr) oder einer anderen anerkannten Berufsgenossenschaft hoch. Diese darf nicht älter als drei Monate sein.** (`F05000017802`) — optional, conditional
  - Rechtsgrundlage: § 3 GBZugV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Weiter Nachweise - Landesspezifisch (`G05000011925`)

- **Laden Sie für die geschäftsführende Person die Auskunft aus dem Fahreignungsregister des Kraftfahrt-Bundesamtes (KBA) Flensburg hoch. Diese darf nicht älter als drei Monate sein.** (`F05000017803`) — optional
  - Rechtsgrundlage: referenzbasiert
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie für jedes Fahrzeug die Zulassungsbescheinigung (Fahrzeugschein) oder den Miet- oder Leasingvertrags hoch.** (`F05000017804`) — optional
  - Rechtsgrundlage: § 3 GBZugV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Weiter Nachweise - Landesspezifisch › Auszug aus dem Gewerbezentralregister (`G05000011948`)

- **Hinweis zum Gewerbezentralregisterauszug (Belegart 9):** (`F05000017727`) — optional
  - Rechtsgrundlage: § 150 GewO
- **Die Auskunft aus dem Gewerbezentralregister (Belegart 9)** (`F05000017728`) — Pflicht
  - Rechtsgrundlage: § 3 GBZugV; § 10 (2) GBZugV _(geerbt)_
  - Hilfe: Die Auskunft wird direkt übersandt.
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Nachweise › Weiter Nachweise - Landesspezifisch › Auszug aus dem Gewerbezentralregister › Name der zu überprüfenden Person (`G05000011944`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Haben Sie ein bestehendes Gewerbe?" gleich „wahr" ist | „Gewerbeanmeldung" | muss ausgefüllt werden | — | `R05000012876` |
| wenn „Haben Sie ein bestehendes Gewerbe?" ungleich „wahr" ist | „Gewerbeanmeldung" | entfällt | — | `R05000012876` |
| wenn „Die Verkehrsleitung ist" gleich „001 angestellt" ist | „Arbeitsvertrag oder Geschäftsbesorgungsvertrag" | muss ausgefüllt werden | — | `R05000012879` |
| wenn „Die Verkehrsleitung ist" ungleich „001 angestellt" ist | „Arbeitsvertrag oder Geschäftsbesorgungsvertrag" | entfällt | — | `R05000012879` |
| wenn „Die Verkehrsleitung ist" ungleich „001 angestellt" ist | „Geschäftsbesorgungsvertrag" | muss ausgefüllt werden | — | `R05000012880` |
| wenn „Die Verkehrsleitung ist" gleich „001 angestellt" ist | „Geschäftsbesorgungsvertrag" | entfällt | — | `R05000012880` |
| wenn „Die Verkehrsleitung ist" ungleich „001 angestellt" ist | „Gewerbeanmeldung der externen Verkehrsleitung" | muss ausgefüllt werden | — | `R05000012882` |
| wenn „Die Verkehrsleitung ist" gleich „001 angestellt" ist | „Gewerbeanmeldung der externen Verkehrsleitung" | entfällt | — | `R05000012882` |
| wenn „Haben Sie ein bestehendes Gewerbe?" gleich „wahr" ist | „Unbedenklichkeitsbescheinigung Berufsgenossenschaft" | muss ausgefüllt werden | — | `R05000012883` |
| wenn „Haben Sie ein bestehendes Gewerbe?" ungleich „wahr" ist | „Unbedenklichkeitsbescheinigung Berufsgenossenschaft" | entfällt | — | `R05000012883` |
| wenn „Wollen Sie eine weitere Niederlassungen angeben?" gleich „ja" ist | „Angaben zur Niederlassung" | muss ausgefüllt werden | — | `R05000015777` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | muss ausgefüllt werden | — | `R05000015133` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Gesellschafter" | entfällt | — | `R05000015133` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | muss ausgefüllt werden | — | `R05000015134` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Gesellschafter" | entfällt | — | `R05000015134` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | muss ausgefüllt werden | — | `R05000015135` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Gesellschafter" | entfällt | — | `R05000015135` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Ansprechperson" | muss ausgefüllt werden | — | `R05000015136` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | entfällt | — | `R05000015136` |
| wenn „Rechtsform" gleich „Personenhandelsgesellschaft" oder „Partenreederei (§ 489 HGB a. F.)" oder „ oder 411100=" oder „ oder 411200 " ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015138` |
| wenn „Rechtsform" gleich „Genossenschaft" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015140` |
| wenn „Rechtsform" gleich „ oder 230000=" oder „ bis 232000=" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015146` |
| wenn „Rechtsform" gleich „121000 nicht eingetragene Gesellschaft des bürgerlichen Rechts" oder „ oder 214000 " oder „ oder 261000=" oder „ oder 310000=" oder „ bis 381000=" oder „ oder 412000=" oder „ bis 412200=" oder „ oder 421000=" oder „ oder 423000=" oder „ bis 424000=" oder „ oder 510000=" oder „ bis 530000=" oder „ oder 550000=" oder „ bis 560000=" oder „ oder 590000=" oder „ bis 610000=" oder „ oder 691000=" ist | „Art der Eintragung oder des Registers" | entfällt | — | `R05000015150` |
| wenn „Eingetragener Name" gesetzt auf einem beliebigen Wert ist | „Geschäftsbezeichnung" | muss ausgefüllt werden | — | `R05000015153` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | muss ausgefüllt werden | — | `R05000015158` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | entfällt | — | `R05000015158` |
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
| wenn „Ist eine zuvor erfasste Person Verkehrsleitung?" ungleich „wahr" ist | „Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters" | muss ausgefüllt werden | — | `R05000012844` |
| wenn „Ist eine zuvor erfasste Person Verkehrsleitung?" gleich „wahr" ist | „Persönliche Angaben der Verkehrsleiterin oder des Verkehrsleiters" | entfällt | — | `R05000012844` |
| wenn „Ist eine zuvor erfasste Person Verkehrsleitung?" ungleich „wahr" ist | „Hauptwohnsitz" | muss ausgefüllt werden | — | `R05000012857` |
| wenn „Ist eine zuvor erfasste Person Verkehrsleitung?" gleich „wahr" ist | „Hauptwohnsitz" | entfällt | — | `R05000012857` |
| wenn „Ist eine zuvor erfasste Person Verkehrsleitung?" gleich „wahr" ist | „Welche Person ist als Verkehrsleiterin oder Verkehrsleiter tätig?" | muss ausgefüllt werden | — | `R05000012858` |
| wenn „Ist eine zuvor erfasste Person Verkehrsleitung?" ungleich „wahr" ist | „Welche Person ist als Verkehrsleiterin oder Verkehrsleiter tätig?" | entfällt | — | `R05000012858` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Ist die Verkehrsleitung in weiteren Unternehmen als Verkehrsleiterin oder Verkehrsleiter tätig?" gleich „wahr" ist | „Angaben zur Tätigkeit in weiteren Unternehmen" | entfällt und muss ausgefüllt werden | — | `R05000012863` |
| wenn „Ist die Verkehrsleitung in weiteren Unternehmen als Verkehrsleiterin oder Verkehrsleiter tätig?" gleich „wahr" ist | „Regelmäßige wöchentliche Arbeitszeit in Stunden" | entfällt und muss ausgefüllt werden | — | `R05000012864` |
| wenn „Entspricht die Niederlassung der vorher erfassten Geschäftsanschrift?" ungleich „wahr" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012855` |
| wenn „Entspricht die Niederlassung der vorher erfassten Geschäftsanschrift?" gleich „wahr" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `R05000012855` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden und wird gezeigt | — | `R05000015794` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Straßenanschrift Inland" ist | „Anschrift Postfach" | entfällt | — | `R05000015794` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Anschrift Postfach" | muss ausgefüllt werden und wird gezeigt | — | `R05000015794` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „Postfach- oder Großempfängeranschrift" ist | „Straßenanschrift Inland" | entfällt | — | `R05000015794` |
| wenn „Die Gewerbeanmeldung" gleich „002 liegt vor" ist | „Laden Sie die Gewerbeanmeldung hoch." | muss ausgefüllt werden | — | `R05000012861` |
| wenn „Die Gewerbeanmeldung" ungleich „002 liegt vor" ist | „Laden Sie die Gewerbeanmeldung hoch." | entfällt | — | `R05000012861` |
| wenn „Ein aktueller Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister" gleich „001 liegt vor" ist | „Fügen Sie einen aktuellen Registerauszug bei." | muss ausgefüllt werden | — | `R05000012862` |
| wenn „Ein aktueller Auszug aus dem Handels-, Genossenschafts-, Gesellschafts-, Partnerschafts- oder Vereinsregister" ungleich „001 liegt vor" ist | „Fügen Sie einen aktuellen Registerauszug bei." | entfällt | — | `R05000012862` |
| wenn „Der Gesellschaftsvertrag oder die Satzung" gleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012782` |
| wenn „Der Gesellschaftsvertrag oder die Satzung" ungleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | entfällt | — | `R05000012782` |
| wenn „Die Auskunft aus dem Fahreignungsregister wird" gleich „002 beigefügt" ist | „Laden Sie eine Auskunft aus dem Fahreignungsregister des Kraftfahrt-Bundesamtes (KBA) Flensburg hoch. Diese darf nicht älter als drei Monate sein." | muss ausgefüllt werden | — | `R05000012865` |
| wenn „Die Auskunft aus dem Fahreignungsregister wird" ungleich „002 beigefügt" ist | „Laden Sie eine Auskunft aus dem Fahreignungsregister des Kraftfahrt-Bundesamtes (KBA) Flensburg hoch. Diese darf nicht älter als drei Monate sein." | darf nicht ausgefüllt werden | — | `R05000012865` |
| wenn „Die Auskunft aus dem Fahreignungsregister wird" ungleich „002 beigefügt" ist | „Name der zu überprüfenden Person" | muss ausgefüllt werden | — | `R05000012866` |
| wenn „Die Auskunft aus dem Fahreignungsregister wird" gleich „002 beigefügt" ist | „Name der zu überprüfenden Person" | darf nicht ausgefüllt werden | — | `R05000012866` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „002 ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | muss ausgefüllt werden | — | `R05000012761` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „002 ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | darf nicht ausgefüllt werden | — | `R05000012761` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „001 ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000012762` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „001 ist beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | — | `R05000012762` |
| wenn „Das Dokument" gleich „001" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `G05000011917` |
| wenn „Das Dokument" ungleich „001" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `G05000011917` |
| wenn „Das Dokument" gleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012868` |
| wenn „Das Dokument" ungleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | entfällt | — | `R05000012868` |
| wenn „Liegt Ihnen eine Bescheinigung in Steuersachen des Finanzamtes vor, die Ihre Unbedenklichkeit bestätigt? Diese darf nicht älter als drei Monate sein." gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000012869` |
| wenn „Liegt Ihnen eine Bescheinigung in Steuersachen des Finanzamtes vor, die Ihre Unbedenklichkeit bestätigt? Diese darf nicht älter als drei Monate sein." ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000012869` |
| wenn „Eine Unbedenklichkeitsbescheinigung der Krankenkasse" gleich „002 liegt vor" ist | „Laden Sie die Unbedenklichkeitsbescheinigung der Krankenkasse hoch. Diese darf nicht älter als drei Monate sein." | muss ausgefüllt werden | — | `R05000012870` |
| wenn „Eine Unbedenklichkeitsbescheinigung der Krankenkasse" ungleich „002 liegt vor" ist | „Laden Sie die Unbedenklichkeitsbescheinigung der Krankenkasse hoch. Diese darf nicht älter als drei Monate sein." | entfällt | — | `R05000012870` |
| wenn „Eine Unbedenklichkeitsbescheinigung der Berufsgenossenschaft" gleich „002 liegt vor" ist | „Laden Sie die Unbedenklichkeitsbescheinigung der Berufsgenossenschaft Verkehrswirtschaft, Post-Logistik, Telekommunikation (BG Verkehr) oder einer anderen anerkannten Berufsgenossenschaft hoch. Diese darf nicht älter als drei Monate sein." | muss ausgefüllt werden | — | `R05000012871` |
| wenn „Eine Unbedenklichkeitsbescheinigung der Berufsgenossenschaft" ungleich „002 liegt vor" ist | „Laden Sie die Unbedenklichkeitsbescheinigung der Berufsgenossenschaft Verkehrswirtschaft, Post-Logistik, Telekommunikation (BG Verkehr) oder einer anderen anerkannten Berufsgenossenschaft hoch. Diese darf nicht älter als drei Monate sein." | entfällt | — | `R05000012871` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" gleich „001 Ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000012872` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" ungleich „001 Ist beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | — | `R05000012872` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" gleich „002 Ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | muss ausgefüllt werden | — | `R05000012873` |
| wenn „Die Auskunft aus dem Gewerbezentralregister (Belegart 9)" ungleich „002 Ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | darf nicht ausgefüllt werden | — | `R05000012873` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>WENN in Datenfeld F05000017753 "Abfrage weitere Niederlassungen" Auswahl <> "ja", DANN ist Feldgruppe G05000011895 "Niederlassung Güterkraftverkehr" nicht ein weiteres Mal anzuzeigen.</mark> — Regel `R05000015777`
- <mark>WENN das Feld F05000017742 "Gemeinschaftslizenz" = "WAHR" ist, DANN darf das Feld F05000017743 "Erlaubnis gewerblicher Güterkraftverkehr" nicht mehr ausgefüllt werden.</mark> — Regel `R05000012970`
- <mark>WENN das Feld F05000017742 "Gemeinschaftslizenz" <> "WAHR" ist, dann darf das Feld F05000017743 "Erlaubnis gewerblicher Güterkraftverkehr" ausgefüllt werden.</mark> — Regel `R05000012970`
- <mark>Es muss mindestens eines der Felder F05000017742 "Gemeinschaftslizenz" oder F05000017743 "Erlaubnis gewerblicher Güterkraftverkehr" = "wahr" sein.</mark> — Regel `R05000012971`
- <mark>WENN das Feld F05000017743 "Erlaubnis gewerblicher Güterkraftverkehr" = "WAHR" ist, DANN darf das Feld F05000017742 "Gemeinschaftslizenz" nicht mehr ausgefüllt werden.</mark> — Regel `R05000012972`
- <mark>WENN das Feld F05000017743 "Erlaubnis gewerblicher Güterkraftverkehr" <> "WAHR" ist, dann darf das Feld F05000017742 "Gemeinschaftslizenz" ausgefüllt werden.</mark> — Regel `R05000012972`
- <mark>WENN im Feld F6000000339 "Rechtsform (XUnternehmen)" Auswahl = 120000="Gesellschaft des bürgerlichen Rechts (BGB-Gesellschaft) ; auch eingetragene Gesellschaft des bürgerlichen Rechts" oder 123000="eingetragene Gesellschaft des bürgerlichen Rechts", DANN darf in Feld F6000000347 "Art Eintragung / Register" nur der Code GesR "Gesellschaftsregister" ausgewählt sein.</mark> — Regel `R05000015137`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 252000="Europäische Genossenschaft (SCE)" oder 292000="ausländische Genossenschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes G "Eintragung im Genossenschaftsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015141`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 294000="ausländische juristische Person (EU-Recht)" oder 295000="ausländische juristische Person (Nicht-EU-Recht)" bis 298100="sonstige ausländische juristische Person des privaten Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015142`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 220000="Kapitalgesellschaft", 222000="Aktiengesellschaft (AG); auch Europäische Aktiengesellschaft (SE); Investmentaktiengesellschaft (Investment-AG)", 222200="Europäische Aktiengesellschaft (SE)", 293000="ausländische Kapitalgesellschaft" oder 293100="Limited Company (unspezifisch)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015143`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 260000="sonstige juristische Person" oder 268000="Auffangtatbestände (juristische Person)" bis 268200="sonstige juristische Person des Privatrechts (Auffangtatbestand Steuer)" oder 268300="sonstige juristische Person des öffentlichen Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000015144`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 682000="Freitext (Auffangtatbestand Justiz)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015145`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 211000="eingetragener Verein (e.V.)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000015147`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 138000="Auffangtatbestände (Personengesellschaft)", 138100="sonstige rechtsfähige Personengesellschaft (Auffangstatbestand)", 212000="Wirtschaftlicher Verein", 240000="Körperschaft des öffentlichen Rechts (KöR)" bis 243000="öffentlich-rechtliche Religionsgesellschaft", 262000="rechtsfähige Anstalt des öffentlichen Rechts (rechtsf. AöR)", 268400="sonstige juristische Person, die im Handelsregister Abteilung A eingetragen ist (Auffangtatbestand Justiz)", 410000="gewerbliches Einzelunternehmen (ohne Hausgewerbe)", 411000="eingetragenes gewerbliches Einzelunternehmen (e.K.; e.Kfm.; e.Kfr.)", 420000="sonstige wirtschaftliche Tätigkeit einer natürlichen Person", 422000="Land-/Forstwirt", 428000="Auffangtatbestände (wirtschaftliche Tätigkeit einer natürlichen Person)", 428100="sonstige wirtschaftliche Tätigkeit einer natürlichen Person (Auffangstatbestand)", 540000="Gewerbebetrieb einer Körperschaft des öffentlichen Rechts", 580000="Auffangtatbestände (wirtschaftliche Tätigkeit einer nicht-natürlichen Person)" oder 581000="sonstige wirtschaftliche Tätigkeit einer nicht-natürlichen Person (Auffangtatbestand)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code A "Eintragung im Handelsregister A" ausgewählt sein.</mark> — Regel `R05000015148`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 190000="ausländische Personengesellschaft" bis 192000="ausländische Personengesellschaft (Nicht-EU-Recht)" oder 291000="ausländische Körperschaft des öffentlichen Rechts" oder 490000="ausländische wirtschaftliche Tätigkeit einer natürlichen Person" bis 492000="ausländisches gewerbliches Einzelunternehmen (Nicht-EU-Recht)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015149`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 210000="rechtsfähiger Verein", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000015151`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 213000 "Versicherungsverein auf Gegenseitigkeit; auch Pensionsfondsverein auf Gegenseitigkeit", 213100="Versicherungsverein auf Gegenseitigkeit", 213200="Pensionsfondsverein auf Gegenseitigkeit" oder 221000 "Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH ; auch Unternehmergesellschaft (haftungsbeschränkt)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000015152`
- <mark>WENN in F60000000319 "Eingetragener Name / Organisationsname" ein Eintrag vorgenommen wurde, DANN ist F60000000320 "Geschäftsbezeichnung / Organisationsbezeichnung" ein optionales Feld.</mark> — Regel `R05000015153`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 130000="sonstige rechtsfähige Personengesellschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000015154`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 131000="Partnerschaftsgesellschaft (PartG)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000015155`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 221100="Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH" bis 221200="Unternehmergesellschaft (haftungsbeschränkt)" oder 222100="Aktiengesellschaft (AG); auch Investmentaktiengesellschaft (InvAG)" bis 222120="Investmentaktiengesellschaft (InvAG)" oder 223000="Kommanditgesellschaft auf Aktien (KGaA); auch & Co. KGaA" bis 224810="sonstige Kapitalgesellschaft (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000015156`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 290000="ausländische juristische Person" oder 681000="Freitext (Auffangtatbestand)" oder 683000="Ersatzwert (Auffangtatbestand Steuer)" bis 690000="ausländische Rechtsform" oder 698000="Auffangtatbestände (ausländische Rechtsform)" oder 680000="Auffangtatbestände (ohne Rechtsform-Typ)" oder 698100="sonstige ausländische Rechtsform (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015157`
- <mark>Die Mitgliedstaaten der Europäischen Union und EWR sowie Schweiz sind (Stand 2025) sind alphabetisch sortiert: 124 Belgien, 125 Bulgarien, 126 Dänemark, 0 Deutschland, 127 Estland, 128 Finnland, 129 Frankreich, 134 Griechenland, 135 Irland, 137 Italien, 130 Kroatien, 139 Lettland, 142 Litauen, 143 Luxemburg, 145 Malta, 148 Niederlande, 151 Österreich, 152 Polen, 153 Portugal, 154 Rumänien, 157 Schweden, 155 Slowakei, 131 Slowenien, 161 Spanien, 164 Tschechien, 165 Ungarn, 181 Zypern, 136 Island, Lichtenstein, 149 Norwegen und 158 Schweiz.</mark> — Regel `R05000015158`
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

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000011888_F05000017747["Haben Sie ein bestehendes Gewerbe?"] ==>|"= wahr → required"| G05000011910_G05000011911["Gewerbeanmeldung"]
  G05000011888_F05000017747["Haben Sie ein bestehendes Gewerbe?"] -.->|"<> wahr → hide"| G05000011910_G05000011911["Gewerbeanmeldung"]
  G05000011906_G05000011909_G05000011940_F05000017760["Die Verkehrsleitung ist"] ==>|"= 001 angestellt → required"| G05000011910_G05000011912_F05000017772["Arbeitsvertrag oder Geschäftsbesorgung"]
  G05000011906_G05000011909_G05000011940_F05000017760["Die Verkehrsleitung ist"] -.->|"<> 001 angestellt → hide"| G05000011910_G05000011912_F05000017772["Arbeitsvertrag oder Geschäftsbesorgung"]
  G05000011906_G05000011909_G05000011940_F05000017760["Die Verkehrsleitung ist"] ==>|"<> 001 angestellt → required"| G05000011910_G05000011912_F05000017773["Geschäftsbesorgungsvertrag"]
  G05000011906_G05000011909_G05000011940_F05000017760["Die Verkehrsleitung ist"] -.->|"= 001 angestellt → hide"| G05000011910_G05000011912_F05000017773["Geschäftsbesorgungsvertrag"]
  G05000011906_G05000011909_G05000011940_F05000017760["Die Verkehrsleitung ist"] ==>|"<> 001 angestellt → required"| G05000011910_G05000011912_F05000017774["Gewerbeanmeldung der externen Verkehrs"]
  G05000011906_G05000011909_G05000011940_F05000017760["Die Verkehrsleitung ist"] -.->|"= 001 angestellt → hide"| G05000011910_G05000011912_F05000017774["Gewerbeanmeldung der externen Verkehrs"]
  G05000011888_F05000017747["Haben Sie ein bestehendes Gewerbe?"] ==>|"= wahr → required"| G05000011910_G05000011913_G05000011924["Unbedenklichkeitsbescheinigung Berufsg"]
  G05000011888_F05000017747["Haben Sie ein bestehendes Gewerbe?"] -.->|"<> wahr → hide"| G05000011910_G05000011913_G05000011924["Unbedenklichkeitsbescheinigung Berufsg"]
  F05000017753["Wollen Sie eine weitere Niederlassunge"] ==>|"= ja → required"| G05000011895["Angaben zur Niederlassung"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013184_G05000011759["Nicht Natürliche Person"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013184_G05000011759_G05000011757["Gesellschafter"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013184_G05000011759["Nicht Natürliche Person"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013184_G05000011759_G05000011757["Gesellschafter"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013184_G05000011759["Nicht Natürliche Person"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013184_G05000011759_G05000011757["Gesellschafter"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013184_G05000013186["Ansprechperson"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013184_G05000011759["Nicht Natürliche Person"]
  G05000013184_G05000013185_F60000000339["Rechtsform"] ==>|"= Personenhandelsgesellschaft, → required"| G05000013184_G05000013185_F60000000347["Art der Eintragung oder des Registers"]
  G05000013184_G05000013185_F60000000339["Rechtsform"] ==>|"= Genossenschaft → required"| G05000013184_G05000013185_F60000000347["Art der Eintragung oder des Registers"]
  G05000013184_G05000013185_F60000000339["Rechtsform"] ==>|"=  oder 230000=,  bis 232000= → required"| G05000013184_G05000013185_F60000000347["Art der Eintragung oder des Registers"]
  G05000013184_G05000013185_F60000000339["Rechtsform"] -.->|"= 121000 nicht eingetragene Ge → hide"| G05000013184_G05000013185_F60000000347["Art der Eintragung oder des Registers"]
  G05000013184_G05000013185_F60000000319["Eingetragener Name"] ==>|"? ? → required"| G05000013184_G05000013185_F60000000320["Geschäftsbezeichnung"]
  G05000013184_G05000013186_F60000000236["Staatsangehörigkeit"] ==>|"? ? → required"| G05000013184_G05000013186_G05000011749["Aufenthaltsgenehmigung"]
  G05000013184_G05000013186_F60000000236["Staatsangehörigkeit"] -.->|"? ? → hide"| G05000013184_G05000013186_G05000011749["Aufenthaltsgenehmigung"]
  G05000013184_G05000013186_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000013184_G05000013186_G60000000083_F60000000232["Monat"]
  G05000013184_G05000013186_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013184_G05000013186_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013184_G05000013186_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000013184_G05000013186_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013184_G05000013186_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013184_G05000013186_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013184_G05000013186_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000013184_G05000013186_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013184_G05000013186_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Straßenanschrift Inland → required+show"| G05000013184_G05000013186_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013184_G05000013186_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Straßenanschrift Inland → hide"| G05000013184_G05000013186_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013184_G05000013186_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Postfach- oder Großempfänger → required+show"| G05000013184_G05000013186_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013184_G05000013186_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Postfach- oder Großempfänger → hide"| G05000013184_G05000013186_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013184_G05000013186_G05000011749_F05000017638["Welchen Status hat Ihre Aufenthaltsgen"] ==>|"= liegt vor → required"| G05000013184_G05000013186_G05000011749_F60000000292["Ausstellende Behörde"]
  G05000013184_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013184_G05000011759_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013184_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000013184_G05000011759_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013184_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013184_G05000011759_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013184_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000013184_G05000011759_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013184_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Straßenanschrift Inland → required+show"| G05000013184_G05000011759_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013184_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Straßenanschrift Inland → hide"| G05000013184_G05000011759_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013184_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Postfach- oder Großempfänger → required+show"| G05000013184_G05000011759_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013184_G05000011759_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Postfach- oder Großempfänger → hide"| G05000013184_G05000011759_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013184_G05000011759_G05000011756_G05000011751_F60000000236["Staatsangehörigkeit"] ==>|"? ? → required"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000013184_G05000011759_G05000011756_G05000011751_F60000000236["Staatsangehörigkeit"] -.->|"? ? → hide"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000013184_G05000011759_G05000011756_G05000011751_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000013184_G05000011759_G05000011756_G05000011751_G60000000083_F60000000232["Monat"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Straßenanschrift Inland → required+show"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Straßenanschrift Inland → hide"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= Postfach- oder Großempfänger → required+show"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= Postfach- oder Großempfänger → hide"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013184_G05000011759_G05000011756_G05000011751_G05000011749_F05000017638["Welchen Status hat Ihre Aufenthaltsgen"] ==>|"= liegt vor → required"| G05000013184_G05000011759_G05000011756_G05000011751_G05000011749_F60000000292["Ausstellende Behörde"]
  G05000013184_G05000011759_G05000011757_F05000018285["Ist der Gesellschafter eine Natürliche"] ==>|"= ? → required"| G05000013184_G05000011759_G05000011757_G05000011751["Natürliche Person - Vertreter"]
  G05000013184_G05000011759_G05000011757_F05000018285["Ist der Gesellschafter eine Natürliche"] -.->|"= ? → hide"| G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"]
  G05000013184_G05000011759_G05000011757_F05000018285["Ist der Gesellschafter eine Natürliche"] ==>|"= ? → required"| G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"]
  G05000013184_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013184_G05000011759_G05000011757_G05000011751["Natürliche Person - Vertreter"]
  unclear0["?: WENN in Datenfeld F05000017753 "Abfrage weitere Niederlassun"]:::unclear
  unclear1["?: WENN das Feld F05000017742 "Gemeinschaftslizenz" = "WAHR" is"]:::unclear
  unclear2["?: WENN das Feld F05000017742 "Gemeinschaftslizenz" <> "WAHR" i"]:::unclear
  unclear3["?: Es muss mindestens eines der Felder F05000017742 "Gemeinscha"]:::unclear
  unclear4["?: WENN das Feld F05000017743 "Erlaubnis gewerblicher Güterkraf"]:::unclear
  unclear5["?: WENN das Feld F05000017743 "Erlaubnis gewerblicher Güterkraf"]:::unclear
  unclear6["?: WENN im Feld F6000000339 "Rechtsform (XUnternehmen)" Auswahl"]:::unclear
  unclear7["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear8["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear9["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
