### --------------- Backend Modul 5 Einstieg in Django ---------------- ###

## --------------- Sektion 2: URL & Views --------------------##

# -----------   01 - Deine erste View ------------- #

#views.py
#   Hier werden die Views definiert die als funktion angelegt werden, mit einen 
#   request als übergabe Parameter, hinter den Request stehn später die Art des 
#   Request, GET, POST, PUT, DELETE usw. 
#   Die view kann auch als Klassenform angelegt werden, dies ist dann keine
#   Funktion.

#        def start_page_view(request):
#            return HttpResponse("hey das funktioniert ja :)!")

#   Desweiteren wird ein Import benötigt für den HTTPResponse

#        from django.http import HttpResponse


#urls.py (in der neuen APP anlegen)
#    Hier müssen wir die Angelegte View jetzt Importieren

#        from tech_gadgets.views import start_page_view

#    Als nächstes legen wir die Route an, bzw. regestrieren diese 
#    Dies machen wir im Bereich "urlpatterns"

#    urlpatterns = [
#        path('', start_page_view)
#    ]

#   Faziet: Die view wird in der erstellten APP in der view.py definert, in 
#   diesem Fall über eine Funktion, danach gehn wir in das haupt Projekt 
#   Verzeichnis und defieneren in der urls.py den Endpunkt. Sprich die Routen
#   die über urls erreicht und aufgerufen werden können. Das ist nicht der HOW 
#   TO GO WAY, dieser kommt im nächsten Schritt. Um es Sauberer und 
#    übersichtlicher zu lösen, definieren wir im nächsten schrit jeden 
#   relevanten Endpunkt direkt in einer urls.py im App verzeichnis.



# ---------------- 02 - urlpatterns in app auslagern ------------- #

#   Endpunkte App basiert anlegen, die sauberer lösung, so hat jede App seine 
#   Relevanten Endpunkte. Da jede App eine eigene urls.py bekommt.

#   App basierte urls.py
#        1. Neue urls.py anlegen im App verzeichnis.
#        2. Wir Importieren aus .views die start_page_view
#       
#               from .views import start_page_view

#        3. urlspattern anlegen:

#                urlpatterns = [
#                    path('', start_page_view)
#                ]



#   Änderung in der Haupt urls.py 
#       Im Hauptverzeinis benötigen wir einen neuen Import von Path & include.
#       Dadurch können wir den URL Path aufrufen Und Die URL includen
#       
#           from django.urls import path, include

#       urlspatterns anlegen

#           path('texh_gadgets/', include('tech_gadgets.urls') )     


#   Fazit: In der neu erstellten ulrs.py im app verzeichnis definieren wir 
#   keinen Pfad im urlpatterns, sprich lassen diesen leer.

#       app urls.py
#            path('', start_page_view) 

#  Der Pfad kommt aus der haupt urls.py 

#       haupt urls.py
#            path('tech_gadgets/', include('tech_gadgets.urls') )




# ------------   03 - redirect() ---------------- #

#   Redirect beeispiel für diese Projekt, wichtig das ist nicht der
#   Weg wie man es normalerweiße löst. 

#   Im Hauptvberzeichnes legen wir in der urls.py eine redirect funktion an
#   urls.py
        
#        Schrit 1. neuer imprort, wir benöiegen redirect welches von django.
#                  shortcuts kommt. 

#                    from django.shortcuts import redirect

#        Schrit 2. Eine view funktion für den redirct schreiben
#                  (dies ist nicht der normale weg, nur für das projekt ) 

#                    def redirect_to_tech_gadgets(request):
#                        return redirect('tech_gadgets/', permanent=True)

#                  permanent=True = HttpResonsePermanentRedirect   
#                                     Status code 301
#                   ohne          = HttpResonseRedirect   
#                                     Status code 302                       

#        Schrit 3. Den urlpatterns den neuen redirect Path mitgeben.

