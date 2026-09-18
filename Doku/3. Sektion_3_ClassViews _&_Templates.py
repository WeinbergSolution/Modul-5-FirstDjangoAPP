### --------------- Backend Modul 5 Einstieg in Django ---------------- ###

## --------------- Sektion 3: ClassViews & Templates --------------------##

# ------------   01 - GET und POST in einer View -------------- #

#   Bisher hatten GET und POST getrennte Views.
#   Jetzt werden beide Anfragen über dieselbe URL und View verarbeitet:
#
#       /tech_gadgets/gadget/
#
#   Django erkennt über request.method, ob GET oder POST gesendet wurde.
#
#
#   Schritt 1. urls.py aufräumen:
#
#       path("gadget/", single_gadget_view),
#       path("gadget/<int:gadget_id>", single_gadget_int_view),
#       path(
#           "gadget/<slug:gadget_slug>",
#           single_gadget_view,
#           name="gadget_slug_url"
#       )
#
#   Die alte single_gadget_post_view wird nicht mehr benötigt.
#
#
#   Schritt 2. ID-View umbenennen:
#
#       def single_gadget_int_view(request, gadget_id):
#
#           if len(gadgets) > gadget_id:
#               new_slug = slugify(gadgets[gadget_id]["name"])
#               new_url = reverse("gadget_slug_url", args=[new_slug])
#               return redirect(new_url)
#
#           return HttpResponseNotFound("not found in list")
#
#   Diese View kümmert sich nur noch um den Aufruf über eine ID
#   und leitet anschließend auf die Slug-URL weiter.
#
#
#   Schritt 3. GET und POST in single_gadget_view zusammenführen:
#
#       def single_gadget_view(request, gadget_slug=""):
#
#           if request.method == "GET":
#               gadget_match = None
#
#               for gadget in gadgets:
#                   if slugify(gadget["name"]) == gadget_slug:
#                       gadget_match = gadget
#
#               if gadget_match:
#                   return JsonResponse(gadget_match)
#
#               raise Http404()
#
#
#           if request.method == "POST":
#               try:
#                   data = json.loads(request.body)
#                   print(f"received data: {data['test']}")
#
#                   return JsonResponse({"response": "perfekt :)"})
#
#               except:
#                   return JsonResponse({"response": "Das war wohl nix"})
#
#
#   Wichtig:
#
#       request.method == "GET"
#       -> Daten vom Backend abrufen
#
#       request.method == "POST"
#       -> Daten an das Backend senden
#
#   Damit kann dieselbe View abhängig von der HTTP-Methode
#   unterschiedliche Aufgaben übernehmen.
#
#
#   Neue Struktur:
#
#       GET  /gadget/<id>
#       -> ID wird in Slug umgewandelt und weitergeleitet
#
#       GET  /gadget/<slug>
#       -> Gadget wird gesucht und als JSON zurückgegeben
#
#       POST /gadget/
#       -> JSON-Daten werden empfangen und verarbeitet





# ------------   02 - Basic Class-Based Views -------------- #

#   Django unterstützt neben Function-Based Views auch Class-Based Views.
#   Dabei wird eine View als Klasse erstellt und erbt von Django View.
#
#   Doku:
#   https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/
#
#
#   Schritt 1. View importieren:
#
#       from django.views import View
#
#
#   Schritt 2. GadgetView erstellen:
#
#       class GadgetView(View):
#
#           def get(self, request, gadget_slug):
#               gadget_match = None
#
#               for gadget in gadgets:
#                   if slugify(gadget["name"]) == gadget_slug:
#                       gadget_match = gadget
#
#               if gadget_match:
#                   return JsonResponse(gadget_match)
#
#               raise Http404()
#
#
#           def post(self, request, *args, **kwargs):
#               try:
#                   data = json.loads(request.body)
#                   print(f"received data: {data['test']}")
#
#                   return JsonResponse({"response": "perfekt :)"})
#
#               except:
#                   return JsonResponse({"response": "Das war wohl nix"})
#
#
#   Statt request.method selbst zu prüfen, verwendet die Klasse
#   eigene Methoden für die verschiedenen HTTP-Anfragen:
#
#       def get()  -> verarbeitet GET-Anfragen
#       def post() -> verarbeitet POST-Anfragen
#
#   self verweist dabei auf die aktuelle Instanz der GadgetView.
#
#
#   Schritt 3. Class-Based View in urls.py verwenden:
#
#       from .views import GadgetView
#
#       path("gadget/", GadgetView.as_view()),
#
#       path(
#           "gadget/<slug:gadget_slug>",
#           GadgetView.as_view(),
#           name="gadget_slug_url"
#       )
#
#
#   Wichtig:
#
#       GadgetView.as_view()
#
#   -> macht aus der Klasse eine View, die Django in urlpatterns
#      verwenden und aufrufen kann.
#
#
#   Vorher:
#
#       def single_gadget_view(...)
#           if request.method == "GET":
#           if request.method == "POST":
#
#   Jetzt:
#
#       class GadgetView(View):
#           def get(...):
#           def post(...):
#
#   GET und POST sind dadurch sauber in eigene Methoden getrennt.





