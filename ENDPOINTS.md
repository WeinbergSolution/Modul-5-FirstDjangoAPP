# API Endpoints – Django Tech Gadgets

Diese Datei enthält eine Übersicht über die aktuell verfügbaren Endpoints
des Django-Backends.

Damit können die Endpoints direkt im Browser, mit Postman oder über ein
Frontend mit `fetch()` getestet werden.

## Server starten

Zuerst muss die virtuelle Python-Umgebung im Backend aktiviert werden:

```cmd
env\Scripts\activate
```

Anschließend kann der Django-Server gestartet werden:

```cmd
python manage.py runserver
```

Der Server läuft anschließend standardmäßig unter:

    http://127.0.0.1:8000/

## Base URL

Alle Endpoints unserer `tech_gadgets` App beginnen mit:

    http://127.0.0.1:8000/tech_gadgets/

---

# GADGET ENDPOINTS

## 1. Erstes Gadget aufrufen

**Methode:**

    GET

**Endpoint:**

    /tech_gadgets/

**Vollständige URL:**

    http://127.0.0.1:8000/tech_gadgets/

**Beschreibung:**

Beim Aufruf wird automatisch auf das erste Gadget und anschließend
auf dessen Slug-URL weitergeleitet.

## 2. Gadget über ID aufrufen

**Methode:**

    GET

**Endpoint:**

    /tech_gadgets/<gadget_id>

**Beispiel:**

    http://127.0.0.1:8000/tech_gadgets/1

**Beschreibung:**

Die ID wird verwendet, um das entsprechende Gadget zu finden.
Anschließend wird automatisch auf die Slug-URL des Gadgets
weitergeleitet.

## 3. Gadget über Slug abrufen

**Methode:**

    GET

**Endpoint:**

    /tech_gadgets/gadget/<gadget_slug>

**Beispiel:**

    http://127.0.0.1:8000/tech_gadgets/gadget/wearabletracker-x10

**Beschreibung:**

Das Gadget wird anhand seines Slugs gesucht und anschließend
als JSON zurückgegeben.

**Beispiel Response:**

```json
{
  "name": "WearableTracker X10",
  "category": "Wearable Technology",
  "manufacturer": "FitTrack Inc.",
  "price": 149.99,
  "currency": "EUR"
}
```

## 4. Gadget-Daten per POST senden

**Methode:**

    POST

**Endpoint:**

    /tech_gadgets/gadget/

**Vollständige URL:**

    http://127.0.0.1:8000/tech_gadgets/gadget/

**Content-Type:**

    application/json

**Beispiel Body:**

```json
{
  "test": "funktioniert"
}
```

**Beispiel Response:**

```json
{
  "response": "perfekt :)"
}
```

Dieser Endpoint kann zum Beispiel mit Postman oder über `fetch()`
im Frontend getestet werden.

---

# DJANGO TEMPLATE

## 5. Gadget-Liste als HTML anzeigen

**Methode:**

    GET

**Endpoint:**

    /tech_gadgets/start/

**Vollständige URL:**

    http://127.0.0.1:8000/tech_gadgets/start/

**Beschreibung:**

Django rendert hier ein HTML-Template.

Die Gadget-Liste wird von der View an das Template übergeben und
mit einer Django Template for-Schleife ausgegeben.

---

# MANUFACTURER ENDPOINTS

Die Manufacturer-Endpunkte wurden im Rahmen der Aufgabe 4 erstellt.

## 6. Manufacturer über ID abrufen

**Methode:**

    GET

**Endpoint:**

    /tech_gadgets/manufacturer/<manufacturer_id>

**Beispiel:**

    http://127.0.0.1:8000/tech_gadgets/manufacturer/1

**Beschreibung:**

Über die `manufacturer_id` wird ein bestimmter Manufacturer aus
der `manufacturers`-Liste in `dummy_data.py` abgerufen.

Die ID wird von Django an die View übergeben:

```python
def start_manufacturer_view(request, manufacturer_id):
    return JsonResponse(manufacturers[manufacturer_id])
```

Der entsprechende Manufacturer wird anschließend als JSON
zurückgegeben.

## 7. Manufacturer-Daten per POST senden

**Methode:**

    POST

**Endpoint:**

    /tech_gadgets/manufacturer/send_manufacturer/

**Vollständige URL:**

    http://127.0.0.1:8000/tech_gadgets/manufacturer/send_manufacturer/

**Content-Type:**

    application/json

**Beispiel Body:**

```json
{
  "test": "funktioniert"
}
```

**Beispiel Response:**

```json
{
  "response": "perfekt :)"
}
```

**Beschreibung:**

Über diesen Endpoint können JSON-Daten per POST an das
Django-Backend gesendet werden.

Die Daten werden über:

```python
json.loads(request.body)
```

eingelesen und in Python-Daten umgewandelt.

Aktuell dient der Endpoint zum Empfangen und Testen der POST-Daten.
Die empfangenen Daten werden noch nicht dauerhaft gespeichert.

---

# FRONTEND TEST

In der `test_w_post.html` können sowohl die Gadget- als auch die
Manufacturer-Endpunkte getestet werden.

Dafür stehen vier Buttons zur Verfügung:

- Gadget-Daten empfangen
- Gadget-Daten senden
- Manufacturer-Daten empfangen
- Manufacturer-Daten senden

Die Manufacturer-Requests verwenden:

**GET:**

    http://127.0.0.1:8000/tech_gadgets/manufacturer/1

**POST:**

    http://127.0.0.1:8000/tech_gadgets/manufacturer/send_manufacturer/

---

# KURZÜBERSICHT

| Methode | Endpoint                                        | Beschreibung                    |
| ------- | ----------------------------------------------- | ------------------------------- |
| GET     | `/tech_gadgets/`                                | Weiterleitung zum ersten Gadget |
| GET     | `/tech_gadgets/<gadget_id>`                     | Gadget über ID / Redirect       |
| GET     | `/tech_gadgets/gadget/<gadget_slug>`            | Gadget als JSON abrufen         |
| POST    | `/tech_gadgets/gadget/`                         | Gadget-Testdaten senden         |
| GET     | `/tech_gadgets/start/`                          | Gadget-Liste als HTML anzeigen  |
| GET     | `/tech_gadgets/manufacturer/<manufacturer_id>`  | Manufacturer als JSON abrufen   |
| POST    | `/tech_gadgets/manufacturer/send_manufacturer/` | Manufacturer-Testdaten senden   |

---

# Beispiele zum direkten Testen

## Im Browser

Diese GET-Endpunkte können direkt im Browser geöffnet werden:

    http://127.0.0.1:8000/tech_gadgets/

    http://127.0.0.1:8000/tech_gadgets/1

    http://127.0.0.1:8000/tech_gadgets/gadget/wearabletracker-x10

    http://127.0.0.1:8000/tech_gadgets/start/

    http://127.0.0.1:8000/tech_gadgets/manufacturer/1

## POST Requests

POST-Endpunkte sollten über Postman oder das Test-Frontend
`test_w_post.html` aufgerufen werden:

**Gadget POST:**

    http://127.0.0.1:8000/tech_gadgets/gadget/

**Manufacturer POST:**

    http://127.0.0.1:8000/tech_gadgets/manufacturer/send_manufacturer/