#                   path('', redirect_to_tech_gadgets)




# ------------- 04 - dummydaten hinzufügen ------------- #

#   Dummy Daten anlegen in einer Liste:
#       Schrit 1. im App verzeichnis dummy_data.py erzeugen

#       schrit 2. Liste names gadegets [] erzeugen mit dummy daten
#            gadgets = [
#                    
#            ]
# 
#            manufacturers = [
#
#            ]

#       Schrit 3. View hinzufügen in App Ordner tech_gadgets
#            views.py
#                1. gadget Liste aus dummy_data.py importieren in die view.py:

#                       from .dummy_data import gadgets

#                2. View Funktion anlegen um single gadgets an zu zeigen!

#                       def single_gadget_view(request)
#                           return HttpResponse(gadgets[0])  
# 
#       Schrit 4. Neuen path anlegen in app urls.py Import und path erweitern

#                   Schrit 1: single_gadget_view importieren aus .views

#                       from .views import start_page_view, single_gadget_view 

#                    Schrit 2: urlpatterns anpassen

#                       path('gadget', single_gadget_view ) 



# ------------ 05 - httpresponse mit json ----------------- #

#   Es ist notwendig zu konvertieren zwischen Listen, dictinatys usw. zu JSON
#   Dafür benötiegen wir json direkt aus Python über einen import, damit wir 
#   mit dem aufruf json.dumps(), den inhalt in den (), in ein echtes JSON 
#   umwandeln.

#    Schrit 1. tech_gadgets views.py aufrufen

#    Schrit 2. in die views.py import json einfügen

#       views.py
#           import json 
# 
#   Schrit 3. single_gadget_view(request): anpassen genauer den HttpResponse

#        def single_gadget_view(request):
#            return HttpResponse(json.dumps(gadgets[0]))
#                               (umwandeln in echtes JSON)    
# 
#   Schrit 4. Wir geben dem HttpResponse noch einen content-type damit
#             es als JSON zurück gegeben wird und nicht als text. 
#       
#   return HttpResponse(json.dumps(gadgets[0]), content_type="application/json")
#                      (umwandeln in echtes JSON)       (Response als JSON)
                                
# Im Absatz 06 - JsonResponse, gibt es eine bessere lösng mit JsonResonse




# ------------   06 - JsonResponse -------------- #

#   Django hat für den content.type eine interne bessere variante als den 
#   content-type extra mit zugeben, über einen import JsonResponse, welches aus
#   django.http kommt.

#   tech_gedgets views.py
#   Schrit 1. Improt from django.http um JsonResponse erweitern

#       from django.http import HttpResponse, JsonResponse

#   Schrit 2. HttpResponse anpassen, zu JsonResponse  content-type raus nehm. 
#             denn dieser wird jetzt automatisch mitgegeben.

#       return JsonResponse(json.dumps(gadgets[0]))




# --------------- 07 - Test mit Mini-Frontend -------------- #

#   Mini Frontend test.html in einem neuen Frontend ordner angelegt.

#   Ausgabe der Daten findet über die console statt, test erfolgreich!




# ----------------- 08 - URL-Parameter ----------------------- # 

# Woe kommen wir auf ein spezifisches Object aus tech_gadget ?

# tech_gadget urls.py
#   Schrit 1. im Path von gadget/ in der tech_gadget urls.py, egänzen wir den
#              Path um <int:gadget_id>. mit int: geben wir direkt den Type mit,
#              damit es nicht zu einem Type Error kommt

#               path('gadget/<int:gadget_id>', single_gadget_view )
#                         (dies wird ergäntzt)

# tech_gadget views.py
#   Schrit 2. In der tech_gadget views.py wird in der Fuction single_gadget_view
#             zu dem Response Parameter ein weiterer übergeben "gadget_id"

#               def single_gadget_view(request,gadget_id):
#                   return HttpResponse(json.dumps(gadgets[0]))

