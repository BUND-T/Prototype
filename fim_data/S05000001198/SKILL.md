---
name: antrag-s05000001198
description: Führt Antragstellende durch „Erlaubnis als Finanzanlagenvermittler beantragen" (FIM S05000001198 3.3.0). Fragt nur, was in der jeweiligen Situation gebraucht wird, und begründet jede Frage mit ihrer Rechtsgrundlage.
---

# Erlaubnis als Finanzanlagenvermittler beantragen

- **FIM-ID:** `S05000001198 3.3.0` · **Reifegrad:** fachlich freigegeben (silber)
- **Rechtsgrundlagen:** § 34f Abs 1 Gewerbeordnung (GewO) Finanzanlagenvermittlungsverordnung § 11a Abs. 3a GewO
- **Kompiliert:** 2026-08-13T15:37:52Z aus https://fimportal.de/api/v1/schemas/S05000001198/3.3.0/xdf
- **Umfang:** 255 Felder, 53 gesicherte Bedingungen, 1 ungeklärt

## Verbindliche Arbeitsweise

1. **`graph.json` entscheidet, nicht du.** Ob ein Feld gebraucht wird, welcher Nachweis fehlt und welche Bedingung gilt, steht dort. Leite das nie selbst ab.
2. **Übersetze nur.** Deine Aufgabe ist Alltagssprache ↔ Feldwert. Nenne auf Nachfrage die amtliche Formulierung und die Rechtsgrundlage.
3. **Frage nur, was offen ist.** Felder, deren Bedingung nach den bisherigen Antworten nicht erfüllt ist, entfallen — frage sie nicht ab.
4. **Bei ungeklärten Regeln sag das.** Der Abschnitt „Ungeklärte Regeln" enthält Bedingungen, die nicht maschinell gelesen werden konnten. Rate dort nicht, sondern verweise auf die zuständige Stelle.

## Felder

### Antragsart (`G05000010453`)

- **Möchten Sie den Antrag als natürliche oder als juristische Person stellen?** (`F05000016480`) — Pflicht
  - Rechtsgrundlage: XUnternehmen Rechtsformen
- **Soll der Antrag auf Erlaubniserteilung und/oder Eintragung in das Vermittlerregister gestellt werden?** (`F05000016369`) — Pflicht
  - Rechtsgrundlage: § 34f Abs. 1 Gewerbeordnung; §§ 34f Absatz 5 i. V. m. 11a Absatz 1 Gewerbeordnung
  - Hilfe: Wenn Sie eine Tätigkeit als Finanzanlagenvermittler:in nach § 34f Absatz 1 GewO aufnehmen möchten, sind Sie zum einen verpflichtet, die Erlaubnis als Finanzanlagenvermittler:in einzuholen. Zum anderen sind Sie verpflichtet, sich unverzüglich nach Aufnahme Ihrer Tätigkeit in das Vermittlerregister nach §§ 34f Absatz 5, 11a Absatz 1 GewO eintragen zu lassen. Der Antrag auf Eintragung in das Vermittlerregister kann gleichzeitig mit dem Erlaubnisantrag gestellt werden.

### Person › Angaben zur antragstellenden Person (`G05000010367`)

- **IHK-Identnummer** (`F05000007410`) — optional
  - Rechtsgrundlage: § 34 Gewerbeordnung
  - Hilfe: Geben Sie hier Ihre 10-stellige IHK-Identnummer an. Diese haben Sie von der zuständigen IHK zu Beginn der Mitgliedschaft erhalten.
- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsdatum** (`F05000016340`) — Pflicht
  - Rechtsgrundlage: DIN 5008
  - Hilfe: Bitte geben Sie das Geburtsdatum an (Tag, Monat und Jahr).
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Person › Angaben zur antragstellenden Person › Anschrift Hauptwohnsitz (`G05000010369`)

- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016370`) — optional
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:anschrift
  - Hilfe: z.B. Hinterhaus, Gartenhaus.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **E-Mail-Adresse** (`F60000000242`) — Pflicht
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Mobilfunknummer** (`F05000016214`) — optional
  - Rechtsgrundlage: ITU E.124
  - Hilfe: Geben Sie bitte bei Mobilfunknummern innerhalb Deutschlands zuerst die Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, z.B. (0211) 12345678. Geben Sie bitte bei Telefonnummern außerhalb von Deutschland zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, z.B. +49 211 123456789.
- **Bestanden in den letzten fünf Jahren abweichende Meldeanschriften?** (`F05000016245`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung

### Person › Angaben zur antragstellenden Person › Anschrift Hauptwohnsitz › Abweichende Meldeanschriften der letzten 5 Jahre (`G05000010363`)

- **Von** (`F05000016235`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für den Anfang des Zeitraumes an.
- **Bis** (`F05000016236`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für das Ende des Zeitraums an.
- **Straße** (`F05000016237`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie den Namen der Straße an.
- **Hausnummer** (`F05000016239`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016242`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an, zum Beispiel "Hinterhaus".
- **Postleitzahl** (`F05000016240`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F05000016241`) — Pflicht
  - Rechtsgrundlage: Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie hier den Namen des Ortes (Gemeinde, Ortschaft oder Stadt) an.
- **Land** (`F05000016243`) — Pflicht
  - Rechtsgrundlage: Xmeld.Anschrift.Melderecht.Ausland.staat Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staatsgebiete (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsgebiete)
  - Hilfe: Geben Sie den Namen des Staates bzw. Landes an.

### Person › Angaben Unternehmen › Angaben zum Unternehmen (`G05000010340`)

- **Eingetragener Name des Unternehmens:** (`F05000006115`) — optional
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.0
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Name mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Registergericht** (`F60000000325`) — optional
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Nummer des Registereintrages** (`F60000000328`) — optional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2

### Person › Angaben Unternehmen › Adress- und Kontaktdaten des Unternehmens (`G05000010341`)

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
- **E-Mail-Adresse** (`F60000000242`) — Pflicht
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Mobilfunknummer** (`F05000016214`) — optional
  - Rechtsgrundlage: ITU E.124
  - Hilfe: Geben Sie bitte bei Mobilfunknummern innerhalb Deutschlands zuerst die Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, z.B. (0211) 12345678. Geben Sie bitte bei Telefonnummern außerhalb von Deutschland zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, z.B. +49 211 123456789.
- **Gab es abweichende gewerbliche Hauptniederlassungen in den letzten fünf Jahren?** (`F05000016234`) — optional
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Geben Sie hier an, ob abweichende gewerbliche Hauptniederlassungen in den letzten fünf Jahren bestanden.

### Person › Angaben Unternehmen › Adress- und Kontaktdaten des Unternehmens › Abweichende Hauptniederlassungen (`G05000010359`)

- **Von** (`F05000016235`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für den Anfang des Zeitraumes an.
- **Bis** (`F05000016236`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für das Ende des Zeitraums an.
- **Straße** (`F05000016237`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie den Namen der Straße an.
- **Hausnummer** (`F05000016239`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F05000016240`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F05000016241`) — Pflicht
  - Rechtsgrundlage: Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie hier den Namen des Ortes (Gemeinde, Ortschaft oder Stadt) an.

### Person › Umfang der Erlaubnis / Tätigkeitsart (`G05000011074`)

- **Beantragt wird die Erlaubnis als Finanzanlagenvermittler:in nach 34f Abs. 1 S. 1 GewO für die Beratung und Vermittlung von** (`F05000016518`) — Pflicht
  - Rechtsgrundlage: § 34 f Absatz 1 Satz 1 Gewerbeordnung
- **Sind Sie bereits in dem von der Bundesanstalt für Finanzdienstleistungsaufsicht geführten Register der vertraglich gebundenen Vermittler:innen nach § 2 Absatz 10 Satz 5 KWG bzw. § 3 Absatz 2 Satz 5 WpIG eingetragen?** (`F05000016913`) — Pflicht
  - Rechtsgrundlage: § 2 Absatz 10 Satz 5 KWG bzw. § 3 Absatz 2 Satz 5 WpIG

### Person › Erforderliche Unterlagen (`G05000010605`)

- **Ich verfüge über eine Erlaubnis nach § 34c GewO, § 34d GewO und/oder § 34i GewO - nicht älter als 3 Monate.** (`F05000016520`) — optional
  - Rechtsgrundlage: § 34 f Gewerbeordnung
  - Hilfe: Wenn Sie im Besitz einer Erlaubnis nach § 34c GewO (Immobilienmakler:in, Darlehensvermittler:in, Bauträger:in/-betreuer:in und/oder Wohnimmobilienverwalter:in), § 34d GewO (Versicherungsvermittler:in/-berater:in) oder § 34i GewO (Immobiliardarlehensvermittler:in) sind, die im Regelverfahren erteilt wurde und die bei Antragstellung nicht älter als sechs Monate ist, können Sie diese Frage mit "Ja " beantworten. Im weiteren Verlauf der Antragstellung wird dies dann berücksichtigt. Bitte beachten Sie, dass, wenn Sie bereits im Besitz einer Erlaubnis nach § 34h GewO sind, eine Erlaubniserteilung nach § 34f GewO nicht möglich ist, da die beiden Gewerbe nicht nebeneinander ausgeübt werden dürfen, vgl. § 34h Absatz 2 Satz 1 GewO.
- **Laden Sie hier den bestehenden gewerberechtlichen Erlaubnisbescheid hoch, sofern dieser nicht älter als 3 Monate ist.** (`F05000016254`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Haben Sie bereits ein Führungszeugnis beantragt?** (`F05000016255`) — optional
  - Rechtsgrundlage: § 30 Abs. 5 BZRG, Belegart O
- **Datum der Beantragung** (`F05000016256`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?** (`F05000016257`) — optional
  - Rechtsgrundlage: § 150 Abs. 5 Gewerbeordnung, Belegart O
  - Hilfe: Für Fragen zur Beantragung eines Gewerbezentralregisterauszug wenden Sie sich bitte an Ihre zuständige IHK.
- **Datum der Beantragung** (`F05000016258`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Sachkundenachweis** (`F05000016260`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Laden Sie hier Ihren Sachkundenachweis hoch. Als Sachkundenachweis dienen z.B. eine beglaubigte Kopie einer gleichgestellten Berufsqualifikation, eine beglaubigte Kopie des abgelegten Abschlusses nach dem Standard des Lernzielkatalogs, eine beglaubigte Kopie der erfolgreich abgelegten Sachkundeprüfung.
- **Versicherungsbestätigung Ihrer Vermögensschaden-Haftpflichtversicherung oder gleichwertige Garantie** (`F05000016261`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Laden Sie hier eine Bescheinigung über den Bestand einer Vermögensschaden-Haftpflichtversicherung oder einer gleichwertigen Garantie hoch. Bitte beachten Sie, dass hier nicht der Versicherungsschein eingereicht werden soll, sondern die Versicherungsbestätigung zur Vorlage bei der IHK im sogenannten Musterwortlaut
- **Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung)** (`F05000016262`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
  - Hilfe: Laden Sie hier die Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung) hoch. Diese erhalten Sie vom Finanzamt.
- **Auskunft aus dem Schuldnerverzeichnis des Vollstreckungsportals** (`F05000016263`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
- **Bestätigung über Insolvenzfreiheit des Insolvenzgerichts** (`F05000016264`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
  - Hilfe: Laden Sie hier Ihre Bestätigung zur Insolvenzfreiheit hoch, diese erhalten Sie von einem zuständigen Insolvenzgericht.
- **Handelsregisterauszug** (`F05000016272`) — optional
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Laden Sie hier Ihren Handelsregisterauszug hoch.
- **Laden Sie hier Ihren Erlaubnisbescheid für die Eintragung in das Vermittlerregister hoch.** (`F05000017119`) — optional
  - Rechtsgrundlage: § 34 c, d, i, f Gewerbeordnung (GewO)
- **Gewerbeanmeldung** (`F05000017120`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, i Gewerbeordnung (GewO)
  - Hilfe: Bitte laden Sie hier Ihre Gewerbeanmeldung hoch.

### Person › Personenhandelsgesellschaft (`G05000010774`)

- **Vertreten Sie als antragstellende Person als geschäftsführende/r Gesellschafter/in mit Vertretungsmacht eine oder mehrere Personen(handels)gesellschaft/en bei der Finanzanlagenvermittlung?** (`F05000016671`) — Pflicht
  - Rechtsgrundlage: § 34 f Gewerbeordnung
  - Hilfe: Wenn die antragstellende Person als Gesellschafter/in mit Vertretungsmacht eine oder mehrere Personenhandelsgesellschaft/en vertritt, bitte die Daten der Personenhandelsgesellschaften hier erfassen.

### Person › Personenhandelsgesellschaft › Personenhandelsgesellschaft hinzufügen (`G05000010397`)

- **Eingetragener Name des Unternehmens:** (`F05000006115`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.0
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Name mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Registergericht** (`F60000000325`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Nummer des Registereintrages** (`F60000000328`) — Pflicht
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
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
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Versicherungsbestätigung Ihrer Vermögensschaden-Haftpflichtversicherung oder gleichwertige Garantie** (`F05000016261`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Laden Sie hier eine Bescheinigung über den Bestand einer Vermögensschaden-Haftpflichtversicherung oder einer gleichwertigen Garantie hoch. Bitte beachten Sie, dass hier nicht der Versicherungsschein eingereicht werden soll, sondern die Versicherungsbestätigung zur Vorlage bei der IHK im sogenannten Musterwortlaut

### Person › Leitung (`G05000010398`)

- **Stellen Sie eine:n Betriebsleiter:in ein oder wird eine Zweigstelle Ihres Betriebes von einer beauftragten Person geleitet?** (`F05000016273`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Die IHK ist als Erlaubnisbehörde verpflichtet, zu prüfen, ob eine mit der Leitung des Betriebs oder einer Zweigniederlassung beauftragte Person die erforderliche Zuverlässigkeit besitzt. Sofern ein:e Betriebs- oder Zweigniederlassungsleiter:in mit der Übermittlung der Daten an die Erlaubnisbehörde nicht einverstanden ist, kann diese Person nicht als Betriebs- oder Zweigniederlassungsleiter:in tätig sein.

### Person › Leitung › Betriebsleitung/Zweigstellenleitung (`G05000010399`)

- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsdatum** (`F05000016340`) — Pflicht
  - Rechtsgrundlage: DIN 5008
  - Hilfe: Bitte geben Sie das Geburtsdatum an (Tag, Monat und Jahr).
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016370`) — optional
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:anschrift
  - Hilfe: z.B. Hinterhaus, Gartenhaus.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Land** (`F05000016250`) — Pflicht
  - Rechtsgrundlage: Xmeld.Anschrift.Melderecht.Ausland.staat Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staatsgebiete (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsgebiete)
  - Hilfe: Geben Sie den Namen des Staates bzw. Landes an.
