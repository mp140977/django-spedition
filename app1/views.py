from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request,"app1/base.html", {})

def bestellung(request):
    return render(request, "app1/bestellung.html", {})