### --------------- Backend Modul 5 Einstieg in Django ---------------- ###

## --------------- Sektion 4: Aufgabe --------------------##

# ------------   01 - Aufgabenstellung -------------- #

#   In der dummy_data.py befinden sich neben den Gadgets auch
#   Manufacturers, die wir bisher noch nicht verwendet oder angezeigt haben.
#
#   Aufgabe:
#
#   -> In der urls.py einen oder mehrere neue Pfade für die Manufacturers anlegen.
#
#   -> Eine GET-View erstellen, über die die Manufacturers abgerufen
#      und angezeigt werden können.
#
#   -> Eine POST-View erstellen, über die ein neuer Manufacturer
#      hinzugefügt werden kann.
#
#   -> In der test_w_post.html die vorhandene GET-URL und POST-URL
#      entsprechend auf die neuen Manufacturer-Endpunkte anpassen.
#
#   GET und POST haben wir bereits zu Beginn des Projekts verwendet.
#   Dieses Wissen soll nun auf die Manufacturers übertragen werden.





#                                Lösung


# ------------   04 - Aufgabe: Manufacturers GET und POST -------------- #
#
#   Was ich gemacht habe, um die Aufgabe 4 zu lösen:
#
#
#   1. views.py
#
#   Wir importieren manufacturers aus der dummy_data.py:
#
#       from .dummy_data import manufacturers
#
#
#   Anschließend legen wir eine GET- und eine POST-View
#   für die Manufacturers an.
#
#
#   GET-View Manufacturers:
#
#       def start_manufacturer_view(request, manufacturer_id):
#           return JsonResponse(manufacturers[manufacturer_id])
#
#   Über manufacturer_id können wir einen bestimmten Manufacturer
#   aus der Liste abrufen.
#
#   Beispiel:
#
#       manufacturer/1
#
#   -> manufacturer_id hat den Wert 1
#   -> manufacturers[1] wird als JSON zurückgegeben.
#
#
#   POST-View Manufacturers:
#
#       def start_manufacturer_Post_view(request):
#
#           if request.method == "POST":
#
#               try:
#                   data = json.loads(request.body)
#                   print(f"received data: {data}")
#
#                   return JsonResponse({"response": "perfekt :)"})
#
#               except:
#                   return JsonResponse({
#                       "response": "Das war wohl nix mit dem POST"
#                   })
#
#   Die über POST gesendeten JSON-Daten befinden sich in request.body.
#
#       json.loads(request.body)
#
#   wandelt die empfangenen JSON-Daten wieder in Python-Daten um.
#
#
# ---------------------------------------------------------------------- #
#
#   2. urls.py
#
#   Wir fügen dem Import die beiden neuen Views hinzu:
#
#       from .views import start_manufacturer_view, start_manufacturer_Post_view
#
#
#   Anschließend legen wir die neuen Routen an:
#
#       path(
#           'manufacturer/<int:manufacturer_id>',
#           start_manufacturer_view
#       ),
#
#       path(
#           'manufacturer/send_manufacturer/',
#           start_manufacturer_Post_view
#       ),
#
#   <int:manufacturer_id> wird bei einem GET-Aufruf an die
#   start_manufacturer_view übergeben.
#
#
# ---------------------------------------------------------------------- #
#
#   3. Anpassung des Frontends
#
#   Wir erweitern das Frontend test_w_post.html um eigene Fetch-URLs für GET und POST
#   der Manufacturers:
#
#       const fetchGetUrlManu =
#           "http://127.0.0.1:8000/tech_gadgets/manufacturer/1";
#
#       const fetchPostUrlManu =
#           "http://127.0.0.1:8000/tech_gadgets/manufacturer/send_manufacturer/";
#
#
#   Danach erzeugen wir eine eigene Fetch-Funktion für den GET-Request:
#
#       async function fetchTestGetManu() {
#           let result = await fetch(fetchGetUrlManu);
#           let resultToText = await result.text();
#           console.log(resultToText);
#       }
#
#
#   Und eine eigene Fetch-Funktion für den POST-Request:
#
#       async function fetchTestPostManu() {
#
#           const data = { "test": "funktioniert" };
#
#           let response = await fetch(fetchPostUrlManu, {
#               method: "POST",
#               headers: {
#                   "Content-Type": "application/json",
#               },
#               body: JSON.stringify(data),
#           });
#
#           let result = await response.json();
#           console.log(result);
#       }
#
#   JSON.stringify(data)
#   -> wandelt unsere JavaScript-Daten in JSON um, damit wir sie
#      an das Django-Backend senden können.
#
#
# ---------------------------------------------------------------------- #
#
#   4. Zwei neue Buttons anlegen
#
#   Zum Schluss legen wir zwei neue Buttons für die Manufacturer-
#   Funktionen an:
#
#       <button onclick="fetchTestGetManu()">
#           empfange manufacturer Daten
#       </button>
#
#       <button onclick="fetchTestPostManu()">
#           Sende manufacturer Daten
#       </button>
#
#
#   Ablauf GET:
#
#       Button
#           ↓
#       fetchTestGetManu()
#           ↓
#       GET /manufacturer/1
#           ↓
#       start_manufacturer_view()
#           ↓
#       JsonResponse(manufacturers[1])
#
#
#   Ablauf POST:
#
#       Button
#           ↓
#       fetchTestPostManu()
#           ↓
#       JSON.stringify(data)
#           ↓
#       POST /manufacturer/send_manufacturer/
#           ↓
#       request.body
#           ↓
#       json.loads(request.body)
#           ↓
#       JsonResponse()
#