- **Möchten Sie eine abweichende Meldeanschrift für die Betriebs-/Zweigstellenleitung angeben?** (`F05000016397`) — Pflicht
  - Rechtsgrundlage: XInneres-Basismodul; Version 7
- **Mit der o.g. Datenweitergabe versichere ich, dass ich das Einverständnis des:der Betriebsleiters:in /Zweigniederlassungsleiters:in eingeholt habe, dass ich ihn:sie gegenüber der IHK  als mit der Leitung des Betriebes oder einer Zweigniederlassung benennen darf. Der:die Niederlassungsleiter:in / Zweigniederlassungsleiter:in hat mich dazu ermächtigt, die oben stehenden Daten (Name, Vorname, Wohnanschrift) in elektronischer Form an die IHK weiterzuleiten, welche diese Daten zu o.g. Zweck speichert und verarbeitet.Ich habe den:die Niederlassungsleiter:in / Zweigniederlassungsleiter:in darüber informiert, dass die Einwilligung freiwillig ist und jederzeit für die Zukunft gegenüber der IHK elektronisch, telefonisch oder schriftlich widerrufen werden kann.Bei der IHK findet eine über diesen Zweck hinausgehende Datenverarbeitung nur statt, wenn dies aufgrund gesetzlicher Regelungen vorgeschrieben ist.** (`F05000016486`) — Pflicht
  - Rechtsgrundlage: Gewerbeordnung

### Person › Leitung › Betriebsleitung/Zweigstellenleitung › Abweichende Meldeanschrift (`G05000010487`)

