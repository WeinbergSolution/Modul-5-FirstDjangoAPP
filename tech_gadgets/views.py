from django.shortcuts import render
from django.http import HttpResponse
from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse("hey das funktioniert ja :)!")

def single_gadget_view(request):
    return HttpResponse(gadgets[0])