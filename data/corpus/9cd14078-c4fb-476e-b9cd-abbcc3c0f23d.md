# Zu-/Abschläge zuweisen | CASABLANCA hotelsoftware - Dokumentation

# Zu-/Abschläge zuweisen

In CASABLANCA können Sie Zu- und Abschläge erstellen und den entsprechenden Raten zuweisen, z. B. einen Kurzaufenthaltszuschlag.  
Ein Kurzaufenthaltszuschlag ist ein zusätzlicher Betrag, der auf Buchungen mit einer kurzen Aufenthaltsdauer, z. B. 1 bis 3 Nächte, angewendet wird. Er dient dazu, die höheren Kosten für kürzere Buchungen auszugleichen und wird prozentual oder als fixer Betrag berechnet. Dieser Zuschlag wird automatisch zur Reservierung hinzugefügt, sobald die definierten Bedingungen erfüllt sind.

## Zuschlag erstellen und Raten zuweisen

Direkter Link: https://docs.casablanca.at/desktop/raten/rates/shortstay/#zuschlag-erstellen-und-raten-zuweisen

In dieser Anleitung wird Schritt für Schritt erklärt, wie ein Kurzaufenthaltszuschlag in CASABLANCA erstellt und einer Rate zugewiesen werden kann. Der Prozess gliedert sich in folgende Hauptschritte:

* Erstellen eines Artikels, der dem Zuschlag zugewiesen wird.
* Definieren des Zuschlags in der Preis-/Artikelverwaltung.
* Zuweisen des Zuschlags zu einer Rate oder einem Zimmertyp.

## Artikel erstellen

Direkter Link: https://docs.casablanca.at/desktop/raten/rates/shortstay/#artikel-erstellen

Bevor der Zuschlag angelegt werden kann, muss im System ein Artikel definiert werden. Dieser Artikel bildet die Grundlage für den Kurzaufenthaltszuschlag.