# tech_gadget views.py
#   Schrit 3. Nun müssen wir den Parameter im JsonResponse anpassen




# ---------------- 09 - URL-Parameter Reihenfolge beachten -------#

#   Bei URL Parametern ist die Rheinfolge wichtig in der sie in der urls.py in 
#   den urlpatterns angeordnet sind.

#   Beispiel:

#               urlpatterns = [
#                  path('', start_page_view),
#                  path('gadget/<str:gadget_id>', single_gadget_view )
#                  path('gadget/<int:gadget_id>', single_gadget_view )
#               ]

#   Der str: Parameter greift hier zuerst und erst dann der int:




# ------------   10 - type slug und slugify -------------- #

#   Mit slugify können wir einen String in einen sogenannten Slug umwandeln.
#   Ein Slug ist eine URL-freundliche Schreibweise eines Textes.
#
#   Beispiel:
#
#       "WearableTracker X10"
#
#   wird zu:
#
#       "wearabletracker-x10"
#
#
#   tech_gadgets views.py
#
#   Schritt 1. slugify aus django.utils.text importieren
#
#       from django.utils.text import slugify
#
#
#   Schritt 2. In der single_gadget_view das Gadget anhand der gadget_id
#              aus unserer gadgets-Liste holen und in einer Variable speichern.
#
#       gadget = gadgets[gadget_id]
#
#   Dadurch enthält gadget jetzt das Dictionary des ausgewählten Gadgets.
#
#
#   Schritt 3. Dem Dictionary einen neuen Key "slug" hinzufügen.
#              Als Wert verwenden wir den Namen des Gadgets und wandeln
#              diesen mit slugify() in einen Slug um.
#
#       gadget["slug"] = slugify(gadget["name"])
#
#   Beispiel:
#
#       gadget["name"] = "WearableTracker X10"
#
#   wird durch:
#
#       slugify(gadget["name"])
#
#   zu:
#
#       "wearabletracker-x10"
#
#
#   Schritt 4. Das erweiterte Gadget als JSON zurückgeben.
#
#       return JsonResponse(gadget)
#
#
#   Die gesamte View:
#
#       def single_gadget_view(request, gadget_id):
#
#           gadget = gadgets[gadget_id]
#
#           gadget["slug"] = slugify(gadget["name"])
#
#           return JsonResponse(gadget)
#
#
#   Die JSON-Ausgabe enthält jetzt zusätzlich den Key "slug":
#
#       {
#           "name": "WearableTracker X10",
#           "category": "Wearable Technology",
#           ...
#           "slug": "wearabletracker-x10"
#       }




# ------------   11 - slug anwenden -------------- #

#   Bisher wurde ein Gadget über seine ID aufgerufen:
#
#       /tech_gadgets/gadget/1
#
#   Jetzt soll ein Gadget über einen Slug aufgerufen werden:
#
#       /tech_gadgets/gadget/wearabletracker-x10
#
#
#   Schritt 1. Neue View in urls.py importieren:
#
#       from .views import start_page_view, single_gadget_view, single_gadget_slug_view
#
#
#   Schritt 2. URL mit dem Path Converter <slug:gadget_slug> anlegen:
#
#       path('gadget/<slug:gadget_slug>', single_gadget_slug_view)
#
#   Dabei bedeutet:
#
#       slug        -> Django erwartet einen gültigen Slug
#       gadget_slug -> Variable, die an die View übergeben wird
#
#   Beispiel:
#
#       /gadget/wearabletracker-x10
#
#   übergibt:
#
#       gadget_slug = "wearabletracker-x10"
#
#
#   Schritt 3. Neue View erstellen:
#
#       def single_gadget_slug_view(request, gadget_slug):
#
#           gadget_match = {"result": "nothing"}
#
#           for gadget in gadgets:
#               if slugify(gadget["name"]) == gadget_slug:
#                   gadget_match = gadget
#
#           return JsonResponse(gadget_match)
#
#
#   Erklärung:
#
#       gadget_match
#       -> Standardwert, falls kein Gadget gefunden wird
#
#       for gadget in gadgets
#       -> durchsucht alle Gadgets
#
#       slugify(gadget["name"]) == gadget_slug
#       -> wandelt den Namen in einen Slug um und vergleicht ihn
#          mit dem Slug aus der URL
#
#       gadget_match = gadget
#       -> speichert das passende Gadget
#
#       JsonResponse(gadget_match)
#       -> gibt das gefundene Gadget als JSON zurück
#
#
#   Beispiel:
#
#       "WearableTracker X10"
#               ↓ slugify()
#       "wearabletracker-x10"
#               ↓ Vergleich mit URL
#       Gadget gefunden
#
#
#   Wird kein Gadget gefunden:
#
#       {"result": "nothing"}