# ------------   03 - BaseView und RedirectView -------------- #

#   Mit RedirectView können Weiterleitungen als Class-Based View
#   umgesetzt werden.
#
#   Doku:
#   https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/
#
#
#   Schritt 1. RedirectView importieren:
#
#       from django.views.generic.base import RedirectView
#
#
#   Schritt 2. Eigene RedirectView erstellen:
#
#       class RedirectToGadgetView(RedirectView):
#
#           pattern_name = "gadget_slug_url"
#
#           def get_redirect_url(self, *args, **kwargs):
#
#               slug = slugify(
#                   gadgets[kwargs.get("gadget_id", 0)]["name"]
#               )
#
#               new_kwargs = {"gadget_slug": slug}
#
#               return super().get_redirect_url(
#                   *args, **new_kwargs
#               )
#
#
#   Erklärung:
#
#       pattern_name
#       -> Name der URL, zu der weitergeleitet werden soll
#
#       kwargs.get("gadget_id", 0)
#       -> liest die gadget_id aus der URL
#       -> ist keine ID vorhanden, wird standardmäßig 0 verwendet
#
#       slugify(...)
#       -> erstellt aus dem Gadget-Namen den passenden Slug
#
#       new_kwargs = {"gadget_slug": slug}
#       -> übergibt den erzeugten Slug an die Ziel-URL
#
#       super().get_redirect_url(...)
#       -> verwendet die Redirect-Funktion der übergeordneten
#          RedirectView und erzeugt die Ziel-URL
#
#
#   Schritt 3. RedirectView in urls.py verwenden:
#
#       from .views import RedirectToGadgetView
#
#       path('', RedirectToGadgetView.as_view()),
#       path('<int:gadget_id>', RedirectToGadgetView.as_view()),
#
#
#   Die alte start_page_view wird dadurch nicht mehr benötigt:
#
#       # path('', start_page_view),
#
#
#   Ablauf ohne ID:
#
#       /tech_gadgets/
#           ↓
#       gadget_id nicht vorhanden -> Standardwert 0
#           ↓
#       erstes Gadget -> Slug
#           ↓
#       Redirect auf /gadget/<slug>
#
#
#   Ablauf mit ID:
#
#       /tech_gadgets/1
#           ↓
#       gadget_id = 1
#           ↓
#       Gadget-Name -> slugify()
#           ↓
#       Redirect auf /gadget/<slug>
#
#
#   Wichtig:
#
#       RedirectView
#       -> fertige Django-Klasse für Weiterleitungen
#
#       get_redirect_url()
#       -> bestimmt, wohin weitergeleitet wird
#
#       .as_view()
#       -> macht die Klasse als Django-View verwendbar





# -----------   04 - Hinweis: Wann HTML Templates sinnvoll sind ------------- #

#   Django kann HTML-Seiten direkt im Backend erzeugen.
#   Dafür besitzt Django ein eigenes Template-System.
#
#   In Django Templates können unter anderem:
#
#       -> HTML-Seiten erstellt werden
#       -> Variablen aus Python verwendet werden
#       -> eigene Schleifen und Bedingungen verwendet werden
#       -> Formulare (Forms) erstellt und verarbeitet werden
#
#
#   Dadurch könnte eine Anwendung theoretisch komplett mit Django
#   erstellt werden, ohne ein separates Frontend zu benötigen.
#
#   Bei größeren Anwendungen werden Frontend und Backend jedoch
#   häufig getrennt entwickelt.
#
#
#   Templates sind trotzdem für bestimmte Bereiche sinnvoll,
#   zum Beispiel:
#
#       -> eigene 404-Fehlerseiten
#       -> Django Admin-Panel anpassen
#       -> einfache serverseitig erzeugte HTML-Seiten
#
#
#   In den nächsten Videos schauen wir uns einige Beispiele
#   für Django Templates an.





# ------------------ 05 - Eigene 404.html ----------------- #
      # Eigene tamplates erstellen und regestrieren