* 1. Melden Sie sich mit Ihren Zugangsdaten in CASABLANCA an.
* 2. Klicken Sie im Reiter **Preis/Artikelverwaltung** auf **Artikel**.  
  ![Bild1](https://docs.casablanca.at/assets/images/preis_artikelverwaltung-2084a980de290f6c77fc343d346ec2ca.png "Preis/Artikelverwaltung")
* 3. Klicken Sie auf das **+ Symbol** zum Erstellen eines neuen Artikels.  
  ![Bild1](https://docs.casablanca.at/assets/images/artikel_neu.png-8649f4106658220876feb025f98611f9.png "Artikel neu")
* 4. Passen Sie die Artikeleinstellungen rechts im Fenster an:
  * **Bezeichnung** – Geben Sie den Namen des Artikels ein.
  * Falls mehrsprachige Bezeichnungen erforderlich sind, klicken Sie auf die **Flagge**, um die Bezeichnung in anderen Sprachen zu hinterlegen.
  * **Kategorie** – Wählen Sie immer **Hotel Umsatz**.
  * **Steuersatz** – Klären Sie mit der Steuerberatung, welcher Steuersatz hinterlegt werden soll.
  * **Verwendung** – **Bei Zuschlägen** wählen Sie **Normal (+)** (**Bei Abschlägen** wählen Sie **Zahlung (-)**).  
  ![Bild1](https://docs.casablanca.at/assets/images/ka_zuschlag-bc6ea6e958e32cbc75cec49f7ba3fea8.png "Einstellungen Zuschlag")
* 5. Klicken Sie rechts unten auf **Artikelgruppe generieren**.  
  ![Bild1](https://docs.casablanca.at/assets/images/artikelgruppe-485d55d1d967281459f07a3927cbf796.png "Artikelgruppe neu")
* 6. Speichern Sie die Änderungen mit **Ok**.

## Zuschlag definieren

Direkter Link: https://docs.casablanca.at/desktop/raten/rates/shortstay/#zuschlag-definieren

Nachdem der Artikel erstellt wurde, können Sie den tatsächlichen Kurzaufenthaltszuschlag definieren.

* 1. Wechseln Sie in den Reiter **Preis/Artikelverwaltung** > **Zu-/Abschläge**.
* 2. Klicken Sie auf **+ Symbol** zum Erstellen eines neuen Zu-/Abschlags.
* 3. Es wird eine neue Zeile hinzugefügt. Geben Sie die Daten des Zuschlags ein:
  * **Name** – Dieser Text wird in der Reservierungsmaske und auf der Rechnung angezeigt.
  * **Schwellenwert** – Definieren Sie, wann der Zuschlag auftritt:
    * **Immer** – Der Zuschlag wird verwendet, sobald er einer Rate zugewiesen ist.
    * **Anzahl der Nächte** – Der Zuschlag wird verwendet, wenn die Anzahl der Nächte zwischen den Min.- und Max.-Werten liegt.
    * **Tage vor Anreise** – Der Zuschlag wird verwendet, wenn der Abstand zwischen Erstelldatum und Anreisedatum innerhalb der Min.- und Max.-Werte liegt.
  * **Berechnung** – Legen Sie fest, wie der Preis berechnet wird.
  * **Wert** – Geben Sie den Wert des Zuschlags an. Wählen Sie zwischen:
    * **+ / -** (positiver oder negativer Betrag)
    * **% / €** (Prozent oder fixer Betrag)
  * **Artikel** – Wählen Sie den zuvor erstellten Artikel aus.  
    ![Bild1](https://docs.casablanca.at/assets/images/ka_zuschlag_einstellungen-ce71ec390a5bf7a5a8b7183d04a7183c.png "Kurzaufenthaltszuschlag")
* 4. Speichern Sie den Zuschlag mit **Ok**.

## Zuschlag einer Rate zuweisen

Direkter Link: https://docs.casablanca.at/desktop/raten/rates/shortstay/#zuschlag-einer-rate-zuweisen

Nachdem der Zuschlag definiert wurde, kann er einer Rate zugewiesen werden. Es gibt zwei Möglichkeiten, den Zuschlag einer Rate zuzuweisen:

* Zuschlag einer Saison einer Rate zuweisen: Wenn der Zuschlag einer Saison zugewiesen wird, gilt er für alle Zimmertypen dieser Saison.
* Zuschlag einem Zimmertyp einer Saison einer Rate zuweisen: Falls der Zuschlag nur für bestimmte Zimmertypen gelten soll, muss er separat bei den jeweiligen Zimmertypen hinzugefügt werden.

Um den Zuschlag einer Rate zuzuweisen:

* 1. Klicken Sie im Reiter **Preis/Artikelverwaltung** auf **Raten**.
* 2. Klicken Sie in der Zeile der gewünschten Rate auf **Preisliste**.
* 3. Klicken Sie auf **einen der beiden + Buttons**, um den Zuschlag entweder einem Zeitraum oder einem Zimmertyp zuzuweisen.
* 4. Ein neues Fenster öffnet sich. Wählen Sie hier die gewünschten Zu-/Abschläge aus.
* 5. Klicken Sie auf **Ok**, um die Änderungen zu speichern.  
  ![Bild1](https://docs.casablanca.at/assets/images/zuschlag_saison-5ee057d06dc229275fd560c16037e4af.png "Kurzaufenthaltszuschlag")  
  ![Bild1](https://docs.casablanca.at/assets/images/zuschlag_zimmertyp-f8288de2c94594400ff4ecb292cb924c.png "Kurzaufenthaltszuschlag")

Mit dieser Vorgehensweise können Sie auch Abschläge erstellen und den entsprechenden Raten zuweisen.

## Navigation

* [Zurück — Preise kopieren](https://docs.casablanca.at/desktop/raten/rates/copy)
* [Weiter — Raten / Rabatte](https://docs.casablanca.at/desktop/raten/rates/accommodation_discounts)

* [Zuschlag erstellen und Raten zuweisen](https://docs.casablanca.at/desktop/raten/rates/shortstay/#zuschlag-erstellen-und-raten-zuweisen)
* [Artikel erstellen](https://docs.casablanca.at/desktop/raten/rates/shortstay/#artikel-erstellen)
* [Zuschlag definieren](https://docs.casablanca.at/desktop/raten/rates/shortstay/#zuschlag-definieren)
* [Zuschlag einer Rate zuweisen](https://docs.casablanca.at/desktop/raten/rates/shortstay/#zuschlag-einer-rate-zuweisen)