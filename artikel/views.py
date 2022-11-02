from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def show_artikel(request):
    return render(request, "artikel.html")

def show_huskey(request):
    return render(request, "huskey.html")

def show_bulldog(request):
    return render(request, "bulldog.html")

def show_germanshepherd(request):
    return render(request, "GermanShepherd.html")

def show_poodles(request):
    return render(request, "poodles.html")

def show_shihtzu(request):
    return render(request, "shihtzu.html")

def show_pomeranians(request):
    return render(request, "pomeranians.html")

def show_chihuahua(request):
    return render(request, "chihuahua.html")

def show_chowchow(request):
    return render(request, "chowchow.html")