#   Django kann für Fehlerseiten eigene HTML-Templates verwenden.
#   In diesem Beispiel erstellen wir eine eigene 404-Seite.
#
#
#   Schritt 1. Im Hauptprojekt einen Ordner "templates" erstellen:
#
#       your_project/
#           templates/
#               404.html
#
#
#   Schritt 2. In templates eine 404.html erstellen:
#
#       <!doctype html>
#       <html lang="en">
#           <head>
#               <meta charset="UTF-8">
#               <title>404</title>
#           </head>
#           <body>
#               Leider nix gefunden!
#           </body>
#       </html>
#
#
#   Schritt 3. Template-Ordner in settings.py registrieren im bereich Templates:
#
#       'DIRS': [BASE_DIR / 'your_project/templates'],
#
#   Dadurch weiß Django, wo nach eigenen Templates gesucht werden soll.
#
#
#   Wird jetzt in einer View ein 404-Fehler ausgelöst:
#
#       raise Http404()
#
#   sucht Django automatisch nach:
#
#       templates/404.html
#
#   und zeigt unsere eigene 404-Seite an.
#
#
#   Wichtig:
#
#       DEBUG = False
#
#   muss gesetzt sein, damit Django die eigene 404.html anzeigt.
#   Bei DEBUG = True wird stattdessen die Django-Debug-Seite angezeigt.





# ------------------ 06 - render() ----------------- #

# Doku 
#https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse


#   Wir erzeugen in unserer App ein templates-Verzeichnis.
#   Darin erstellen wir ein weiteres Verzeichnis mit dem Namen unserer App,
#   um das Template später eindeutig der App zuordnen zu können.
#
#   Unsere Struktur sieht dann so aus:
#
#       tech_gadgets/
#           templates/
#               tech_gadgets/
#                   test.html
#
#
#   In tech_gadgets/templates/tech_gadgets erzeugen wir eine test.html.
#
#
#   Damit Django die Templates unserer App finden kann, wird es jetzt Zeit,
#   unsere App in der settings.py unter INSTALLED_APPS zu registrieren:
#
#       INSTALLED_APPS = [
#           ...
#           'tech_gadgets',
#       ]
#
#   Da APP_DIRS = True gesetzt ist, sucht Django in den registrierten Apps
#   automatisch nach einem templates-Verzeichnis.
#
#
#   In der Haupt-urls.py legen wir wieder einen neuen URL-Pfad an:
#
#       path('start/', start_page_view),
#
#
#   Nun gehen wir in die views.py und passen die bereits vorhandene
#   start_page_view(request) an.
#
#   Zusätzlich erweitern wir den Import aus shortcuts wieder um render,
#   den wir vorher einmal entfernt hatten:
#
#       from django.shortcuts import redirect, render
#
#
#   render() lässt sich nutzen, um HTML-Templates zu rendern
#   und als Antwort an den Browser zurückzugeben:
#
#       def start_page_view(request):
#           return render(request, 'tech_gadgets/test.html')
#
#
#   Dabei bedeutet:
#
#       request
#       -> die aktuelle Anfrage
#
#       'tech_gadgets/test.html'
#       -> Pfad zu unserem Template
#
#
#   Rufen wir jetzt /start/ auf, rendert Django unsere test.html.
#
#   So können wir zunächst ein statisches HTML-Template über Django
#   anzeigen lassen.




# ---------------- 07 - Django-Templates (for-loops) ------------------- #

#   Doku:
#   https://docs.djangoproject.com/en/5.0/ref/templates/language/#templates
#
#   Wir erweitern unsere test.html im <body> um eine for-Schleife.
#
#   Django Templates besitzen eine eigene Syntax, mit der wir unter anderem
#   Schleifen verwenden und auf übergebene Daten zugreifen können.
#
#
#   In der test.html:
#
#       {% for gadget in gadget_list %}
#
#           <h2>{{ gadget.name }}</h2>
#
#       {% endfor %}
#
#
#   Dabei bedeutet:
#
#       {% for gadget in gadget_list %}
#       -> durchläuft alle Gadgets aus gadget_list
#
#       {{ gadget.name }}
#       -> gibt den Namen des aktuellen Gadgets im HTML aus
#
#       {% endfor %}
#       -> beendet die for-Schleife
#
#
#   In der views.py erweitern wir unsere start_page_view().
#   Über render() übergeben wir ein Dictionary an unser Template:
#
#       def start_page_view(request):
#           return render(
#               request,
#               'tech_gadgets/test.html',
#               {'gadget_list': gadgets}
#           )
#
#
#   Das Dictionary:
#
#       {'gadget_list': gadgets}
#
#   übergibt unsere gadgets-Liste unter dem Namen "gadget_list"
#   an das HTML-Template.
#
#   Dadurch kann die for-Schleife in der test.html auf unsere
#   Gadget-Daten zugreifen.
#
#
#   Unter:
#
#       http://127.0.0.1:8000/tech_gadgets/start/
#
#   bekommen wir nun eine Liste unserer Gadgets angezeigt.
#
#
#   Kurz gesagt:
#
#       View -> übergibt Daten mit render()
#       Template -> empfängt gadget_list
#       for-Schleife -> durchläuft die Liste
#       {{ gadget.name }} -> gibt den jeweiligen Namen aus



