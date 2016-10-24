# Projekt Vorschläge

THINK Big! Da wir die Projekte gemeinsam angehen werden (mind. 6 Personen pro Projekt) können die Projekte ruhig größer ausfallen. Sie brauchen aber keine Angst haben, falls Sie ein Projekt nicht zeitgerecht abschließen können. Ich werde mir hier speziell die Fortschritte in ihren Projekten und wie die Zusammenarbeit in ihrem Team funktioniert ansehen, kommentieren und natürlich auch benoten. Denken Sie an Programme, die vielleicht in ihrer Arbeit oder für ihre Masterarbeit nützlich wären oder an Programme die es eigentlich schon längst geben müsste aber noch niemand für Sie entwickelt hat.

Die einzige Voraussetzung ist, dass das Endprodukt unter einer Open Source Lizenz stehen wird. Verwenden Sie deshalb auch keine geheimen oder vertraulichen Daten ihrer Firma oder anderer nicht beteiligter Personen. Vergessen Sie nicht unsere Github Accounts sind öffentlich zugänglich.

Nach Abschluss dieser Vorlesung können Sie natürlich diese Projekte in Eigenverantwortung oder im Team weiter vorantreiben.

## Was geht ...

+ **Web Scraping** - Parsen von Webseiten. Holen Sie sich jederlei Information von diversen Seiten. Nutzen Sie Restful Web APIs wie die von KEGG oder NCBI um Datenbanken abzufragen.
+ **Web Service** - Oder erstellen Sie gleich ihr eigenes Webservice mit mächtigen Python Web Frameworks wie Django oder Flask. Kennen Sie Instagram oder Pinterest? Die und viele mehr laufen in Python.
+ **Embedded Software Engineering** - Sie besitzen eine Raspberry pi und wollen ihr Heim automatisieren. Kein Problem Python läuft auch darauf. Bedenken Sie nur, dass alle in dem Team Zugriff auf einen Raspberry oder vergleichbares haben sollte. Ich kann sie hier nur mit meinem Raspberry pi 2 und einigen Sensoren unterstützen
+ **Game Development** - Sie wollten schon immer ihr eigenes Spiel entwickeln. Auch das ist möglich mit Frameworks wie Panda3D. Aber seien sie gewarnt. Spiele gehörten schon immer zur Königsdisziplin in der Programmierung und erfordern großes Wissen in vielen anderen Themengebieten.
+ **Desktop Applications** - Eine eigene Fotoapp mit einer grafischen Benutzeroberfläche. Python unterstützt diverse GUI Frameworks wie GTK, Qt oder dem etwas verstaubten Python eigenen TKinter.
+ **Image Processing** - Auswertung von Mikroskopbildern, Bildmanipulationen kein Problem. Mit den mächtigen Frameworks cv2 und/oder skimage beinahe zu leicht.
+ **Bioinformatic Tools and Workflows** - Speziell im wissenschaftlichen Bereich gibt es eine Flut an Modulen, die sie hier unterstützen. Hier ein paar der wichtigsten: Numpy (numerisches Rechnen), Pandas (das bessere Excel), Biopython (Arbeiten mit Sequenzen und biologischen Daten), Rpy2 (laufen Sie R Code direkt in ihrem Python Skript), Snakemake (Bauen Sie flexible, mächtige Workflows in R, Python und in der Shell). Wahrscheinlich auch ein Grund warum das MIT intern alle Skripte auf Python umgestellt hat.
+ **Coding Music** - Sie wollten schon immer DJ sein und selbst Musik produzieren. Mit Sonic pi auch am Raspberry möglich.
+ **Working with Databases** - Python unterstützt sie mit einer Menge von Modulen um direkt oder auch indirekt (ORM) mit den verschiedensten Datenbanken zu arbeiten. Das ist vorallem in Verbindung mit *Web Services* ein mächtiges Werkzeug.
+ **Or all together** - Natürlich kann es hier auch zu Überlappungen kommen. In Python ist so gut wie alles möglich wie der Comic Strip zeigt.

![Python universal](examples/python.png "Python universal")

Wie gesagt Python wird heute bereits universal für so ziemlich alles eingesetzt. Lassen Sie sich von meinen Vorschlägen inspirieren aber bedenken Sie, dass Sie bei den meisten Projekten Zeit und manchmal sogar Geld (kauf eines Raspberry) investieren müssen um sich in die zu verwendeten Frameworks oder andere Technologien (HTML, Image Processing) einzuarbeiten.


# Vorschläge:

## Formularauswertung von gescannten Dokumenten (Tolios, Alexander):

Schreiben einer OMR-Software zur automatischen Erkennung sowie Auswertung von gescannten Dokumenten (z.B. Fragebögen).

## Annotation Browser

Ein Programm zur einfachen Visualisierung von Gen/Sequenz Annotation im Vektor-Grafikformat für das Internet oder für Publikationen.

## Web-Client für Datenbank ein- oder abfragen

Erstellung eines datenbankbasierten Webinterfaces das einfache Formulare einliest und auswertet.

## Webscraping Tool für die automatisierte Abfrage von Aktienkursen

Einfaches Clientprogramm, dass automatisch Aktienkurse von vorgegeben Aktien in kurzen Zeitintervallen abruft.

## Client Server Programm - Uno über das Netzwerk spielen

Computer über Sockets verbinden und Daten (Spielkarten) austauschen.

## Trainingsdaten von Geräten (z.B.Sportuhren) und APPS (z.B.Runtastic) einlesen und auswerten (Michael Lehrach)

*.tcx , *.gpx (=XML) Parser , csv - mit Weitergabe an R und Datenbank zur Auswertung / Sicherung => Berechnung Vorgabe von weiteren Traingsdaten - vgl Polar Flow oder Velo Hero - besonders interessant wäre ein Sportartenübergreifende Eingliederung da es dies noch nicht verbreitet

