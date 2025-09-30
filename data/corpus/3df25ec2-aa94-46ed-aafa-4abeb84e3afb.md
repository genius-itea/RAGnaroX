# RKSV | CASABLANCA hotelsoftware - Dokumentation

# RKSV

## Österreich - Registrierkassensicherheitsverordnung (RKSV)
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#österreich---registrierkassensicherheitsverordnung-rksv)

Die Registrierkassensicherheitsverordnung (RKSV) in Österreich schreibt vor, dass Rechnungen mittels einem maschinenlesbaren Code (*QR-Code*) digital signiert und miteinander verkettet werden müssen.  
Die Verkettung der Rechnungen stellt sicher, dass keine nachträglichen Manipulationen an der Reihenfolge oder den Beträgen der Belege vorgenommen werden können.  
Alle wesentlichen Belegdaten (*z. B. Betrag, Datum, Uhrzeit, Belegnummer, Signaturwert*) sind dabei im QR-Code enthalten.

### Was wird fiskalisiert
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#was-wird-fiskalisiert)

* Rechnungen werden mit einem maschinenlesbaren Code (*QR-Code*) versehen bzw. digital signiert.

### Was benötigt CASABLANCA für die Einrichtung
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#was-benötigt-casablanca-für-die-einrichtung)

Für die Einrichtung sind folgende Daten notwendig:

* Benutzer für "Registrierkassen-Webservice" (*Anlage erfolgt in FinanzOnline*)
* RKSV KeyLabel
* RKSV-Formular

#### Benutzer für "Registrierkassen-Webservice"
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#benutzer-für-registrierkassen-webservice)

Damit die Meldung der Kassa sowie die notwendige Überprüfung von z.B. Start- oder Jahresbelegen erfolgen kann, ist es notwendig, einen Benutzer für den Zugriff über die Schnittstelle zu Ihrem FinanzOnline Account zu erstellen. Jener Benutzer, welcher Zugriff auf Ihren FinanzOnline Account besitzt, sollte die Anlage des "Registrierkassen-Webservice" Benutzers durchführen (*meist Buchhalter oder Steuerberater*).

Wie die Anlage des Benutzers erfolgen kann, finden Sie im Handbuch zur RKSV (*beschrieben ab Seite 57 bzw. 61*):