- **Von** (`F05000016235`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für den Anfang des Zeitraumes an.
- **Bis** (`F05000016236`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für das Ende des Zeitraums an.
- **Straße (Meldeadresse)** (`F05000016345`) — Pflicht
  - Rechtsgrundlage: XInneres Basismodul 7
  - Hilfe: Geben Sie den Namen der Straße an.
- **Hausnummer** (`F05000016346`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:anschrift
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016347`) — optional
  - Rechtsgrundlage: XInneres Basismodul 7: Meldeanschrift.Zusatzangaben
  - Hilfe: Geben Sie hier Zusatzangaben zur Anschrift an, z.B. Hinterhaus, Gartenhaus.
- **Postleitzahl** (`F05000016348`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F05000016349`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
- **Land** (`F05000016350`) — Pflicht
  - Rechtsgrundlage: XInneres Basismodul 7 http://osci.de/xinneres/basismodul7/2019-01-31_XInneres-Basismodul_v7_final.pdf urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehoerigkeit_2023-02-24

### Person › Leitung › Betriebsleitung/Zweigstellenleitung › Erforderliche Unterlagen (Betriebsleitung/Zweigstellenleitung) (`G05000010400`)

- **Hat die Betriebs- oder Zweigstellenleitung bereits ein Führungszeugnis beantragt?** (`F05000016680`) — optional
  - Rechtsgrundlage: § 30 Abs. 5 BZRG, Belegart O
- **Datum der Beantragung** (`F05000016256`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?** (`F05000016257`) — optional
  - Rechtsgrundlage: § 150 Abs. 5 Gewerbeordnung, Belegart O
  - Hilfe: Für Fragen zur Beantragung eines Gewerbezentralregisterauszug wenden Sie sich bitte an Ihre zuständige IHK.
- **Datum der Beantragung** (`F05000016258`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung)** (`F05000016262`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
  - Hilfe: Laden Sie hier die Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung) hoch. Diese erhalten Sie vom Finanzamt.

### Person › Mitarbeitende (`G05000010401`)

- **Möchten Sie bei der Beratung und Vermittlung mitwirkende Mitarbeitende eintragen?** (`F05000016274`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung

### Person › Mitarbeitende › Mitwirkende Mitarbeitende (`G05000010403`)

- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Geburtsdatum** (`F05000016340`) — Pflicht
  - Rechtsgrundlage: DIN 5008
  - Hilfe: Bitte geben Sie das Geburtsdatum an (Tag, Monat und Jahr).
- **Mit der o.g. Datenweitergabe versichere ich, dass ich das Einverständnis des/der Mitarbeiters/in zur Datenweitergabe eingeholt habe. Der/die Mitarbeiter/in hat mich dazu ermächtigt, die oben stehenden Daten (Name, Vorname, Wohnanschrift) in elektronischer Form an die IHK weiterzuleiten, welche diese Daten zu o.g. Zweck speichert und verarbeitet. Ich habe den/die Mitarbeiter/in darüber informiert, dass die Einwilligung freiwillig ist und jederzeit für die Zukunft gegenüber der IHK elektronisch, telefonisch oder schriftlich widerrufen werden kann.Bei der IHK findet eine über diesen Zweck hinausgehende Datenverarbeitung nur statt, wenn dies aufgrund gesetzlicher Regelungen vorgeschrieben ist.** (`F05000016400`) — Pflicht
  - Rechtsgrundlage: Art. 6 Abs. 1 lit. a EU-Datenschutzgrundverordnung (DSGVO)

### Person › Weitere Erlaubnisverfahren (`G05000010603`)

- **Ich habe bereits bei einer anderen Stelle einen Antrag auf Erlaubnis nach § 34f Abs. 1 GewO gestellt.** (`F05000016519`) — Pflicht
  - Rechtsgrundlage: § 34 f Absatz 1 Gewerbeordnung
- **Zuständige Behörde** (`F05000016277`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung; XGewerbeanzeige Version 2.2
  - Hilfe: Bitte geben Sie die zuständige Behörde des weiteren Erlaubnisverfahrens an.
- **Sind sie bereits im Besitz einer weiteren Erlaubnis zur Ausübung einer gewerblichen Tätigkeit (z. B. nach §§ 34 c, 34 d, 34 f, 34 i Gewerbeordnung) oder haben Sie eine solche Erlaubnis beantragt?** (`F05000016278`) — Pflicht
  - Rechtsgrundlage: §§ 34c, d, f, i Gewerbeordnung

### Person › Weitere Erlaubnisverfahren › Sonstige gewerberechtliche Erlaubnisverfahren (`G05000010405`)

- **Art der Erlaubnis** (`F05000016279`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Geben Sie die Art der Erlaubnis an.
- **Ausstellungsdatum Erlaubnisbescheid** (`F05000016280`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Zuständige Behörde** (`F05000016281`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung; XGewerbeanzeige name.behoerde
  - Hilfe: Bitte geben Sie die zuständige Behörde des weiteren Erlaubnisverfahrens an.

### Person › Verhältnisse (`G05000010406`)

- **Ist oder war gegen Sie ein Strafverfahren anhängig?** (`F05000016282`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Wird oder wurde gegen Sie ein Bußgeldverfahren wegen Verstößen bei einer gewerblichen Tätigkeit betrieben?** (`F05000016284`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Ist oder war gegen Sie ein Gewerbeuntersagungsverfahren anhängig?** (`F05000016285`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an.** (`F05000016407`) — optional, conditional
  - Rechtsgrundlage: Gewerbeordnung
- **Ist über Ihr Vermögen ein Insolvenzverfahren eröffnet?** (`F05000016286`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
- **Ist über Ihr Vermögen ein Insolvenzverfahren eröffnet?** (`F05000016530`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Haben Sie eine Vermögensauskunft gemäß § 802c Zivilprozessordnung (ZPO) abgegeben?** (`F05000016288`) — Pflicht
  - Rechtsgrundlage: § 802c Zivilprozessordnung (ZPO); §§ 34 c, d, f, und i Gewerbeordnung (GewO)
- **Liegt eine entsprechende Haftanordnung nach § 802 g Zivilprozessordnung (ZPO) gegen Sie vor?** (`F05000016289`) — Pflicht
  - Rechtsgrundlage: § 802 g Zivilprozessordnung (ZPO)
- **Liegt eine Eintragungsanordnung in das Schuldnerverzeichnis vor?** (`F05000016405`) — Pflicht
  - Rechtsgrundlage: § 882 b Zivilprozessordnung (ZPO)
- **Wenn vorstehend ja, bei welchem Insolvenzgericht? Welcher Behörde? Geben Sie das zugehörige Aktenzeichen an.** (`F05000016978`) — optional
  - Rechtsgrundlage: Gewerbeordnung

### Antragsteller/in › Angaben zum Unternehmen (`G05000010386`)

- **IHK-Identnummer** (`F05000007410`) — optional
  - Rechtsgrundlage: § 34 Gewerbeordnung
  - Hilfe: Geben Sie hier Ihre 10-stellige IHK-Identnummer an. Diese haben Sie von der zuständigen IHK zu Beginn der Mitgliedschaft erhalten.
- **Status der antragstellenden Gesellschaft** (`F05000016251`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Eingetragener Name des Unternehmens:** (`F05000006115`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.0
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Name mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Registergericht** (`F60000000325`) — optional
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Nummer des Registereintrages** (`F60000000328`) — optional
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
- **Datum der Eintragung ins Handelsregister** (`F05000016490`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung; urn:xoev-de:kosit:xoev:kernkomponente:zeitraum vom 31.08.2020
  - Hilfe: Geben Sier hier das Datum im Format TT.MM.JJJJ an.
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
- **Gab es abweichende gewerbliche Hauptniederlassungen in den letzten fünf Jahren?** (`F05000016252`) — optional
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Geben Sie hier an, ob abweichende gewerbliche Hauptniederlassungen in den letzten fünf Jahren bestanden.

### Antragsteller/in › Angaben zum Unternehmen › Kontaktperson für Rückfragen (`G05000010434`)

- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **E-Mail-Adresse** (`F60000000242`) — Pflicht
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Funktion** (`F60000000322`) — optional
  - Rechtsgrundlage: § 34 Gewerbeordnung _(geerbt)_
  - Hilfe: Geben Sie die Funktion oder Rolle der Person an.
- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Mobilfunknummer** (`F05000016214`) — optional
  - Rechtsgrundlage: ITU E.124
  - Hilfe: Geben Sie bitte bei Mobilfunknummern innerhalb Deutschlands zuerst die Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, z.B. (0211) 12345678. Geben Sie bitte bei Telefonnummern außerhalb von Deutschland zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, z.B. +49 211 123456789.

### Antragsteller/in › Angaben zum Unternehmen › Abweichende Hauptniederlassungen (`G05000010359`)

- **Von** (`F05000016235`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für den Anfang des Zeitraumes an.
- **Bis** (`F05000016236`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für das Ende des Zeitraums an.
- **Straße** (`F05000016237`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie den Namen der Straße an.
- **Hausnummer** (`F05000016239`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Postleitzahl** (`F05000016240`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F05000016241`) — Pflicht
  - Rechtsgrundlage: Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie hier den Namen des Ortes (Gemeinde, Ortschaft oder Stadt) an.

### Antragsteller/in › Umfang der Erlaubnis / Tätigkeitsart (`G05000011074`)

- **Beantragt wird die Erlaubnis als Finanzanlagenvermittler:in nach 34f Abs. 1 S. 1 GewO für die Beratung und Vermittlung von** (`F05000016518`) — Pflicht
  - Rechtsgrundlage: § 34 f Absatz 1 Satz 1 Gewerbeordnung
- **Sind Sie bereits in dem von der Bundesanstalt für Finanzdienstleistungsaufsicht geführten Register der vertraglich gebundenen Vermittler:innen nach § 2 Absatz 10 Satz 5 KWG bzw. § 3 Absatz 2 Satz 5 WpIG eingetragen?** (`F05000016913`) — Pflicht
  - Rechtsgrundlage: § 2 Absatz 10 Satz 5 KWG bzw. § 3 Absatz 2 Satz 5 WpIG

### Antragsteller/in › Erforderliche Unterlagen für die antragstellende Person (`G05000010759`)

- **Ich verfüge über eine Erlaubnis nach § 34c GewO, § 34d GewO und/oder § 34i GewO - nicht älter als 6 Monate** (`F05000016517`) — optional
  - Rechtsgrundlage: § 34 f Absatz 1 Gewerbeordnung
  - Hilfe: Wenn Sie als antragstellende Person (Gesellschaft) im Besitz einer Erlaubnis nach § 34c GewO (Immobilienmakler:in, Darlehensvermittler:in, Bauträger:in/-betreuer:in und/oder Wohnimmobilienverwalter:in), § 34d GewO (Versicherungsvermittler:in/-berater:in) oder § 34i GewO (Immobiliardarlehensvermittler:in) sind, die im Regelverfahren erteilt wurde und die bei Antragstellung nicht älter als sechs Monate ist, können Sie diese Frage mit "Ja "zu beantworten. Im weiteren Verlauf der Antragstellung wird dies dann berücksichtigt.
- **Laden Sie hier den bestehenden gewerberechtlichen Erlaubnisbescheid hoch, sofern dieser nicht älter als 3 Monate ist.** (`F05000016254`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?** (`F05000016257`) — optional
  - Rechtsgrundlage: § 150 Abs. 5 Gewerbeordnung, Belegart O
  - Hilfe: Für Fragen zur Beantragung eines Gewerbezentralregisterauszug wenden Sie sich bitte an Ihre zuständige IHK.
- **Datum der Beantragung** (`F05000016258`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Bescheinigung in Steuersachen für die Gesellschaft (sog. Unbedenklichkeitsbescheinigung) vom Finanzamt:** (`F05000016492`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Auskunft für die Gesellschaft aus dem Schuldnerverzeichnis des Vollstreckungsportals** (`F05000016493`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Bestätigung des Insolvenzgerichts über Insolvenzfreiheit der Gesellschaft** (`F05000016494`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Die Auskünfte sind bei dem/den Insolvenzgericht/en (Amtsgericht/en), einzuholen, in dessen Zuständigkeitsbereich die antragstellende Person (Gesellschaft) in den letzten fünf Jahren ihre Hauptniederlassung hatte.
- **Versicherungsbestätigung Ihrer Vermögensschaden-Haftpflichtversicherung der Gesellschaft oder gleichwertige Garantie** (`F05000016495`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Bitte beachten Sie, dass hier nicht der Versicherungsschein eingereicht werden soll, sondern die Versicherungsbestätigung zur Vorlage bei der IHK im sogenannten Musterwortlaut.
- **Auszug aus dem Handels-, Genossenschafts- oder Vereinsregister** (`F05000016266`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Laden Sie hier Ihren Auszug aus dem Handels-, Genossenschafts- oder Vereinsregister hoch. Falls sich die Gesellschaft in Gründung befindet ist an dieser Stelle der Gesellschaftsvertrag hochzuladen.
- **Laden Sie hier Ihren Erlaubnisbescheid für die Eintragung in das Vermittlerregister hoch.** (`F05000017119`) — optional
  - Rechtsgrundlage: § 34 c, d, i, f Gewerbeordnung (GewO)
- **Gewerbeanmeldung** (`F05000017120`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, i Gewerbeordnung (GewO)
  - Hilfe: Bitte laden Sie hier Ihre Gewerbeanmeldung hoch.

### Antragsteller/in › Vertretung › Gesetzliche Vertretung (`G05000010391`)

- **Familienname** (`F00000000013`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Zunamen bzw. Familiennamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsdatum** (`F05000016340`) — Pflicht
  - Rechtsgrundlage: DIN 5008
  - Hilfe: Bitte geben Sie das Geburtsdatum an (Tag, Monat und Jahr).
- **Geburtsort** (`F00000000067`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde (z.B.: Berlin).
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.

### Antragsteller/in › Vertretung › Anschrift Hauptwohnsitz (`G05000011189`)

- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016370`) — optional
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:anschrift
  - Hilfe: z.B. Hinterhaus, Gartenhaus.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **E-Mail-Adresse** (`F60000000242`) — Pflicht
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Mobilfunknummer** (`F05000016214`) — optional
  - Rechtsgrundlage: ITU E.124
  - Hilfe: Geben Sie bitte bei Mobilfunknummern innerhalb Deutschlands zuerst die Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, z.B. (0211) 12345678. Geben Sie bitte bei Telefonnummern außerhalb von Deutschland zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, z.B. +49 211 123456789.
- **Bestanden in den letzten fünf Jahren abweichende Meldeanschriften?** (`F05000016245`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Land** (`F05000016250`) — Pflicht
  - Rechtsgrundlage: Xmeld.Anschrift.Melderecht.Ausland.staat Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staatsgebiete (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsgebiete)
  - Hilfe: Geben Sie den Namen des Staates bzw. Landes an.

### Antragsteller/in › Vertretung › Anschrift Hauptwohnsitz › Abweichende Meldeanschriften der letzten 5 Jahre (`G05000010363`)

- **Von** (`F05000016235`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für den Anfang des Zeitraumes an.
- **Bis** (`F05000016236`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für das Ende des Zeitraums an.
- **Straße** (`F05000016237`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie den Namen der Straße an.
- **Hausnummer** (`F05000016239`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016242`) — optional
  - Rechtsgrundlage: XInneres.Meldeanschrift.zusatzangaben Version 8
  - Hilfe: Geben Sie Zusatzangaben zur Anschrift an, zum Beispiel "Hinterhaus".
- **Postleitzahl** (`F05000016240`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F05000016241`) — Pflicht
  - Rechtsgrundlage: Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie hier den Namen des Ortes (Gemeinde, Ortschaft oder Stadt) an.
- **Land** (`F05000016243`) — Pflicht
  - Rechtsgrundlage: Xmeld.Anschrift.Melderecht.Ausland.staat Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staatsgebiete (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsgebiete)
  - Hilfe: Geben Sie den Namen des Staates bzw. Landes an.

### Antragsteller/in › Vertretung › Erforderliche Unterlagen (gesetzliche Vertretung) (`G05000010392`)

- **Verfügt der/die gesetzliche Vertreter:in über eine Erlaubnis nach § 34c GewO, § 34f GewO, § 34h und/oder § 34i GewO, nicht älter als 3 Monate?** (`F05000016496`) — optional
  - Rechtsgrundlage: § 34 i Gewerbeordnung
  - Hilfe: Wenn Sie als vertretungsberechtigte Person im Besitz einer auf Sie persönlich ausgestellten Erlaubnis nach § 34c GewO, § 34d GewO, § 34f und/oder § 34h GewO sind, die im Regelverfahren erteilt wurde und die bei Antragstellung nicht älter als drei Monate ist, können Sie dies hier angeben. Das Gleiche gilt, wenn Sie auch vertretungsberechtigte Person einer anderen juristischen Person (Gesellschaft) sind, die über eine entsprechende Erlaubnis - nicht älter als drei Monate - verfügt.
- **Laden Sie hier den bestehenden gewerberechtlichen Erlaubnisbescheid hoch, sofern dieser nicht älter als 3 Monate ist.** (`F05000016254`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Haben Sie bereits ein Führungszeugnis beantragt?** (`F05000016255`) — optional
  - Rechtsgrundlage: § 30 Abs. 5 BZRG, Belegart O
- **Datum der Beantragung** (`F05000016256`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?** (`F05000016257`) — optional
  - Rechtsgrundlage: § 150 Abs. 5 Gewerbeordnung, Belegart O
  - Hilfe: Für Fragen zur Beantragung eines Gewerbezentralregisterauszug wenden Sie sich bitte an Ihre zuständige IHK.
- **Datum der Beantragung** (`F05000016258`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung)** (`F05000016262`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
  - Hilfe: Laden Sie hier die Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung) hoch. Diese erhalten Sie vom Finanzamt.
- **Auskunft aus dem Schuldnerverzeichnis des Vollstreckungsportals** (`F05000016263`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
- **Bestätigung über Insolvenzfreiheit des Insolvenzgerichts** (`F05000016264`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
  - Hilfe: Laden Sie hier Ihre Bestätigung zur Insolvenzfreiheit hoch, diese erhalten Sie von einem zuständigen Insolvenzgericht.
- **Sachkundenachweis** (`F05000016260`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Laden Sie hier Ihren Sachkundenachweis hoch. Als Sachkundenachweis dienen z.B. eine beglaubigte Kopie einer gleichgestellten Berufsqualifikation, eine beglaubigte Kopie des abgelegten Abschlusses nach dem Standard des Lernzielkatalogs, eine beglaubigte Kopie der erfolgreich abgelegten Sachkundeprüfung.

### Antragsteller/in › Personenhandelsgesellschaft (`G05000011191`)

- **Vertreten Sie als antragstellende Person als geschäftsführende/r Gesellschafter/in mit Vertretungsmacht eine oder mehrere Personen(handels)gesellschaft/en bei der Finanzanlagenvermittlung?** (`F05000016671`) — Pflicht
  - Rechtsgrundlage: § 34 f Gewerbeordnung
  - Hilfe: Wenn die antragstellende Person als Gesellschafter/in mit Vertretungsmacht eine oder mehrere Personenhandelsgesellschaft/en vertritt, bitte die Daten der Personenhandelsgesellschaften hier erfassen.

### Antragsteller/in › Personenhandelsgesellschaft › Personenhandelsgesellschaft hinzufügen (`G05000011190`)

- **Eingetragener Name des Unternehmens:** (`F05000006115`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NameOrganisation.name vom 01.08.2017; XGewerbeanzeige.Betrieb.eingetragenerName Version 2.2; XUnternehmen.Kerndatenmodell.Eingetragener Name Version 1.0
  - Hilfe: Geben Sie den im Handelsregister, im Genossenschaftsregister, im Vereinsregister oder im Stiftungsverzeichnis eingetragenen Name mit Rechtsform an, soweit eine Eintragung vorliegt.
- **Registergericht** (`F60000000325`) — Pflicht
  - Rechtsgrundlage: XUnternehmen.Eintragung.Registergericht; urn:xoev-de:xunternehmen:codeliste:registergerichte_14
  - Hilfe: Geben Sie das Registergericht an, bei dem die Organisation eingetragen ist.
- **Nummer des Registereintrages** (`F60000000328`) — Pflicht
  - Rechtsgrundlage: Anlage 1-3 GewAnzV vom 03.07.2019; XGewerbeanzeige.Betrieb.EintragungOrt Version 2.2; angelehnt an XGewerbeanzeige.Betrieb.eintragungNr und XGewerbeanzeige.Betrieb.eintragungNrSonstige Version 2.2
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
- **E-Mail-Adresse** (`F60000000242`) — optional
  - Rechtsgrundlage: RFC 5322; RFC 5321
  - Hilfe: Geben Sie eine E-Mail-Adresse an, z.B. Max.Mustermann@email.de
- **Telefonnummer** (`F60000000240`) — optional
  - Rechtsgrundlage: ITU E.123
  - Hilfe: Geben Sie bei Telefonnummern innerhalb Deutschlands zuerst die Ortsvorwahl bzw. Mobilnetzvorwahl in Klammern, gefolgt von der Rufnummer an, Beispiel (0211) 12345678.
Geben Sie bei Telefonnummern außerhalb Deutschlands zuerst den Internationalen Ländercode mit vorgestelltem Plus, gefolgt von der Ortsvorwahl bzw. Mobilnetzvorwahl ohne der führenden Null, gefolgt von der Rufnummer an, Beispiel +49 211 123456789.
- **Versicherungsbestätigung Ihrer Vermögensschaden-Haftpflichtversicherung oder gleichwertige Garantie** (`F05000016261`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Laden Sie hier eine Bescheinigung über den Bestand einer Vermögensschaden-Haftpflichtversicherung oder einer gleichwertigen Garantie hoch. Bitte beachten Sie, dass hier nicht der Versicherungsschein eingereicht werden soll, sondern die Versicherungsbestätigung zur Vorlage bei der IHK im sogenannten Musterwortlaut
- **Handelsregisterauszug** (`F05000016272`) — optional
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Laden Sie hier Ihren Handelsregisterauszug hoch.

### Antragsteller/in › Leitung (`G05000010398`)

- **Stellen Sie eine:n Betriebsleiter:in ein oder wird eine Zweigstelle Ihres Betriebes von einer beauftragten Person geleitet?** (`F05000016273`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Die IHK ist als Erlaubnisbehörde verpflichtet, zu prüfen, ob eine mit der Leitung des Betriebs oder einer Zweigniederlassung beauftragte Person die erforderliche Zuverlässigkeit besitzt. Sofern ein:e Betriebs- oder Zweigniederlassungsleiter:in mit der Übermittlung der Daten an die Erlaubnisbehörde nicht einverstanden ist, kann diese Person nicht als Betriebs- oder Zweigniederlassungsleiter:in tätig sein.

### Antragsteller/in › Leitung › Betriebsleitung/Zweigstellenleitung (`G05000010399`)

- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Geburtsname** (`F60000000230`) — optional
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.geburtsname vom 31.01.2020
  - Hilfe: Geben Sie den Geburtsnamen an. Manche Menschen ändern ihren Familiennamen, wenn sie heiraten oder eine Lebenspartnerschaft eingehen. Der  Geburtsname ist der Familienname den die Person bei der Geburt hatte, bevor sie ihren Namen geändert hat.
- **Geburtsdatum** (`F05000016340`) — Pflicht
  - Rechtsgrundlage: DIN 5008
  - Hilfe: Bitte geben Sie das Geburtsdatum an (Tag, Monat und Jahr).
- **Geburtsort** (`F60000000234`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 4 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.Geburt.geburtsort vom 31.01.2020
  - Hilfe: Geben Sie die Bezeichnung des Ortes an, in dem die Person geboren wurde, Beispiel Düsseldorf.
- **Staatsangehörigkeit** (`F60000000236`) — Pflicht
  - Rechtsgrundlage: XOEV.Kernkomponente.NatuerlichePerson.staatsangehoerigkeit vom 31.08.2020; Codeliste laut XMeld und DSMeld: Codeliste Destatis Staatsangehörigkeit (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehörigkeit)
  - Hilfe: Wählen Sie aus, welcher Nationalität bzw. welchen Nationalitäten die Person angehört. Es ist auch die Auswahl "ohne Angabe" möglich, falls die Person keiner Nationalität angehört.
- **Straße** (`F60000000243`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.strasse Version 8
  - Hilfe: Geben Sie an, wie die Straße heißt, ohne Abkürzungen zu verwenden, Beispiel Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße
- **Hausnummer** (`F60000000244`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.hausnummer Version 8
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016370`) — optional
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:anschrift
  - Hilfe: z.B. Hinterhaus, Gartenhaus.
- **Postleitzahl** (`F60000000246`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F60000000247`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Anhang 3 Abschnitt 1 (Wohnort) PAuswV vom 28.9.2017; Tabelle 11 BSI TR-03123, Version 1.5.1; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
  - Hilfe: Geben Sie an, wie der Ort heißt. Benennen Sie dafür den Namen der Ortschaft, Gemeinde oder Stadt; nicht jedoch den Namen des Ortsteils, Beispiel Berlin.
- **Land** (`F05000016250`) — Pflicht
  - Rechtsgrundlage: Xmeld.Anschrift.Melderecht.Ausland.staat Codeliste laut Xmeld und DSMeld: Codeliste Destatis Staatsgebiete (urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsgebiete)
  - Hilfe: Geben Sie den Namen des Staates bzw. Landes an.
- **Möchten Sie eine abweichende Meldeanschrift für die Betriebs-/Zweigstellenleitung angeben?** (`F05000016397`) — Pflicht
  - Rechtsgrundlage: XInneres-Basismodul; Version 7
- **Mit der o.g. Datenweitergabe versichere ich, dass ich das Einverständnis des:der Betriebsleiters:in /Zweigniederlassungsleiters:in eingeholt habe, dass ich ihn:sie gegenüber der IHK  als mit der Leitung des Betriebes oder einer Zweigniederlassung benennen darf. Der:die Niederlassungsleiter:in / Zweigniederlassungsleiter:in hat mich dazu ermächtigt, die oben stehenden Daten (Name, Vorname, Wohnanschrift) in elektronischer Form an die IHK weiterzuleiten, welche diese Daten zu o.g. Zweck speichert und verarbeitet.Ich habe den:die Niederlassungsleiter:in / Zweigniederlassungsleiter:in darüber informiert, dass die Einwilligung freiwillig ist und jederzeit für die Zukunft gegenüber der IHK elektronisch, telefonisch oder schriftlich widerrufen werden kann.Bei der IHK findet eine über diesen Zweck hinausgehende Datenverarbeitung nur statt, wenn dies aufgrund gesetzlicher Regelungen vorgeschrieben ist.** (`F05000016486`) — Pflicht
  - Rechtsgrundlage: Gewerbeordnung

### Antragsteller/in › Leitung › Betriebsleitung/Zweigstellenleitung › Abweichende Meldeanschrift (`G05000010487`)

- **Von** (`F05000016235`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für den Anfang des Zeitraumes an.
- **Bis** (`F05000016236`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:zeitraum
  - Hilfe: Bitte geben Sie das Datum für das Ende des Zeitraums an.
- **Straße (Meldeadresse)** (`F05000016345`) — Pflicht
  - Rechtsgrundlage: XInneres Basismodul 7
  - Hilfe: Geben Sie den Namen der Straße an.
- **Hausnummer** (`F05000016346`) — Pflicht
  - Rechtsgrundlage: urn:xoev-de:kosit:xoev:kernkomponente:anschrift
  - Hilfe: Geben Sie die Ziffern und ggf. Buchstaben der Hausnummer der Anschrift an, Beispiel 124a.
- **Adresszusatz** (`F05000016347`) — optional
  - Rechtsgrundlage: XInneres Basismodul 7: Meldeanschrift.Zusatzangaben
  - Hilfe: Geben Sie hier Zusatzangaben zur Anschrift an, z.B. Hinterhaus, Gartenhaus.
- **Postleitzahl** (`F05000016348`) — Pflicht
  - Rechtsgrundlage: XInneres.Meldeanschrift.postleitzahl Version 8
  - Hilfe: Geben Sie die Postleitzahl des Ortes an, Beispiel 10115.
- **Ort** (`F05000016349`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 9 PAuswG vom 21.6.2019; Xinneres.Meldeanschrift.Wohnort Version 8; XOEV.Kernkomponente.Anschrift.ort vom 31.01.2020
- **Land** (`F05000016350`) — Pflicht
  - Rechtsgrundlage: XInneres Basismodul 7 http://osci.de/xinneres/basismodul7/2019-01-31_XInneres-Basismodul_v7_final.pdf urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:staatsangehoerigkeit_2023-02-24

### Antragsteller/in › Leitung › Betriebsleitung/Zweigstellenleitung › Erforderliche Unterlagen (Betriebsleitung/Zweigstellenleitung) (`G05000010400`)

- **Hat die Betriebs- oder Zweigstellenleitung bereits ein Führungszeugnis beantragt?** (`F05000016680`) — optional
  - Rechtsgrundlage: § 30 Abs. 5 BZRG, Belegart O
- **Datum der Beantragung** (`F05000016256`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?** (`F05000016257`) — optional
  - Rechtsgrundlage: § 150 Abs. 5 Gewerbeordnung, Belegart O
  - Hilfe: Für Fragen zur Beantragung eines Gewerbezentralregisterauszug wenden Sie sich bitte an Ihre zuständige IHK.
- **Datum der Beantragung** (`F05000016258`) — optional, conditional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
  - Hilfe: Geben Sie hier das Datum der Beantragung an.
- **Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung)** (`F05000016262`) — optional
  - Rechtsgrundlage: §§ 34 c, d, f, und i Gewerbeordnung
  - Hilfe: Laden Sie hier die Bescheinigung in Steuersachen (sog. Unbedenklichkeitsbescheinigung) hoch. Diese erhalten Sie vom Finanzamt.

### Antragsteller/in › Mitarbeitende (`G05000010401`)

- **Möchten Sie bei der Beratung und Vermittlung mitwirkende Mitarbeitende eintragen?** (`F05000016274`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung

### Antragsteller/in › Mitarbeitende › Mitwirkende Mitarbeitende (`G05000010403`)

- **Familienname** (`F60000000227`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 1 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.familienname vom 31.01.2020
  - Hilfe: Geben Sie den Nachnamen, Familiennamen bzw. Zunamen an.
- **Vornamen** (`F60000000228`) — Pflicht
  - Rechtsgrundlage: § 5 (2) Nr. 2 PAuswG vom 21.6.2019; Anhang 3 PAuswV vom 28.9.2017; Tabelle 9 BSI TR-03123 Version 1.5.1; XOEV.Kernkomponente.NameNatuerlichePerson.vorname vom 31.08.2020
  - Hilfe: Geben Sie die Vornamen so an, wie sie auf den offiziellen Ausweisen angegeben sind, zum Beispiel im Personalausweis.
- **Geburtsdatum** (`F05000016340`) — Pflicht
  - Rechtsgrundlage: DIN 5008
  - Hilfe: Bitte geben Sie das Geburtsdatum an (Tag, Monat und Jahr).
- **Mit der o.g. Datenweitergabe versichere ich, dass ich das Einverständnis des/der Mitarbeiters/in zur Datenweitergabe eingeholt habe. Der/die Mitarbeiter/in hat mich dazu ermächtigt, die oben stehenden Daten (Name, Vorname, Wohnanschrift) in elektronischer Form an die IHK weiterzuleiten, welche diese Daten zu o.g. Zweck speichert und verarbeitet. Ich habe den/die Mitarbeiter/in darüber informiert, dass die Einwilligung freiwillig ist und jederzeit für die Zukunft gegenüber der IHK elektronisch, telefonisch oder schriftlich widerrufen werden kann.Bei der IHK findet eine über diesen Zweck hinausgehende Datenverarbeitung nur statt, wenn dies aufgrund gesetzlicher Regelungen vorgeschrieben ist.** (`F05000016400`) — Pflicht
  - Rechtsgrundlage: Art. 6 Abs. 1 lit. a EU-Datenschutzgrundverordnung (DSGVO)

### Antragsteller/in › Weitere Erlaubnisverfahren (`G05000010603`)

- **Ich habe bereits bei einer anderen Stelle einen Antrag auf Erlaubnis nach § 34f Abs. 1 GewO gestellt.** (`F05000016519`) — Pflicht
  - Rechtsgrundlage: § 34 f Absatz 1 Gewerbeordnung
- **Zuständige Behörde** (`F05000016277`) — optional
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung; XGewerbeanzeige Version 2.2
  - Hilfe: Bitte geben Sie die zuständige Behörde des weiteren Erlaubnisverfahrens an.
- **Sind sie bereits im Besitz einer weiteren Erlaubnis zur Ausübung einer gewerblichen Tätigkeit (z. B. nach §§ 34 c, 34 d, 34 f, 34 i Gewerbeordnung) oder haben Sie eine solche Erlaubnis beantragt?** (`F05000016278`) — Pflicht
  - Rechtsgrundlage: §§ 34c, d, f, i Gewerbeordnung

### Antragsteller/in › Weitere Erlaubnisverfahren › Sonstige gewerberechtliche Erlaubnisverfahren (`G05000010405`)

- **Art der Erlaubnis** (`F05000016279`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Geben Sie die Art der Erlaubnis an.
- **Ausstellungsdatum Erlaubnisbescheid** (`F05000016280`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung
  - Hilfe: Geben Sie das Datum der Ausstellung des Dokumentes an.
- **Zuständige Behörde** (`F05000016281`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, i Gewerbeordnung; XGewerbeanzeige name.behoerde
  - Hilfe: Bitte geben Sie die zuständige Behörde des weiteren Erlaubnisverfahrens an.

### Antragsteller/in › Verhältnisse (`G05000010584`)

- **Ist oder war gegen die Gesellschaft oder eine gesetzliche Vertretung ein Strafverfahren anhängig?** (`F05000016546`) — Pflicht
  - Rechtsgrundlage: Gewerbeordnung
- **Wird oder wurde gegen die Gesellschaft oder eine gesetzliche Vertretung oder eine Betriebsleitung oder eine mit der Leitung beauftragte Person der Gesellschaft strafrechtlich ermittelt?** (`F05000016979`) — Pflicht
  - Rechtsgrundlage: Gewerbeordnung
- **Wird oder wurde gegen die Gesellschaft oder eine gesetzliche Vertretung ein Bußgeldverfahren wegen Verstößen bei einer gewerblichen Tätigkeit betrieben?** (`F05000016547`) — Pflicht
  - Rechtsgrundlage: Gewerbeordnung
- **Ist oder war gegen die Gesellschaft oder eine gesetzliche Vertretung ein Gewerbeuntersagungsverfahren anhängig?** (`F05000016548`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an.** (`F05000016407`) — optional, conditional
  - Rechtsgrundlage: Gewerbeordnung
- **Ist über das Vermögen der Gesellschaft ein Insolvenzverfahren eröffnet?** (`F05000016549`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Ist über das Vermögen der Gesellschaft die Eröffnung eines Insolvenzverfahrens mangels Masse abgelehnt worden?** (`F05000016287`) — Pflicht
  - Rechtsgrundlage: § 34 c, d, f, h, i Gewerbeordnung
- **Hat die Gesellschaft eine Vermögensauskunft (§ 802c ZPO) abgegeben?** (`F05000016514`) — Pflicht
  - Rechtsgrundlage: § 802c Zivilprozessordnung (ZPO); §§ 34 c, d, f, h, i Gewerbeordnung (GewO)
- **Liegt eine entsprechende Haftanordnung nach §802g ZPO gegen die Gesellschaft vor?** (`F05000016515`) — Pflicht
  - Rechtsgrundlage: § 802 g Zivilprozessordnung (ZPO)
- **Liegt eine Eintragungsanordnung in das Schuldnerverzeichnis nach § 882b ZPO vor?** (`F05000016516`) — Pflicht
  - Rechtsgrundlage: § 882 b Zivilprozessordnung (ZPO)
- **Wenn vorstehend ja, bei welchem Insolvenzgericht? Welcher Behörde? Geben Sie das zugehörige Aktenzeichen an.** (`F05000016978`) — optional
  - Rechtsgrundlage: Gewerbeordnung

### Abschluss › Datenschutzrechtliche Hinweise (`G05000010673`)

- **Datenschutzrechtlicher Hinweis** (`F05000016569`) — Pflicht
  - Rechtsgrundlage: Art. 6 Abs. 1 S. 1 lit. e DSGVO; Art. 13 DSGVO
- **Ich versichere die Richtigkeit und Aktualität aller vorstehenden Angaben sowie aller eingereichten Unterlagen und erkläre zugleich, dass ich jede Veränderung meiner Tätigkeit und meiner persönlichen Verhältnisse mit Relevanz für das Erlaubnis- bzw. Registrierungsverfahren unverzüglich mitteile.** (`F05000016570`) — Pflicht
  - Rechtsgrundlage: § 34 Gewerbeordnung

### Abschluss › Einwilligung zur digitalen Zustellung (`G05000010756`)

- **Ich willige ein, dass Ergebnisdokumente meines Antrags, beispielsweise Bescheide, rechtsverbindlich in mein digitales Postfach im ELSTER-Konto bzw. Nutzerkonto Bund zugestellt werden.** (`F05000016639`) — Pflicht
  - Rechtsgrundlage: § 34 d, f, h, i Gewerbeordnung
  - Hilfe: Mit der Einwilligung zur digitalen Zustellung erklären Sie sich gegenüber der von Ihnen ausgewählten und für Sie zuständigen Industrie- und Handelskammer einverstanden, dass diese, bis zum Eingang eines Widerrufs dieser Einwilligung, den von Ihnen begehrten elektronischen Verwaltungsakt Ihnen gegenüber dadurch bekanntgibt, dass der Verwaltungsakt von Ihnen oder Ihrem Bevollmächtigten über Ihr Postfach, das Bestandteil Ihres Nutzerkontos bei ELSTER oder Ihrem BundID-Konto ist, abgerufen wird. Der Verwaltungsakt gilt am dritten Tag nach der Bereitstellung zum Abruf als bekannt gegeben. Sie oder Ihr Bevollmächtigter, wenn Sie einen solchen benannt haben, werden spätestens am Tag der Bereitstellung zum Abruf über die zu diesem Zweck von Ihnen angegebene Adresse über die Möglichkeit des Abrufs benachrichtigt. Erfolgt der Abruf vor einer erneuten Bekanntgabe des Verwaltungsaktes, bleibt der Tag des ersten Abrufs für den Zugang maßgeblich. Diese Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen. Weitere Einzelheiten entnehmen Sie bitte der Privacy Policy auf dem IHK Portal.
- **Nicht-Einwilligung der digitalen Zustellung** (`F05000016640`) — Pflicht
  - Rechtsgrundlage: § 34 d, f, h, i Gewerbeordnung

## Bedingungen

| Bedingung | Feld | Folge | Rechtsgrundlage | Regel |
|---|---|---|---|---|
| wenn „Soll der Antrag auf Erlaubniserteilung und/oder Eintragung in das Vermittlerregister gestellt werden?" gesetzt auf einem beliebigen Wert ist | „Angaben zum Unternehmen" | muss ausgefüllt werden | § 34 f Gewerbeordnung (GewO) | `R05000011893` |
| wenn „Bestanden in den letzten fünf Jahren abweichende Meldeanschriften?" gleich „wahr" ist | „Abweichende Meldeanschriften der letzten 5 Jahre" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010369` |
| wenn „Bestanden in den letzten fünf Jahren abweichende Meldeanschriften?" ungleich „wahr" ist | „Abweichende Meldeanschriften der letzten 5 Jahre" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010369` |
| wenn „Gab es abweichende gewerbliche Hauptniederlassungen in den letzten fünf Jahren?" ungleich „wahr" ist | „Abweichende Hauptniederlassungen" | darf nicht ausgefüllt werden | § 34 d, f, h, i Gewerbeordnung | `G05000010341` |
| wenn „Gab es abweichende gewerbliche Hauptniederlassungen in den letzten fünf Jahren?" gleich „wahr" ist | „Abweichende Hauptniederlassungen" | muss ausgefüllt werden | § 34 d, f, h, i Gewerbeordnung | `G05000010341` |
| wenn „Haben Sie bereits ein Führungszeugnis beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010605` |
| wenn „Haben Sie bereits ein Führungszeugnis beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010605` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010605` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010605` |
| wenn „Stellen Sie eine:n Betriebsleiter:in ein oder wird eine Zweigstelle Ihres Betriebes von einer beauftragten Person geleitet?" gleich „wahr" ist | „Betriebsleitung/Zweigstellenleitung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010398` |
| wenn „Stellen Sie eine:n Betriebsleiter:in ein oder wird eine Zweigstelle Ihres Betriebes von einer beauftragten Person geleitet?" ungleich „wahr" ist | „Betriebsleitung/Zweigstellenleitung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010398` |
| wenn „Hat die Betriebs- oder Zweigstellenleitung bereits ein Führungszeugnis beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Hat die Betriebs- oder Zweigstellenleitung bereits ein Führungszeugnis beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Möchten Sie bei der Beratung und Vermittlung mitwirkende Mitarbeitende eintragen?" gleich „wahr" ist | „Mitwirkende Mitarbeitende" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010401` |
| wenn „Möchten Sie bei der Beratung und Vermittlung mitwirkende Mitarbeitende eintragen?" gleich „falsch" ist | „Mitwirkende Mitarbeitende" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010401` |
| wenn „Sind sie bereits im Besitz einer weiteren Erlaubnis zur Ausübung einer gewerblichen Tätigkeit (z. B. nach §§ 34 c, 34 d, 34 f, 34 i Gewerbeordnung) oder haben Sie eine solche Erlaubnis beantragt?" gleich „wahr" ist | „Sonstige gewerberechtliche Erlaubnisverfahren" | muss ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010603` |
| wenn „Sind sie bereits im Besitz einer weiteren Erlaubnis zur Ausübung einer gewerblichen Tätigkeit (z. B. nach §§ 34 c, 34 d, 34 f, 34 i Gewerbeordnung) oder haben Sie eine solche Erlaubnis beantragt?" ungleich „wahr" ist | „Sonstige gewerberechtliche Erlaubnisverfahren" | darf nicht ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010603` |
| wenn „Ist oder war gegen Sie ein Strafverfahren anhängig?" gleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | muss ausgefüllt werden | — | `G05000010406` |
| wenn „Ist oder war gegen Sie ein Strafverfahren anhängig?" ungleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | darf nicht ausgefüllt werden | — | `G05000010406` |
| wenn „Wird oder wurde gegen Sie ein Bußgeldverfahren wegen Verstößen bei einer gewerblichen Tätigkeit betrieben?" gleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | muss ausgefüllt werden | — | `G05000010406` |
| wenn „Wird oder wurde gegen Sie ein Bußgeldverfahren wegen Verstößen bei einer gewerblichen Tätigkeit betrieben?" ungleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | darf nicht ausgefüllt werden | — | `G05000010406` |
| wenn „Ist oder war gegen Sie ein Gewerbeuntersagungsverfahren anhängig?" gleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | muss ausgefüllt werden | — | `G05000010406` |
| wenn „Ist oder war gegen Sie ein Gewerbeuntersagungsverfahren anhängig?" ungleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | darf nicht ausgefüllt werden | — | `G05000010406` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010759` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010759` |
| wenn „Bestanden in den letzten fünf Jahren abweichende Meldeanschriften?" gleich „wahr" ist | „Abweichende Meldeanschriften der letzten 5 Jahre" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000011189` |
| wenn „Bestanden in den letzten fünf Jahren abweichende Meldeanschriften?" ungleich „wahr" ist | „Abweichende Meldeanschriften der letzten 5 Jahre" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000011189` |
| wenn „Haben Sie bereits ein Führungszeugnis beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010392` |
| wenn „Haben Sie bereits ein Führungszeugnis beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010392` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010392` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010392` |
| wenn „Stellen Sie eine:n Betriebsleiter:in ein oder wird eine Zweigstelle Ihres Betriebes von einer beauftragten Person geleitet?" gleich „wahr" ist | „Betriebsleitung/Zweigstellenleitung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010398` |
| wenn „Stellen Sie eine:n Betriebsleiter:in ein oder wird eine Zweigstelle Ihres Betriebes von einer beauftragten Person geleitet?" ungleich „wahr" ist | „Betriebsleitung/Zweigstellenleitung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010398` |
| wenn „Hat die Betriebs- oder Zweigstellenleitung bereits ein Führungszeugnis beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Hat die Betriebs- oder Zweigstellenleitung bereits ein Führungszeugnis beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" ungleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Wurde bereits eine Auskunft aus dem Gewerbezentralregister beantragt?" gleich „001 Auskunft wurde bereits beantragt" ist | „Datum der Beantragung" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010400` |
| wenn „Möchten Sie bei der Beratung und Vermittlung mitwirkende Mitarbeitende eintragen?" gleich „wahr" ist | „Mitwirkende Mitarbeitende" | muss ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010401` |
| wenn „Möchten Sie bei der Beratung und Vermittlung mitwirkende Mitarbeitende eintragen?" gleich „falsch" ist | „Mitwirkende Mitarbeitende" | darf nicht ausgefüllt werden | § 34 c, d, f, h, i Gewerbeordnung | `G05000010401` |
| wenn „Sind sie bereits im Besitz einer weiteren Erlaubnis zur Ausübung einer gewerblichen Tätigkeit (z. B. nach §§ 34 c, 34 d, 34 f, 34 i Gewerbeordnung) oder haben Sie eine solche Erlaubnis beantragt?" gleich „wahr" ist | „Sonstige gewerberechtliche Erlaubnisverfahren" | muss ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010603` |
| wenn „Sind sie bereits im Besitz einer weiteren Erlaubnis zur Ausübung einer gewerblichen Tätigkeit (z. B. nach §§ 34 c, 34 d, 34 f, 34 i Gewerbeordnung) oder haben Sie eine solche Erlaubnis beantragt?" ungleich „wahr" ist | „Sonstige gewerberechtliche Erlaubnisverfahren" | darf nicht ausgefüllt werden | § 34 f Gewerbeordnung | `G05000010603` |
| wenn „Ist oder war gegen die Gesellschaft oder eine gesetzliche Vertretung ein Strafverfahren anhängig?" gleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | muss ausgefüllt werden | — | `G05000010584` |
| wenn „Ist oder war gegen die Gesellschaft oder eine gesetzliche Vertretung ein Strafverfahren anhängig?" gleich „falsch" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | darf nicht ausgefüllt werden | — | `G05000010584` |
| wenn „Wird oder wurde gegen die Gesellschaft oder eine gesetzliche Vertretung ein Bußgeldverfahren wegen Verstößen bei einer gewerblichen Tätigkeit betrieben?" gleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | muss ausgefüllt werden | — | `G05000010584` |
| wenn „Wird oder wurde gegen die Gesellschaft oder eine gesetzliche Vertretung ein Bußgeldverfahren wegen Verstößen bei einer gewerblichen Tätigkeit betrieben?" ungleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | darf nicht ausgefüllt werden | — | `G05000010584` |
| wenn „Ist oder war gegen die Gesellschaft oder eine gesetzliche Vertretung ein Gewerbeuntersagungsverfahren anhängig?" gleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | muss ausgefüllt werden | — | `G05000010584` |
| wenn „Ist oder war gegen die Gesellschaft oder eine gesetzliche Vertretung ein Gewerbeuntersagungsverfahren anhängig?" ungleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | darf nicht ausgefüllt werden | — | `G05000010584` |
| wenn „Wird oder wurde gegen die Gesellschaft oder eine gesetzliche Vertretung oder eine Betriebsleitung oder eine mit der Leitung beauftragte Person der Gesellschaft strafrechtlich ermittelt?" gleich „wahr" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | muss ausgefüllt werden | — | `G05000010584` |
| wenn „Wird oder wurde gegen die Gesellschaft oder eine gesetzliche Vertretung oder eine Betriebsleitung oder eine mit der Leitung beauftragte Person der Gesellschaft strafrechtlich ermittelt?" gleich „falsch" ist | „Wenn vorstehend ja, bei welcher Staatsanwaltschaft, welchem Gericht, welcher Behörde? Geben Sie das zugehörige Aktenzeichen an." | darf nicht ausgefüllt werden | — | `G05000010584` |

## Ungeklärte Regeln

Diese Bedingungen standen im FIM-Freitext, ließen sich aber nicht eindeutig in eine Edge übersetzen. Sie sind **nicht** im Graphen wirksam und brauchen eine menschliche Entscheidung:

- <mark>Wenn F05000016480 Auswahl der Person 01 Natürliche Person, dann zeige G05000010604 Person, wenn F05000016480 Auswahl der Person 02 Juristische Person, dann zeige G05000010600 Person (juristische Person).</mark> — Regel `R05000011269`

## Abhängigkeitsgraph

```mermaid
flowchart TD
  G05000010453_F05000016369["Soll der Antrag auf Erlaubniserteilung"] ==>|"? ? → required"| G05000010600_G05000010386["Angaben zum Unternehmen"]
  G05000010604_G05000010367_G05000010369_F05000016245["Bestanden in den letzten fünf Jahren a"] ==>|"= wahr → required"| G05000010604_G05000010367_G05000010369_G05000010363["Abweichende Meldeanschriften der letzt"]
  G05000010604_G05000010367_G05000010369_F05000016245["Bestanden in den letzten fünf Jahren a"] -.->|"<> wahr → forbidden"| G05000010604_G05000010367_G05000010369_G05000010363["Abweichende Meldeanschriften der letzt"]
  G05000010604_G05000010339_G05000010341_F05000016234["Gab es abweichende gewerbliche Hauptni"] -.->|"<> wahr → forbidden"| G05000010604_G05000010339_G05000010341_G05000010359["Abweichende Hauptniederlassungen"]
  G05000010604_G05000010339_G05000010341_F05000016234["Gab es abweichende gewerbliche Hauptni"] ==>|"= wahr → required"| G05000010604_G05000010339_G05000010341_G05000010359["Abweichende Hauptniederlassungen"]
  G05000010604_G05000010605_F05000016255["Haben Sie bereits ein Führungszeugnis "] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010604_G05000010605_F05000016256["Datum der Beantragung"]
  G05000010604_G05000010605_F05000016255["Haben Sie bereits ein Führungszeugnis "] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010604_G05000010605_F05000016256["Datum der Beantragung"]
  G05000010604_G05000010605_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010604_G05000010605_F05000016258["Datum der Beantragung"]
  G05000010604_G05000010605_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010604_G05000010605_F05000016258["Datum der Beantragung"]
  G05000010604_G05000010398_F05000016273["Stellen Sie eine:n Betriebsleiter:in e"] ==>|"= wahr → required"| G05000010604_G05000010398_G05000010399["Betriebsleitung/Zweigstellenleitung"]
  G05000010604_G05000010398_F05000016273["Stellen Sie eine:n Betriebsleiter:in e"] -.->|"<> wahr → forbidden"| G05000010604_G05000010398_G05000010399["Betriebsleitung/Zweigstellenleitung"]
  G05000010604_G05000010398_G05000010399_G05000010400_F05000016680["Hat die Betriebs- oder Zweigstellenlei"] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010604_G05000010398_G05000010399_G05000010400_F05000016256["Datum der Beantragung"]
  G05000010604_G05000010398_G05000010399_G05000010400_F05000016680["Hat die Betriebs- oder Zweigstellenlei"] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010604_G05000010398_G05000010399_G05000010400_F05000016256["Datum der Beantragung"]
  G05000010604_G05000010398_G05000010399_G05000010400_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010604_G05000010398_G05000010399_G05000010400_F05000016258["Datum der Beantragung"]
  G05000010604_G05000010398_G05000010399_G05000010400_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010604_G05000010398_G05000010399_G05000010400_F05000016258["Datum der Beantragung"]
  G05000010604_G05000010401_F05000016274["Möchten Sie bei der Beratung und Vermi"] ==>|"= wahr → required"| G05000010604_G05000010401_G05000010403["Mitwirkende Mitarbeitende"]
  G05000010604_G05000010401_F05000016274["Möchten Sie bei der Beratung und Vermi"] -.->|"= falsch → forbidden"| G05000010604_G05000010401_G05000010403["Mitwirkende Mitarbeitende"]
  G05000010604_G05000010603_F05000016278["Sind sie bereits im Besitz einer weite"] ==>|"= wahr → required"| G05000010604_G05000010603_G05000010405["Sonstige gewerberechtliche Erlaubnisve"]
  G05000010604_G05000010603_F05000016278["Sind sie bereits im Besitz einer weite"] -.->|"<> wahr → forbidden"| G05000010604_G05000010603_G05000010405["Sonstige gewerberechtliche Erlaubnisve"]
  G05000010604_G05000010406_F05000016282["Ist oder war gegen Sie ein Strafverfah"] ==>|"= wahr → required"| G05000010604_G05000010406_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010604_G05000010406_F05000016282["Ist oder war gegen Sie ein Strafverfah"] -.->|"<> wahr → forbidden"| G05000010604_G05000010406_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010604_G05000010406_F05000016284["Wird oder wurde gegen Sie ein Bußgeldv"] ==>|"= wahr → required"| G05000010604_G05000010406_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010604_G05000010406_F05000016284["Wird oder wurde gegen Sie ein Bußgeldv"] -.->|"<> wahr → forbidden"| G05000010604_G05000010406_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010604_G05000010406_F05000016285["Ist oder war gegen Sie ein Gewerbeunte"] ==>|"= wahr → required"| G05000010604_G05000010406_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010604_G05000010406_F05000016285["Ist oder war gegen Sie ein Gewerbeunte"] -.->|"<> wahr → forbidden"| G05000010604_G05000010406_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010759_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010600_G05000010759_F05000016258["Datum der Beantragung"]
  G05000010600_G05000010759_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010600_G05000010759_F05000016258["Datum der Beantragung"]
  G05000010600_G05000010390_G05000011189_F05000016245["Bestanden in den letzten fünf Jahren a"] ==>|"= wahr → required"| G05000010600_G05000010390_G05000011189_G05000010363["Abweichende Meldeanschriften der letzt"]
  G05000010600_G05000010390_G05000011189_F05000016245["Bestanden in den letzten fünf Jahren a"] -.->|"<> wahr → forbidden"| G05000010600_G05000010390_G05000011189_G05000010363["Abweichende Meldeanschriften der letzt"]
  G05000010600_G05000010390_G05000010392_F05000016255["Haben Sie bereits ein Führungszeugnis "] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010600_G05000010390_G05000010392_F05000016256["Datum der Beantragung"]
  G05000010600_G05000010390_G05000010392_F05000016255["Haben Sie bereits ein Führungszeugnis "] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010600_G05000010390_G05000010392_F05000016256["Datum der Beantragung"]
  G05000010600_G05000010390_G05000010392_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010600_G05000010390_G05000010392_F05000016258["Datum der Beantragung"]
  G05000010600_G05000010390_G05000010392_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010600_G05000010390_G05000010392_F05000016258["Datum der Beantragung"]
  G05000010600_G05000010398_F05000016273["Stellen Sie eine:n Betriebsleiter:in e"] ==>|"= wahr → required"| G05000010600_G05000010398_G05000010399["Betriebsleitung/Zweigstellenleitung"]
  G05000010600_G05000010398_F05000016273["Stellen Sie eine:n Betriebsleiter:in e"] -.->|"<> wahr → forbidden"| G05000010600_G05000010398_G05000010399["Betriebsleitung/Zweigstellenleitung"]
  G05000010600_G05000010398_G05000010399_G05000010400_F05000016680["Hat die Betriebs- oder Zweigstellenlei"] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010600_G05000010398_G05000010399_G05000010400_F05000016256["Datum der Beantragung"]
  G05000010600_G05000010398_G05000010399_G05000010400_F05000016680["Hat die Betriebs- oder Zweigstellenlei"] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010600_G05000010398_G05000010399_G05000010400_F05000016256["Datum der Beantragung"]
  G05000010600_G05000010398_G05000010399_G05000010400_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] -.->|"<> 001 Auskunft wurde bereits b → forbidden"| G05000010600_G05000010398_G05000010399_G05000010400_F05000016258["Datum der Beantragung"]
  G05000010600_G05000010398_G05000010399_G05000010400_F05000016257["Wurde bereits eine Auskunft aus dem Ge"] ==>|"= 001 Auskunft wurde bereits b → required"| G05000010600_G05000010398_G05000010399_G05000010400_F05000016258["Datum der Beantragung"]
  G05000010600_G05000010401_F05000016274["Möchten Sie bei der Beratung und Vermi"] ==>|"= wahr → required"| G05000010600_G05000010401_G05000010403["Mitwirkende Mitarbeitende"]
  G05000010600_G05000010401_F05000016274["Möchten Sie bei der Beratung und Vermi"] -.->|"= falsch → forbidden"| G05000010600_G05000010401_G05000010403["Mitwirkende Mitarbeitende"]
  G05000010600_G05000010603_F05000016278["Sind sie bereits im Besitz einer weite"] ==>|"= wahr → required"| G05000010600_G05000010603_G05000010405["Sonstige gewerberechtliche Erlaubnisve"]
  G05000010600_G05000010603_F05000016278["Sind sie bereits im Besitz einer weite"] -.->|"<> wahr → forbidden"| G05000010600_G05000010603_G05000010405["Sonstige gewerberechtliche Erlaubnisve"]
  G05000010600_G05000010584_F05000016546["Ist oder war gegen die Gesellschaft od"] ==>|"= wahr → required"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010584_F05000016546["Ist oder war gegen die Gesellschaft od"] -.->|"= falsch → forbidden"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010584_F05000016547["Wird oder wurde gegen die Gesellschaft"] ==>|"= wahr → required"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010584_F05000016547["Wird oder wurde gegen die Gesellschaft"] -.->|"<> wahr → forbidden"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010584_F05000016548["Ist oder war gegen die Gesellschaft od"] ==>|"= wahr → required"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010584_F05000016548["Ist oder war gegen die Gesellschaft od"] -.->|"<> wahr → forbidden"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010584_F05000016979["Wird oder wurde gegen die Gesellschaft"] ==>|"= wahr → required"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  G05000010600_G05000010584_F05000016979["Wird oder wurde gegen die Gesellschaft"] -.->|"= falsch → forbidden"| G05000010600_G05000010584_F05000016407["Wenn vorstehend ja, bei welcher Staats"]
  unclear0["?: Wenn F05000016480 Auswahl der Person 01 Natürliche Person, d"]:::unclear
  classDef unclear fill:#fff3b0,stroke:#c9a227,color:#000
```