# ------------   12 - Redirect und Reverse -------------- #

#   Mit redirect() können wir auf eine andere URL weiterleiten.
#   Mit reverse() können wir eine URL über ihren vergebenen Namen erzeugen.
#
#   Ziel:
#
#       /tech_gadgets/gadget/1
#
#   soll automatisch weiterleiten zu:
#
#       /tech_gadgets/gadget/wearabletracker-x10
#
#
#   Schritt 1. Der Slug-URL in urls.py einen Namen geben:
#
#       path(
#           'gadget/<slug:gadget_slug>',
#           single_gadget_slug_view,
#           name="gadget_slug_url"
#       )
#
#   Durch den Namen können wir die URL später mit reverse() aufrufen.
#
#
#   Schritt 2. redirect und reverse in views.py importieren:
#
#       from django.shortcuts import redirect
#       from django.urls import reverse
#
#
#   Schritt 3. single_gadget_view anpassen:
#
#       def single_gadget_view(request, gadget_id):
#
#           new_slug = slugify(gadgets[gadget_id]["name"])
#
#           new_url = reverse("gadget_slug_url", args=[new_slug])
#
#           return redirect(new_url)
#
#
#   Erklärung:
#
#       new_slug
#       -> erstellt aus dem Namen einen Slug
#       -> "WearableTracker X10" wird "wearabletracker-x10"
#
#       reverse("gadget_slug_url", args=[new_slug])
#       -> sucht die URL über ihren Namen
#       -> setzt new_slug für <slug:gadget_slug> ein
#       -> erzeugt /tech_gadgets/gadget/wearabletracker-x10
#
#       redirect(new_url)
#       -> leitet den Browser auf die erzeugte URL weiter
#
#
#   Kurz gesagt:
#
#       slugify()  -> erstellt den Slug
#       reverse()  -> erstellt die passende URL
#       redirect() -> leitet auf diese URL weiter




# ------------   13 - Http404 und HttpResponseNotFound -------------- #

#   Bisher gehen unsere Views davon aus, dass ein Gadget existiert.
#   Jetzt behandeln wir auch den Fall, dass keine passende ID oder
#   kein passender Slug gefunden wird.
#
#
#   Schritt 1. HttpResponseNotFound und Http404 importieren:
#
#       from django.http import (
#           HttpResponse,
#           JsonResponse,
#           HttpResponseNotFound,
#           Http404
#       )
#
#
#   Schritt 2. single_gadget_view absichern:
#
#       def single_gadget_view(request, gadget_id):
#
#           if len(gadgets) > gadget_id:
#               new_slug = slugify(gadgets[gadget_id]["name"])
#               new_url = reverse("gadget_slug_url", args=[new_slug])
#               return redirect(new_url)
#
#           return HttpResponseNotFound("not found in list")
#
#   len(gadgets) > gadget_id
#   -> prüft, ob der angeforderte Index in der Liste existiert.
#
#   Existiert er nicht:
#
#       return HttpResponseNotFound("not found in list")
#
#   -> gibt eine HTTP-404-Antwort mit eigenem Text zurück.
#
#
#   Schritt 3. single_gadget_slug_view absichern:
#
#       def single_gadget_slug_view(request, gadget_slug):
#
#           gadget_match = None
#
#           for gadget in gadgets:
#               if slugify(gadget["name"]) == gadget_slug:
#                   gadget_match = gadget
#
#           if gadget_match:
#               return JsonResponse(gadget_match)
#
#           raise Http404()
#
#   gadget_match startet mit None.
#   Wird ein Gadget gefunden, wird es als JSON zurückgegeben.
#
#   Wird kein Gadget gefunden:
#
#       raise Http404()
#
#   -> Django erzeugt eine normale 404-Fehlerantwort.
#
#
#   Unterschied:
#
#       HttpResponseNotFound(...)
#       -> 404-Response wird direkt zurückgegeben
#
#       raise Http404()
#       -> Django übernimmt die Behandlung der 404-Fehlermeldung