> [BMF Handbuch Registrierkassen (PDF)](https://finanzonline.bmf.gv.at/eLearning/BMF_Handbuch_Registrierkassen.pdf)

Bitte **senden Sie die Daten** des für CASABLANCA erstellten Registrierkassen-Webservice-Benutzers **an technik@casablanca.at**.  
Unser Onboarding-Team wird damit alles zur finalen Aktivierung bereits vorkonfigurieren.

#### RKSV KeyLabel
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#rksv-keylabel)

Zur Signierung der Rechnung wird ein **RKSV KeyLabel** benötigt. Dieses KeyLabel ist im "RKSV Fiskalpaket" Ihrer Bestellung enthalten. Es muss unter Angabe der **UID Nummer Ihres Betriebs** ausgestellt werden. Das KeyLabel für Ihren Betrieb wird ebenfalls direkt von unserem Onboarding-Team erstellt.

## Info

Bitte achten Sie darauf, dass die Angabe der UID-Nummer im folgenden RKSV-Formular korrekt erfolgt. Durch eine fehlerhafte Angabe könnten weitere Kosten entstehen (*da in einem solchen Fall ein neues KeyLabel ausgestellt werden müsste!*).

#### RKSV-Formular
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#rksv-formular)

Auf den Rechnungen, welche über die Hotelsoftware ausgestellt werden, müssen alle Informationen zum Betrieb angegeben werden. Damit diese Informationen von unserem Onboarding-Team vorab korrekt hinterlegt werden können, bitten wir Sie folgendes Online-Formular korrekt auszufüllen und zu senden.

> [RKSV-Formular](https://www.casablanca.at/rksv-formular/)

### Aktivierung der Software-Kassa
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#aktivierung-der-software-kassa)

Die Aktivierung der RKSV-Kassa in CASABLANCA wird nach der Einschulung in die Hotelsoftware von einem Mitarbeiter des Customer Support Teams durchgeführt. Dabei wird die Software-Kassa sowie ein Startbeleg über unsere Software erstellt und mit den von Ihnen bereitgestellten Daten (*Registrierkassen-Webservice-Benutzer*) an Ihren FinanzOnline Account übermittelt. Die Kassa wird dabei korrekt über FinanzOnline registriert.

### Was muss im laufenden Betrieb beachtet werden
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#was-muss-im-laufenden-betrieb-beachtet-werden)

#### Datenexportprotokoll-Sicherung
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#datenexportprotokoll-sicherung)

Gesetzlich ist jeder Betrieb verpflichtet, eine Datensicherung des Datenexportprotokolls (*kurz DEP*) vierteljährlich (*also einmal pro Quartal*) auf ein externes Medium (*z. B. USB-Stick*) zu speichern. Dieser Export des DEP kann z. B. bei einer Kassennachschau oder einer Finanzprüfung vom Finanzamt gefordert werden.  
Wie das über CASABLANCA hotelsoftware funktioniert, finden Sie in folgendem Artikel:  
* [Datensicherung RKSV](https://docs.casablanca.at/desktop/fiscalization/rksv/data_backup_rksv)

#### Jahresbeleg
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#jahresbeleg)

Für jede in FinanzOnline registrierte Kassa ist es notwendig, am Ende jeden Jahres einen "Jahresbeleg" zu erstellen und über FinanzOnline zu prüfen. Der Jahresbeleg wird in CASABLANCA hotelsoftware dabei automatisch erstellt und ebenso automatisch geprüft. Näheres dazu finden Sie unter folgendem Artikel:  
* [RKSV - Jahresbeleg erstellen](https://docs.casablanca.at/desktop/fiscalization/rksv/rksv_annual_receipt)

#### Kassennachschau bzw. Finanzprüfung
(Direkter Link: https://docs.casablanca.at/onboarding/fiscalization/rksv/#kassennachschau-bzw-finanzprüfung)

Sollte bei Ihrem Betrieb eine Kassennachschau oder eine Finanzprüfung durchgeführt werden, können Sie die dafür benötigten Daten sehr schnell aus der Software exportieren. Wie das funktioniert wird in folgendem Artikel beschrieben:  
* [RKSV - Daten exportieren](https://docs.casablanca.at/desktop/fiscalization/rksv/rksv_data_export)

## Navigation

* [Zurück: Fiskalisierung](https://docs.casablanca.at/onboarding/fiscalization/)
* [Weiter: KassenSichV](https://docs.casablanca.at/onboarding/fiscalization/kassensichv)

* [Österreich - Registrierkassensicherheitsverordnung (RKSV)](https://docs.casablanca.at/onboarding/fiscalization/rksv/#österreich---registrierkassensicherheitsverordnung-rksv)
* [Was wird fiskalisiert](https://docs.casablanca.at/onboarding/fiscalization/rksv/#was-wird-fiskalisiert)
* [Was benötigt CASABLANCA für die Einrichtung](https://docs.casablanca.at/onboarding/fiscalization/rksv/#was-benötigt-casablanca-für-die-einrichtung)
* [Benutzer für "Registrierkassen-Webservice"](https://docs.casablanca.at/onboarding/fiscalization/rksv/#benutzer-für-registrierkassen-webservice)
* [RKSV KeyLabel](https://docs.casablanca.at/onboarding/fiscalization/rksv/#rksv-keylabel)
* [RKSV-Formular](https://docs.casablanca.at/onboarding/fiscalization/rksv/#rksv-formular)
* [Aktivierung der Software-Kassa](https://docs.casablanca.at/onboarding/fiscalization/rksv/#aktivierung-der-software-kassa)
* [Was muss im laufenden Betrieb beachtet werden](https://docs.casablanca.at/onboarding/fiscalization/rksv/#was-muss-im-laufenden-betrieb-beachtet-werden)
* [Datenexportprotokoll-Sicherung](https://docs.casablanca.at/onboarding/fiscalization/rksv/#datenexportprotokoll-sicherung)
* [Jahresbeleg](https://docs.casablanca.at/onboarding/fiscalization/rksv/#jahresbeleg)
* [Kassennachschau bzw. Finanzprüfung](https://docs.casablanca.at/onboarding/fiscalization/rksv/#kassennachschau-bzw-finanzprüfung)