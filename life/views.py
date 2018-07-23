from django.shortcuts import render, HttpResponse
from django.core import serializers
from life.models import *
from django.core.serializers import serialize
import json

def item(request):
    if request.method == "POST":
      print(json.load(request.body))
      return HttpResponse("")
    else:
      all_groups = Item.objects.all()
      response = serialize("json", all_groups)
      return HttpResponse(response, content_type="application/json")
    
def recipe(request):
    if request.method == "POST":
      print(json.load(request.body))
      return HttpResponse("")
    else:
      all_groups = Recipe.objects.all()
      response = serialize("json", all_groups)
      return HttpResponse(response, content_type="application/json")
  
def index(request):
    all_groups = Item.objects.all()
    return render(request, 'life/index.html', {"items": all_groups}) 
