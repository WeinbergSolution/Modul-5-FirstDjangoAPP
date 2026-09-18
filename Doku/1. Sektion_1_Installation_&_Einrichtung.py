### --------------- Backend Modul 5 Einstieg in Django ---------------- ###

## ------------ Sektion 1: Installation & Einrichtung --------------------##

# -----------   01 - Django installieren (auch venv) ------------- #

# Schnellanleitung Django Installieren und starten:

# python -m venv env
# pip freeze
# "env/Scripts/activate"
# python -m pip install Django
# django-admin startproject your_project .
# python manage.py startapp your_app
# pip freeze > requirements.txt




# Das erste Django Projekt Schrit für Schrit Ausführlicher

# Nr 1. Neune Ordner für das Projekt erstellen

# Nr 2. Command Promt konsole aus dem Projektpfad öffnen 

# Nr 3. Virtuelle Python Umgebung einrichten
#         python -m venv env

# Nr 4. Virtuelle Umgebung aktivieren 
#         "env/Scripts/activate"

# Nr 5. Prüfen ob es geklapt hat und ob abhängigkeiten da sind, es sollten keine da sein.
#         pip freeze

# Nr 6. Django installieren in der Virtuellen Pythen umgebnung
#         python -m pip install Django    
#             Danach die mit pip freeze noch maclk checken!

# Nr 7. Django starten in der Virtuellen Python Umgebung
#         django-admin startproject your_project .






# ---------------   02 - die requirements.txt  ----------- #

# Reuirement.txt einrichten in der Virtuellen Python Umgebung in meinem Projekt.
#         pip freeze > requirements.txt

# Immer wenn neue Abhängikeiten installiert werden muss die Requirements.txt upgedatet werden. 

# Andere Nutzer die mein Projekt ansehn oder verwenden wollen benötiegen diese Datei, damit sie es zum laufen birngen können. 



# ------------- 03 - Liste von VSCode-Erweiterungen -------- #

# Im folgenden eine Liste von VSCode Erweiterungen die in den Videos genutzt werden.

# Die Verwendung ist kein Zwang und wenn manche zu Problemen führen, ist es 
# auch ohne möglich dem Kurs zu folgen. Es geht hier zum Teil auch nur um
# Autovervollständigungen usw. außer ein Viewer für eine SQLite Datenbank ist 
# stark empfohlen, da dies VSCode (hier "SQLite viewer") nicht von haus aus
# anzeigen kann.


# In Klammern dahinter der publisher.

# Extensions:
# Python debugger (Microsoft)
# Python (Microsoft)
# autopep8 (Microsoft)
# Django (Baptiste Darthenay)
# Django Template Support (junstyle)
# pylance (Microsoft)
# SQLite viewer (Florian Klampfer)


# ------------ 04 - Projektaufbau und lokalen Server starten -------- #

# Welche DAtein in Angelegten Python Projekt und der Virtuellen Umgebung haben welche bedeutung:

# _pycache_
#     zwischenspeicher des Python Projects

# __init__.py
#     Ist dafür gedacht um andern Systemen zu sagen, das wir hier ein Python Projekt haben 
    

# asgi.py
#     Fürs Deployment zuständige Datei & für server geschichten
#     Doku:
#         https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/

# settings.py
#     Zustädnig fürs 
#     Base_Direktory
#     SECRET_KEY
#     INSTALLED_APPS
#         Hier werden Apps Registriert die das Backend benutzt
#     MIDDLEWARE
#         Was ankommt und was wir im Hintergrund schreiben.
#     TEMPLATES
#         Hier können weitere TAMPLATES hinzugefügt werden, vor allem im
#         bereich des "DIRS" : []
#     STATIC_URL
#         CSS, JAVASCRIPT, IMAGES werden hier genauer definiert!
#         DOKU: 
#         https://docs.djangoproject.com/en/6.1/howto/static-files/
#     Doku:
#     https://docs.djangoproject.com/en/6.1/topics/settings/
#     For the full list of settings and their values, see
#     https://docs.djangoproject.com/en/6.1/ref/settings/