# ------------   14 - DEBUG = False und 404-Fehlerseite -------------- #

#   Bisher läuft Django mit DEBUG = True.
#   Dadurch zeigt Django bei Fehlern ausführliche Informationen an.
#
#   Mit DEBUG = False verhält sich Django wie im Produktivbetrieb
#   und zeigt keine ausführlichen Debug-Informationen mehr.
#
#
#   Schritt 1. settings.py im Hauptprojekt öffnen und DEBUG ändern:
#
#       DEBUG = False
#
#
#   Schritt 2. Bei DEBUG = False müssen erlaubte Hosts angegeben werden:
#
#       ALLOWED_HOSTS = ['127.0.0.1']
#
#   Dadurch darf das Projekt weiterhin über:
#
#       http://127.0.0.1:8000
#
#   aufgerufen werden.
#
#
#   Wird jetzt ein nicht vorhandenes Gadget aufgerufen und Http404 ausgelöst:
#
#       raise Http404()
#
#   -> Browser zeigt eine normale "Not Found"-404-Seite
#   -> Konsole zeigt den HTTP-Statuscode 404
#
#
#   Wichtig:
#
#       DEBUG = True
#       -> ausführliche Fehlerseiten für die Entwicklung
#
#       DEBUG = False
#       -> keine internen Debug-Informationen für den Benutzer
#
#   In Produktion sollte DEBUG immer False sein.




# ------------   15 - Die erste POST-View -------------- #

#   Mit einer POST-Anfrage können Daten an unser Backend gesendet werden.
#   Dafür erstellen wir eine neue View und eine passende URL.
#
#
#   Schritt 1. Neue View in urls.py importieren:
#
#       from .views import ..., single_gadget_post_view
#
#   Neue URL anlegen:
#
#       path("gadget/send_gadget/", single_gadget_post_view)
#
#
#   Schritt 2. POST-View in views.py erstellen:
#
#       def single_gadget_post_view(request):
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
#                   return JsonResponse({"response": "Das war wohl nix"})
#
#
#   Erklärung:
#
#       request.method == "POST"
#       -> prüft, ob die Anfrage eine POST-Anfrage ist
#
#       request.body
#       -> enthält die gesendeten Daten
#
#       json.loads(request.body)
#       -> wandelt die empfangenen JSON-Daten in Python-Daten um
#
#       try / except
#       -> versucht die Daten zu verarbeiten und fängt Fehler ab
#
#       JsonResponse(...)
#       -> sendet eine JSON-Antwort zurück
#
#
#   Ablauf:
#
#       POST-Anfrage mit JSON
#           ↓
#       request.body
#           ↓
#       json.loads()
#           ↓
#       Python-Daten
#           ↓
#       JsonResponse()



# ---------- 16 - die erste Post view testen mit frontend -------- #

# Neues Frontend im im Frontend Ordner angelegt, Post funktioniert, ausgabe über die console




# Done