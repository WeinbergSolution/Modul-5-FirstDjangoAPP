# API Endpoints – Django Tech Gadgets

Diese Datei enthält eine Übersicht über die aktuell verfügbaren Endpoints
des Django-Backends.

Damit können die Endpoints direkt im Browser, mit Postman oder über ein
Frontend mit `fetch()` getestet werden.

## Server starten

Zuerst muss der Django-Server im Backend gestartet werden:

    python manage.py runserver

Der Server läuft anschließend standardmäßig unter:

    http://127.0.0.1:8000/

## Base URL

Alle Endpoints unserer `tech_gadgets` App beginnen mit:

    http://127.0.0.1:8000/tech_gadgets/

---

## GADGET ENDPOINTS

### 1. Erstes Gadget aufrufen

Methode:

    GET

Endpoint:

    /tech_gadgets/

Vollständige URL:

    http://127.0.0.1:8000/tech_gadgets/

Beschreibung:

Beim Aufruf wird automatisch auf das erste Gadget und anschließend
auf dessen Slug-URL weitergeleitet.

### 2. Gadget über ID aufrufen

Methode:

    GET

Endpoint:

    /tech_gadgets/<gadget_id>

Beispiel:

    http://127.0.0.1:8000/tech_gadgets/1

Beschreibung:

Die ID wird verwendet, um das entsprechende Gadget zu finden.

Anschließend wird automatisch auf die Slug-URL des Gadgets
weitergeleitet.

### 3. Gadget über Slug abrufen

Methode:

    GET

Endpoint:

    /tech_gadgets/gadget/<gadget_slug>

Beispiel:

    http://127.0.0.1:8000/tech_gadgets/gadget/wearabletracker-x10

Beschreibung:

Das Gadget wird anhand seines Slugs gesucht und anschließend
als JSON zurückgegeben.

Beispiel Response:

    {
        "name": "WearableTracker X10",
        "category": "Wearable Technology",
        "manufacturer": "FitTrack Inc.",
        "price": 149.99,
        "currency": "EUR"
    }

### 4. Daten per POST senden

Methode:

    POST

Endpoint:

    /tech_gadgets/gadget/

Vollständige URL:

    http://127.0.0.1:8000/tech_gadgets/gadget/

Content-Type:

    application/json

Beispiel Body:

    {
        "test": "funktioniert"
    }

Beispiel Response:

    {
        "response": "perfekt :)"
    }

Dieser Endpoint kann zum Beispiel mit Postman oder über `fetch()`
im Frontend getestet werden.

---

## DJANGO TEMPLATE

### 5. Gadget-Liste als HTML anzeigen

Methode:

    GET

Endpoint:

    /tech_gadgets/start/

Vollständige URL:

    http://127.0.0.1:8000/tech_gadgets/start/

Beschreibung:

Django rendert hier ein HTML-Template.

Die Gadget-Liste wird von der View an das Template übergeben und
mit einer Django Template for-Schleife ausgegeben.

---

## MANUFACTURER ENDPOINTS

Diese Endpoints werden im Rahmen der aktuellen Aufgabe erstellt.

### 6. Manufacturers abrufen

Methode:

    GET

Geplanter Endpoint:

    /tech_gadgets/manufacturer/

Vollständige URL:

    http://127.0.0.1:8000/tech_gadgets/manufacturer/

Beschreibung:

Soll die vorhandenen Manufacturers aus `dummy_data.py` abrufen.

### 7. Manufacturer hinzufügen

Methode:

    POST

Geplanter Endpoint:

    /tech_gadgets/manufacturer/

Vollständige URL:

    http://127.0.0.1:8000/tech_gadgets/manufacturer/

Content-Type:

    application/json

Beschreibung:

Über diesen Endpoint soll ein neuer Manufacturer an das
Django-Backend gesendet werden.

---

## KURZÜBERSICHT

GET
http://127.0.0.1:8000/tech_gadgets/

GET
http://127.0.0.1:8000/tech_gadgets/1

GET
http://127.0.0.1:8000/tech_gadgets/gadget/wearabletracker-x10

POST
http://127.0.0.1:8000/tech_gadgets/gadget/

GET
http://127.0.0.1:8000/tech_gadgets/start/

GEPLANT:

GET
http://127.0.0.1:8000/tech_gadgets/manufacturer/

POST
http://127.0.0.1:8000/tech_gadgets/manufacturer/
