# Meldedaten-Faker
Python CLI-Tool zum Erzeugen von Meldedaten auf Basis eines räumlichen definierten Bereichs.

## Voraussetzungen:
Benötigt Python 3

## Installation
Für die Installation folgenden Befehl ausführen:

```pip install meldedaten_faker```

Alternativ kann auch das Repository geklont und innerhalb des Ordners folgender Befehl ausgeführt werden:

```python setup.py install```

Beide Befehle installieren das Paket global, sodass `meldedaten_faker` überall auf dem System zur Verfügung steht.

## Nutzung
Die Eingabe des folgenden Befehls erzeugt Meldedaten als CSV-Datei für über ein GeoJSON definiertes, räumliches Gebiet.

```meldedaten_faker generate <Anzahl an Einträgen> <Pfad zum GeoJSON>```

Die Anzahl der Einträge bestimmt, wie viele Meldedaten-Zeilen in der Ausgabe vorhanden sein werden. Ist die Anzahl der Einträge kleiner als die Anzahl möglicher Adressen im Gebiet, werden zufällige Adressen weiteren Inhalten (Geburtsjahr, Geschlecht etc.) angereichert. Ist die Anzahl der Einträge größer als die Anzahl möglicher Adressen, wird jede Adresse mindestens einmal ausgeben, die restlichen gewünschten Einträge werden zufallsbasiert auf die Adressen verteilt.

Der Pfad zum GeoJSON kann absolut oder relativ sein. Berücksichtigt wird derzeit nur das erste Polygon in einerm GeoJSON, welches eine FeatureCollection enthält (Standard-Export aus QGIS).

## Feedbach
Gerne in Form von Issues, Pull Requests oder per E-Mail an dominik.visca@hs-mainz.de