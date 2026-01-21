Intersport Rent Integration | CASABLANCA hotelsoftware - Dokumentation  
[Zum Hauptinhalt springen](https://docs.casablanca.at/cloud/interfaces/seekda/#__docusaurus_skipToContent_fallback)[![CASABLANCA hotelsoftware Logo](https://docs.casablanca.at/img/logo.png) ![CASABLANCA hotelsoftware Logo](https://docs.casablanca.at/img/Casablanca_LOGO_2022_neg.png)](https://docs.casablanca.at/) [Desktop](https://docs.casablanca.at/desktop/desktop/)[Cloud](https://docs.casablanca.at/cloud/cloud_systems/)[FAQ](https://docs.casablanca.at/faq)[Onboarding](https://docs.casablanca.at/onboarding/fiscalization)[Systemvoraussetzungen](https://docs.casablanca.at/system_requirements)  
* [Übersicht](https://docs.casablanca.at/cloud/cloud_systems/)
* [Dashboard](https://docs.casablanca.at/cloud/dashboard/)
* [Benutzerverwaltung](https://docs.casablanca.at/cloud/user_management/)
* [Betriebe](https://docs.casablanca.at/cloud/company/)
* [Personengruppen](https://docs.casablanca.at/cloud/person_groups/)
* [Zimmerverwaltung](https://docs.casablanca.at/cloud/rooms/)
* [Stammdaten](https://docs.casablanca.at/cloud/main_data/)
* [Buchungen](https://docs.casablanca.at/cloud/bookings/)
* [Raten / Preiseingabe](https://docs.casablanca.at/cloud/raten/)
* [Online Check-In](https://docs.casablanca.at/cloud/online_checkin/)
* [Korrespondenz](https://docs.casablanca.at/cloud/online_corr/)
* [Schnittstellen](https://docs.casablanca.at/cloud/interfaces/)
+ [ABM WebsLine](https://docs.casablanca.at/cloud/interfaces/abm/)
+ [Booking.com](https://docs.casablanca.at/cloud/interfaces/bookingcom/)
+ [CapCorn](https://docs.casablanca.at/cloud/interfaces/capcorn/)
+ [Datatrans Direktzahlung](https://docs.casablanca.at/cloud/interfaces/datatrans/)
+ [Gastfreund](https://docs.casablanca.at/cloud/interfaces/gastfreund/)
+ [HotelNetSolutions](https://docs.casablanca.at/cloud/interfaces/hns/)
+ [HRS](https://docs.casablanca.at/cloud/interfaces/hrs/)
+ [Seekda](https://docs.casablanca.at/cloud/interfaces/seekda/)
* [Module](https://docs.casablanca.at/cloud/module/)  
* [Schnittstellen](https://docs.casablanca.at/cloud/interfaces/)
* Seekda
Auf dieser Seite

# Integration von INTERSPORT Rent in Seekda und CASABLANCA  
info  
Die Integration von **INTERSPORT Rent** ist standardmäßig für alle Betriebe in Österreich als kostenloses Feature für Gäste **von Seekda** aktiviert.  
Bei einer Reservierung wird INTERSPORT Rent als Fixleistung mitgesendet. Diese Fixleistung muss in CASABLANCA mit einem Artikel und dem entsprechenden Steuersatz gemappt werden, damit sie korrekt angezeigt und gegebenenfalls verrechnet werden kann. Dies ist auch notwendig, wenn der Artikel mit einem Preis von 0 € gesendet wird.  
Hinweis  
Ist kein Mapping hinterlegt, wird der Artikel in der Buchung als „Nicht definiert Umsatz“ importiert.  
![Artikel in CASABLANCA](https://docs.casablanca.at/assets/images/article_in_casablanca-3a965a4743d162c94b6f85076c790a56.png)  
**Lösungen**:  
1. [Artikel in CASABLANCA Online Systems mappen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-mappen)
2. [Funktion in Seekda deaktivieren](https://docs.casablanca.at/cloud/interfaces/seekda/#intersport-rent-in-seekda-deaktivieren)

## Artikel mappen[](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-mappen "Direkter Link zu Artikel mappen")  
Damit der Artikel korrekt importiert werden kann, müssen Sie in CASABLANCA ein Mapping hinterlegen. Gehen Sie dazu wie folgt vor:

### 1. Neuen Artikel in CASABLANCA Desktop anlegen[](https://docs.casablanca.at/cloud/interfaces/seekda/#1-neuen-artikel-in-casablanca-desktop-anlegen "Direkter Link zu 1. Neuen Artikel in CASABLANCA Desktop anlegen")  
Navigieren Sie in CASABLANCA Desktop zu **Preis / Artikelverwaltung > Artikel**, und legen Sie einen neuen Artikel an:  
![Preis / Artikelverwaltung -&gt; Artikel](https://docs.casablanca.at/assets/images/job_base_data-24a0a92b88417748076cbb85407e7cb0.png "Preis / Artikelverwaltung -> Artikel")

### Artikel-Einstellungen[](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-einstellungen "Direkter Link zu Artikel-Einstellungen")  
![Artikel anlegen](https://docs.casablanca.at/assets/images/insert_job-1dd8a425e66651c9f9053779a0fce298.png "Artikel anlegen")  
1. **Bezeichnung**: `INTERSPORT Rent in unserer Nähe!`
2. **Kategorie**: `Hotelumsatz`
3. **Steuersatz**: `0% MWST`
4. **Verwendung**: `Normal (+)`
5. Aktivieren Sie „Artikelgruppe generieren“
6. Bestätigen Sie die Eingabe mit **OK**.

### 2. Mapping in [CASABLANCA Online Systems](https://booking.casablanca.at) hinterlegen[](https://docs.casablanca.at/cloud/interfaces/seekda/#2-mapping-in-casablanca-online-systems-hinterlegen "Direkter Link zu 2-mapping-in-casablanca-online-systems-hinterlegen")  
Navigieren Sie in CASABLANCA Online Systems zu **Einstellungen > Stammdaten**.  
![Einstellungen -&gt; Stammdaten](https://docs.casablanca.at/assets/images/settings_basedata-2f7dc1085fa74b958d6a81b242521c87.png "Einstellungen -> Stammdaten")  
Wählen Sie anschließend den Punkt **Artikel** aus, und klicken Sie auf **Mapping**.  
![Artikel](https://docs.casablanca.at/assets/images/jobs-5de20e6913689533de720fa0e98937d1.png "Artikel")  
![Mapping](https://docs.casablanca.at/assets/images/mapping-ff05d2ed9fe40d5ea6e2845580b9c4c6.png "Mapping")  
Hinterlegen Sie das Mapping für den neuen Artikel:  
![Mapping hinzufügen](https://docs.casablanca.at/assets/images/add_mapping-9066bbf9c06c1e33455e9b444f91e9cb.png)  
1. Klicken Sie auf **Hinzufügen**.
2. Tragen Sie in der Spalte **Mapping** den folgenden Wert ein *(exakt in dieser Schreibweise, auch darauf achten, dass **keine Leerzeichen hinterlegt** werden)*:
`IntersportRent`
3. Wählen Sie in der Spalte **Job ID** den neu angelegten Artikel aus. Sie können auch nach dem Artikel suchen.
4. **Speichern** Sie die Änderungen.  
Wichtig  
Bereits importierte Buchungen werden **nicht automatisch aktualisiert**. Sie müssen die Fixleistung „Nicht Definiert Umsatz“ in diesen Buchungen manuell entfernen und den neuen Artikel **INTERSPORT Rent** hinzufügen.

## INTERSPORT Rent in Seekda deaktivieren[](https://docs.casablanca.at/cloud/interfaces/seekda/#intersport-rent-in-seekda-deaktivieren "Direkter Link zu INTERSPORT Rent in Seekda deaktivieren")  
Falls Sie die Funktion nicht nutzen möchten, können Sie die Integration jederzeit deaktivieren. Folgen Sie diesen Schritten:  
1. Melden Sie sich im **Seekda-Backend** an.
2. Navigieren Sie zum **Marketplace**.
3. Deaktivieren Sie die Option **INTERSPORT Rent** mit einem Klick.  
![Intersport Rent deaktivieren](https://docs.casablanca.at/assets/images/deactivate_intersport_rent-6d69d876cb156420ed3b49076961d425.png)  
[ZurückHRS Schnittstelle](https://docs.casablanca.at/cloud/interfaces/hrs/)[WeiterModule](https://docs.casablanca.at/cloud/module/)  
* [Artikel mappen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-mappen)
+ [1. Neuen Artikel in CASABLANCA Desktop anlegen](https://docs.casablanca.at/cloud/interfaces/seekda/#1-neuen-artikel-in-casablanca-desktop-anlegen)
+ [Artikel-Einstellungen](https://docs.casablanca.at/cloud/interfaces/seekda/#artikel-einstellungen)
+ [2. Mapping in CASABLANCA Online Systems hinterlegen](https://docs.casablanca.at/cloud/interfaces/seekda/#2-mapping-in-casablanca-online-systems-hinterlegen)
* [INTERSPORT Rent in Seekda deaktivieren](https://docs.casablanca.at/cloud/interfaces/seekda/#intersport-rent-in-seekda-deaktivieren)