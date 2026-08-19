---
name: antrag-s05000001346
description: Führt Antragstellende durch „Antrag auf EU-Zulassung von Lebensmittelbetrieben" (FIM S05000001346 1.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag auf EU-Zulassung von Lebensmittelbetrieben

- **FIM-ID:** `S05000001346 1.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** Art. 6 (1-3) VO (EG) Nr. 852/2004; Art. 3 Nr. 3 VO (EG) Nr. 178/2002; Art. 4 VO (EG) 853/2004; §9 Tier-LMHV vom 18.04.2018; : Artikel 3 Nr. 2 VO (EG) Nr. 178/2002
- **Kompiliert:** 2026-08-13T15:51:52Z aus https://fimportal.de/api/v1/schemas/S05000001346/1.0.0/xdf
- **Umfang:** 727 Felder, 306 gesicherte Bedingungen, 42 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

> **Hinweis:** Die zugehörige Leistung konnte nicht zweifelsfrei zugeordnet werden (Rechtsgrundlage stimmt nicht überein (D99000001965)). Zu Fristen, Kosten, Unterlagen und Zuständigkeit daher keine Auskunft geben, sondern an die zuständige Stelle verweisen.

## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Antragsumfang EU-Zulassung Lebensmittelbetriebe (`G05000012595`)

- **Hinweis:** (`F05000018734`) — optional
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?** (`F05000018735`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004

### Antragsumfang EU-Zulassung Lebensmittelbetriebe › Zustandekommen von Änderungen gegenüber dem vorherigen Antrag (`G05000012596`)

- **Hinweis:** (`F05000018741`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Unternehmensdaten** (`F05000018736`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Daten der Betriebsstätte** (`F05000018737`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Betriebsbereiche** (`F05000018738`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Großküche zum Betriebsspiegel** (`F05000018739`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Kühllager zum Betriebsspiegel** (`F05000018740`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Eiprodukte zum Betriebsspiegel** (`F05000018742`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Fischereiprodukte zum Betriebsspiegel** (`F05000018743`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Muscheln zum Betriebsspiegel** (`F05000018744`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Milch zum Betriebsspiegel** (`F05000018745`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Gelatine und Kollagen zum Betriebsspiegel** (`F05000018746`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004
- **Beiblatt Fleisch zum Betriebsspiegel** (`F05000018747`) — Pflicht
  - Rechtsgrundlage: Art. 6 Nr. 3 der VO (EG) 853/2004

### Angaben zum Unternehmen › Betriebsangaben (`G05000013202`)

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
  - Rechtsgrundlage: § 8a HGB; § 705 BGB; § 8b HGB; § 706 BGB; § 707 BGB

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Ansprechperson › Gesetzlicher Vertreter NP › Natürliche Person - Vertreter › Anschrift (`G05000011746`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO; Xinneres.Auslandsanschrift.Druckbild Version 8; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.4; Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; XInneres.PostalischeInlandsanschrift.Postfachanschrift Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland; urn:xoev-de:xunternehmen:standard:basismodul_1.1; referenzbasiert; XInneres.PostalischeInlandsanschrift.postfach Version 8; urn:xoev-de:xunternehmen:kerndatenobjekt:staat; Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1; referenzbasiert; § 69 GewO; XInneres.Meldeanschrift.postleitzahl Version 8 _(geerbt)_
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

### Lebensmittelrechtlich für das Unternehmen verantwortliche Person (`G05000012598`)

- **Hinweis:** (`F05000018748`) — Pflicht
  - Rechtsgrundlage: Artikel 3 Nr. 2 und Nr. 3 der VO (EG) Nr. 178/2002
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Daten der Betriebsstätte (`G05000012600`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Geben Sie den Namen der Betriebsstätte an.** (`F05000018759`) — Pflicht
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie Ihre Registriernummer an.** (`F05000018760`) — optional
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie Ihre Zulassungsnummer an.** (`F05000018761`) — optional
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Veterinärkontroll-Nummer (HIT) an.** (`F05000018762`) — optional
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Geschäftszeiten an** (`F05000018763`) — optional
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Baujahr** (`F60000000300`) — optional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; §9 Tier-LMHV _(geerbt)_
- **Geben Sie den letzten Umbau an.** (`F05000018765`) — Pflicht
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Weicht die Geschäftsanschrift von der Betriebsstätte ab?** (`F05000018770`) — Pflicht
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Daten der Betriebsstätte › Lebensmittelunternehmer (`G05000012620`)

- **Ist die lebensmittelrechtlich verantwortliche Person des Unternehmens auch für diese Betriebsstätte zuständig?** (`F05000018768`) — Pflicht
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Daten der Betriebsstätte › Lebensmittelunternehmer › Verantwortliche Person (`G05000012621`)

- **Hinweis:** (`F05000018769`) — optional
  - Rechtsgrundlage: Art. 3 Nr. 3 der VO (EG) Nr. 178/2002; Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Daten der Betriebsstätte › Abweichende Anschrift der Betriebsstätte (`G05000013416`)

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

### Daten der Betriebsstätte › Erreichbarkeit (`G05000011747`)

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
  - Rechtsgrundlage: Art. 6 (1) VO (EU) 2016/679 _(geerbt)_

### Daten der Betriebsstätte › Personal › Geben Sie je Geschlecht die Anzahl der Mitarbeitenden im gesamten Betrieb an. (`G05000012626`)

- **Männlich** (`F05000018772`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Weiblich** (`F05000018773`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Divers** (`F05000018775`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Keine Angabe zum Geschlecht** (`F05000018776`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Daten der Betriebsstätte › Personal › Davon im Produktionsbereich (`G05000012627`)

- **Männlich** (`F05000018772`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Weiblich** (`F05000018773`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Divers** (`F05000018775`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Keine Angabe zum Geschlecht** (`F05000018776`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Daten der Betriebsstätte › Personal › Davon externes Personal (z.B. Reinigungskräfte) (`G05000012629`)

- **Männlich** (`F05000018772`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Weiblich** (`F05000018773`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Divers** (`F05000018775`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Keine Angabe zum Geschlecht** (`F05000018776`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Daten der Betriebsstätte › Geben Sie die Art der Wasserversorgung an (`G05000012630`)

- **Öffentliche Wasserversorgung** (`F05000018780`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Eigenwasserversorgung (Brunnen)** (`F05000018781`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Sauberes Meerwasser** (`F05000018783`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Daten der Betriebsstätte › Vorhandensein eines Waschplatzes für Transportmittel (`G05000012631`)

- **Waschplatz für Transportmittel ist vorhanden** (`F05000018784`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Waschplatz für Transportmittel ist nicht erforderlich** (`F05000018785`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Sonstige** (`F05000018786`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Sonstige Angaben** (`F05000018787`) — optional, conditional
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Betriebsangaben › Geben Sie die Bereiche des Betriebs an (`G05000012632`)

- **Großküche** (`F05000018788`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Fleisch** (`F05000018789`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Fette und Grieben** (`F05000018790`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Mägen, Blasen und Därme** (`F05000018791`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Milch** (`F05000018792`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Fischereierzeugnisse** (`F05000018793`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Lebende Muscheln** (`F05000018794`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Ei/Eiprodukte** (`F05000018795`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004
- **Gelatine/Kollagen** (`F05000018796`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Kühllager** (`F05000018797`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Umpacken** (`F05000018798`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Großhandel** (`F05000018799`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstiges** (`F05000018800`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige Betriebsbereiche** (`F05000018801`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: Hinweis: Melden Sie sich bei Ihrer zuständigen Kreisordnungsbehörde.

### Betriebsangaben › Beiblatt Großküche zum Betriebsspiegel › Wählen Sie Ihre Produktionsverfahren (`G05000012637`)

- **Frischkost (cook and serve)** (`F05000018802`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Warmkost (cook, hold and serve)** (`F05000018803`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Kühlkost (cook and chill)** (`F05000018804`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Tiefkühlkost (cook and freeze)** (`F05000018805`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Erhitzen (Regenerieren)** (`F05000018806`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Sonstiges** (`F05000018800`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige Produktionsverfahren** (`F05000018807`) — optional, conditional
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Betriebsangaben › Beiblatt Großküche zum Betriebsspiegel › Geben Sie den Zeitraum der Produktion an (`G05000012638`)

- **Geben Sie den Zeitraum der Produktion an** (`F05000018808`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Geben Sie die Anzahl der Produktionstage pro Woche an** (`F05000018824`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Werden Lebensmittel transportiert?** (`F05000018825`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Großküche zum Betriebsspiegel › Geben Sie den Zeitraum der Produktion an › Geben Sie die Produktionsmonate an (`G05000012639`)

- **Januar** (`F05000018812`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Februar** (`F05000018813`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **März** (`F05000018814`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **April** (`F05000018815`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Mai** (`F05000018816`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juni** (`F05000018817`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juli** (`F05000018818`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **August** (`F05000018819`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **September** (`F05000018820`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Oktober** (`F05000018821`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **November** (`F05000018822`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Dezember** (`F05000018823`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Betriebsangaben › Beiblatt Großküche zum Betriebsspiegel › Beantragte Be- oder Verarbeitung von unverarbeiteten Lebensmitteln tierischen Ursprungs › Geben Sie die unverarbeiteten Lebensmittel an (`G05000012641`)

- **Frisches Fleisch von Rindern, Schweinen, Ziegen, Schafen oder Pferden** (`F05000018827`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Hackfleisch/Fleischzubereitungen** (`F05000018828`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Frisches Wildfleisch** (`F05000018829`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Frisches Geflügelfleisch** (`F05000018831`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Frischer Fisch** (`F05000018833`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Rohe Eier oder nicht pasteurisiertes Flüssigei** (`F05000018834`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Rohmilch, Rohrahm** (`F05000018835`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Lebende Muscheln** (`F05000018837`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Unverarbeitete Froschschenkel, Schnecken** (`F05000018838`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Großküche zum Betriebsspiegel › Beantragte Be- oder Verarbeitung von unverarbeiteten Lebensmitteln tierischen Ursprungs (`G05000012640`)

- **Verwenden Sie darüber hinaus weitere Rohstoffe im Sinne von unverarbeiteten Lebensmitteln tierischen Ursprungs?** (`F05000018840`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die weiteren Rohstoffe an** (`F05000018842`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Großküche zum Betriebsspiegel › Geben Sie die Herstellungsmenge an Speisen an (`G05000012643`)

- **Feinkostsalate** (`F05000018846`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in Portionen/Woche
- **Suppen/Eintöpfe** (`F05000018848`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in Portionen/Woche
- **Gerichte für den Kaltverzehr** (`F05000018850`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in Portionen/Woche
- **Gerichte für den Warmverzehr** (`F05000018852`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in Portionen/Woche
- **Desserts/Feinbackwaren** (`F05000018853`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in Portionen/Woche
- **Existieren darüber hinaus weitere Speisen?** (`F05000018855`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Großküche zum Betriebsspiegel › Geben Sie die Herstellungsmenge an Speisen an › Weitere Speisen (`G05000012644`)

- **Geben Sie die weiteren Speisen an** (`F05000018856`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge der Portionen pro Woche** (`F05000018857`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Durchschnittliche Anzahl der Verbraucher pro Tag** (`F05000018858`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten (`G05000012651`)

- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Tiefkühlräume (`G05000012652`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Komissionierungsräume (`G05000012653`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Sonstige Räume (`G05000012654`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Palettenstellplätze (`G05000012655`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Kühlräume (`G05000012656`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Lagerräume (`G05000012657`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Personalräume (`G05000012658`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Abfallsammelräume (`G05000012659`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Betriebsdaten › Kühl- und Tiefkühlfahrzeuge (`G05000012660`)

- **Anzahl** (`F05000018860`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtfläche (m²)** (`F05000018859`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel (`G05000012650`)

- **Existiert eine Schockfrostanlage?** (`F05000018861`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Art der Waren (`G05000012661`)

- **Tierische Lebensmittel** (`F05000018862`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Pflanzliche Lebensmittel** (`F05000018863`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Arzneimittel** (`F05000018864`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Futtermittel** (`F05000018865`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Zusatzstoffe** (`F05000018866`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Chemikalien** (`F05000018867`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstiges** (`F05000018800`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige Art der Waren** (`F05000018868`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Tätigkeitsfelder (`G05000012662`)

- **Lagerung** (`F05000018869`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für die Lagerung an** (`F05000018870`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Kühlung (+2°C bis +6°C)** (`F05000018871`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für die Kühlung an.** (`F05000018872`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Tiefkühllagerung (bei min. -12°C)** (`F05000018873`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für die Tiefkühlung an.** (`F05000018874`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Schockfrosten / Einfrieren** (`F05000018875`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für die Frostung an.** (`F05000018876`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Umpacken mit Entfernen des Identitätskennzeichens und vollständiger Entfernung der Umhüllung an** (`F05000018877`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Umpacken ohne Entfernung der Umhüllung** (`F05000018880`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für das Umpacken an** (`F05000018881`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Verpacken** (`F05000018882`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für das Verpacken an** (`F05000018883`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Kommissionierung** (`F05000018884`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für die Kommissionierung an** (`F05000018885`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Transport** (`F05000018886`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für den Transport an** (`F05000018887`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstiges** (`F05000018800`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Bezeichnung der jeweiligen Waren für Sonstiges an** (`F05000018888`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Tätigkeitsfelder › Bezeichnung Waren Umpacken (`G05000012663`)

- **Geben Sie die Bezeichnung der jeweiligen Waren für das Umpacken an** (`F05000018878`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Mengenangabe in kg/Woche** (`F05000018879`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Geben Sie den Gegenstand der Fremdvermietung an (`G05000012664`)

- **Stellplätze** (`F05000018889`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Räume** (`F05000018890`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Einlagerung für Dritte** (`F05000018891`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Trifft nicht zu** (`F05000018892`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der vermieteten Stellplätze** (`F05000018893`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der vermieteten Räume** (`F05000018894`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Geben Sie den Gegenstand der Fremdanmietung an (`G05000012665`)

- **Stellplätze** (`F05000018889`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Räume** (`F05000018890`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Einlagerung für Dritte** (`F05000018891`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Trifft nicht zu** (`F05000018892`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der angemieteten Stellplätze** (`F05000018896`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der angemieteten Räume** (`F05000018897`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Geben Sie die Vertriebswege an (`G05000012666`)

- **Regional** (`F05000018898`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **National** (`F05000018899`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Bundesland** (`F05000018900`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Innergemeinschaftlich** (`F05000018901`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Drittland** (`F05000018902`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Geben Sie die Art der Rückverfolgung an (`G05000012667`)

- **EDV** (`F05000018903`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Papierform** (`F05000018904`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sind die Daten vor Ort verfügbar?** (`F05000018905`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Lagermanagement › Geben Sie die Art des Lagermanagements an (`G05000012669`)

- **EDV** (`F05000018903`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Papierform** (`F05000018904`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Lagermanagement › Kreuzen Sie Zutreffendes an (`G05000012670`)

- **Einlagerdatum abrufbar** (`F05000018906`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **MHD abrufbar** (`F05000018907`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **First In/First Out** (`F05000018908`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Regelmäßige Inventuren (`G05000012671`)

- **Finden regelmäßige Inventuren statt?** (`F05000018909`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie den Zeitabstand der Inventuren an** (`F05000018910`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Kühllager zum Betriebsspiegel › Weitere Zulassungen/Registrierungen nach der Verordnung (EG) Nr. 1069/2009 bzw. ältere Zulassungen/Registrierungen nach VO (EG) Nr. 1774/2002 (`G05000012672`)

- **Gibt es weitere Zulassungen nach der VO (EG) 1774/2002 ?** (`F05000018911`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Art und Zulassungs- / Registrierungsnummer an** (`F05000018912`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die Betriebsbereiche an (`G05000012674`)

- **Eierpackstelle** (`F05000018913`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gewinnung von Flüssigei/Eiaufschlagbetrieb** (`F05000018914`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellung von Eierprodukten  (z.B. Volleinudeln, Eierlikör)** (`F05000018915`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Eierpackstelle › Art der Eier (`G05000012676`)

- **Hühnereier** (`F05000018916`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige** (`F05000018917`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige Eier** (`F05000018918`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Eierpackstelle (`G05000012675`)

- **Geben Sie die durchschnittliche Menge an** (`F05000018919`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in tausend Eier pro Woche

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an › Schaleneier eigene Produktion (`G05000012688`)

- **Schaleneier aus eigener Produktion** (`F05000018920`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die durchschnittliche Menge an** (`F05000018927`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an › Schaleneier zugekauft (`G05000012689`)

- **Schaleneier zugekauft** (`F05000018921`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die durchschnittliche Menge an** (`F05000018927`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an › Flüssigei, gekühlt (`G05000012690`)

- **Flüssigei, gekühlt** (`F05000018922`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die durchschnittliche Menge an** (`F05000018927`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an › Flüssigei, tiefgefroren (`G05000012691`)

- **Flüssigei, tiefgefroren** (`F05000018923`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die durchschnittliche Menge an** (`F05000018927`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an › Flüssigei, entzuckert (`G05000012692`)

- **Flüssigei, entzuckert** (`F05000018924`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die durchschnittliche Menge an** (`F05000018927`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an › Eiprodukte (`G05000012693`)

- **Eiprodukte** (`F05000018925`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die durchschnittliche Menge an** (`F05000018927`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an › Sonstige Rohstoffe (`G05000012694`)

- **Sonstige Rohstoffe** (`F05000018926`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die durchschnittliche Menge an** (`F05000018927`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige Rohstoffe** (`F05000018928`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Eiprodukte zum Betriebsspiegel › Geben Sie die verwendeten Rohstoffe an (`G05000012677`)

- **Bezeichnung Eiprodukte** (`F05000018929`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Geben Sie die Betriebsarten an (`G05000012696`)

- **Versteigerungshalle** (`F05000018930`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Großmarkt** (`F05000018931`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Betrieb zur Herstellung von Fischereierzeugnissen** (`F05000018932`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Fischereifahrzeug** (`F05000018933`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gefrierschiff** (`F05000018934`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Fabrikschiff** (`F05000018935`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Angabe des Heimathafens  (Angabe im Schiffsregister)*** (`F05000018936`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Geben Sie die Betriebsbereiche an (`G05000012698`)

- **Frische Fischereierzeugnisse, ganze Fische** (`F05000018937`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Zubereitete Fischereierzeugnisse** (`F05000018938`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Verarbeitete Fischereierzeugnisse** (`F05000018939`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Durch maschinelles Ablösen von Fleisch gewonnene Fischereierzeugnisse** (`F05000018940`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie den Zeitraum der Produktion an** (`F05000018941`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Geben Sie die Betriebsbereiche an › Geben Sie die Produktionsmonate an (`G05000012639`)

- **Januar** (`F05000018812`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Februar** (`F05000018813`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **März** (`F05000018814`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **April** (`F05000018815`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Mai** (`F05000018816`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juni** (`F05000018817`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juli** (`F05000018818`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **August** (`F05000018819`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **September** (`F05000018820`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Oktober** (`F05000018821`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **November** (`F05000018822`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Dezember** (`F05000018823`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Frische Fischereierzeugnisse (`G05000012699`)

- **Kapazität der Hälterung** (`F05000018942`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg
- **Schlachtkapazität** (`F05000018943`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg
- **Maximale Schlachtkapazität** (`F05000018944`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg
- **Existieren weitere frische Fischereierzeugnisse?** (`F05000018945`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Frische Fischereierzeugnisse › Weitere Fischereierzeugnisse (`G05000012701`)

- **Weiteres Fischereierzeugnis** (`F05000018946`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Menge** (`F05000018947`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Zubereitete Fischereierzeugnisse (`G05000012709`)

- **Süßwasserfische** (`F05000018949`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Schalentiere** (`F05000018950`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Salzwasserfische** (`F05000018951`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Krustentiere** (`F05000018952`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Existieren weitere frische Fischereierzeugnisse?** (`F05000018945`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Zubereitete Fischereierzeugnisse › Weitere Fischereierzeugnisse (`G05000012701`)

- **Weiteres Fischereierzeugnis** (`F05000018946`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Menge** (`F05000018947`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Zubereitete Fischereierzeugnisse › Durchführung von Arbeitsgängen (`G05000012710`)

- **Ausnehmen** (`F05000018954`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Köpfen** (`F05000018955`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Zerteilen, Filetieren, Zerkleinern** (`F05000018956`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Verpacken** (`F05000018957`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Kühlen** (`F05000018958`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Tiefgefrieren** (`F05000018959`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Geben Sie die Menge verarbeiteter Fischereierzeugnisse an (`G05000012711`)

- **Getrocknete Fischereierzeugnisse** (`F05000018960`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Heißgeräucherte Fischereierzeugnisse** (`F05000018961`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Kaltgeräucherte Fischereierzeugnisse** (`F05000018964`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Anchosen** (`F05000018962`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Erhitzte Fischereierzeugnisse** (`F05000018963`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Gesalzene Fischereierzeugnisse** (`F05000018965`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Marinaden** (`F05000018966`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Durch maschinelles Abtrennen von Fleisch gewonnene Fischereierzeugnisse** (`F05000018967`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Existieren weitere frische Fischereierzeugnisse?** (`F05000018945`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fischereierzeugnisse zum Betriebsspiegel › Geben Sie die Menge verarbeiteter Fischereierzeugnisse an › Weitere Fischereierzeugnisse (`G05000012701`)

- **Weiteres Fischereierzeugnis** (`F05000018946`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Menge** (`F05000018947`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Betriebsarten (`G05000012737`)

- **Versandzentrum** (`F05000018971`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Reinigungszentrum** (`F05000018972`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Geben Sie die Muschelarten an. (`G05000012738`)

- **Miesmuscheln** (`F05000018973`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Austern** (`F05000018974`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige** (`F05000018975`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Verarbeitete Menge der Muscheln** (`F05000018978`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Geben Sie die Muschelarten an. › Sonstige Muscheln (`G05000012739`)

- **Geben Sie die sonstigen Muschelarten an.** (`F05000018976`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Verarbeite Menge der Muscheln.** (`F05000018977`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel (`G05000012721`)

- **Geben Sie den Zeitraum der Produktion an** (`F05000018941`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Geben Sie die Produktionsmonate an (`G05000012639`)

- **Januar** (`F05000018812`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Februar** (`F05000018813`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **März** (`F05000018814`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **April** (`F05000018815`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Mai** (`F05000018816`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juni** (`F05000018817`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juli** (`F05000018818`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **August** (`F05000018819`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **September** (`F05000018820`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Oktober** (`F05000018821`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **November** (`F05000018822`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Dezember** (`F05000018823`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Geben Sie die Produktionstage im Produktionszeitraum an. (`G05000012740`)

- **Montag** (`F05000018980`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Dienstag** (`F05000018981`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Mittwoch** (`F05000018982`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Donnerstag** (`F05000018983`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Freitag** (`F05000018984`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Samstag** (`F05000018985`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonntag** (`F05000018986`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Geben Sie die Menge der Muscheln nach Herkunft an (`G05000012741`)

- **Deutschland** (`F05000018987`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Drittland** (`F05000018988`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Andere EU-Mitgliedstaaten** (`F05000018989`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Geben Sie die Menge der Produktabgaben an (`G05000012742`)

- **Verarbeitungsbetriebe/Versandzentren** (`F05000018990`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Großhandel** (`F05000018991`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Einzelhandel/Gastronomie** (`F05000018992`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Möchten Sie weitere Abgaben angeben?** (`F05000018993`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Muscheln zum Betriebsspiegel › Geben Sie die Menge der Produktabgaben an › Weitere Abgaben (`G05000012743`)

- **Abgaben an** (`F05000018994`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Menge der anderen Produktabgaben** (`F05000018995`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Milch zum Betriebsspiegel › Geben Sie den Betriebsbereich an. (`G05000012747`)

- **Herstellung von Milcherzeugnissen (Käse, Eis, Joghurt etc.)** (`F05000018996`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sammlung von Milch** (`F05000018997`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Lagerkapazität an** (`F05000018998`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg

### Betriebsangaben › Beiblatt Milch zum Betriebsspiegel › Geben Sie die ungefähre Anlieferungsmenge an. (`G05000012748`)

- **Rohmilch** (`F05000018999`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Milch zum Betriebsspiegel › Geben Sie die ungefähre Anlieferungsmenge an. › Milcherzeugnisse (`G05000012749`)

- **Milcherzeugnisse** (`F05000019000`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Menge** (`F05000019001`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Milch zum Betriebsspiegel › Geben Sie die die verwendeten Rohstoffe an (`G05000012750`)

- **Kuhmilch** (`F05000019002`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Milch folgender weiterer Tierarten** (`F05000019003`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Weitere Tierarten** (`F05000019004`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Milcherzeugnisse** (`F05000019005`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Verarbeitungserzeugnisse tierischen Ursprungs** (`F05000019006`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Pflanzliche Lebensmittel** (`F05000019007`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Milch zum Betriebsspiegel › Geben Sie die Menge aller vorhandenen Produktarten an (`G05000012751`)

- **Produkt** (`F05000019008`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige Produktart** (`F05000019013`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Milch zum Betriebsspiegel (`G05000012745`)

- **Aus Rohmilch** (`F05000019014`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Aus Milch, die sonstigen Behandlungsverfahren unterzogen wurde** (`F05000019015`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Aus erhitzter Milch** (`F05000019016`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Gelatine und Kollagen zum Betriebsspiegel › Geben Sie den Betriebsbereich an (`G05000012754`)

- **Herstellung von Gelatine** (`F05000019017`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellung von Kollagen** (`F05000019018`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die Menge der Herstellung von Gelatine an** (`F05000019019`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Geben Sie die Menge der Herstellung von Kollagen an** (`F05000019020`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Gelatine und Kollagen zum Betriebsspiegel › Geben Sie Art und Menge der Rohstoffe für die Gelatineherstellung an (`G05000012755`)

- **Knochen** (`F05000019021`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Schweinehäute** (`F05000019022`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Wildhäute** (`F05000019023`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Fischhäute und Gräten** (`F05000019024`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Geflügelhäute** (`F05000019025`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Häute und Felle von als Nutztieren gehaltenen Wiederkäuern** (`F05000019026`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Bänder und Sehnen** (`F05000019027`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Gelatine und Kollagen zum Betriebsspiegel › Geben Sie Art und Menge der Rohstoffe für die Kollagenherstellung an (`G05000012756`)

- **Häute und Felle von als Nutztieren gehaltenen Wiederkäuern** (`F05000019026`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Schweinehäute und -knochen** (`F05000019028`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Geflügelhäute und -knochen** (`F05000019029`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Bänder** (`F05000019030`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Häute und Felle von frei lebendem Wild** (`F05000019031`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Fischhäute und Gräten** (`F05000019024`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Geben Sie die Tierarten an (`G05000012758`)

- **Huftiere** (`F05000019032`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geflügel und Hasentiere** (`F05000019033`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Farmwild** (`F05000019034`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Großwild** (`F05000019035`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Kleinwild** (`F05000019036`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Schafe** (`F05000019037`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Ziegen** (`F05000019038`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige Tierarten** (`F05000019039`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstiges** (`F05000019040`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Geben Sie die Betriebsarten an (`G05000012759`)

- **Schlachtung** (`F05000019041`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Zerlegung** (`F05000019042`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellung von Hackfleisch** (`F05000019043`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellung von Fleischzubereitungen** (`F05000019044`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellung von Separatorenfleisch** (`F05000019045`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Verarbeitung / Herstellung von Fleischerzeugnissen** (`F05000019046`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Wildbearbeitung** (`F05000019047`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Wildsammelstelle** (`F05000019048`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sammlung von rohen Schlachtfetten** (`F05000019049`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellung sonstiger Erzeugnisse (z. B. ausgeschmolzene tierische Fette und Grieben; gesalzene, erhitzte oder getrocknete Mägen, Blasen und Därme)** (`F05000019050`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Produktionszeitraum (`G05000012760`)

- **Geben Sie den Zeitraum der Produktion an** (`F05000018941`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Produktionszeitraum › Geben Sie die Produktionsmonate an (`G05000012639`)

- **Januar** (`F05000018812`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Februar** (`F05000018813`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **März** (`F05000018814`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **April** (`F05000018815`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Mai** (`F05000018816`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juni** (`F05000018817`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Juli** (`F05000018818`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **August** (`F05000018819`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **September** (`F05000018820`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Oktober** (`F05000018821`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **November** (`F05000018822`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
- **Dezember** (`F05000018823`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Geben Sie beantragte Schlachtmenge und Regelschlachttage an › Tierart (`G05000012762`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamt Schlachtmenge pro Woche** (`F05000019052`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Geben Sie beantragte Schlachtmenge und Regelschlachttage an › Beantragte Regelschlachttage (`G05000012763`)

- **Montag** (`F05000018980`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Dienstag** (`F05000018981`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Mittwoch** (`F05000018982`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Donnerstag** (`F05000018983`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Freitag** (`F05000018984`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Samstag** (`F05000018985`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonntag** (`F05000018986`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Schlachtmenge am Montag** (`F05000019053`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: als Stückzahl
- **Schlachtmenge am Dienstag** (`F05000019054`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: als Stückzahl
- **Schlachtmenge am Mittwoch** (`F05000019055`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: als Stückzahl
- **Schlachtmenge am Donnerstag** (`F05000019056`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: als Stückzahl
- **Schlachtmenge am Freitag** (`F05000019057`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: als Stückzahl
- **Schlachtmenge am Samstag** (`F05000019058`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: als Stückzahl
- **Schlachtmenge am Sonntag** (`F05000019059`) — Pflicht, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: als Stückzahl

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Höchstzahl der Tiere pro Stunde für jede Schlachtlinie (`G05000012764`)

- **Schlachtlinie (jeweils bezeichnen)** (`F05000019060`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Höchstzahl Tiere (je Tierart) / Stunde** (`F05000019061`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Kategorien und Gewichtsklassen der Tiere, für die Geräte zur Ruhigstellung oder Betäubung eingesetzt werden können (`G05000012765`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gewichtsklasse** (`F05000019062`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Bezeichnung der Anlage** (`F05000019063`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Betäubungsart** (`F05000019064`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Höchstkapazität bei jeder Stallung (Stallung benennen und Kapazität je Tierart angeben) (`G05000012766`)

- **Stallung benennen** (`F05000019065`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Kapazität** (`F05000019066`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Beantragte Zerlegemengen (ca.) in kg pro Woche (Gesamtmenge Wareneingänge) (`G05000012767`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Zerlegte kg pro Woche** (`F05000019067`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Gesamtmenge** (`F05000019068`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Beantragte Zerlegemengen (ca.) in kg pro Woche (Gesamtmenge Wareneingänge) › Beantragte Regelzerlegetage (`G05000012768`)

- **Montag** (`F05000018980`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Dienstag** (`F05000018981`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Mittwoch** (`F05000018982`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Donnerstag** (`F05000018983`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Freitag** (`F05000018984`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Samstag** (`F05000018985`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonntag** (`F05000018986`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Geben Sie das verwendete Ausgangsmaterial an (`G05000012769`)

- **Schweinefleisch** (`F05000019069`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Rindfleisch** (`F05000019070`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geflügelfleisch** (`F05000019071`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Wildfleisch** (`F05000019072`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Fischereiprodukte** (`F05000019073`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Milcherzeugnisse** (`F05000019074`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Pflanzliche Lebensmittel** (`F05000019075`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Eier und Eierzeugnisse** (`F05000019076`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstige** (`F05000019077`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie das sonstige Ausgangsmaterial an** (`F05000019078`) — Pflicht, conditional
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Geben Sie das verwendete Ausgangsmaterial an › Geben Sie die beantragte Herstellungsmengen an Fleischerzeugnissen (kg/Woche) an (`G05000012770`)

- **Beantragte Menge an Fleischerzeugnissen pro Woche** (`F05000019079`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Menge (kg/Woche)** (`F05000019080`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Geben Sie das verwendete Ausgangsmaterial an › Geben Sie die beantragte Herstellungsmengen an Fleischerzeugnissen (kg/Woche) an › Geben Sie die Fleischerzeugnisse an (`G05000012771`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Fleischerzeugnis** (`F05000019081`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Menge (kg/Woche)** (`F05000019080`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV; Art. 4 der VO (EG) 853/2004

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Lagerung der Körper und Eingeweide von erlegtem Wild, die aus einer anderen Sammelstelle aufgenommen werden, vor der Beförderung zu einem Wildbearbeitungsbetrieb (`G05000012772`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl Betriebstage pro Woche** (`F05000019082`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge pro Woche in Stück** (`F05000019083`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Wildbearbeitung › Zurichten von erlegtem Wild (`G05000012774`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Produktionstage pro Woche** (`F05000019084`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge pro Woche in Stück** (`F05000019083`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge pro Woche in kg** (`F05000019086`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Wildbearbeitung › Zurichten von Wildbret (Zerlegen von Wildkörpern und Wildfleisch): (`G05000012775`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der Zerlegetage pro Woche** (`F05000019087`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge pro Woche in kg** (`F05000019086`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Herstellung von Hackfleisch, Fleischzubereitungen und Separatorenfleisch › Geben Sie die beantragte Herstellungsmengen an Hackfleisch an (`G05000012777`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellungsmenge/Woche** (`F05000019088`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge pro Woche in kg** (`F05000019086`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der Herstellungstage pro Woche** (`F05000019089`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Herstellung von Hackfleisch, Fleischzubereitungen und Separatorenfleisch › Geben Sie die beantrage Herstellungsmengen an Fleischzubereitungen (`G05000012778`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellungsmenge/Woche** (`F05000019088`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge pro Woche in kg** (`F05000019086`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der Herstellungstage pro Woche** (`F05000019089`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Herstellung von Hackfleisch, Fleischzubereitungen und Separatorenfleisch › Geben Sie die beantragte Herstellungsmengen an Separatorenfleisch an (`G05000012779`)

- **Tierart** (`F05000019051`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Herstellungsmenge/Woche** (`F05000019088`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Gesamtmenge pro Woche in kg** (`F05000019086`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Anzahl der Herstellungstage pro Woche** (`F05000019089`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel (`G05000012757`)

- **Geben Sie die Menge an rohen Schlachtfetten an (kg/Woche)** (`F05000019090`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Herstellung von sonstigen Erzeugnissen (`G05000012780`)

- **Fette und Grieben** (`F05000019091`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Geben Sie die beantragte Menge ausgeschmolzener tierischer Fette und Grieben an** (`F05000019092`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
  - Hilfe: in kg/Woche
- **Mägen, Blasen und Därme** (`F05000019099`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Sonstiges** (`F05000019100`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Herstellung von sonstigen Erzeugnissen › Erzeugung weiterer Erzeugnisse (falls zutreffend) (`G05000012782`)

- **Gesalzene Mägen, Blasen und Därme** (`F05000019093`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **In kg/Woche:** (`F05000019094`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Erhitzte Mägen, Blasen und Därme** (`F05000019095`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **In kg/Woche** (`F05000019096`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **Getrocknete Mägen, Blasen und Därme** (`F05000019097`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **In kg/Woche** (`F05000019098`) — optional, conditional
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Betriebsangaben › Beiblatt Fleisch zum Betriebsspiegel › Herstellung von sonstigen Erzeugnissen › Sonstiges (`G05000012783`)

- **Beschreibung des Erzeugnisses** (`F05000019101`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV
- **In kg/Woche** (`F05000019102`) — Pflicht
  - Rechtsgrundlage: Art. 4 der VO (EG) 853/2004; §9 Tier-LMHV

### Nachweise EU-Zulassung Lebensmittelbetriebe › Strafverfahren (`G05000012791`)

- **Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen Sie, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?** (`F05000017675`) — Pflicht
  - Rechtsgrundlage: § 11 S. 2 Nr. 1 GewO vom 04.02.2026
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise EU-Zulassung Lebensmittelbetriebe › Auszug aus dem Gewerbezentralregister (`G05000012794`)

- **Hinweis zum Gewerbezentralregisterauszug (Belegart 9):** (`F05000017727`) — optional
  - Rechtsgrundlage: § 150 GewO
- **Die Auskunft aus dem Gewerbezentralregister** (`F05000019109`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
  - Hilfe: Die Auskunft wird direkt übersandt.
- **Datum der Beantragung** (`F05000017693`) — optional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional
  - Rechtsgrundlage: DIN 5008
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000019110`) — optional
  - Rechtsgrundlage: §9 (1) Tier-LMHV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise EU-Zulassung Lebensmittelbetriebe › Auszug aus dem Gewerbezentralregister › Name der zu überprüfenden Person (`G05000011944`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Nachweise EU-Zulassung Lebensmittelbetriebe › Bundeszentralregisterauszug (Führungszeugnis) › Name der zu überprüfenden Person (`G05000011944`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Nachweise EU-Zulassung Lebensmittelbetriebe › Bundeszentralregisterauszug (Führungszeugnis) › Auszug aus dem Bundeszentralregisterauszug (`G05000012796`)

- **Hinweis zum Bundeszentralregisterauszug (Belegart O):** (`F05000017730`) — optional
  - Rechtsgrundlage: § 30 (1) BRZG vom 19.07.2024; § 30a (1) BRZG vom 19.07.2024
- **Die Auskunft aus dem Bundeszentralregister** (`F05000019112`) — Pflicht
  - Rechtsgrundlage: §9 (1) Tier-LMHV
  - Hilfe: Die Auskunft ist bei der Wohnsitzgemeinde zur Vorlage bei einer Behörde zu beantragen. Es erfolgt die direkte Übermittlung vom Bundesamt für Justiz an die Erlaubnisbehörde. Daher ist es unerlässlich, dass Sie bei der Beantragung die genaue Anschrift der zuständigen Erlaubnisbehörde sowie den Verwendungszweck "Erlaubnisantrag für eine gewerberechtliche Tätigkeit" angeben. Die Auskunft darf nicht älter als drei Monate sein. Achten Sie auf die korrekte Belegart (Belegart O).
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Datum der geplanten Beantragung** (`F05000017694`) — optional, conditional
  - Rechtsgrundlage: DIN 5008
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000019111`) — optional, conditional
  - Rechtsgrundlage: §9 (1) Tier-LMHV
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise EU-Zulassung Lebensmittelbetriebe › Aktueller Grundrissplan (`G05000012785`)

- **Hinweis:** (`F05000019105`) — optional
  - Rechtsgrundlage: §9 Tier-LMHV
- **Der Grundrissplan** (`F05000019103`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — Pflicht, conditional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise EU-Zulassung Lebensmittelbetriebe › Betriebsplan (`G05000012786`)

- **Hinweis:** (`F05000019106`) — optional
  - Rechtsgrundlage: §9 Tier-LMHV
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise EU-Zulassung Lebensmittelbetriebe › Fügen Sie einen aktuellen Maschinen/Aufstellungsplan Ihrer Betriebsstätte bei. (`G05000012787`)

- **Hinweis:** (`F05000019107`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV
- **Der Maschinenaufstellungsplan** (`F05000019108`) — Pflicht
  - Rechtsgrundlage: §9 Tier-LMHV
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise EU-Zulassung Lebensmittelbetriebe (`G05000012792`)

- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika EU-Zulassung Lebensmittelbetriebe › Hälterung (`G05000012797`)

- **Tierart** (`F05000019113`) — Pflicht
  - Rechtsgrundlage: Referenzbasiert
- **Kapazität der Hälterung** (`F05000019114`) — Pflicht
  - Rechtsgrundlage: Art. 6 VO (EG) Nr. 852/2004
  - Hilfe: in kg

### Landesspezifika EU-Zulassung Lebensmittelbetriebe › Betäubung (`G05000012798`)

- **Tierart** (`F05000019115`) — Pflicht
  - Rechtsgrundlage: Referenzbasiert
- **Methode** (`F05000019116`) — Pflicht
  - Rechtsgrundlage: Art. 6 VO (EG) Nr. 852/2004
- **Parameter** (`F05000019117`) — Pflicht
  - Rechtsgrundlage: Art. 6 VO (EG) Nr. 852/2004

### Landesspezifika EU-Zulassung Lebensmittelbetriebe › Schlachtung (`G05000012799`)

- **Geben Sie die Schlachtart an.** (`F05000019118`) — Pflicht
  - Rechtsgrundlage: Art. 6 VO (EG) Nr. 852/2004
- **Maximale Schlachtkapazität** (`F05000019119`) — Pflicht
  - Rechtsgrundlage: Art. 6 VO (EG) Nr. 852/2004
  - Hilfe: in kg/Stunde

### Landesspezifika EU-Zulassung Lebensmittelbetriebe › Auszug aus dem Handelsregister (`G05000012800`)

- **Hinweis:** (`F05000019120`) — optional
  - Rechtsgrundlage: Referenzbasiert _(geerbt)_
- **Ein aktueller Auszug aus dem Handelsregister** (`F05000018054`) — Pflicht
  - Rechtsgrundlage: Referenzbasiert _(geerbt)_
- **Auszug aus dem Handelsregister** (`F05000018703`) — optional, conditional
  - Rechtsgrundlage: Referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie einen Auszug aus dem Handelsregister hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika EU-Zulassung Lebensmittelbetriebe › Gesellschaftsvertrag/Satzung (`G05000012801`)

- **Hinweis:** (`F05000019121`) — optional
  - Rechtsgrundlage: Referenzbasiert
- **Ein Gesellschaftsvertrag oder eine Satzung** (`F05000018387`) — Pflicht
  - Rechtsgrundlage: § 7 (1) GewO vom 04.02.2026
  - Hilfe: Im Gesellschaftsvertrag oder in der Satzung hat sich der Gesellschaftszweck bei juristischen Personen auf das ausgeübte oder auszuübende Gewerbe zu beziehen.
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:standard:basismodul:nachr:nachweisdokument.upload, Version 1.2
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Landesspezifika EU-Zulassung Lebensmittelbetriebe › Vermarktung (`G05000012802`)

- **Am Ort der Herstellung (Laden)** (`F05000019122`) — Pflicht
  - Rechtsgrundlage: Referenzbasiert
- **An Herstellerbetriebe, an Einzelhandelsbetriebe (auch eigene Filialen)** (`F05000019123`) — Pflicht
  - Rechtsgrundlage: Referenzbasiert
- **sonstige (z.B. an Großhandel, Export)** (`F05000019124`) — Pflicht
  - Rechtsgrundlage: Referenzbasiert

### Landesspezifika EU-Zulassung Lebensmittelbetriebe (`G05000012788`)

- **Laden Sie einen aktuellen Nachweis zur Einhaltung der Anlage 1 der TrinkwasserVO hoch. Beachten Sie, dass dieser Nachweis ohne Beanstandung vorliegen und nicht älter als 12 Monate sein darf.** (`F05000019125`) — optional
  - Rechtsgrundlage: Referenzbasiert
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie einen Nachweis über die Planung bezüglich der Gefahrenanalyse und kritischen Kontrollpunkte hoch.** (`F05000019126`) — optional
  - Rechtsgrundlage: Referenzbasiert
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000019127`) — optional, conditional
  - Rechtsgrundlage: Referenzbasiert
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Laden Sie einen Sachkundenachweis des Tierschutzes hoch. Beachten Sie, dass dieser für jede Tierart einzeln zu erbringen ist.** (`F05000019128`) — optional, conditional
  - Rechtsgrundlage: Referenzbasiert
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?" gleich „001 Erstantrag" oder „Daten der Betriebsstätte" oder „wahr" ist | „Daten der Betriebsstätte" | muss ausgefüllt werden | — | `R05000013983` |
| wenn „Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?" ungleich „001 Erstantrag" oder „Daten der Betriebsstätte" oder „wahr" ist | „Daten der Betriebsstätte" | darf nicht ausgefüllt werden | — | `R05000013983` |
| wenn „Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?" gleich „001 Erstantrag" oder „Betriebsbereiche" oder „wahr" ist | „Geben Sie die Bereiche des Betriebs an" | muss ausgefüllt werden | — | `R05000013984` |
| wenn „Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?" ungleich „001 Erstantrag" oder „Betriebsbereiche" oder „wahr" ist | „Geben Sie die Bereiche des Betriebs an" | darf nicht ausgefüllt werden | — | `R05000013984` |
| wenn „Großküche" gleich „wahr" oder „Beiblatt Großküche zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Großküche zum Betriebsspiegel" | muss ausgefüllt werden | — | `R05000013986` |
| wenn „Großküche" ungleich „wahr" oder „Beiblatt Großküche zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Großküche zum Betriebsspiegel" | darf nicht ausgefüllt werden | — | `R05000013986` |
| wenn „Geben Sie die Bereiche des Betriebs an" gleich „wahr" oder „Kühllager" oder „wahr" oder „Großhandel" oder „wahr" oder „Beiblatt Kühllager zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Kühllager zum Betriebsspiegel" | muss ausgefüllt werden | — | `R05000014003` |
| wenn „Geben Sie die Bereiche des Betriebs an" ungleich „wahr" oder „Kühllager" oder „wahr" oder „Großhandel" oder „wahr" oder „Beiblatt Kühllager zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Kühllager zum Betriebsspiegel" | entfällt | — | `R05000014003` |
| wenn „Ei/Eiprodukte" gleich „wahr" oder „Beiblatt Eiprodukte zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Eiprodukte zum Betriebsspiegel" | muss ausgefüllt werden | — | `R05000014019` |
| wenn „Ei/Eiprodukte" ungleich „wahr" oder „Beiblatt Eiprodukte zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Eiprodukte zum Betriebsspiegel" | darf nicht ausgefüllt werden | — | `R05000014019` |
| wenn „Fischereierzeugnisse" gleich „wahr" oder „Beiblatt Fischereiprodukte zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Fischereierzeugnisse zum Betriebsspiegel" | muss ausgefüllt werden | — | `R05000014039` |
| wenn „Fischereierzeugnisse" ungleich „wahr" oder „Beiblatt Fischereiprodukte zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Fischereierzeugnisse zum Betriebsspiegel" | darf nicht ausgefüllt werden | — | `R05000014039` |
| wenn „Lebende Muscheln" gleich „wahr" oder „Beiblatt Muscheln zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Muscheln zum Betriebsspiegel" | muss ausgefüllt werden | — | `R05000014151` |
| wenn „Lebende Muscheln" ungleich „wahr" oder „Beiblatt Muscheln zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Muscheln zum Betriebsspiegel" | darf nicht ausgefüllt werden | — | `R05000014151` |
| wenn „Milch" gleich „wahr" oder „Beiblatt Milch zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Milch zum Betriebsspiegel" | muss ausgefüllt werden | — | `R05000014167` |
| wenn „Milch" ungleich „wahr" oder „Beiblatt Milch zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Milch zum Betriebsspiegel" | darf nicht ausgefüllt werden | — | `R05000014167` |
| wenn „Gelatine/Kollagen" gleich „wahr" oder „Beiblatt Gelatine und Kollagen zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Gelatine und Kollagen zum Betriebsspiegel" | muss ausgefüllt werden | — | `R05000014177` |
| wenn „Gelatine/Kollagen" ungleich „wahr" oder „Beiblatt Gelatine und Kollagen zum Betriebsspiegel" oder „wahr" ist | „Beiblatt Gelatine und Kollagen zum Betriebsspiegel" | darf nicht ausgefüllt werden | — | `R05000014177` |
| wenn „Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?" gleich „Folgeantrag" oder „Unternehmensdaten" ist | _mehrere Felder_ | entfällt | — | `R05000014196` |
| wenn „Herstellung von Milcherzeugnissen (Käse, Eis, Joghurt etc.)" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000014256` |
| wenn „Herstellung von Milcherzeugnissen (Käse, Eis, Joghurt etc.)" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000014256` |
| wenn „Schlachtung" gleich „wahr" ist | „Laden Sie einen Sachkundenachweis des Tierschutzes hoch. Beachten Sie, dass dieser für jede Tierart einzeln zu erbringen ist." | muss ausgefüllt werden | — | `R05000014258` |
| wenn „Schlachtung" ungleich „wahr" ist | „Laden Sie einen Sachkundenachweis des Tierschutzes hoch. Beachten Sie, dass dieser für jede Tierart einzeln zu erbringen ist." | darf nicht ausgefüllt werden | — | `R05000014258` |
| wenn „Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?" gleich „002 Folgeantrag" ist | „Zustandekommen von Änderungen gegenüber dem vorherigen Antrag" | muss ausgefüllt werden | — | `R05000013941` |
| wenn „Handelt es sich bei diesem Antrag um einen Erst- oder Folgeantrag?" ungleich „002 Folgeantrag" ist | „Zustandekommen von Änderungen gegenüber dem vorherigen Antrag" | darf nicht ausgefüllt werden | — | `R05000013941` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | muss ausgefüllt werden | — | `R05000015164` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Ansprechperson" | entfällt | — | `R05000015164` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | muss ausgefüllt werden | — | `R05000015165` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Gesellschafter" | entfällt | — | `R05000015165` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Ansprechperson" | muss ausgefüllt werden | — | `R05000015166` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | entfällt | — | `R05000015166` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Nicht Natürliche Person" | muss ausgefüllt werden | — | `R05000015167` |
| wenn „Betriebsangaben" gleich einem beliebigen Wert ist | „Gesetzlicher Vertreter JP" | entfällt | — | `R05000015167` |
| wenn „Rechtsform" gleich „121000 nicht eingetragene Gesellschaft des bürgerlichen Rechts" oder „ oder 214000 " oder „ oder 261000=" oder „ oder 310000=" oder „ bis 381000=" oder „ oder 412000=" oder „ bis 412200=" oder „ oder 421000=" oder „ oder 423000=" oder „ bis 424000=" oder „ oder 510000=" oder „ bis 530000=" oder „ oder 550000=" oder „ bis 560000=" oder „ oder 590000=" oder „ bis 610000=" oder „ oder 691000=" ist | „Art der Eintragung oder des Registers" | entfällt | — | `R05000015182` |
| wenn „Rechtsform" gleich „ oder 230000=" oder „ bis 232000=" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015184` |
| wenn „Eingetragener Name" gesetzt auf einem beliebigen Wert ist | „Geschäftsbezeichnung" | muss ausgefüllt werden | — | `R05000015186` |
| wenn „Rechtsform" gleich „Genossenschaft" ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015189` |
| wenn „Rechtsform" gleich „Personenhandelsgesellschaft" oder „Partenreederei (§ 489 HGB a. F.)" oder „ oder 411100=" oder „ oder 411200 " ist | „Art der Eintragung oder des Registers" | muss ausgefüllt werden | — | `R05000015193` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | muss ausgefüllt werden | — | `R05000012512` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | entfällt | — | `R05000012512` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" gleich „002" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Anschrift in Deutschland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012493` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012494` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | entfällt und darf nicht ausgefüllt werden | — | `R05000012494` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | muss ausgefüllt werden | — | `R05000012512` |
| wenn „Staatsangehörigkeit" gesetzt auf einem beliebigen Wert ist | „Aufenthaltsgenehmigung" | entfällt | — | `R05000012512` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „001" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" gleich „002" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
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
| wenn „Wo befindet sich die Anschrift?" gleich „001" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" gleich „002" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Welchen Status hat Ihre Aufenthaltsgenehmigung?" gleich „liegt vor" ist | „Ausstellende Behörde" | muss ausgefüllt werden | — | `R05000012496` |
| wenn „Wo befindet sich die Anschrift?" gleich „001" ist | „Anschrift in Deutschland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001" ist | „Anschrift in Deutschland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" gleich „002" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `G05000011746` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `G05000011746` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „001" ist | „Anschrift Postfach" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Anschrift Postfach" | muss ausgefüllt werden | — | `G05000011745` |
| wenn „Wollen Sie eine Straßenanschrift oder eine Postfach- bzw. Großempfängeranschrift angeben?" gleich „002" ist | „Straßenanschrift Inland" | darf nicht ausgefüllt werden | — | `G05000011745` |
| wenn „Weicht die Geschäftsanschrift von der Betriebsstätte ab?" gleich „wahr" ist | „Erreichbarkeit" | wird gezeigt | — | `R05000013979` |
| wenn „Weicht die Geschäftsanschrift von der Betriebsstätte ab?" ungleich „wahr" ist | „Abweichende Anschrift der Betriebsstätte" | entfällt | — | `R05000013979` |
| wenn „Ist die lebensmittelrechtlich verantwortliche Person des Unternehmens auch für diese Betriebsstätte zuständig?" ungleich „wahr" ist | „Verantwortliche Person" | muss ausgefüllt werden | — | `R05000013978` |
| wenn „Ist die lebensmittelrechtlich verantwortliche Person des Unternehmens auch für diese Betriebsstätte zuständig?" gleich „wahr" ist | „Verantwortliche Person" | darf nicht ausgefüllt werden | — | `R05000013978` |
| wenn „Sonstige" gleich „wahr" ist | „Sonstige Angaben" | muss ausgefüllt werden | — | `R05000013981` |
| wenn „Sonstige" ungleich „wahr" ist | „Sonstige Angaben" | darf nicht ausgefüllt werden | — | `R05000013981` |
| wenn „Sonstiges" gleich „wahr" ist | „Sonstige Betriebsbereiche" | muss ausgefüllt werden | — | `R05000013985` |
| wenn „Sonstiges" ungleich „wahr" ist | „Sonstige Betriebsbereiche" | darf nicht ausgefüllt werden | — | `R05000013985` |
| wenn „Sonstiges" gleich „wahr" ist | „Sonstige Produktionsverfahren" | muss ausgefüllt werden | — | `R05000013987` |
| wenn „Sonstiges" ungleich „wahr" ist | „Sonstige Produktionsverfahren" | darf nicht ausgefüllt werden | — | `R05000013987` |
| wenn „Geben Sie den Zeitraum der Produktion an" gleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | muss ausgefüllt werden | — | `R05000013988` |
| wenn „Geben Sie den Zeitraum der Produktion an" ungleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | darf nicht ausgefüllt werden | — | `R05000013988` |
| wenn „Verwenden Sie darüber hinaus weitere Rohstoffe im Sinne von unverarbeiteten Lebensmitteln tierischen Ursprungs?" gleich „wahr" ist | „Geben Sie die weiteren Rohstoffe an" | muss ausgefüllt werden | — | `R05000013991` |
| wenn „Verwenden Sie darüber hinaus weitere Rohstoffe im Sinne von unverarbeiteten Lebensmitteln tierischen Ursprungs?" ungleich „wahr" ist | „Geben Sie die weiteren Rohstoffe an" | darf nicht ausgefüllt werden | — | `R05000013991` |
| wenn „Existieren darüber hinaus weitere Speisen?" gleich „wahr" ist | „Weitere Speisen" | muss ausgefüllt werden | — | `R05000013992` |
| wenn „Existieren darüber hinaus weitere Speisen?" ungleich „wahr" ist | „Weitere Speisen" | darf nicht ausgefüllt werden | — | `R05000013992` |
| wenn „Sonstiges" gleich „wahr" ist | „Sonstige Art der Waren" | muss ausgefüllt werden | — | `R05000014004` |
| wenn „Sonstiges" ungleich „wahr" ist | „Sonstige Art der Waren" | darf nicht ausgefüllt werden | — | `R05000014004` |
| wenn „Lagerung" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Lagerung an" | muss ausgefüllt werden | — | `R05000014005` |
| wenn „Lagerung" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Lagerung an" | darf nicht ausgefüllt werden | — | `R05000014005` |
| wenn „Kühlung (+2°C bis +6°C)" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Kühlung an." | muss ausgefüllt werden | — | `R05000014006` |
| wenn „Kühlung (+2°C bis +6°C)" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Kühlung an." | darf nicht ausgefüllt werden | — | `R05000014006` |
| wenn „Tiefkühllagerung (bei min. -12°C)" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Tiefkühlung an." | muss ausgefüllt werden | — | `R05000014007` |
| wenn „Tiefkühllagerung (bei min. -12°C)" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Tiefkühlung an." | darf nicht ausgefüllt werden | — | `R05000014007` |
| wenn „Schockfrosten / Einfrieren" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Frostung an." | muss ausgefüllt werden | — | `R05000014008` |
| wenn „Schockfrosten / Einfrieren" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Frostung an." | darf nicht ausgefüllt werden | — | `R05000014008` |
| wenn „Umpacken mit Entfernen des Identitätskennzeichens und vollständiger Entfernung der Umhüllung an" gleich „wahr" ist | „Bezeichnung Waren Umpacken" | muss ausgefüllt werden | — | `R05000014009` |
| wenn „Umpacken mit Entfernen des Identitätskennzeichens und vollständiger Entfernung der Umhüllung an" ungleich „wahr" ist | „Bezeichnung Waren Umpacken" | darf nicht ausgefüllt werden | — | `R05000014009` |
| wenn „Umpacken ohne Entfernung der Umhüllung" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für das Umpacken an" | muss ausgefüllt werden | — | `R05000014010` |
| wenn „Umpacken ohne Entfernung der Umhüllung" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für das Umpacken an" | darf nicht ausgefüllt werden | — | `R05000014010` |
| wenn „Verpacken" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für das Verpacken an" | muss ausgefüllt werden | — | `R05000014011` |
| wenn „Verpacken" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für das Verpacken an" | darf nicht ausgefüllt werden | — | `R05000014011` |
| wenn „Kommissionierung" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Kommissionierung an" | muss ausgefüllt werden | — | `R05000014012` |
| wenn „Kommissionierung" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für die Kommissionierung an" | darf nicht ausgefüllt werden | — | `R05000014012` |
| wenn „Transport" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für den Transport an" | muss ausgefüllt werden | — | `R05000014013` |
| wenn „Transport" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für den Transport an" | darf nicht ausgefüllt werden | — | `R05000014013` |
| wenn „Sonstiges" gleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für Sonstiges an" | muss ausgefüllt werden | — | `R05000014014` |
| wenn „Sonstiges" ungleich „wahr" ist | „Geben Sie die Bezeichnung der jeweiligen Waren für Sonstiges an" | darf nicht ausgefüllt werden | — | `R05000014014` |
| wenn „Stellplätze" gleich „wahr" ist | „Anzahl der vermieteten Stellplätze" | muss ausgefüllt werden | — | `R05000014015` |
| wenn „Stellplätze" ungleich „wahr" ist | „Anzahl der vermieteten Stellplätze" | darf nicht ausgefüllt werden | — | `R05000014015` |
| wenn „Räume" gleich „wahr" ist | „Anzahl der vermieteten Räume" | muss ausgefüllt werden | — | `R05000014016` |
| wenn „Räume" ungleich „wahr" ist | „Anzahl der vermieteten Räume" | darf nicht ausgefüllt werden | — | `R05000014016` |
| wenn „Stellplätze" gleich „wahr" ist | „Anzahl der angemieteten Stellplätze" | muss ausgefüllt werden | — | `R05000014017` |
| wenn „Stellplätze" ungleich „wahr" ist | „Anzahl der angemieteten Stellplätze" | darf nicht ausgefüllt werden | — | `R05000014017` |
| wenn „Räume" gleich „wahr" ist | „Anzahl der angemieteten Räume" | muss ausgefüllt werden | — | `R05000014018` |
| wenn „Räume" ungleich „wahr" ist | „Anzahl der angemieteten Räume" | darf nicht ausgefüllt werden | — | `R05000014018` |
| wenn „Eierpackstelle" gleich „wahr" ist | „Eierpackstelle" | muss ausgefüllt werden | — | `R05000014021` |
| wenn „Eierpackstelle" ungleich „wahr" ist | „Eierpackstelle" | darf nicht ausgefüllt werden | — | `R05000014021` |
| wenn „Gewinnung von Flüssigei/Eiaufschlagbetrieb" gleich „wahr" oder „Herstellung von Eierprodukten (z.B. Volleinudeln, Eierlikör)" oder „wahr" ist | „Geben Sie die verwendeten Rohstoffe an" | muss ausgefüllt werden | — | `R05000014022` |
| wenn „Gewinnung von Flüssigei/Eiaufschlagbetrieb" ungleich „wahr" oder „Herstellung von Eierprodukten (z.B. Volleinudeln, Eierlikör)" oder „wahr" ist | „Geben Sie die verwendeten Rohstoffe an" | darf nicht ausgefüllt werden | — | `R05000014022` |
| wenn „Gewinnung von Flüssigei/Eiaufschlagbetrieb" gleich „wahr" ist | „Bezeichnung Eiprodukte" | muss ausgefüllt werden | — | `R05000014038` |
| wenn „Gewinnung von Flüssigei/Eiaufschlagbetrieb" ungleich „wahr" ist | „Bezeichnung Eiprodukte" | darf nicht ausgefüllt werden | — | `R05000014038` |
| wenn „Sonstige" gleich „wahr" ist | „Sonstige Eier" | muss ausgefüllt werden | — | `R05000014020` |
| wenn „Sonstige" ungleich „wahr" ist | „Sonstige Eier" | darf nicht ausgefüllt werden | — | `R05000014020` |
| wenn „Schaleneier aus eigener Produktion" gleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | muss ausgefüllt werden | — | `R05000014030` |
| wenn „Schaleneier aus eigener Produktion" ungleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | darf nicht ausgefüllt werden | — | `R05000014030` |
| wenn „Schaleneier zugekauft" gleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | muss ausgefüllt werden | — | `R05000014031` |
| wenn „Schaleneier zugekauft" ungleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | darf nicht ausgefüllt werden | — | `R05000014031` |
| wenn „Flüssigei, gekühlt" gleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | muss ausgefüllt werden | — | `R05000014032` |
| wenn „Flüssigei, gekühlt" ungleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | darf nicht ausgefüllt werden | — | `R05000014032` |
| wenn „Flüssigei, tiefgefroren" gleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | muss ausgefüllt werden | — | `R05000014033` |
| wenn „Flüssigei, tiefgefroren" ungleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | darf nicht ausgefüllt werden | — | `R05000014033` |
| wenn „Flüssigei, entzuckert" gleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | muss ausgefüllt werden | — | `R05000014034` |
| wenn „Flüssigei, entzuckert" ungleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | darf nicht ausgefüllt werden | — | `R05000014034` |
| wenn „Eiprodukte" gleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | muss ausgefüllt werden | — | `R05000014035` |
| wenn „Eiprodukte" ungleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | darf nicht ausgefüllt werden | — | `R05000014035` |
| wenn „Sonstige Rohstoffe" gleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | muss ausgefüllt werden | — | `R05000014036` |
| wenn „Sonstige Rohstoffe" ungleich „wahr" ist | „Geben Sie die durchschnittliche Menge an" | darf nicht ausgefüllt werden | — | `R05000014036` |
| wenn „Sonstige Rohstoffe" gleich „wahr" ist | „Sonstige Rohstoffe" | muss ausgefüllt werden | — | `R05000014037` |
| wenn „Sonstige Rohstoffe" ungleich „wahr" ist | „Sonstige Rohstoffe" | darf nicht ausgefüllt werden | — | `R05000014037` |
| wenn „Frische Fischereierzeugnisse, ganze Fische" gleich „wahr" ist | „Frische Fischereierzeugnisse" | muss ausgefüllt werden | — | `R05000014148` |
| wenn „Frische Fischereierzeugnisse, ganze Fische" ungleich „wahr" ist | „Frische Fischereierzeugnisse" | darf nicht ausgefüllt werden | — | `R05000014148` |
| wenn „Zubereitete Fischereierzeugnisse" gleich „wahr" ist | „Zubereitete Fischereierzeugnisse" | muss ausgefüllt werden | — | `R05000014149` |
| wenn „Zubereitete Fischereierzeugnisse" ungleich „wahr" ist | „Zubereitete Fischereierzeugnisse" | darf nicht ausgefüllt werden | — | `R05000014149` |
| wenn „Verarbeitete Fischereierzeugnisse" gleich „wahr" ist | „Geben Sie die Menge verarbeiteter Fischereierzeugnisse an" | muss ausgefüllt werden | — | `R05000014150` |
| wenn „Verarbeitete Fischereierzeugnisse" ungleich „wahr" ist | „Geben Sie die Menge verarbeiteter Fischereierzeugnisse an" | darf nicht ausgefüllt werden | — | `R05000014150` |
| wenn „Fischereifahrzeug" gleich „wahr" oder „Gefrierschiff" oder „wahr" oder „Fabrikschiff" oder „wahr" ist | „Angabe des Heimathafens  (Angabe im Schiffsregister)*" | muss ausgefüllt werden | — | `R05000014040` |
| wenn „Fischereifahrzeug" ungleich „wahr" oder „Gefrierschiff" oder „wahr" oder „Fabrikschiff" oder „wahr" ist | „Angabe des Heimathafens  (Angabe im Schiffsregister)*" | darf nicht ausgefüllt werden | — | `R05000014040` |
| wenn „Geben Sie den Zeitraum der Produktion an" gleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | muss ausgefüllt werden | — | `R05000014041` |
| wenn „Geben Sie den Zeitraum der Produktion an" ungleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | darf nicht ausgefüllt werden | — | `R05000014041` |
| wenn „Existieren weitere frische Fischereierzeugnisse?" gleich „wahr" ist | „Weitere Fischereierzeugnisse" | muss ausgefüllt werden | — | `R05000014042` |
| wenn „Existieren weitere frische Fischereierzeugnisse?" ungleich „wahr" ist | „Weitere Fischereierzeugnisse" | darf nicht ausgefüllt werden | — | `R05000014042` |
| wenn „Existieren weitere frische Fischereierzeugnisse?" gleich „wahr" ist | „Weitere Fischereierzeugnisse" | muss ausgefüllt werden | — | `R05000014101` |
| wenn „Existieren weitere frische Fischereierzeugnisse?" ungleich „wahr" ist | „Weitere Fischereierzeugnisse" | darf nicht ausgefüllt werden | — | `R05000014101` |
| wenn „Existieren weitere frische Fischereierzeugnisse?" gleich „wahr" ist | „Weitere Fischereierzeugnisse" | muss ausgefüllt werden | — | `R05000014102` |
| wenn „Existieren weitere frische Fischereierzeugnisse?" ungleich „wahr" ist | „Weitere Fischereierzeugnisse" | darf nicht ausgefüllt werden | — | `R05000014102` |
| wenn „Geben Sie den Zeitraum der Produktion an" gleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | muss ausgefüllt werden | — | `R05000014157` |
| wenn „Geben Sie den Zeitraum der Produktion an" ungleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | darf nicht ausgefüllt werden | — | `R05000014157` |
| wenn „Sonstige" gleich „wahr" ist | „Sonstige Muscheln" | muss ausgefüllt werden | — | `R05000014152` |
| wenn „Sonstige" ungleich „wahr" ist | „Sonstige Muscheln" | darf nicht ausgefüllt werden | — | `R05000014152` |
| wenn „Miesmuscheln" gleich „wahr" oder „Austern" oder „wahr" ist | „Verarbeitete Menge der Muscheln" | muss ausgefüllt werden | — | `R05000014155` |
| wenn „Miesmuscheln" ungleich „wahr" oder „Austern" oder „wahr" ist | „Verarbeitete Menge der Muscheln" | darf nicht ausgefüllt werden | — | `R05000014155` |
| wenn „Möchten Sie weitere Abgaben angeben?" gleich „wahr" ist | „Weitere Abgaben" | muss ausgefüllt werden | — | `R05000014160` |
| wenn „Möchten Sie weitere Abgaben angeben?" ungleich „wahr" ist | „Weitere Abgaben" | darf nicht ausgefüllt werden | — | `R05000014160` |
| wenn „Milch folgender weiterer Tierarten" gleich „wahr" ist | „Weitere Tierarten" | muss ausgefüllt werden | — | `R05000014168` |
| wenn „Milch folgender weiterer Tierarten" ungleich „wahr" ist | „Weitere Tierarten" | darf nicht ausgefüllt werden | — | `R05000014168` |
| wenn „Produkt" gleich „017 Sonstiges" ist | „Sonstige Produktart" | muss ausgefüllt werden | — | `R05000014176` |
| wenn „Produkt" ungleich „017 Sonstiges" ist | „Sonstige Produktart" | darf nicht ausgefüllt werden | — | `R05000014176` |
| wenn „Herstellung von Gelatine" gleich „wahr" ist | „Geben Sie Art und Menge der Rohstoffe für die Gelatineherstellung an" | muss ausgefüllt werden | — | `R05000014180` |
| wenn „Herstellung von Gelatine" ungleich „wahr" ist | „Geben Sie Art und Menge der Rohstoffe für die Gelatineherstellung an" | darf nicht ausgefüllt werden | — | `R05000014180` |
| wenn „Herstellung von Kollagen" gleich „wahr" ist | „Geben Sie Art und Menge der Rohstoffe für die Kollagenherstellung an" | muss ausgefüllt werden | — | `R05000014181` |
| wenn „Herstellung von Kollagen" ungleich „wahr" ist | „Geben Sie Art und Menge der Rohstoffe für die Kollagenherstellung an" | darf nicht ausgefüllt werden | — | `R05000014181` |
| wenn „Herstellung von Gelatine" gleich „wahr" ist | „Geben Sie die Menge der Herstellung von Gelatine an" | muss ausgefüllt werden | — | `R05000014178` |
| wenn „Herstellung von Gelatine" ungleich „wahr" ist | „Geben Sie die Menge der Herstellung von Gelatine an" | darf nicht ausgefüllt werden | — | `R05000014178` |
| wenn „Herstellung von Gelatine" gleich „wahr" ist | „Geben Sie die Menge der Herstellung von Kollagen an" | muss ausgefüllt werden | — | `R05000014179` |
| wenn „Herstellung von Gelatine" ungleich „wahr" ist | „Geben Sie die Menge der Herstellung von Kollagen an" | darf nicht ausgefüllt werden | — | `R05000014179` |
| wenn „Wildsammelstelle" gleich „wahr" ist | „Lagerung der Körper und Eingeweide von erlegtem Wild, die aus einer anderen Sammelstelle aufgenommen werden, vor der Beförderung zu einem Wildbearbeitungsbetrieb" | muss ausgefüllt werden | — | `R05000014193` |
| wenn „Wildsammelstelle" ungleich „wahr" ist | „Lagerung der Körper und Eingeweide von erlegtem Wild, die aus einer anderen Sammelstelle aufgenommen werden, vor der Beförderung zu einem Wildbearbeitungsbetrieb" | darf nicht ausgefüllt werden | — | `R05000014193` |
| wenn „Wildbearbeitung" gleich „wahr" ist | „Wildbearbeitung" | muss ausgefüllt werden | — | `R05000014194` |
| wenn „Wildbearbeitung" ungleich „wahr" ist | „Wildbearbeitung" | darf nicht ausgefüllt werden | — | `R05000014194` |
| wenn „Herstellung von Hackfleisch" gleich „wahr" oder „Herstellung Separatorenfleisch" oder „wahr" oder „Herstellung Fleischzubereitungen" oder „wahr" ist | „Herstellung von Hackfleisch, Fleischzubereitungen und Separatorenfleisch" | muss ausgefüllt werden | — | `R05000014197` |
| wenn „Herstellung von Hackfleisch" ungleich „wahr" oder „Herstellung Separatorenfleisch" oder „wahr" oder „Herstellung Fleischzubereitungen" oder „wahr" ist | „Herstellung von Hackfleisch, Fleischzubereitungen und Separatorenfleisch" | darf nicht ausgefüllt werden | — | `R05000014197` |
| wenn „Sammlung von rohen Schlachtfetten" gleich „wahr" ist | „Geben Sie die Menge an rohen Schlachtfetten an (kg/Woche)" | muss ausgefüllt werden | — | `R05000014198` |
| wenn „Sammlung von rohen Schlachtfetten" ungleich „wahr" ist | „Geben Sie die Menge an rohen Schlachtfetten an (kg/Woche)" | darf nicht ausgefüllt werden | — | `R05000014198` |
| wenn „Herstellung sonstiger Erzeugnisse (z. B. ausgeschmolzene tierische Fette und Grieben; gesalzene, erhitzte oder getrocknete Mägen, Blasen und Därme)" gleich „wahr" ist | „Herstellung von sonstigen Erzeugnissen" | muss ausgefüllt werden | — | `R05000014199` |
| wenn „Herstellung sonstiger Erzeugnisse (z. B. ausgeschmolzene tierische Fette und Grieben; gesalzene, erhitzte oder getrocknete Mägen, Blasen und Därme)" ungleich „wahr" ist | „Herstellung von sonstigen Erzeugnissen" | darf nicht ausgefüllt werden | — | `R05000014199` |
| wenn „Sonstige Tierarten" gleich „wahr" ist | „Sonstiges" | muss ausgefüllt werden | — | `R05000014182` |
| wenn „Sonstige Tierarten" ungleich „wahr" ist | „Sonstiges" | darf nicht ausgefüllt werden | — | `R05000014182` |
| wenn „Geben Sie den Zeitraum der Produktion an" gleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | muss ausgefüllt werden | — | `R05000014183` |
| wenn „Geben Sie den Zeitraum der Produktion an" ungleich „002 Saisonbetrieb" ist | „Geben Sie die Produktionsmonate an" | darf nicht ausgefüllt werden | — | `R05000014183` |
| wenn „Montag" gleich „wahr" ist | „Schlachtmenge am Montag" | muss ausgefüllt werden | — | `R05000014184` |
| wenn „Montag" ungleich „wahr" ist | „Schlachtmenge am Montag" | darf nicht ausgefüllt werden | — | `R05000014184` |
| wenn „Dienstag" gleich „wahr" ist | „Schlachtmenge am Dienstag" | muss ausgefüllt werden | — | `R05000014185` |
| wenn „Dienstag" ungleich „wahr" ist | „Schlachtmenge am Dienstag" | darf nicht ausgefüllt werden | — | `R05000014185` |
| wenn „Mittwoch" gleich „wahr" ist | „Schlachtmenge am Mittwoch" | muss ausgefüllt werden | — | `R05000014186` |
| wenn „Mittwoch" ungleich „wahr" ist | „Schlachtmenge am Mittwoch" | darf nicht ausgefüllt werden | — | `R05000014186` |
| wenn „Donnerstag" gleich „wahr" ist | „Schlachtmenge am Donnerstag" | muss ausgefüllt werden | — | `R05000014187` |
| wenn „Donnerstag" ungleich „wahr" ist | „Schlachtmenge am Donnerstag" | darf nicht ausgefüllt werden | — | `R05000014187` |
| wenn „Freitag" gleich „wahr" ist | „Schlachtmenge am Freitag" | muss ausgefüllt werden | — | `R05000014188` |
| wenn „Freitag" ungleich „wahr" ist | „Schlachtmenge am Freitag" | darf nicht ausgefüllt werden | — | `R05000014188` |
| wenn „Samstag" gleich „wahr" ist | „Schlachtmenge am Samstag" | muss ausgefüllt werden | — | `R05000014189` |
| wenn „Samstag" ungleich „wahr" ist | „Schlachtmenge am Samstag" | darf nicht ausgefüllt werden | — | `R05000014189` |
| wenn „Sonntag" gleich „wahr" ist | „Schlachtmenge am Sonntag" | muss ausgefüllt werden | — | `R05000014190` |
| wenn „Sonntag" ungleich „wahr" ist | „Schlachtmenge am Sonntag" | darf nicht ausgefüllt werden | — | `R05000014190` |
| wenn „Sonstige" gleich „wahr" ist | „Geben Sie das sonstige Ausgangsmaterial an" | muss ausgefüllt werden | — | `R05000014191` |
| wenn „Sonstige" ungleich „wahr" ist | „Geben Sie das sonstige Ausgangsmaterial an" | darf nicht ausgefüllt werden | — | `R05000014191` |
| wenn „Beantragte Menge an Fleischerzeugnissen pro Woche" gleich „wahr" ist | „Geben Sie die Fleischerzeugnisse an" | muss ausgefüllt werden | — | `R05000014192` |
| wenn „Beantragte Menge an Fleischerzeugnissen pro Woche" ungleich „wahr" ist | „Geben Sie die Fleischerzeugnisse an" | darf nicht ausgefüllt werden | — | `R05000014192` |
| wenn „Fette und Grieben" gleich „wahr" ist | „Geben Sie die beantragte Menge ausgeschmolzener tierischer Fette und Grieben an" | muss ausgefüllt werden | — | `R05000014203` |
| wenn „Fette und Grieben" ungleich „wahr" ist | „Geben Sie die beantragte Menge ausgeschmolzener tierischer Fette und Grieben an" | darf nicht ausgefüllt werden | — | `R05000014203` |
| wenn „Mägen, Blasen und Därme" gleich „wahr" ist | „Erzeugung weiterer Erzeugnisse (falls zutreffend)" | muss ausgefüllt werden | — | `R05000014204` |
| wenn „Mägen, Blasen und Därme" ungleich „wahr" ist | „Erzeugung weiterer Erzeugnisse (falls zutreffend)" | darf nicht ausgefüllt werden | — | `R05000014204` |
| wenn „Sonstiges" gleich „wahr" ist | „Sonstiges" | muss ausgefüllt werden | — | `R05000014205` |
| wenn „Sonstiges" ungleich „wahr" ist | „Sonstiges" | darf nicht ausgefüllt werden | — | `R05000014205` |
| wenn „Gesalzene Mägen, Blasen und Därme" gleich „wahr" ist | „In kg/Woche:" | muss ausgefüllt werden | — | `R05000014200` |
| wenn „Gesalzene Mägen, Blasen und Därme" ungleich „wahr" ist | „In kg/Woche:" | darf nicht ausgefüllt werden | — | `R05000014200` |
| wenn „Erhitzte Mägen, Blasen und Därme" gleich „wahr" ist | „In kg/Woche" | muss ausgefüllt werden | — | `R05000014201` |
| wenn „Erhitzte Mägen, Blasen und Därme" ungleich „wahr" ist | „In kg/Woche" | darf nicht ausgefüllt werden | — | `R05000014201` |
| wenn „Getrocknete Mägen, Blasen und Därme" gleich „wahr" ist | „In kg/Woche" | muss ausgefüllt werden | — | `R05000014202` |
| wenn „Getrocknete Mägen, Blasen und Därme" ungleich „wahr" ist | „In kg/Woche" | darf nicht ausgefüllt werden | — | `R05000014202` |
| wenn „Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen Sie, eine Geschäftsführung, Betriebsleitung oder Leitung einer Zweigstelle Ihres Unternehmens?" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000014236` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „001 ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000014241` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „001 ist beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | — | `R05000014241` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „002 Ist noch nicht beantragt" ist | „Auszug aus dem Bundeszentralregisterauszug" | muss ausgefüllt werden | — | `R05000014242` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „002 Ist noch nicht beantragt" ist | „Datum der geplanten Beantragung" | darf nicht ausgefüllt werden | — | `R05000014242` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „003 liegt bereits vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000014243` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „003 liegt bereits vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000014243` |
| wenn „Der Grundrissplan" gleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000014207` |
| wenn „Der Grundrissplan" ungleich „wahr" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000014207` |
| wenn „Ein aktueller Auszug aus dem Handelsregister" gleich „001 liegt vor" ist | „Auszug aus dem Handelsregister" | muss ausgefüllt werden | — | `R05000014248` |
| wenn „Ein aktueller Auszug aus dem Handelsregister" ungleich „001 liegt vor" ist | „Auszug aus dem Handelsregister" | entfällt | — | `R05000014248` |
| wenn „Ein Gesellschaftsvertrag oder eine Satzung" gleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000014250` |
| wenn „Ein Gesellschaftsvertrag oder eine Satzung" ungleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000014250` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Wenn G05000012595.F05000018735 "Abfrage Erst- oder Folgeantrag" = 01 "Erstantrag" UND G05000012792.F05000018736 "Unternehmensdaten" = TRUE, dann muss G05000012792.G05000012794 "Gewerbezentralregister Lebensmittelzulassung" ausgefüllt sein.</mark> — Regel `R05000014240`
- <mark>Wenn G05000012595.F05000018735 "Abfrage Erst- oder Folgeantrag" <> 01 "Erstantrag" UND G05000012792.F05000018736 "Unternehmensdaten" <> TRUE, dann darf G05000012792.G05000012794 "Gewerbezentralregister Lebensmittelzulassung" nicht ausgefüllt sein.</mark> — Regel `R05000014240`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 190000="ausländische Personengesellschaft" bis 192000="ausländische Personengesellschaft (Nicht-EU-Recht)" oder 291000="ausländische Körperschaft des öffentlichen Rechts" oder 490000="ausländische wirtschaftliche Tätigkeit einer natürlichen Person" bis 492000="ausländisches gewerbliches Einzelunternehmen (Nicht-EU-Recht)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015176`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 682000="Freitext (Auffangtatbestand Justiz)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015177`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 213000 "Versicherungsverein auf Gegenseitigkeit; auch Pensionsfondsverein auf Gegenseitigkeit", 213100="Versicherungsverein auf Gegenseitigkeit", 213200="Pensionsfondsverein auf Gegenseitigkeit" oder 221000 "Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH ; auch Unternehmergesellschaft (haftungsbeschränkt)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000015178`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 290000="ausländische juristische Person" oder 681000="Freitext (Auffangtatbestand)" oder 683000="Ersatzwert (Auffangtatbestand Steuer)" bis 690000="ausländische Rechtsform" oder 698000="Auffangtatbestände (ausländische Rechtsform)" oder 680000="Auffangtatbestände (ohne Rechtsform-Typ)" oder 698100="sonstige ausländische Rechtsform (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015179`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 221100="Gesellschaft mit beschränkter Haftung; auch gemeinnützige GmbH" bis 221200="Unternehmergesellschaft (haftungsbeschränkt)" oder 222100="Aktiengesellschaft (AG); auch Investmentaktiengesellschaft (InvAG)" bis 222120="Investmentaktiengesellschaft (InvAG)" oder 223000="Kommanditgesellschaft auf Aktien (KGaA); auch & Co. KGaA" bis 224810="sonstige Kapitalgesellschaft (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code B "Eintragung im Handelsregister B" ausgewählt sein.</mark> — Regel `R05000015181`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 130000="sonstige rechtsfähige Personengesellschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000015183`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 211000="eingetragener Verein (e.V.)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000015185`
- <mark>WENN in F60000000319 "Eingetragener Name / Organisationsname" ein Eintrag vorgenommen wurde, DANN ist F60000000320 "Geschäftsbezeichnung / Organisationsbezeichnung" ein optionales Feld.</mark> — Regel `R05000015186`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 294000="ausländische juristische Person (EU-Recht)" oder 295000="ausländische juristische Person (Nicht-EU-Recht)" bis 298100="sonstige ausländische juristische Person des privaten Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", V "Eintragung im Vereinsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015187`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 138000="Auffangtatbestände (Personengesellschaft)", 138100="sonstige rechtsfähige Personengesellschaft (Auffangstatbestand)", 212000="Wirtschaftlicher Verein", 240000="Körperschaft des öffentlichen Rechts (KöR)" bis 243000="öffentlich-rechtliche Religionsgesellschaft", 262000="rechtsfähige Anstalt des öffentlichen Rechts (rechtsf. AöR)", 268400="sonstige juristische Person, die im Handelsregister Abteilung A eingetragen ist (Auffangtatbestand Justiz)", 410000="gewerbliches Einzelunternehmen (ohne Hausgewerbe)", 411000="eingetragenes gewerbliches Einzelunternehmen (e.K.; e.Kfm.; e.Kfr.)", 420000="sonstige wirtschaftliche Tätigkeit einer natürlichen Person", 422000="Land-/Forstwirt", 428000="Auffangtatbestände (wirtschaftliche Tätigkeit einer natürlichen Person)", 428100="sonstige wirtschaftliche Tätigkeit einer natürlichen Person (Auffangstatbestand)", 540000="Gewerbebetrieb einer Körperschaft des öffentlichen Rechts", 580000="Auffangtatbestände (wirtschaftliche Tätigkeit einer nicht-natürlichen Person)" oder 581000="sonstige wirtschaftliche Tätigkeit einer nicht-natürlichen Person (Auffangtatbestand)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code A "Eintragung im Handelsregister A" ausgewählt sein.</mark> — Regel `R05000015188`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 260000="sonstige juristische Person" oder 268000="Auffangtatbestände (juristische Person)" bis 268200="sonstige juristische Person des Privatrechts (Auffangtatbestand Steuer)" oder 268300="sonstige juristische Person des öffentlichen Rechts (Auffangtatbestand Steuer)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B", G "Eintragung im Genossenschaftsregister", S "Eintragung im Stiftungsverzeichnis" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000015190`
- <mark>WENN im Feld F6000000339 "Rechtsform (XUnternehmen)" Auswahl = 120000="Gesellschaft des bürgerlichen Rechts (BGB-Gesellschaft) ; auch eingetragene Gesellschaft des bürgerlichen Rechts" oder 123000="eingetragene Gesellschaft des bürgerlichen Rechts", DANN darf in Feld F6000000347 "Art Eintragung / Register" nur der Code GesR "Gesellschaftsregister" ausgewählt sein.</mark> — Regel `R05000015191`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 210000="rechtsfähiger Verein", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes A "Eintragung im Handelsregister A", B "Eintragung im Handelsregister B" oder V "Eintragung im Vereinsregister" ausgewählt sein.</mark> — Regel `R05000015192`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 220000="Kapitalgesellschaft", 222000="Aktiengesellschaft (AG); auch Europäische Aktiengesellschaft (SE); Investmentaktiengesellschaft (Investment-AG)", 222200="Europäische Aktiengesellschaft (SE)", 293000="ausländische Kapitalgesellschaft" oder 293100="Limited Company (unspezifisch)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes B "Eintragung im Handelsregister B", X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015194`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 252000="Europäische Genossenschaft (SCE)" oder 292000="ausländische Genossenschaft", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur einer der Codes G "Eintragung im Genossenschaftsregister" oder X "Eintragung im Ausland" ausgewählt sein.</mark> — Regel `R05000015195`
- <mark>WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswahl = 131000="Partnerschaftsgesellschaft (PartG)", DANN darf in Feld F60000000347 "Art Eintragung / Register" nur der Code P "Eintragung im Partnerschaftsregister" ausgewählt sein.</mark> — Regel `R05000015196`
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

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000012595_F05000018735["Handelt es sich bei diesem Antrag um e"] ==>|"= 001 Erstantrag, Daten der Be → required"| G05000012600["Daten der Betriebsstätte"]
  G05000012595_F05000018735["Handelt es sich bei diesem Antrag um e"] -.->|"<> 001 Erstantrag, Daten der Be → forbidden"| G05000012600["Daten der Betriebsstätte"]
  G05000012595_F05000018735["Handelt es sich bei diesem Antrag um e"] ==>|"= 001 Erstantrag, Betriebsbere → required"| G05000012599_G05000012632["Geben Sie die Bereiche des Betriebs an"]
  G05000012595_F05000018735["Handelt es sich bei diesem Antrag um e"] -.->|"<> 001 Erstantrag, Betriebsbere → forbidden"| G05000012599_G05000012632["Geben Sie die Bereiche des Betriebs an"]
  G05000012599_G05000012632_F05000018788["Großküche"] ==>|"= wahr, Beiblatt Großküche zum → required"| G05000012599_G05000012636["Beiblatt Großküche zum Betriebsspiegel"]
  G05000012599_G05000012632_F05000018788["Großküche"] -.->|"<> wahr, Beiblatt Großküche zum → forbidden"| G05000012599_G05000012636["Beiblatt Großküche zum Betriebsspiegel"]
  G05000012599_G05000012632["Geben Sie die Bereiche des Betriebs an"] ==>|"= wahr, Kühllager, wahr, Großh → required"| G05000012599_G05000012650["Beiblatt Kühllager zum Betriebsspiegel"]
  G05000012599_G05000012632["Geben Sie die Bereiche des Betriebs an"] -.->|"<> wahr, Kühllager, wahr, Großh → hide"| G05000012599_G05000012650["Beiblatt Kühllager zum Betriebsspiegel"]
  G05000012599_G05000012632_F05000018795["Ei/Eiprodukte"] ==>|"= wahr, Beiblatt Eiprodukte zu → required"| G05000012599_G05000012673["Beiblatt Eiprodukte zum Betriebsspiege"]
  G05000012599_G05000012632_F05000018795["Ei/Eiprodukte"] -.->|"<> wahr, Beiblatt Eiprodukte zu → forbidden"| G05000012599_G05000012673["Beiblatt Eiprodukte zum Betriebsspiege"]
  G05000012599_G05000012632_F05000018793["Fischereierzeugnisse"] ==>|"= wahr, Beiblatt Fischereiprod → required"| G05000012599_G05000012695["Beiblatt Fischereierzeugnisse zum Betr"]
  G05000012599_G05000012632_F05000018793["Fischereierzeugnisse"] -.->|"<> wahr, Beiblatt Fischereiprod → forbidden"| G05000012599_G05000012695["Beiblatt Fischereierzeugnisse zum Betr"]
  G05000012599_G05000012632_F05000018794["Lebende Muscheln"] ==>|"= wahr, Beiblatt Muscheln zum  → required"| G05000012599_G05000012721["Beiblatt Muscheln zum Betriebsspiegel"]
  G05000012599_G05000012632_F05000018794["Lebende Muscheln"] -.->|"<> wahr, Beiblatt Muscheln zum  → forbidden"| G05000012599_G05000012721["Beiblatt Muscheln zum Betriebsspiegel"]
  G05000012599_G05000012632_F05000018792["Milch"] ==>|"= wahr, Beiblatt Milch zum Bet → required"| G05000012599_G05000012745["Beiblatt Milch zum Betriebsspiegel"]
  G05000012599_G05000012632_F05000018792["Milch"] -.->|"<> wahr, Beiblatt Milch zum Bet → forbidden"| G05000012599_G05000012745["Beiblatt Milch zum Betriebsspiegel"]
  G05000012599_G05000012632_F05000018796["Gelatine/Kollagen"] ==>|"= wahr, Beiblatt Gelatine und  → required"| G05000012599_G05000012753["Beiblatt Gelatine und Kollagen zum Bet"]
  G05000012599_G05000012632_F05000018796["Gelatine/Kollagen"] -.->|"<> wahr, Beiblatt Gelatine und  → forbidden"| G05000012599_G05000012753["Beiblatt Gelatine und Kollagen zum Bet"]
  G05000012599_G05000012745_G05000012747_F05000018996["Herstellung von Milcherzeugnissen (Käs"] ==>|"= wahr → required"| G05000012788_F05000019127["Laden Sie den entsprechenden Nachweis "]
  G05000012599_G05000012745_G05000012747_F05000018996["Herstellung von Milcherzeugnissen (Käs"] -.->|"<> wahr → forbidden"| G05000012788_F05000019127["Laden Sie den entsprechenden Nachweis "]
  G05000012599_G05000012757_G05000012759_F05000019041["Schlachtung"] ==>|"= wahr → required"| G05000012788_F05000019128["Laden Sie einen Sachkundenachweis des "]
  G05000012599_G05000012757_G05000012759_F05000019041["Schlachtung"] -.->|"<> wahr → forbidden"| G05000012788_F05000019128["Laden Sie einen Sachkundenachweis des "]
  G05000012595_F05000018735["Handelt es sich bei diesem Antrag um e"] ==>|"= 002 Folgeantrag → required"| G05000012595_G05000012596["Zustandekommen von Änderungen gegenübe"]
  G05000012595_F05000018735["Handelt es sich bei diesem Antrag um e"] -.->|"<> 002 Folgeantrag → forbidden"| G05000012595_G05000012596["Zustandekommen von Änderungen gegenübe"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013192_G05000011759["Nicht Natürliche Person"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013192_G05000011750["Ansprechperson"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013192_G05000011759["Nicht Natürliche Person"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013192_G05000011759_G05000011757["Gesellschafter"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013192_G05000011750["Ansprechperson"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013192_G05000011759["Nicht Natürliche Person"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] ==>|"= ? → required"| G05000013192_G05000011759["Nicht Natürliche Person"]
  G05000013192_G05000011759_G05000011757_G05000011753["Betriebsangaben"] -.->|"= ? → hide"| G05000013192_G05000011759_G05000011756["Gesetzlicher Vertreter JP"]
  G05000013192_G05000013202_F60000000339["Rechtsform"] -.->|"= 121000 nicht eingetragene Ge → hide"| G05000013192_G05000013202_F60000000347["Art der Eintragung oder des Registers"]
  G05000013192_G05000013202_F60000000339["Rechtsform"] ==>|"=  oder 230000=,  bis 232000= → required"| G05000013192_G05000013202_F60000000347["Art der Eintragung oder des Registers"]
  G05000013192_G05000013202_F60000000319["Eingetragener Name"] ==>|"? ? → required"| G05000013192_G05000013202_F60000000320["Geschäftsbezeichnung"]
  G05000013192_G05000013202_F60000000339["Rechtsform"] ==>|"= Genossenschaft → required"| G05000013192_G05000013202_F60000000347["Art der Eintragung oder des Registers"]
  G05000013192_G05000013202_F60000000339["Rechtsform"] ==>|"= Personenhandelsgesellschaft, → required"| G05000013192_G05000013202_F60000000347["Art der Eintragung oder des Registers"]
  G05000013192_G05000011750_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000013192_G05000011750_G60000000083_F60000000232["Monat"]
  G05000013192_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013192_G05000011750_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013192_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide+forbidden"| G05000013192_G05000011750_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013192_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000013192_G05000011750_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013192_G05000011750_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → hide+forbidden"| G05000013192_G05000011750_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013192_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000013192_G05000011750_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013192_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 001 → forbidden"| G05000013192_G05000011750_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013192_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000013192_G05000011750_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013192_G05000011750_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 002 → forbidden"| G05000013192_G05000011750_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013192_G05000011750_G05000011749_F05000017638["Welchen Status hat Ihre Aufenthaltsgen"] ==>|"= liegt vor → required"| G05000013192_G05000011750_G05000011749_F60000000292["Ausstellende Behörde"]
  G05000013192_G05000011750_G05000011754_G05000011751_F60000000236["Staatsangehörigkeit"] ==>|"? ? → required"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000013192_G05000011750_G05000011754_G05000011751_F60000000236["Staatsangehörigkeit"] -.->|"? ? → hide"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011749["Aufenthaltsgenehmigung"]
  G05000013192_G05000011750_G05000011754_G05000011751_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000013192_G05000011750_G05000011754_G05000011751_G60000000083_F60000000232["Monat"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 → required"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 → forbidden"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745["Anschrift in Deutschland"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 → required"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 → forbidden"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G60000000191["Anschrift Ausland"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 001 → required"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 001 → forbidden"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] ==>|"= 002 → required"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G60000000087["Anschrift Postfach"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_F05000017637["Wollen Sie eine Straßenanschrift oder "] -.->|"= 002 → forbidden"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011746_G05000011745_G05000011743["Straßenanschrift Inland"]
  G05000013192_G05000011750_G05000011754_G05000011751_G05000011749_F05000017638["Welchen Status hat Ihre Aufenthaltsgen"] ==>|"= liegt vor → required"| G05000013192_G05000011750_G05000011754_G05000011751_G05000011749_F60000000292["Ausstellende Behörde"]
  G05000013192_G05000011759_G05000011746_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000013192_G05000011759_G05000011746_G05000011745["Anschrift in Deutschland"]
  unclear0["?: Wenn G05000012595.F05000018735 "Abfrage Erst- oder Folgeantr"]:::unclear
  unclear1["?: Wenn G05000012595.F05000018735 "Abfrage Erst- oder Folgeantr"]:::unclear
  unclear2["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear3["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear4["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear5["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear6["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear7["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear8["?: WENN im Feld F60000000339 "Rechtsform (XUnternehmen)" Auswah"]:::unclear
  unclear9["?: WENN in F60000000319 "Eingetragener Name / Organisationsname"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
