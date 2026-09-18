from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .dummy_data import gadgets
import json
from django.utils.text import slugify

# Create your views here.

def start_page_view(request):
    return HttpResponse("hey das funktioniert ja :)!")

def single_gadget_view(request, gadget_id):
    gadget = gadgets[gadget_id]
    gadget["slug"] = slugify(gadget["name"])

    return JsonResponse(gadget)
    
def single_gadget_slug_view(request,gadget_slug):
    gadget_match = {"result": "nothing"}

    for gadget in gadgets:
        if slugify(gadget["name"]) == gadget_slug:
            gadget_match = gadget

    return JsonResponse(gadget_match)