# ----------------   08 - Static Files (CSS einbinden) ------------------- #

#   Doku:
#   https://docs.djangoproject.com/en/5.0/howto/static-files/
#
#   Über Static Files können wir Dateien wie CSS, JavaScript oder Bilder
#   in unsere Django-Anwendung einbinden.
#
#   Um die Static Files während der Entwicklung direkt über Django
#   ausliefern zu können, stellen wir in der settings.py sicher:
#
#       DEBUG = True
#
#
#   Schritt 1. In unserer App tech_gadgets einen static-Ordner erstellen.
#   Darin erzeugen wir erneut einen Ordner mit dem Namen der App:
#
#       tech_gadgets/
#           static/
#               tech_gadgets/
#                   style.css
#
#   Der zusätzliche tech_gadgets-Ordner sorgt dafür, dass die Static Files
#   eindeutig unserer App zugeordnet werden können.
#
#
#   Schritt 2. In der style.css designen wir zum Test unsere <h2>:
#
#       h2 {
#           color: red;
#           margin: 0;
#       }
#
#
#   Schritt 3. In der test.html laden wir ganz oben die Static-Funktion:
#
#       {% load static %}
#
#
#   Anschließend verlinken wir im <head> unsere style.css:
#
#       <link rel="stylesheet"
#             href="{% static 'tech_gadgets/style.css' %}">
#
#
#   {% static 'tech_gadgets/style.css' %}
#   -> Django erzeugt daraus den richtigen Pfad zu unserer CSS-Datei.
#
#
#   Damit können wir unsere Django-Templates mit eigenen
#   statischen CSS-Dateien gestalten.





# ----------------   09 - base.html und extends ------------------- #

#   Doku:
#   https://docs.djangoproject.com/en/5.0/ref/templates/language/
#
#   Mit einer base.html können wir ein Grundgerüst für mehrere
#   HTML-Templates erstellen.
#
#   Andere Templates können dieses Grundgerüst mit extends übernehmen
#   und bestimmte Bereiche über blocks mit eigenem Inhalt füllen.
#
#
#   Schritt 1. Im templates-Ordner des Hauptprojekts erstellen wir:
#
#       templates/
#           base.html
#
#
#   In der base.html legen wir unter anderem einen Block für den Titel an:
#
#       <title>
#           {% block title %}{{ section.title }}{% endblock %}
#       </title>
#
#   Im <body> erstellen wir einen weiteren Block für den Inhalt:
#
#       <body>
#           {% block content %}leerer content{% endblock %}
#       </body>
#
#
#   Schritt 2. Ein anderes Template kann die base.html erweitern:
#
#       {% extends "base.html" %}
#
#   Anschließend können die definierten Blocks überschrieben werden:
#
#       {% block title %}
#           gadget list
#       {% endblock %}
#
#
#       {% block content %}
#
#           {% for gadget in gadget_list %}
#               <h2>
#                   {{ gadget.name }}
#               </h2>
#           {% endfor %}
#
#       {% endblock %}
#
#
#   Erklärung:
#
#       {% extends "base.html" %}
#       -> übernimmt das Grundgerüst der base.html
#
#       {% block title %} ... {% endblock %}
#       -> ersetzt den title-Block der base.html
#
#       {% block content %} ... {% endblock %}
#       -> ersetzt den content-Block der base.html
#
#
#   Dadurch müssen wiederkehrende HTML-Bereiche nicht in jedem
#   Template erneut geschrieben werden.
#
#
#   Wichtig für dieses Projekt:
#
#   Ich habe diese Änderung nicht dauerhaft auf die test.html angewendet,
#   da ich die bisherige test.html und das eingebundene CSS behalten möchte.
#
#   Das Beispiel zeigt daher nur, wie das Erweitern einer base.html
#   mit extends und blocks funktionieren würde.


# Sektion 3 Done