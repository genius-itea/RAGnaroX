# Intersport Rent Integration | CASABLANCA hotelsoftware - Dokumentation

## Integration von INTERSPORT Rent in Seekda und CASABLANCA

## Info

Die Integration von **INTERSPORT Rent** ist standardmäßig für alle Betriebe in Österreich als kostenloses Feature für Gäste **von Seekda** aktiviert.  
Bei einer Reservierung wird INTERSPORT Rent als Fixleistung mitgesendet. Diese Fixleistung muss in CASABLANCA mit einem Artikel und dem entsprechenden Steuersatz gemappt werden, damit sie korrekt angezeigt und gegebenenfalls verrechnet werden kann. Dies ist auch notwendig, wenn der Artikel mit einem Preis von 0 € gesendet wird.

## Hinweis

Ist kein Mapping hinterlegt, wird der Artikel in der Buchung als „Nicht definiert Umsatz“ importiert.

![Artikel in CASABLANCA](https://docs.casablanca.at/assets/images/article_in_casablanca-3a965a4743d162c94b6f85076c790a56.png)

**Lösungen:**
* [Artikel in CASABLANCA Online Systems mappen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-mappen)
* [Funktion in Seekda deaktivieren](https://docs.casablanca.at/cloud/interfaces/seekda/#intersport-rent-in-seekda-deaktivieren)

## Artikel mappen

Direkter Link: [Artikel mappen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-mappen)

Damit der Artikel korrekt importiert werden kann, müssen Sie in CASABLANCA ein Mapping hinterlegen. Gehen Sie dazu wie folgt vor:

### 1. Neuen Artikel in CASABLANCA Desktop anlegen

Direkter Link: [1. Neuen Artikel in CASABLANCA Desktop anlegen](https://docs.casablanca.at/cloud/interfaces/seekda/#1-neuen-artikel-in-casablanca-desktop-anlegen)

Navigieren Sie in CASABLANCA Desktop zu **Preis / Artikelverwaltung > Artikel**, und legen Sie einen neuen Artikel an:

![Preis / Artikelverwaltung -> Artikel](https://docs.casablanca.at/assets/images/job_base_data-24a0a92b88417748076cbb85407e7cb0.png "Preis / Artikelverwaltung -> Artikel")

### Artikel-Einstellungen

Direkter Link: [Artikel-Einstellungen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-einstellungen)

![Artikel anlegen](https://docs.casablanca.at/assets/images/insert_job-1dd8a425e66651c9f9053779a0fce298.png "Artikel anlegen")

* 1. **Bezeichnung**: `INTERSPORT Rent in unserer Nähe!`
* 2. **Kategorie**: `Hotelumsatz`
* 3. **Steuersatz**: `0% MWST`
* 4. **Verwendung**: `Normal (+)`
* 5. Aktivieren Sie „Artikelgruppe generieren“
* 6. Bestätigen Sie die Eingabe mit **OK**.

### 2. Mapping in CASABLANCA Online Systems hinterlegen

Direkter Link: [2. Mapping in CASABLANCA Online Systems hinterlegen](https://docs.casablanca.at/cloud/interfaces/seekda/#2-mapping-in-casablanca-online-systems-hinterlegen)

Navigieren Sie in CASABLANCA Online Systems zu **Einstellungen > Stammdaten**.

![Einstellungen -> Stammdaten](https://docs.casablanca.at/assets/images/settings_basedata-2f7dc1085fa74b958d6a81b242521c87.png "Einstellungen -> Stammdaten")

Wählen Sie anschließend den Punkt **Artikel** aus, und klicken Sie auf **Mapping**.

![Artikel](https://docs.casablanca.at/assets/images/jobs-5de20e6913689533de720fa0e98937d1.png "Artikel")
![Mapping](https://docs.casablanca.at/assets/images/mapping-ff05d2ed9fe40d5ea6e2845580b9c4c6.png "Mapping")
![Mapping hinzufügen](https://docs.casablanca.at/assets/images/add_mapping-9066bbf9c06c1e33455e9b444f91e9cb.png "Mapping hinzufügen")

* 1. Klicken Sie auf **Hinzufügen**.
* 2. Tragen Sie in der Spalte **Mapping** den folgenden Wert ein (exakt in dieser Schreibweise, auch darauf achten, dass **keine Leerzeichen hinterlegt** werden):
  * `IntersportRent`
* 3. Wählen Sie in der Spalte **Job ID** den neu angelegten Artikel aus. Sie können auch nach dem Artikel suchen.
* 4. **Speichern** Sie die Änderungen.

## Wichtig

Bereits importierte Buchungen werden **nicht automatisch aktualisiert**. Sie müssen die Fixleistung „Nicht Definiert Umsatz“ in diesen Buchungen manuell entfernen und den neuen Artikel **INTERSPORT Rent** hinzufügen.

## INTERSPORT Rent in Seekda deaktivieren

Direkter Link: [INTERSPORT Rent in Seekda deaktivieren](https://docs.casablanca.at/cloud/interfaces/seekda/#intersport-rent-in-seekda-deaktivieren)

Falls Sie die Funktion nicht nutzen möchten, können Sie die Integration jederzeit deaktivieren. Folgen Sie diesen Schritten:

* 1. Melden Sie sich im **Seekda-Backend** an.
* 2. Navigieren Sie zum **Marketplace**.
* 3. Deaktivieren Sie die Option **INTERSPORT Rent** mit einem Klick.

![Intersport Rent deaktivieren](https://docs.casablanca.at/assets/images/deactivate_intersport_rent-6d69d876cb156420ed3b49076961d425.png)

---

* [Zurück HRS Schnittstelle](https://docs.casablanca.at/cloud/interfaces/hrs/)
* [Weiter Module](https://docs.casablanca.at/cloud/module/)
* [Artikel mappen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-mappen)
* [1. Neuen Artikel in CASABLANCA Desktop anlegen](https://docs.casablanca.at/cloud/interfaces/seekda/#1-neuen-artikel-in-casablanca-desktop-anlegen)
* [Artikel-Einstellungen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-einstellungen)
* [2. Mapping in CASABLANCA Online Systems hinterlegen](https://docs.casablanca.at/cloud/interfaces/seekda/#2-mapping-in-casablanca-online-systems-hinterlegen)
* [INTERSPORT Rent in Seekda deaktivieren](https://docs.casablanca.at/cloud/interfaces/seekda/#intersport-rent-in-seekda-deaktivieren)