Trinkgeldverwaltung Restaurant-Kellner | CASABLANCA hotelsoftware - Dokumentation  
[Zum Hauptinhalt springen](https://docs.casablanca.at/desktop/cashbook/tip_management/#__docusaurus_skipToContent_fallback)[![CASABLANCA hotelsoftware Logo](https://docs.casablanca.at/img/logo.png) ![CASABLANCA hotelsoftware Logo](https://docs.casablanca.at/img/Casablanca_LOGO_2022_neg.png)](https://docs.casablanca.at/) [Desktop](https://docs.casablanca.at/desktop/desktop/)[Cloud](https://docs.casablanca.at/cloud/cloud_systems/)[FAQ](https://docs.casablanca.at/faq)[Onboarding](https://docs.casablanca.at/onboarding/fiscalization)[Systemvoraussetzungen](https://docs.casablanca.at/system_requirements)  
* [CASABLANCA Desktop](https://docs.casablanca.at/desktop/desktop/)
* [Übersicht](https://docs.casablanca.at/desktop/interface/)
* [Benutzerverwaltung](https://docs.casablanca.at/desktop/user_management/)
* [Zimmerplan](https://docs.casablanca.at/desktop/room_plan/)
* [Gästekartei](https://docs.casablanca.at/desktop/guest_profile/)
* [Raten / Preiseingabe](https://docs.casablanca.at/desktop/raten/)
* [Artikelverwaltung](https://docs.casablanca.at/desktop/articles/)
* [Gästekarten / Tourismus](https://docs.casablanca.at/desktop/guest_cards/)
* [Reservierungsvorgang](https://docs.casablanca.at/desktop/reservation_process/)
* [Meldewesen](https://docs.casablanca.at/desktop/registration/)
* [Check-In](https://docs.casablanca.at/desktop/check_in/)
* [Korrespondenz](https://docs.casablanca.at/desktop/correspondence/)
* [Buchungsverwaltung](https://docs.casablanca.at/desktop/account/)
* [Check-Out](https://docs.casablanca.at/desktop/check-out/)
* [Rechnungslegung](https://docs.casablanca.at/desktop/accounting/)
* [Kassenbuch](https://docs.casablanca.at/desktop/cashbook/)
+ [Kassenbuch einrichten](https://docs.casablanca.at/desktop/cashbook/cashbook_create)
+ [Kassenbuch Schicht-Abschluss](https://docs.casablanca.at/desktop/cashbook/cashbook_per_user)
+ [Trinkgeldverwaltung Restaurant-Kellner](https://docs.casablanca.at/desktop/cashbook/tip_management)
+ [Bankbuch](https://docs.casablanca.at/desktop/cashbook/bankbook)
* [Tagesabschluss](https://docs.casablanca.at/desktop/daily_closing/)
* [Fiskalisierung](https://docs.casablanca.at/desktop/fiscalization/)
* [Steuerumstellungen](https://docs.casablanca.at/desktop/tax_changes/)
* [Listen](https://docs.casablanca.at/desktop/lists/)
* [Module](https://docs.casablanca.at/desktop/module/)
* [Schnittstellen](https://docs.casablanca.at/desktop/interfaces/)
* [hidden Seite für copilot](https://docs.casablanca.at/desktop/hidden_copilot)
* [Eignungstest für Bewerber/innen](https://docs.casablanca.at/desktop/qualification)
* [Schulversion](https://docs.casablanca.at/desktop/schoolversion)  
* [Kassenbuch](https://docs.casablanca.at/desktop/cashbook/)
* Trinkgeldverwaltung Restaurant-Kellner
Auf dieser Seite

# Trinkgeldverwaltung Restaurant-Kellner  
Die Trinkgeldverwaltung im Kassenbuch ist **ausschließlich zum Ausbuchen von Trinkgeld der Kellner aus der Restaurant-Kasse**.  
Damit diese Verwaltung verwendet werden kann, muss eine Kassenschnittstelle mit Kellnerumsatzübermittlung in CASABLANCA eingerichtet sein.  
Ob der Kellnerumsatz in ihrer Software aktiv ist, kann im Kassenbuch am Trinkgeld-Symbol („rosa Sparschwein“) erkennt werden. Ist dieses Symbol ausgegraut, ist der Kellnerumsatz nicht aktiv. Ist das Symbol nicht ausgegraut (wie in unserem Beispielbild unten), ist der Kellnerumsatz in ihrer Software aktiviert. Sie können auch in der Umsatzliste prüfen, ob der Kellnerumsatz aktiv ist. Scheint in der Umsatzliste Punkt 3 **"Erlöse-Restaurant"** und 4 **"Zahlungen Restaurant"** auf, dann ist dieser aktiv.  
![tip_management_button](https://docs.casablanca.at/assets/images/tip_management_button-e4239b25ba459adf99433320201c5efe.png)

## Einstellungen für Trinkgeldverwaltung[](https://docs.casablanca.at/desktop/cashbook/tip_management/#einstellungen-für-trinkgeldverwaltung "Direkter Link zu Einstellungen für Trinkgeldverwaltung")  
Damit die Trinkgeldverwaltung funktioniert, muss in den Kellnerumsatz-Einstellungen bei der Warengruppe für das Trinkgeld ein Haken gesetzt werden.  
Diese Einstellung ist hier zu finden:  
Schnittstellen --> Kassa --> Kellnerumsatz  
![kellnerumsatz](https://docs.casablanca.at/assets/images/kellnerumsatz-8b0af9f605e8a36c63a655a3261743a2.png)  
Anschließend unten auf Einstellungen --> Warengruppen --> Trinkgeld-Mapping aus der Liste finden und den Haken bei "Trinkgeld" setzen.  
![trinkgeld_haken](https://docs.casablanca.at/assets/images/trinkgeld_haken-9a9a1dd35db33ded8b5fdc2529432284.png)  
Sobald der Haken gesetzt wurde, wird beim nächsten Import vom Kellnerumsatz das Trinkgeld in der Trinkgeldverwaltung mitgerechnet.

## Auszahlen vom Trinkgeld an die Kellner[](https://docs.casablanca.at/desktop/cashbook/tip_management/#auszahlen-vom-trinkgeld-an-die-kellner "Direkter Link zu Auszahlen vom Trinkgeld an die Kellner")  
Wenn der Kellner zum Abrechnen vom Trinkgeld kommt, kann im Kassenbuch mit diesem Button die Trinkgeldverwaltung geöffnet werden.  
![tip_management_button](https://docs.casablanca.at/assets/images/tip_management_button-e4239b25ba459adf99433320201c5efe.png)  
Es öffnet sich ein Fenster, in dem alle in CASABLANCA angelegten Kellner mit dem aktuellen Trinkgeldstand dargestellt werden.
Pro Kellner wird dort angegeben, wann zuletzt ein Trinkgeld erhalten wurde (in der Restaurant-Kasse verbucht), wann der Kellner zuletzt das Trinkgeld erhalten hat sowie der Stand vom Trinkgeld seit diesem Datum.  
![trinkgeld_stand](https://docs.casablanca.at/assets/images/trinkgeld_stand-abe16494d6e9636979116d240418476c.png)  
Hier kann der Kellner ausgewählt werden. Rechts mit dem Button wird das Trinkgeld vom aktuell eingeloggten Benutzer aus dem Kassabuch als Ausgabe ausgebucht.  
![kellner auswaehlen](https://docs.casablanca.at/assets/images/Kellner_auswaehlen-fea57242aee4f835cf9a4572b3e05a0e.png)  
Anschließend kann falls erwünscht noch eine Auszahlungsbestätigung ausgedruckt werden.  
![tip_confirmation](https://docs.casablanca.at/assets/images/tip_confirmation-eaee1a0bca3bd995f4a513a3d56973fe.png)  
Bei dem Benutzer wurde nun das Trinkgeld als Ausgabe verbucht.  
![tip_ausgabe](https://docs.casablanca.at/assets/images/tip_ausgabe-c8317e82f22c969011276f74978f6f5e.png)  
Falls der in CASABLANCA eingeloggte Benutzer nicht genug Bargeld hat, ist der **"Auszahlen"** Button ausgegraut.  
Um das Trinkgeld auszubuchen, muss sich entweder ein anderer Benutzer in CASABLANCA einloggen, oder es könnte auch aus dem Tresor Kassabuch ausgezahlt werden (Tresor Kassabuch links auswählen).  
![Geld_fehlt](https://docs.casablanca.at/assets/images/Geld_fehlt-8260f3c7db12c939ca1c08a77d26ba4c.png)  
[ZurückKassenbuch Schicht-Abschluss](https://docs.casablanca.at/desktop/cashbook/cashbook_per_user)[WeiterBankbuch](https://docs.casablanca.at/desktop/cashbook/bankbook)  
* [Einstellungen für Trinkgeldverwaltung](https://docs.casablanca.at/desktop/cashbook/tip_management/#einstellungen-für-trinkgeldverwaltung)
* [Auszahlen vom Trinkgeld an die Kellner](https://docs.casablanca.at/desktop/cashbook/tip_management/#auszahlen-vom-trinkgeld-an-die-kellner)