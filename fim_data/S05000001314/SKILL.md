---
name: antrag-s05000001314
description: Führt Antragstellende durch „Antrag einer Betriebserlaubnis für eine öffentliche Apotheke" (FIM S05000001314 2.0.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Antrag einer Betriebserlaubnis für eine öffentliche Apotheke

- **FIM-ID:** `S05000001314 2.0.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 1 (2) ApoG vom 22.12.2025; § 2 ApoG vom 22.12.2025; § 8 ApoG vom 22.12.2025; § 9 (1) ApoG vom 22.12.2025; § 10 ApoG vom 22.12.2025; § 11 ApoG vom 22.12.2025; § 14 ApoG vom 22.12.2025; § 4 (1-2) ApBetrO vom 12.12.2023; § 156 StGB vom 09.01.2026; § 161 (1) StGB vom 09.01.2026; referenzbasiert
- **Kompiliert:** 2026-08-13T15:47:55Z aus https://fimportal.de/api/v1/schemas/S05000001314/2.0.0/xdf
- **Umfang:** 246 Felder, 157 gesicherte Bedingungen, 5 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

## Antworten zur Leistung

_Quelle: LeiKa 99004002005000, bundesweiter Stammtext · Zuordnung geprüft über § 1, 2, 4 · apog._

### Wer darf den Antrag stellen?

<p>Sie müssen als Antragstellerin oder Antragsteller</p>
<ul>
 <li>voll geschäftsfähig sein.</li>
 <li>die deutsche Approbation als Apothekerin oder Apotheker besitzen.</li>
 <li>die für den Betrieb einer Apotheke erforderliche Zuverlässigkeit besitzen.</li>
 <li>
  eine eidesstattliche Erklärung abgeben,
  <ul>
   <li>dass Sie keine Vereinbarungen getroffen haben, die gegen § 8 Satz 2, § 9 Abs. 1, § 10 oder § 11 des Apothekengesetzes verstoßen und</li>
   <li>den Kauf- oder Pachtvertrag über die Apotheke sowie auf Verlangen der zuständigen Behörde auch andere Verträge, die mit der Einrichtung und dem Betrieb der Apotheke in Zusammenhang stehen, vorlegen.</li>
  </ul>
 </li>
 <li>nachweisen, dass Sie über die nach der Apothekenbetriebsordnung vorgeschriebenen Räume verfügen.</li>
 <li>gesundheitlich geeignet sein, eine Apotheke ordnungsgemäß zu leiten.</li>
 <li>mitteilen, ob Sie an einem anderen Ort in einem Mitgliedstaat der Europäischen Union oder in einem anderen Vertragsstaat des Abkommens über den Europäischen Wirtschaftsraum oder in einem Vertragsstaat, dem Deutschland und die Europäische Union vertraglich einen entsprechenden Rechtsanspruch eingeräumt haben, eine oder mehrere Apotheke betreiben.</li>
</ul>

### Welche Unterlagen werden gebraucht?

<p>Näheres zu Art und Umfang der Unterlagen können Sie mit der für Sie zuständigen Behörde klären.</p>

### Ausführliche Beschreibung

<p>Bevor Sie eine öffentliche Apotheke übernehmen oder neueröffnen, müssen Sie eine Betriebserlaubnis beantragen.</p>
<p>In den einzureichenden Unterlagen weisen Sie Ihre Qualifikation als Erlaubnisinhaberin oder Erlaubnisinhaber nach. Zudem weisen Sie nach, dass Sie über geeignete Betriebsräume verfügen. Sie versichern eidesstattlich, dass Sie gesetzliche Vorgaben einhalten.</p>
<p>Es empfiehlt sich, vor der Antragstellung Kontakt zu der für Sie zuständigen Behörde aufzunehmen, um den Umfang der notwendigen Unterlagen für Ihren Antrag zu klären.</p>


_Für 13 Länder gibt es abweichende Fassungen mit eigenen Fristen und Zuständigkeiten. Bei Fragen dazu auf die zuständige Stelle des jeweiligen Landes verweisen._


## Felder

### Ohne Gruppe

- **Stellen Sie diesen Antrag / diese Anzeige als Privatperson oder geschäftlich?** (`F05000018286`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Antragsumfang (`G05000012397`)

- **Hinweis:** (`F05000018507`) — optional
  - Rechtsgrundlage: § 2 ApoG
- **Gewünschter Gültigkeitsbeginn der Betriebserlaubnis** (`F05000018474`) — Pflicht
  - Rechtsgrundlage: DIN 5008
- **Die neue Betriebserlaubnis wird beantragt für** (`F05000018477`) — Pflicht
  - Rechtsgrundlage: § 2 (2) ApoG
- **Grund für den Antrag auf Betriebserlaubnis** (`F05000019291`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG
- **Gewünschte Anzahl der Filialen (ohne Hauptapotheke)** (`F05000018476`) — optional, conditional
  - Rechtsgrundlage: § 2 (2) ApoG
- **Betreibt die Leitung der Krankenhausapotheke weitere Apotheken im Ausland? Nähere Erläuterungen finden Sie im Hilfetext.** (`F05000018517`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 8 ApoG
  - Hilfe: Zum Ausland zählt hier :
1) in einem Mitgliedstaat der Europäischen Union oder 
2) in einem anderen Vertragsstaat des Abkommens über den Europäischen Wirtschaftsraum oder 
3) in einem Vertragsstaat, dem Deutschland oder die Europäische Union vertraglich einen entsprechenden Rechtsanspruch eingeräumt haben.

### Antragsumfang › Betriebsort der Apotheke (`G05000012435`)

- **Name der Apotheke** (`F05000018518`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 8 ApoG

### Antragsumfang › Betriebsort der Apotheke › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Antragsumfang › Betriebsort der Apotheke › Anschrift Ausland (`G60000000191`)

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

### Antragsumfang › Eidesstattliche Versicherung (`G05000012940`)

- **Eidesstattliche Versicherung** (`F05000018503`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 8 S. 2 ApoG; § 9 (1) ApoG; § 10 ApoG; § 11 ApoG; § 156 StGB; § 161 (1) StGB
- **Ich bestätige die Eidesstattliche Versicherung** (`F05000019289`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 8 S. 2 ApoG; § 9 (1) ApoG; § 10 ApoG; § 11 ApoG; § 156 StGB; § 161 (1) StGB

### Angaben zum Unternehmen › Identifikation des Unternehmens (`G05000012941`)

- **Rechtsform** (`F05000017511`) — Pflicht
  - Rechtsgrundlage: § 2 ApoG _(geerbt)_
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

### Angaben zum Unternehmen › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers (`G05000012942`)

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

### Angaben zum Unternehmen › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Angaben zum Unternehmen › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Angaben zum Unternehmen › Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers › Erreichbarkeit (`G05000011747`)

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

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Inländische Geschäftsanschrift (`G05000011862`)

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

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Verwaltungssitz (`G05000011861`)

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

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft (`G05000012944`)

- **Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?** (`F05000018285`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO
- **Gesellschafterart** (`F05000019514`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Kerndatenmodell.Gesellschafter.Art Version 1.1; verwendet urn:xoev-de:xunternehmen:codeliste:artgesellschafterpersonengesellschaft Version 1

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters (`G05000012945`)

- **Hinweis:** (`F05000017739`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020; § 5 (2) Nr. 2 PAuswG vom 21.6.2019; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020; § 5 (2) Nr. 4 PAuswG vom 21.6.2019; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020; XMeld.type.AnschriftMelderecht.Ausland.staat Version 2.4.3; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staat (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staat); Art. 6 Abs. 1 VO (EU) 2016/679; § 5 (2) PAuswG vom 21.6.2019 _(geerbt)_
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

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz (`G05000011865`)

- **Wo befindet sich die Anschrift?** (`F60000000263`) — Pflicht
  - Rechtsgrundlage: urn:xoevde:xunternehmen:kerndatenobjekt:anschriftinlandstrassenanschrift; referenzbasiert; XInneres.Meldeanschrift.strasse Version 8; XInneres.Meldeanschrift.hausnummer Version 8; XInneres.Meldeanschrift.postleitzahl Version 8; § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020; XInneres.Meldeanschrift.zusatzangaben Version 8; urn:xoev-de:xunternehmen:standard:basismodul_1.1; urn:xoev-de:xunternehmen:kerndatenobjekt:anschriftausland _(geerbt)_
  - Hilfe: Geben Sie an, ob sich die Anschrift im Inland oder im Ausland befindet.

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Straßenanschrift Inland (`G05000013177`)

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

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland › Staat (`G60000000206`)

- **Staat** (`F60000000377`) — optional
  - Rechtsgrundlage: Codeliste Staat aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsgebiete aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Codeliste Staatsangehörigkeit aus der Staats- und Gebietssystematik des Statistischen Bundesamtes; Country Codes; urn:xoev-de:xunternehmen:kerndatenobjekt:staat
- **Staat** (`F60000000357`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:xunternehmen:kerndatenobjekt:staat Version 1.1

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Hauptwohnsitz › Anschrift Ausland (`G60000000191`)

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

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Personengesellschaft › Persönliche Angaben der geschäftsführungs- und vertretungsberechtigten Gesellschafterin oder des geschäftsführungs- und vertretungsberechtigten Gesellschafters › Erreichbarkeit (`G05000011747`)

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

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft (`G05000012946`)

- **Ist der Gesellschafter eine Natürliche Person oder  eine Juristische Person oder Personengesellschaft?** (`F05000018285`) — Pflicht
  - Rechtsgrundlage: WiPG NRW; WiPG-DVO

### Angaben zum Unternehmen › Weitere Angaben zum Unternehmen › Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft › Angaben zu einer weiteren Gesellschafterin oder zu einem weiteren Gesellschafter (`G05000012542`)

- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.

### Angaben zur Einzelapotheke (`G05000012398`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Geschäftsbezeichnung** (`F60000000320`) — Pflicht
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.

### Angaben zur Einzelapotheke › Straßenanschrift Inland (`G05000012253`)

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

### Angaben zur Einzelapotheke › Angaben zu den Räumlichkeiten (`G05000012400`)

- **Geben Sie die Verfügung über die Räumlichkeiten an.** (`F05000018455`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG
- **Nutzen Sie externe Räumlichkeiten?** (`F05000018456`) — Pflicht
  - Rechtsgrundlage: § 4 (1) ApBetrO; § 4 (2) ApBetrO

### Angaben zur Einzelapotheke › Angaben zu den Räumlichkeiten › Externe Räumlichkeiten (`G05000012401`)

- **Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?** (`F05000018457`) — Pflicht, conditional
  - Rechtsgrundlage: § 4 (1) ApBetrO; § 4 (2) ApBetrO

### Angaben zur Einzelapotheke › Angaben zu den Räumlichkeiten › Externe Räumlichkeiten › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zur Einzelapotheke › Angaben zur Apothekenleitung (`G05000012402`)

- **Verfügt die Apothekenleitung über eine in Deutschland ausgestellte Approbationsurkunde?** (`F05000018484`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 3 ApoG
- **Erläuterung** (`F05000018459`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 3 ApoG _(geerbt)_

### Angaben zur Hauptapotheke (`G05000012403`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Geschäftsbezeichnung** (`F05000018446`) — Pflicht
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den Namen der Hauptapotheke ein.

### Angaben zur Hauptapotheke › Straßenanschrift Inland (`G05000012253`)

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

### Angaben zur Hauptapotheke › Angaben zu den Räumlichkeiten (`G05000012400`)

- **Geben Sie die Verfügung über die Räumlichkeiten an.** (`F05000018455`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG
- **Nutzen Sie externe Räumlichkeiten?** (`F05000018456`) — Pflicht
  - Rechtsgrundlage: § 4 (1) ApBetrO; § 4 (2) ApBetrO

### Angaben zur Hauptapotheke › Angaben zu den Räumlichkeiten › Externe Räumlichkeiten (`G05000012401`)

- **Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?** (`F05000018457`) — Pflicht, conditional
  - Rechtsgrundlage: § 4 (1) ApBetrO; § 4 (2) ApBetrO

### Angaben zur Hauptapotheke › Angaben zu den Räumlichkeiten › Externe Räumlichkeiten › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zur Hauptapotheke › Angaben zur Apothekenleitung (`G05000012402`)

- **Verfügt die Apothekenleitung über eine in Deutschland ausgestellte Approbationsurkunde?** (`F05000018484`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 3 ApoG
- **Erläuterung** (`F05000018459`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 3 ApoG _(geerbt)_

### Angaben zu Filialapotheken (`G05000012404`)

- **Art der Niederlassung** (`F60000000363`) — Pflicht
  - Rechtsgrundlage: urn: xoev-de:xunternehmen:codeliste:artniederlassung_1
- **Hinweis:** (`F05000018461`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG
- **Geschäftsbezeichnung** (`F60000000320`) — Pflicht
  - Rechtsgrundlage: XGewerbeanzeige.Betrieb.geschaeftsbezeichnung Version 2.2; XUnternehmen.Kerndatenmodell.Wirtschaftliche Tätigkeit.Geschäftsbezeichnung Version 1.1
  - Hilfe: Geben Sie den zur Außendarstellung verwendeten Namen an, der nicht im Handelsregister, Genossenschaftsregister oder Vereinsregister eingetragen ist oder davon abweicht. Beispiele: Zum lustigen Wirt, Ruck-Zuck-GbR, McLazy.
- **Die Filialapotheke** (`F05000018481`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG

### Angaben zu Filialapotheken › Straßenanschrift Inland (`G05000012253`)

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

### Angaben zu Filialapotheken › Erreichbarkeit (`G05000011747`)

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

### Angaben zu Filialapotheken › Grund des Antrags (`G05000012405`)

- **Grund für den Antrag auf Betriebserlaubnis einer Filialapotheke** (`F05000018463`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG

### Angaben zu Filialapotheken › Grund des Antrags › Neue Aufnahme einer Filiale (`G05000012407`)

- **Grund der Neuaufnahme** (`F05000018472`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG
- **Erläuterung** (`F05000018459`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG _(geerbt)_

### Angaben zu Filialapotheken › Grund des Antrags › Änderung (`G05000012406`)

- **Verlegung der Filialapotheke** (`F05000018464`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG
- **Änderung der Eigentumsverhältnisse** (`F05000018465`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG
- **Wesentliche Änderung der Apothekenbetriebsräumlichkeiten** (`F05000018466`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG
- **Wegfall der Filiale** (`F05000018467`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG; § 2 (4) S. 1 Nr. 2 ApoG

### Angaben zu Filialapotheken › Angaben zu den Räumlichkeiten (`G05000012400`)

- **Geben Sie die Verfügung über die Räumlichkeiten an.** (`F05000018455`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG
- **Nutzen Sie externe Räumlichkeiten?** (`F05000018456`) — Pflicht
  - Rechtsgrundlage: § 4 (1) ApBetrO; § 4 (2) ApBetrO

### Angaben zu Filialapotheken › Angaben zu den Räumlichkeiten › Externe Räumlichkeiten (`G05000012401`)

- **Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?** (`F05000018457`) — Pflicht, conditional
  - Rechtsgrundlage: § 4 (1) ApBetrO; § 4 (2) ApBetrO

### Angaben zu Filialapotheken › Angaben zu den Räumlichkeiten › Externe Räumlichkeiten › Straßenanschrift Inland (`G05000011743`)

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

### Angaben zu Filialapotheken › Angaben zur Filialleitung (`G05000012409`)

- **Ist die Filialleitung bereits benannt?** (`F05000018483`) — Pflicht
  - Rechtsgrundlage: § 2 (1) Nr. 3 ApoG; § 2 (5) Nr. 2 ApBetrO
- **Hinweis:** (`F05000018487`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) Nr. 3 ApoG; § 2 (5) Nr. 2 ApBetrO
- **Ist die künftige Filialleitung voll geschäftsfähig?** (`F05000018499`) — optional
  - Rechtsgrundlage: referenzbasiert

### Angaben zu Filialapotheken › Angaben zur Filialleitung › Persönliche Angaben der Filialleitung (`G05000012410`)

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

### Angaben zu Filialapotheken › Angaben zur Filialleitung › Persönliche Angaben der Filialleitung › Geburtsdatum (`G60000000083`)

- **Tag** (`F60000000231`) — optional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Monat** (`F60000000232`) — optional, conditional
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_
- **Jahr** (`F60000000233`) — Pflicht
  - Rechtsgrundlage: § 5 (2) PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1 _(geerbt)_

### Nachweise › Nachweise zur antragstellenden Person › Erlaubnis zum Betrieb einer oder mehrere Apotheken (`G05000012414`)

- **Verfügen Sie bereits über eine Erlaubnis zum Betrieb einer oder mehrerer Apotheken in der Bundesrepublik Deutschland?** (`F05000018488`) — Pflicht
  - Rechtsgrundlage: § 1 (2) ApoG
- **Bestehende Apothekenbetriebserlaubnis (Angabe der Bezeichnung der Apotheke im Dateinamen)** (`F05000018489`) — optional, conditional
  - Rechtsgrundlage: § 1 (2) ApoG
  - Hilfe: Laden Sie die bestehende Apothekenbetriebserlaubnis hoch. Geben Sie im Dateinamen die Bezeichnung der Apotheke an. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur antragstellenden Person (`G05000012413`)

- **Zum Zeitpunkt der Wirksamkeit der neu zu erteilenden Betriebserlaubnis verzichte ich hiermit auf meine derzeit bestehende Betriebserlaubnis. Ich verpflichte mich, die Papierversion der bisherigen Betriebserlaubnisurkunde im Original an die erlaubniserteilende Behörde zurückzusenden.** (`F05000018492`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
- **Eidesstattliche Versicherung** (`F05000018525`) — Pflicht
  - Rechtsgrundlage: § 1 (2) ApoG; § 2 (1) ApoG; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie die eidesstattliche Versicherung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Ist die Person voll geschäftsfähig?** (`F05000018573`) — Pflicht
  - Rechtsgrundlage: § 14 (1) S. 1  Nr. 1 ApoG
- **Deutsche Approbationsurkunde** (`F05000018574`) — Pflicht
  - Rechtsgrundlage: § 1 (2) ApoG; § 2 (1) ApoG; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie die deutsche Approbationsurkunde hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Nachweise zur antragstellenden Person › Angaben zur Zuverlässigkeit der antragstellenden Person (`G05000012420`)

- **Hinweis:** (`F05000018490`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 4 ApoG
- **Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen die betriebserlaubnisinnehabende Person?** (`F05000019297`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 4 ApoG _(geerbt)_

### Nachweise › Nachweise zur antragstellenden Person › Angaben zur Zuverlässigkeit der antragstellenden Person › Angaben zum Verfahren (`G05000012491`)

- **Name der Behörde** (`F05000019012`) — optional
  - Rechtsgrundlage: Tabelle 9 BSI TR-03123 Version 1.5.1
- **Tatbezeichnung** (`F05000018577`) — optional
  - Rechtsgrundlage: § 14 (1) S. 1  Nr. 1 ApoG
- **Aktenzeichen** (`F00000000609`) — optional
  - Rechtsgrundlage: § 14 (1) S. 1  Nr. 1 ApoG _(geerbt)_
- **Verfahrensausgang** (`F05000018579`) — optional
  - Rechtsgrundlage: § 14 (1) S. 1  Nr. 1 ApoG

### Nachweise › Nachweise zur antragstellenden Person › Angaben zur Zuverlässigkeit der antragstellenden Person › Auszug aus dem Bundeszentralregisterauszug (`G05000012460`)

- **Hinweis:** (`F05000018546`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 4 ApoG
- **Die Auskunft aus dem Bundeszentralregister** (`F05000018552`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 4 ApoG _(geerbt)_
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Nachweise › Nachweise zur antragstellenden Person › Lebenslauf (`G05000012489`)

- **Hinweis:** (`F05000018572`) — optional
  - Rechtsgrundlage: § 14 ApoG
- **Lebenslauf** (`F05000017277`) — Pflicht
  - Rechtsgrundlage: § 14 ApoG _(geerbt)_
  - Hilfe: Laden Sie den Lebenslauf hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Einzelapotheke (`G05000012426`)

- **Pachtvertrag** (`F05000018506`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Pachtvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Mietvertrag** (`F05000018581`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Mietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Untermietvertrag** (`F05000018583`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Untermietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Kauf- oder sonstiger Übertragungsvertrag oder aktueller Grundbuchauszug** (`F05000018584`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Kauf- oder sonstigen Übertragungsvertrag oder den aktuellen Grundbuchauszug hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Stellungnahme der Apothekerkammer zur Zuverlässigkeit zum Betrieb einer Apotheke** (`F05000018529`) — optional
  - Rechtsgrundlage: referenzbasiert
  - Hilfe: Laden Sie eine Stellungnahme der Apothekerkammer zur Zuverlässigkeit zum Betrieb einer Apotheke hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Einzelapotheke › Prüffähiger Raumplan (`G05000012950`)

- **Hinweis:** (`F05000019293`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO
- **Laden Sie einen prüffähigen Plan (maßstabsgetreuer Grundriss der  Apothekenbetriebsräume in ausreichender Auflösung) hoch. Der Grundriss ist mit Maßangaben zu versehen, die Bezeichnung der Betriebsräume und deren Fläche (in m²) sind anzugeben. Außerdem sind wesentliche Einrichtungsgegenstände einzuzeichnen.** (`F05000018516`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Einzelapotheke › Abfrage Finanzierungsnachweis (`G05000012429`)

- **Hinweis:** (`F05000018494`) — optional
  - Rechtsgrundlage: referenzbasiert
- **Ist ein Finanzierungsnachweis erforderlich?** (`F05000005939`) — Pflicht
  - Rechtsgrundlage: § 14 ApoG
- **Art der Finanzierung** (`F05000018495`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
- **Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten** (`F05000018505`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
  - Hilfe: Laden Sie die Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Einzelapotheke › Gesellschaftsvertrag/Satzung (`G05000012352`)

- **Ein Gesellschaftsvertrag oder eine Satzung** (`F05000018387`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO; referenzbasiert _(geerbt)_
  - Hilfe: Im Gesellschaftsvertrag oder in der Satzung hat sich der Gesellschaftszweck bei juristischen Personen auf das ausgeübte oder auszuübende Gewerbe zu beziehen.
- **Laden Sie den entsprechenden Nachweis hoch.** (`F05000017676`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO; referenzbasiert _(geerbt)_
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Hauptapotheke (`G05000012981`)

- **Pachtvertrag** (`F05000018506`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 ApBetrO _(geerbt)_
  - Hilfe: Laden Sie den Pachtvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Mietvertrag** (`F05000018581`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 ApBetrO _(geerbt)_
  - Hilfe: Laden Sie den Mietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Untermietvertrag** (`F05000018583`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 ApBetrO _(geerbt)_
  - Hilfe: Laden Sie den Untermietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Kauf- oder sonstiger Übertragungsvertrag oder aktueller Grundbuchauszug** (`F05000018584`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 ApBetrO _(geerbt)_
  - Hilfe: Laden Sie den Kauf- oder sonstigen Übertragungsvertrag oder den aktuellen Grundbuchauszug hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Verzichtserklärung der Vorbesitzerin auf ihre Betriebserlaubnis oder des Vorbesitzers auf seine Betriebserlaubnis ab dem Zeitpunkt der Übernahme** (`F05000018536`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
  - Hilfe: Laden Sie die Verzichtserklärung hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Eigentumsnachweis über die Apotheke als Gewerbebetrieb** (`F05000018539`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
  - Hilfe: Laden Sie den Eigentumsnachweis über die Apotheke als Gewerbebetrieb hoch.
Dies kann z.B. durch Vorlage eines Kaufvertrags, Schenkungsvertrags oder eines anderen Übertragungsnachweises erfolgen. Bei Neugründung kann dieser z.B. durch Vorlage von Kaufverträgen über Einrichtungsgegenstände nachgewiesen werden.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Pharmazeutische Baubeschreibung als Nachweis der Eignung der Räume gemäß § 4 ApBetrO** (`F05000018540`) — optional, conditional
  - Rechtsgrundlage: § 4 ApBetrO
  - Hilfe: Laden Sie die pharmazeutische Baubeschreibung als Nachweis der Eignung der Räume gemäß § 4 ApBetrO hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von  20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Hauptapotheke › Prüffähiger Raumplan (`G05000012950`)

- **Hinweis:** (`F05000019293`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO
- **Laden Sie einen prüffähigen Plan (maßstabsgetreuer Grundriss der  Apothekenbetriebsräume in ausreichender Auflösung) hoch. Der Grundriss ist mit Maßangaben zu versehen, die Bezeichnung der Betriebsräume und deren Fläche (in m²) sind anzugeben. Außerdem sind wesentliche Einrichtungsgegenstände einzuzeichnen.** (`F05000018516`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zur Hauptapotheke › Verzicht auf eine bestehende Betriebserlaubnis (`G05000012443`)

- **Hinweis:** (`F05000018537`) — optional
  - Rechtsgrundlage: referenzbasiert
- **Verzichtserklärung** (`F05000018601`) — optional
  - Rechtsgrundlage: referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie die Verzichtserklärung hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zu Filialapotheken (`G05000012427`)

- **Auswahl der Filialapotheke** (`F05000018528`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 5 ApoG
- **Pachtvertrag** (`F05000018506`) — optional
  - Rechtsgrundlage: § 2 (1) ApoG; § 4 (2) ApBetrO; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Pachtvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Mietvertrag** (`F05000018581`) — optional
  - Rechtsgrundlage: § 2 (1) ApoG; § 4 (2) ApBetrO; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Mietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Untermietvertrag** (`F05000018583`) — optional
  - Rechtsgrundlage: § 2 (1) ApoG; § 4 (2) ApBetrO; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Untermietvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Kauf- oder sonstiger Übertragungsvertrag oder aktueller Grundbuchauszug** (`F05000018584`) — optional
  - Rechtsgrundlage: § 2 (1) ApoG; § 4 (2) ApBetrO; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Kauf- oder sonstigen Übertragungsvertrag oder den aktuellen Grundbuchauszug hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zu Filialapotheken › Prüffähiger Raumplan (`G05000012950`)

- **Hinweis:** (`F05000019293`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO
- **Laden Sie einen prüffähigen Plan (maßstabsgetreuer Grundriss der  Apothekenbetriebsräume in ausreichender Auflösung) hoch. Der Grundriss ist mit Maßangaben zu versehen, die Bezeichnung der Betriebsräume und deren Fläche (in m²) sind anzugeben. Außerdem sind wesentliche Einrichtungsgegenstände einzuzeichnen.** (`F05000018516`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 6 ApoG; § 4 (2) ApBetrO
  - Hilfe: Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zu Filialapotheken › Abfrage Finanzierungsnachweis (`G05000012429`)

- **Hinweis:** (`F05000018494`) — optional
  - Rechtsgrundlage: referenzbasiert
- **Ist ein Finanzierungsnachweis erforderlich?** (`F05000005939`) — Pflicht
  - Rechtsgrundlage: § 14 ApoG
- **Art der Finanzierung** (`F05000018495`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
- **Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten** (`F05000018505`) — optional, conditional
  - Rechtsgrundlage: referenzbasiert
  - Hilfe: Laden Sie die Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zu Filialapotheken › Angaben zur Filialleitung (`G05000012982`)

- **Arbeitsvertrag** (`F05000018530`) — optional, conditional
  - Rechtsgrundlage: § 2 ApoG; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie den Arbeitsvertrag hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.
- **Ausweisdokument** (`F05000017328`) — optional
  - Rechtsgrundlage: § 2 ApoG; § 14 ApoG; referenzbasiert _(geerbt)_
  - Hilfe: Laden Sie ein Foto des Personalausweises, des Nationalpasses oder eines anderen (amtlichen) Ausweisdokuments hoch.  
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zu Filialapotheken › Angaben zur Filialleitung › Auszug aus dem Bundeszentralregisterauszug (`G05000012460`)

- **Hinweis:** (`F05000018546`) — optional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 4 ApoG
- **Die Auskunft aus dem Bundeszentralregister** (`F05000018552`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 4 ApoG _(geerbt)_
- **Datum der Beantragung** (`F05000017693`) — optional, conditional
  - Rechtsgrundlage: DIN 5008

### Nachweise › Angaben zu Filialapotheken › Angaben zur Filialleitung › Angaben zur Approbationsurkunde (`G05000012411`)

- **Verfügt die Filialleitung über eine in Deutschland ausgestellte Approbationsurkunde?** (`F05000018485`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 3 ApoG
- **Erläuterung** (`F05000018459`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 3 ApoG _(geerbt)_
- **Deutsche Approbationsurkunde** (`F05000018574`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 3 ApoG _(geerbt)_
  - Hilfe: Laden Sie die deutsche Approbationsurkunde hoch. Beachten Sie, dass das maximal zulässige Datenvolumen von 20 MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zu Filialapotheken › Angaben zur Filialleitung › Ärztliche Bescheinigung der Filialleitung (`G05000012481`)

- **Die ärztliche Bescheinigung ist** (`F05000018550`) — Pflicht
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 7 ApoG
  - Hilfe: Ärztliche Bescheinigung, dass die Person in gesundheitlicher Hinsicht geeignet ist, eine Apotheke ordnungsgemäß zu leiten nach § 2  Abs. 1 Nr. 7 ApoG
- **Ärztliche Bescheinigung, dass die Person in gesundheitlicher Hinsicht geeignet ist, eine Apotheke ordnungsgemäß zu leiten nach § 2  Abs. 1 Nr. 7 ApoG** (`F05000018575`) — optional, conditional
  - Rechtsgrundlage: § 2 (1) S. 1 Nr. 7 ApoG
  - Hilfe: Laden Sie die ärztliche Bescheinigung hoch, dass die Person in gesundheitlicher Hinsicht geeignet ist, eine Apotheke ordnungsgemäß zu leiten nach § 2  Abs. 1 Nr. 7 ApoG.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise › Angaben zu Filialapotheken › Angaben zur Filialleitung › Lebenslauf (`G05000012489`)

- **Hinweis:** (`F05000018572`) — optional
  - Rechtsgrundlage: § 14 ApoG
- **Lebenslauf** (`F05000017277`) — Pflicht
  - Rechtsgrundlage: § 14 ApoG _(geerbt)_
  - Hilfe: Laden Sie den Lebenslauf hoch.
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

### Nachweise (`G05000012412`)

- **Sonstige Unterlagen** (`F05000017309`) — optional
  - Rechtsgrundlage: leer, da Referenzkontext
  - Hilfe: Laden Sie weitere Unterlagen hoch, falls nötig. 
Beachten Sie, dass das maximal zulässige Datenvolumen von 20MB nicht überschritten werden darf. Akzeptierte Dateiformate sind JPG, PNG und PDF.

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „001 eine Einzelapotheke" ist | „Angaben zur Einzelapotheke" | muss ausgefüllt werden | — | `R05000014679` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" ungleich „001 eine Einzelapotheke" ist | „Angaben zur Einzelapotheke" | entfällt | — | `R05000014679` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" ist | „Angaben zur Hauptapotheke" | muss ausgefüllt werden | — | `R05000014680` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" ungleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" ist | „Angaben zur Hauptapotheke" | entfällt | — | `R05000014680` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" ist | „Angaben zu Filialapotheken" | muss ausgefüllt werden | — | `R05000014681` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" ungleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" ist | „Angaben zu Filialapotheken" | entfällt | — | `R05000014681` |
| wenn „Ist die Filialleitung bereits benannt?" gleich „wahr" ist | „Arbeitsvertrag" | muss ausgefüllt werden | — | `R05000014706` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" oder „Grund Betriebserlaubnis" oder „002 Übernahme einer bestehenden Apotheke in Eigentum" oder „003 Übernahme einer bestehenden Apotheke in Pacht" ist | „Verzichtserklärung der Vorbesitzerin auf ihre Betriebserlaubnis oder des Vorbesitzers auf seine Betriebserlaubnis ab dem Zeitpunkt der Übernahme" | muss ausgefüllt werden | — | `R05000014731` |
| wenn „Grund für den Antrag auf Betriebserlaubnis" ungleich „002 Übernahme einer bestehenden Apotheke in Eigentum" oder „003 Übernahme einer bestehenden Apotheke in Pacht" ist | „Verzichtserklärung der Vorbesitzerin auf ihre Betriebserlaubnis oder des Vorbesitzers auf seine Betriebserlaubnis ab dem Zeitpunkt der Übernahme" | entfällt | — | `R05000014731` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" oder „Grund Betriebserlaubnis" oder „004 Verlegung einer Apotheke" oder „ ODER = 006 " ist _(nur BW)_ | „Verzicht auf eine bestehende Betriebserlaubnis" | muss ausgefüllt werden | — | `R05000014732` |
| wenn „Grund für den Antrag auf Betriebserlaubnis" ungleich „004 Verlegung einer Apotheke" oder „ UND <> 006 " ist _(nur BW)_ | „Verzicht auf eine bestehende Betriebserlaubnis" | entfällt | — | `R05000014732` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" oder „Grund Betriebserlaubnis" oder „007 Sonstiger Grund" ist | „Eigentumsnachweis über die Apotheke als Gewerbebetrieb" | muss ausgefüllt werden | — | `R05000014733` |
| wenn „Grund für den Antrag auf Betriebserlaubnis" gleich „007 Sonstiger Grund" ist | „Eigentumsnachweis über die Apotheke als Gewerbebetrieb" | entfällt | — | `R05000014733` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" oder „Grund Betriebserlaubnis" oder „001 Neugründung" oder „004 Verlegung einer Apotheke" ist _(nur TH)_ | „Pharmazeutische Baubeschreibung als Nachweis der Eignung der Räume gemäß § 4 ApBetrO" | muss ausgefüllt werden | — | `R05000014734` |
| wenn „Grund für den Antrag auf Betriebserlaubnis" ungleich „001 Neugründung" oder „004 Verlegung einer Apotheke" ist _(nur TH)_ | „Pharmazeutische Baubeschreibung als Nachweis der Eignung der Räume gemäß § 4 ApBetrO" | entfällt | — | `R05000014734` |
| wenn „Grund für den Antrag auf Betriebserlaubnis" ungleich „007 Sonstiger Grund" oder „001 Neugründung" ist _(nur BW)_ | „Zum Zeitpunkt der Wirksamkeit der neu zu erteilenden Betriebserlaubnis verzichte ich hiermit auf meine derzeit bestehende Betriebserlaubnis. Ich verpflichte mich, die Papierversion der bisherigen Betriebserlaubnisurkunde im Original an die erlaubniserteilende Behörde zurückzusenden." | muss ausgefüllt werden | — | `R05000014746` |
| wenn „Grund für den Antrag auf Betriebserlaubnis" gleich „007 Sonstiger Grund" oder „001 Neugründung" ist _(nur BW)_ | „Zum Zeitpunkt der Wirksamkeit der neu zu erteilenden Betriebserlaubnis verzichte ich hiermit auf meine derzeit bestehende Betriebserlaubnis. Ich verpflichte mich, die Papierversion der bisherigen Betriebserlaubnisurkunde im Original an die erlaubniserteilende Behörde zurückzusenden." | entfällt | — | `R05000014746` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" gleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" ist | „Gewünschte Anzahl der Filialen (ohne Hauptapotheke)" | muss ausgefüllt werden | — | `R05000013554` |
| wenn „Die neue Betriebserlaubnis wird beantragt für" ungleich „002 einen Filialverbund (eine Haupt- und bis zu drei Filialapotheken)" ist | „Gewünschte Anzahl der Filialen (ohne Hauptapotheke)" | entfällt | — | `R05000013554` |
| wenn „Betreibt die Leitung der Krankenhausapotheke weitere Apotheken im Ausland? Nähere Erläuterungen finden Sie im Hilfetext." gleich „wahr" ist | „Betriebsort der Apotheke" | muss ausgefüllt werden | — | `R05000013653` |
| wenn „Betreibt die Leitung der Krankenhausapotheke weitere Apotheken im Ausland? Nähere Erläuterungen finden Sie im Hilfetext." ungleich „wahr" ist | „Betriebsort der Apotheke" | entfällt | — | `R05000013653` |
| wenn „Rechtsform" gleich „411000 e.K., e.Kfm., e.Kfr." oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers" | muss ausgefüllt werden | — | `R05000014671` |
| wenn „Rechtsform" ungleich „411000 e.K., e.Kfm., e.Kfr." oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Einzelunternehmen - Persönliche Angaben der Inhaberin oder des Inhabers" | entfällt | — | `R05000014671` |
| wenn „Rechtsform" gleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Personengesellschaft" | muss ausgefüllt werden | — | `R05000014672` |
| wenn „Rechtsform" ungleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Personengesellschaft" | entfällt | — | `R05000014672` |
| wenn „Rechtsform" gleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft" | wird gezeigt | — | `R05000014673` |
| wenn „Rechtsform" ungleich „111221 AG & Co. OHG" oder „111230 KGaA & Co. OHG" oder „112100 KG" oder „112211 GmbH & Co. KG" oder „112212 UG & Co. KG" oder „112221 AG & Co. KG" oder „112222 SE & Co. KG" oder „112230 KGaA & Co. KG" oder „112310 eG & Co. KG" oder „112500 Stiftung & Co. KG" oder „113000 EWIV" oder „121000 GbR" oder „138100 sonst. rechtsf. Personengesellschaft" oder „123000 eGbR" ist | „Angaben zur Gesellschafterin oder zum Gesellschafter einer Personengesellschaft" | entfällt | — | `R05000014673` |
| wenn „Rechtsform" gleich „121000 GbR" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014663` |
| wenn „Rechtsform" ungleich „121000 GbR" ist | „Unternehmensname" | entfällt | — | `R05000014663` |
| wenn „Rechtsform" gleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | muss ausgefüllt werden | — | `R05000014664` |
| wenn „Rechtsform" ungleich „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Unternehmensname" | entfällt | — | `R05000014664` |
| wenn „Rechtsform" ungleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | muss ausgefüllt werden | — | `R05000014665` |
| wenn „Rechtsform" gleich „121000 GbR" oder „340000 GmbH i.G." oder „350000 UG i.G." oder „360000 nichtrechtsf. Verein" oder „412000 nicht eingetr. gew. Einzelunternehmen" ist | „Eingetragener Name" | entfällt | — | `R05000014665` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Wo befindet sich die Anschrift?" gleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | muss ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" ungleich „002 außerhalb von Deutschland" ist | „Anschrift Ausland" | darf nicht ausgefüllt werden | — | `R05000012718` |
| wenn „Wo befindet sich die Anschrift?" gleich „001 in Deutschland" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000012719` |
| wenn „Wo befindet sich die Anschrift?" ungleich „001 in Deutschland" ist | „Straßenanschrift Inland" | entfällt | — | `R05000012719` |
| wenn „Nutzen Sie externe Räumlichkeiten?" gleich „wahr" ist | „Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?" | muss ausgefüllt werden | — | `R05000014676` |
| wenn „Nutzen Sie externe Räumlichkeiten?" ungleich „wahr" ist | „Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?" | entfällt | — | `R05000014676` |
| wenn „Nutzen Sie externe Räumlichkeiten?" gleich „wahr" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000014677` |
| wenn „Nutzen Sie externe Räumlichkeiten?" ungleich „wahr" ist | „Straßenanschrift Inland" | entfällt | — | `R05000014677` |
| wenn „Verfügt die Apothekenleitung über eine in Deutschland ausgestellte Approbationsurkunde?" gleich „002 Wird beantragt" ist | „Erläuterung" | muss ausgefüllt werden | — | `R05000013550` |
| wenn „Verfügt die Apothekenleitung über eine in Deutschland ausgestellte Approbationsurkunde?" ungleich „002 Wird beantragt" ist | „Erläuterung" | entfällt | — | `R05000013550` |
| wenn „Nutzen Sie externe Räumlichkeiten?" gleich „wahr" ist | „Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?" | muss ausgefüllt werden | — | `R05000014676` |
| wenn „Nutzen Sie externe Räumlichkeiten?" ungleich „wahr" ist | „Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?" | entfällt | — | `R05000014676` |
| wenn „Nutzen Sie externe Räumlichkeiten?" gleich „wahr" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000014677` |
| wenn „Nutzen Sie externe Räumlichkeiten?" ungleich „wahr" ist | „Straßenanschrift Inland" | entfällt | — | `R05000014677` |
| wenn „Verfügt die Apothekenleitung über eine in Deutschland ausgestellte Approbationsurkunde?" gleich „002 Wird beantragt" ist | „Erläuterung" | muss ausgefüllt werden | — | `R05000013550` |
| wenn „Verfügt die Apothekenleitung über eine in Deutschland ausgestellte Approbationsurkunde?" ungleich „002 Wird beantragt" ist | „Erläuterung" | entfällt | — | `R05000013550` |
| wenn „Grund für den Antrag auf Betriebserlaubnis einer Filialapotheke" gleich einem beliebigen Wert ist | „Angaben zur Filialleitung" | muss ausgefüllt werden | — | `R05000014688` |
| wenn „Grund für den Antrag auf Betriebserlaubnis einer Filialapotheke" ungleich einem beliebigen Wert ist | „Angaben zur Filialleitung" | entfällt | — | `R05000014688` |
| wenn „Grund für den Antrag auf Betriebserlaubnis einer Filialapotheke" gleich „Wegfall Filiale" oder „wahr" ist | „Angaben zu den Räumlichkeiten" | muss ausgefüllt werden | — | `R05000014690` |
| wenn „Grund für den Antrag auf Betriebserlaubnis einer Filialapotheke" gleich „003 Änderung" ist | „Änderung" | muss ausgefüllt werden | — | `R05000013551` |
| wenn „Grund für den Antrag auf Betriebserlaubnis einer Filialapotheke" gleich „003 Änderung" ist | „Änderung" | entfällt | — | `R05000013551` |
| wenn „Grund für den Antrag auf Betriebserlaubnis einer Filialapotheke" ungleich „001 Neue Aufnahme einer Filiale" ist | „Neue Aufnahme einer Filiale" | entfällt | — | `R05000013655` |
| wenn „Grund der Neuaufnahme" gleich „005 Sonstiger Grund" ist | „Erläuterung" | muss ausgefüllt werden | — | `R05000013552` |
| wenn „Grund der Neuaufnahme" gleich „005 Sonstiger Grund" ist | „Erläuterung" | entfällt | — | `R05000013552` |
| wenn „Nutzen Sie externe Räumlichkeiten?" gleich „wahr" ist | „Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?" | muss ausgefüllt werden | — | `R05000014676` |
| wenn „Nutzen Sie externe Räumlichkeiten?" ungleich „wahr" ist | „Liegt eine Betriebserlaubnis für die externen Räumlichkeiten vor?" | entfällt | — | `R05000014676` |
| wenn „Nutzen Sie externe Räumlichkeiten?" gleich „wahr" ist | „Straßenanschrift Inland" | muss ausgefüllt werden | — | `R05000014677` |
| wenn „Nutzen Sie externe Räumlichkeiten?" ungleich „wahr" ist | „Straßenanschrift Inland" | entfällt | — | `R05000014677` |
| wenn „Ist die Filialleitung bereits benannt?" ungleich „wahr" ist | „Hinweis:" | wird gezeigt | — | `R05000013559` |
| wenn „Ist die Filialleitung bereits benannt?" gleich „wahr" ist | „Hinweis:" | entfällt | — | `R05000013559` |
| wenn „Ist die Filialleitung bereits benannt?" gleich „wahr" ist | „Persönliche Angaben der Filialleitung" | muss ausgefüllt werden | — | `R05000014704` |
| wenn „Ist die Filialleitung bereits benannt?" ungleich „wahr" ist | „Persönliche Angaben der Filialleitung" | entfällt | — | `R05000014704` |
| wenn „Tag" nicht leer ist | „Monat" | muss ausgefüllt werden | — | `G60000000083` |
| wenn „Verfügen Sie bereits über eine Erlaubnis zum Betrieb einer oder mehrerer Apotheken in der Bundesrepublik Deutschland?" gleich „wahr" ist | „Bestehende Apothekenbetriebserlaubnis (Angabe der Bezeichnung der Apotheke im Dateinamen)" | muss ausgefüllt werden | — | `R05000013561` |
| wenn „Verfügen Sie bereits über eine Erlaubnis zum Betrieb einer oder mehrerer Apotheken in der Bundesrepublik Deutschland?" ungleich „wahr" ist | „Bestehende Apothekenbetriebserlaubnis (Angabe der Bezeichnung der Apotheke im Dateinamen)" | entfällt | — | `R05000013561` |
| wenn „Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen die betriebserlaubnisinnehabende Person?" gleich „wahr" ist | „Angaben zum Verfahren" | wird gezeigt | — | `R05000013578` |
| wenn „Gibt oder gab es in den letzten fünf Jahren strafrechtliche Ermittlungsverfahren, abhängige (schwebende) oder durch Freispruch, Einstellung oder Verurteilung rechtskräftig abgeschlossene Strafverfahren gegen die betriebserlaubnisinnehabende Person?" gleich „wahr" ist | „Angaben zum Verfahren" | entfällt | — | `R05000013578` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „001 ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000013622` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „001 ist beantragt" ist | „Datum der Beantragung" | entfällt | — | `R05000013622` |
| wenn „Ist ein Finanzierungsnachweis erforderlich?" gleich „wahr" ist | „Art der Finanzierung" | muss ausgefüllt werden | — | `R05000013572` |
| wenn „Ist ein Finanzierungsnachweis erforderlich?" ungleich „wahr" ist | „Art der Finanzierung" | entfällt | — | `R05000013572` |
| wenn „Art der Finanzierung" gleich „001 Finanzierung mit Fremdkapital" ist | „Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten" | muss ausgefüllt werden | — | `R05000013625` |
| wenn „Art der Finanzierung" ungleich „001 Finanzierung mit Fremdkapital" ist | „Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten" | entfällt | — | `R05000013625` |
| wenn „Ein Gesellschaftsvertrag oder eine Satzung" gleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | muss ausgefüllt werden | — | `R05000013461` |
| wenn „Ein Gesellschaftsvertrag oder eine Satzung" ungleich „001 liegt vor" ist | „Laden Sie den entsprechenden Nachweis hoch." | darf nicht ausgefüllt werden | — | `R05000013461` |
| wenn „Ist ein Finanzierungsnachweis erforderlich?" gleich „wahr" ist | „Art der Finanzierung" | muss ausgefüllt werden | — | `R05000013572` |
| wenn „Ist ein Finanzierungsnachweis erforderlich?" ungleich „wahr" ist | „Art der Finanzierung" | entfällt | — | `R05000013572` |
| wenn „Art der Finanzierung" gleich „001 Finanzierung mit Fremdkapital" ist | „Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten" | muss ausgefüllt werden | — | `R05000013625` |
| wenn „Art der Finanzierung" ungleich „001 Finanzierung mit Fremdkapital" ist | „Darlehensverträge sowie eventuelle Verträge über bestellte Sicherheiten" | entfällt | — | `R05000013625` |
| wenn „Die Auskunft aus dem Bundeszentralregister" gleich „001 ist beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | — | `R05000013622` |
| wenn „Die Auskunft aus dem Bundeszentralregister" ungleich „001 ist beantragt" ist | „Datum der Beantragung" | entfällt | — | `R05000013622` |
| wenn „Verfügt die Filialleitung über eine in Deutschland ausgestellte Approbationsurkunde?" gleich „002 Wird beantragt" ist | „Erläuterung" | muss ausgefüllt werden | — | `R05000013555` |
| wenn „Verfügt die Filialleitung über eine in Deutschland ausgestellte Approbationsurkunde?" ungleich „002 Wird beantragt" ist | „Erläuterung" | entfällt | — | `R05000013555` |
| wenn „Verfügt die Filialleitung über eine in Deutschland ausgestellte Approbationsurkunde?" gleich „001 Ja" ist _(nur BW)_ | „Deutsche Approbationsurkunde" | wird gezeigt | — | `R05000014739` |
| wenn „Verfügt die Filialleitung über eine in Deutschland ausgestellte Approbationsurkunde?" gleich „001 Ja" ist | „Deutsche Approbationsurkunde" | muss ausgefüllt werden | — | `R05000014739` |
| wenn „Verfügt die Filialleitung über eine in Deutschland ausgestellte Approbationsurkunde?" ungleich „001 Ja" ist | „Deutsche Approbationsurkunde" | entfällt | — | `R05000014739` |
| wenn „Die ärztliche Bescheinigung ist" gleich „001 vorhanden" ist | „Ärztliche Bescheinigung, dass die Person in gesundheitlicher Hinsicht geeignet ist, eine Apotheke ordnungsgemäß zu leiten nach § 2  Abs. 1 Nr. 7 ApoG" | muss ausgefüllt werden | — | `R05000014741` |
| wenn „Die ärztliche Bescheinigung ist" ungleich „001 vorhanden" ist | „Ärztliche Bescheinigung, dass die Person in gesundheitlicher Hinsicht geeignet ist, eine Apotheke ordnungsgemäß zu leiten nach § 2  Abs. 1 Nr. 7 ApoG" | entfällt | — | `R05000014741` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Im Feld F05000017511 "Rechtsform (XUnternehmen) Verwendung-in-XGewO" dürfen nur folgende Rechtsformen zur Auswahl stehen: 111100 "OHG", 111211 "GmbH & Co. OHG", 111212 "UG & Co. OHG", 111221 "AG & Co. OHG", 111230 "KGaA & Co. OHG", 120000 "GbR (auch eGbR)", 411100 "e.K.; e.Kfm.; e.Kfr."</mark> — Regel `R05000014666`
- <mark>Wenn im Datenfeld F05000018463 "Auswahl Grund" Auswahl = 001 "Neue Aufnahme einer Filiale", dann erscheint die GruppeG05000012407 "Neue Aufnahme Filiale" und muss ausgefüllt werden.</mark> — Regel `R05000013655`
- <mark>Mindestens eines der Felder F05000018464 "Verlegung", F05000018465 "Eigentumsverhältnisse", F05000018466 "Änderung Apothekenräumlichkeiten" oder F05000018467 "Wegfall Filiale" muss den Wert "wahr" haben.</mark> — Regel `R05000014687`
- <mark>Für das Bundesland BW ist die Gruppe G05000012414 "Vorhandene Apothekenbetriebserlaubnis" anzuzeigen.</mark> — Regel `R05000014745`
- <mark>Für das Bundesland BW ist die Gruppe G05000012950 "Prüffähiger Raumplan - Öffentliche Apotheke" anzuzeigen.</mark> — Regel `R05000014703`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 001 eine Einzelapotheke → required"| G05000012398["Angaben zur Einzelapotheke"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] -.->|"<> 001 eine Einzelapotheke → hide"| G05000012398["Angaben zur Einzelapotheke"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 002 einen Filialverbund (ein → required"| G05000012403["Angaben zur Hauptapotheke"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] -.->|"<> 002 einen Filialverbund (ein → hide"| G05000012403["Angaben zur Hauptapotheke"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 002 einen Filialverbund (ein → required"| G05000012404["Angaben zu Filialapotheken"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] -.->|"<> 002 einen Filialverbund (ein → hide"| G05000012404["Angaben zu Filialapotheken"]
  G05000012404_G05000012409_F05000018483["Ist die Filialleitung bereits benannt?"] ==>|"= wahr → required"| G05000012412_G05000012427_G05000012982_F05000018530["Arbeitsvertrag"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 002 einen Filialverbund (ein → required"| G05000012412_G05000012981_F05000018536["Verzichtserklärung der Vorbesitzerin a"]
  G05000012397_F05000019291["Grund für den Antrag auf Betriebserlau"] -.->|"<> 002 Übernahme einer bestehen → hide"| G05000012412_G05000012981_F05000018536["Verzichtserklärung der Vorbesitzerin a"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 002 einen Filialverbund (ein → required [BW]"| G05000012412_G05000012981_G05000012443["Verzicht auf eine bestehende Betriebse"]
  G05000012397_F05000019291["Grund für den Antrag auf Betriebserlau"] -.->|"<> 004 Verlegung einer Apotheke → hide [BW]"| G05000012412_G05000012981_G05000012443["Verzicht auf eine bestehende Betriebse"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 002 einen Filialverbund (ein → required"| G05000012412_G05000012981_F05000018539["Eigentumsnachweis über die Apotheke al"]
  G05000012397_F05000019291["Grund für den Antrag auf Betriebserlau"] -.->|"= 007 Sonstiger Grund → hide"| G05000012412_G05000012981_F05000018539["Eigentumsnachweis über die Apotheke al"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 002 einen Filialverbund (ein → required [TH]"| G05000012412_G05000012981_F05000018540["Pharmazeutische Baubeschreibung als Na"]
  G05000012397_F05000019291["Grund für den Antrag auf Betriebserlau"] -.->|"<> 001 Neugründung, 004 Verlegu → hide [TH]"| G05000012412_G05000012981_F05000018540["Pharmazeutische Baubeschreibung als Na"]
  G05000012397_F05000019291["Grund für den Antrag auf Betriebserlau"] ==>|"<> 007 Sonstiger Grund, 001 Neu → required [BW]"| G05000012412_G05000012413_F05000018492["Zum Zeitpunkt der Wirksamkeit der neu "]
  G05000012397_F05000019291["Grund für den Antrag auf Betriebserlau"] -.->|"= 007 Sonstiger Grund, 001 Neu → hide [BW]"| G05000012412_G05000012413_F05000018492["Zum Zeitpunkt der Wirksamkeit der neu "]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] ==>|"= 002 einen Filialverbund (ein → required"| G05000012397_F05000018476["Gewünschte Anzahl der Filialen (ohne H"]
  G05000012397_F05000018477["Die neue Betriebserlaubnis wird beantr"] -.->|"<> 002 einen Filialverbund (ein → hide"| G05000012397_F05000018476["Gewünschte Anzahl der Filialen (ohne H"]
  G05000012397_F05000018517["Betreibt die Leitung der Krankenhausap"] ==>|"= wahr → required"| G05000012397_G05000012435["Betriebsort der Apotheke"]
  G05000012397_F05000018517["Betreibt die Leitung der Krankenhausap"] -.->|"<> wahr → hide"| G05000012397_G05000012435["Betriebsort der Apotheke"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] ==>|"= 411000 e.K., e.Kfm., e.Kfr., → required"| G05000012471_G05000012942["Einzelunternehmen - Persönliche Angabe"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] -.->|"<> 411000 e.K., e.Kfm., e.Kfr., → hide"| G05000012471_G05000012942["Einzelunternehmen - Persönliche Angabe"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] ==>|"= 111221 AG & Co. OHG, 111230  → required"| G05000012471_G05000012943_G05000012944["Personengesellschaft"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] -.->|"<> 111221 AG & Co. OHG, 111230  → hide"| G05000012471_G05000012943_G05000012944["Personengesellschaft"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] -->|"= 111221 AG & Co. OHG, 111230  → show"| G05000012471_G05000012943_G05000012946["Angaben zur Gesellschafterin oder zum "]
  G05000012471_G05000012941_F05000017511["Rechtsform"] -.->|"<> 111221 AG & Co. OHG, 111230  → hide"| G05000012471_G05000012943_G05000012946["Angaben zur Gesellschafterin oder zum "]
  G05000012471_G05000012941_F05000017511["Rechtsform"] ==>|"= 121000 GbR → required"| G05000012471_G05000012941_F05000017734["Unternehmensname"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] -.->|"<> 121000 GbR → hide"| G05000012471_G05000012941_F05000017734["Unternehmensname"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] ==>|"= 412000 nicht eingetr. gew. E → required"| G05000012471_G05000012941_F05000017735["Unternehmensname"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] -.->|"<> 412000 nicht eingetr. gew. E → hide"| G05000012471_G05000012941_F05000017735["Unternehmensname"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] ==>|"<> 121000 GbR, 340000 GmbH i.G. → required"| G05000012471_G05000012941_F60000000319["Eingetragener Name"]
  G05000012471_G05000012941_F05000017511["Rechtsform"] -.->|"= 121000 GbR, 340000 GmbH i.G. → hide"| G05000012471_G05000012941_F60000000319["Eingetragener Name"]
  G05000012471_G05000012942_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000012471_G05000012942_G60000000083_F60000000232["Monat"]
  G05000012471_G05000012942_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000012471_G05000012942_G05000011865_G60000000191["Anschrift Ausland"]
  G05000012471_G05000012942_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → forbidden"| G05000012471_G05000012942_G05000011865_G60000000191["Anschrift Ausland"]
  G05000012471_G05000012942_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000012471_G05000012942_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000012471_G05000012942_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide"| G05000012471_G05000012942_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000012471_G05000012943_G05000012944_G05000012945_G60000000083_F60000000231["Tag"] ==>|"nicht leer ? → required"| G05000012471_G05000012943_G05000012944_G05000012945_G60000000083_F60000000232["Monat"]
  G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 002 außerhalb von Deutschlan → required"| G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_G60000000191["Anschrift Ausland"]
  G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 002 außerhalb von Deutschlan → forbidden"| G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_G60000000191["Anschrift Ausland"]
  G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] ==>|"= 001 in Deutschland → required"| G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_F60000000263["Wo befindet sich die Anschrift?"] -.->|"<> 001 in Deutschland → hide"| G05000012471_G05000012943_G05000012944_G05000012945_G05000011865_G05000013177["Straßenanschrift Inland"]
  G05000012398_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] ==>|"= wahr → required"| G05000012398_G05000012400_G05000012401_F05000018457["Liegt eine Betriebserlaubnis für die e"]
  G05000012398_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] -.->|"<> wahr → hide"| G05000012398_G05000012400_G05000012401_F05000018457["Liegt eine Betriebserlaubnis für die e"]
  G05000012398_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] ==>|"= wahr → required"| G05000012398_G05000012400_G05000012401_G05000011743["Straßenanschrift Inland"]
  G05000012398_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] -.->|"<> wahr → hide"| G05000012398_G05000012400_G05000012401_G05000011743["Straßenanschrift Inland"]
  G05000012398_G05000012402_F05000018484["Verfügt die Apothekenleitung über eine"] ==>|"= 002 Wird beantragt → required"| G05000012398_G05000012402_F05000018459["Erläuterung"]
  G05000012398_G05000012402_F05000018484["Verfügt die Apothekenleitung über eine"] -.->|"<> 002 Wird beantragt → hide"| G05000012398_G05000012402_F05000018459["Erläuterung"]
  G05000012403_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] ==>|"= wahr → required"| G05000012403_G05000012400_G05000012401_F05000018457["Liegt eine Betriebserlaubnis für die e"]
  G05000012403_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] -.->|"<> wahr → hide"| G05000012403_G05000012400_G05000012401_F05000018457["Liegt eine Betriebserlaubnis für die e"]
  G05000012403_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] ==>|"= wahr → required"| G05000012403_G05000012400_G05000012401_G05000011743["Straßenanschrift Inland"]
  G05000012403_G05000012400_F05000018456["Nutzen Sie externe Räumlichkeiten?"] -.->|"<> wahr → hide"| G05000012403_G05000012400_G05000012401_G05000011743["Straßenanschrift Inland"]
  G05000012403_G05000012402_F05000018484["Verfügt die Apothekenleitung über eine"] ==>|"= 002 Wird beantragt → required"| G05000012403_G05000012402_F05000018459["Erläuterung"]
  G05000012403_G05000012402_F05000018484["Verfügt die Apothekenleitung über eine"] -.->|"<> 002 Wird beantragt → hide"| G05000012403_G05000012402_F05000018459["Erläuterung"]
  G05000012404_G05000012405_F05000018463["Grund für den Antrag auf Betriebserlau"] ==>|"= ? → required"| G05000012404_G05000012409["Angaben zur Filialleitung"]
  G05000012404_G05000012405_F05000018463["Grund für den Antrag auf Betriebserlau"] -.->|"<> ? → hide"| G05000012404_G05000012409["Angaben zur Filialleitung"]
  G05000012404_G05000012405_F05000018463["Grund für den Antrag auf Betriebserlau"] ==>|"= Wegfall Filiale, wahr → required"| G05000012404_G05000012400["Angaben zu den Räumlichkeiten"]
  G05000012404_G05000012405_F05000018463["Grund für den Antrag auf Betriebserlau"] ==>|"= 003 Änderung → required"| G05000012404_G05000012405_G05000012406["Änderung"]
  G05000012404_G05000012405_F05000018463["Grund für den Antrag auf Betriebserlau"] -.->|"= 003 Änderung → hide"| G05000012404_G05000012405_G05000012406["Änderung"]
  unclear0["?: Im Feld F05000017511 "Rechtsform (XUnternehmen) Verwendung-i"]:::unclear
  unclear1["?: Wenn im Datenfeld F05000018463 "Auswahl Grund" Auswahl = 001"]:::unclear
  unclear2["?: Mindestens eines der Felder F05000018464 "Verlegung", F05000"]:::unclear
  unclear3["?: Für das Bundesland BW ist die Gruppe G05000012414 "Vorhanden"]:::unclear
  unclear4["?: Für das Bundesland BW ist die Gruppe G05000012950 "Prüffähig"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