# urls.py
#     Hier werden alle URLS Regestriert, die mit dem Backend arbeiten 
#     Doku:
#     https://docs.djangoproject.com/en/6.1/topics/http/urls/

# wsgi.py
#     Ist verantworlich für server geschichten
#     Doku: 
#     https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/

# db.splite3
#     das ist die Datenbank sozusagen

# manage.py
#     Ist der Kern den wir benutzen um einen Server zu starten!
#         Befehl: python manage.py runserver



# Wenn wir eine neue Interne App erzeugen, gibt es noch weitere Datein 

# ordner migrations:
#     Hier sehn wir was Django aus den angelegten Datenbank Tabellen der Models.py macht

# admin.py:
#     Hier Definieren wir wie unser Admin Panel aussehn wird. Einstellungen usw.

# apps.py
#     Hier wird die liegt die App Config sozusagen, wie heißt die app z.b.

# models.py
#     Hier wird definiert wie die Datenbank Tabellen aussehen

# test.py
#     Hier werden Test geschrieben !

# views.py
#     Hier werden die Views createt, regestriert, sprich was wir sehn wenn wir die Seite aufrufen bzw. einen Endpunkt.



# --------------   05 - neue App erstellen (startapp) ----------- #

# Wenn wir etwas neues erstellen, erstellen wir dafür immer ein neue APP
# Vergleichbar mit Amazon, da gibt es Amazon Music, Amzone Pirime, Amazon 
# Shopping usw, alles kommt aus einem Backend aber sind einzelne Apps des selben BAckends

# Um eine neue app zu erzeugen benutzen wir folgenden Befehl:
#     python manage.py startapp tech_gadgets

# Der neu erzeugte App im Backend Projekt unterscheidet sich etwas vom Aufbau des Hauptprojekt Ordners

# ordner migrations:
#     Hier sehn wir was Django aus den angelegten Datenbank Tabellen der Models.py macht

# admin.py:
#     Hier Definieren wir wie unser Admin Panel aussehn wird. Einstellungen usw.

# apps.py
#     Hier wird die liegt die App Config sozusagen, wie heißt die app z.b.

# models.py
#     Hier wird definiert wie die Datenbank Tabellen aussehen

# test.py
#     Hier werden Test geschrieben !

# views.py
#     Hier werden die Views createt, regestriert, sprich was wir sehn wenn wir die Seite aufrufen bzw. einen Endpunkt.



# -------------   06 - django.cors.headers installieren ---------- #

# Hier Schauen wir uns an wie wir CSRF bzw. CORS Probleme vermeiden!

# das ist recht simple.

# Wenn die Virtuelle Umgebung nicht mehr aktiv sein sollte, noch mal aktiviern 
#     "env/Scripts/activate"

# Installiere Django CORS Headers
#     python -m pip install django-cors-headers

# Noch mal mit prüfen ob installiert wurde 
#     pip freeze

# Nun muss es in der Settings.py Installieren, initalisieren, mit einbringen, 
# wie auch wie auch immer es nennen möchte. Dies geschieht in der MIDDLEWARE
#     'corsheaders.middleware.CorsMiddleware', 
#         (bedeutet das wir darauf zugreifen können!, dadurch können wir die 
#         CSRF ausführen!)
#     Für die CSRF wird folgendes benötigt, was nach der MIDDLEEWARE eingefügt
#     wird, damit wir das Frontent welches in dem Projekt eine HTML datei sein 
#     wird im Liveserver betreib testen können und zulassen.
#         CSRF_TRUSTED_ORIGINS = [

#                                 'http://127.0.0.1:5500',

#                                 'http://localhost:5500',

#                                 ]



#         CORS_ALLOWED_ORIGINS = [

#                                 'http://127.0.0.1:5500',

#                                 'http://localhost:5500',

#                                 ]

# Für den Test hier müssen wir in der MIDDLEWARE folgenden punkt deaktiviern 
#     'django.middleware.csrf.CsrfViewMiddleware',

# Wichtiger zusatz run Server nur noch aus der Virtuellen umgebung heraus ausführen.
