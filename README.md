GERMAN

Benutzungsstunden_APP über die Django-Admin Seite http://127.0.0.1:8000/admin/upload/ nutzbar und dort kann man eine Excel-Datei mit Lastgangdaten hochladen und die APP rechnet die Benutzungsstunden jedes Kunden aus. Die zugehörige Excel-Datei mit den Lastgangdaten zum Testen ist im Ordner beigefügt.

Die Ergebnisse werden über http://127.0.0.1:8000/results/ ausgegeben und das Programm prüft ob es redundante Daten gibt(falls man dieselbe Datei oder dieselben Kunden nochmal hochlädt). Diese werden dann gelöscht und nicht in die Tabelle aufgenommen. 

Auf http://127.0.0.1:8000/clean-results/ habe ich eine sortierte und bereinigte Ausgabe der Tabelle gemacht.
Es wird nach Kundennummer aufsteigend sortiert und man hat auf jeder Seite einen Link um auf die anderen Seiten zuzugreifen. Es wird auch überprüft ob es ein Schaltjahr ist oder kein Schaltjahr.


Nach Download

-virtuelle Umgebung erstellen

-requirements.txt Packete installieren

-mit Befehl python manage.py makemigrations Datenbank migrieren

-mit Befehl python manage.py migrate Datenbankmigrationen anwenden

-SuperUser für die Admin-Seite ist hier 	-IHK und -Ihk2024 für Passwort

-runserver über localhost mit Befehl python manage.py runserver


Jetzt kann man über die oben genannte Admin-Seite mit dem genannten SuperUser in die APP reinkommen und diese auch benutzen! Beim Hochladen muss man die Excel-Datei benutzen um zu prüfen ob es ordnungsgemäß läuft. Viel Spaß beim verändern und probieren. :-)







ENGLISH

Hours of use(in electricity)_APP can be used via the Django admin page http://127.0.0.1:8000/admin/upload/ and there you can upload an Excel file with load profile data and the APP calculates the hours of use for each customer. The associated Excel file with the load profile data for testing is attached in the folder.

The results are output via http://127.0.0.1:8000/results/ and the program checks whether there is redundant data (if you upload the same file or the same customers again). These are then deleted and not included in the table.

I made a sorted and cleaned output of the table on http://127.0.0.1:8000/clean-results/.
It is sorted in ascending order by customer number and there is a link on each page to access the other pages. It is also checked whether it is a leap year or not.


After downloading

-create virtual environment

-requirements.txt Install packages

-Migrate database with command python manage.py makemigrations

-apply database migrations using the python manage.py migrate command

-SuperUser for the admin page is here -IHK and -Ihk2024 for password

-runserver via localhost with command python manage.py runserver


Now you can get into the APP via the above-mentioned admin page with the mentioned SuperUser and use it! When uploading you have to use the Excel file to check whether it runs properly. Have fun changing and trying things out. :-)
