from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from .models import DogDescription
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.

def get_model_json(request) :
    data = []
    for obj in DogDescription.objects.all():
        data.append({
            "name": str(obj.name),
            "url": str(obj.image.url),
            "first_description": str(obj.first_description)
        })
    return JsonResponse(data, safe=False)
    dog_object = DogDescription.objects.all()
    return HttpResponse(serializers.serialize("json", dog_object), content_type="application/json")

def show_dog_list(request) :
    return render(request, "show_dog_list.html")

def get_dog_detail_json(request) :
    data = []
    for obj in DogDescription.objects.all():
        data.append({
            "secont_description": str(obj.secont_description),
            "url": str(obj.image.url),
            "funfact": str(obj.funfact)
        })
    return JsonResponse(data, safe=False)
    dog_object = DogDescription.objects.get(pk = int(id))
    return HttpResponse(serializers.serialize("json", [dog_object]), content_type="application/json")

@login_required(login_url='/authentication/login/')
def get_dog_detail(request, id) :
    dog_object = DogDescription.objects.get(pk = int(id))
    context = {
        "id" : dog_object.id,
        "name" : dog_object.name.upper()
    }
    return render(request, "get_dog_detail.html", context)
