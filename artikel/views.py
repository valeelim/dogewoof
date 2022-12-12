from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse 
from .models import DogDescription
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.

def get_model_json(request) :
    data = DogDescription.objects.all()
    data_list = list(data)
    res_data = []
    for i in data_list :
        temp_data = {
            "id": i.id,
            "image" : i.image.url,
            "name" : i.name,
            "first_description" : i.first_description,
            "secont_description" : i.secont_description,
            "funfact" : i.funfact,
        }
        res_data.append(temp_data)
    return JsonResponse({
        "data":res_data
    })

def post_flutter(request) :
    if(request.method == POST) :
        image = request.POST.get("image"),
        name = request.POST.get("name,")
        first_description = request.POST.get("first_description"),
        secont_description = request.POST.get("secont_description"),
        funfact = request.POST.get("funfact"),

        dog_description = DogDescription.objects.create(
            image = image,
            name = name,
            first_description = first_description,
            secont_description = secont_description,
            funfact = funfact
        )
        return JsonResponse({
            "messages" : "succes"
        })
    return JsonResponse(data, safe=False)
    #dog_object = DogDescription.objects.all()
    #return HttpResponse(serializers.serialize("json", dog_object), content_type="application/json")


def show_dog_list(request) :
    return render(request, "show_dog_list.html")


def get_dog_detail_json(request, id) :
    data = DogDescription.objects.get(pk=int(id))
    print("TEST")
    data_values = {
        "image" : data.image.url,
        "name" : data.name,
        "first_description" : data.first_description,
        "secont_description" : data.secont_description,
        "funfact" : data.funfact,
        #"user" : data.user,
    }
    return JsonResponse({
        "data":data_values
    })

# def get_dog_detail_json(request) :
#     data = []
#     for obj in DogDescription.objects.all():
#         data.append({
#             "secont_description": str(obj.secont_description),
#             "url": str(obj.image.url),
#             "funfact": str(obj.funfact)
#         })
#     return JsonResponse(data, safe=False)

    #dog_object = DogDescription.objects.get(pk = int(id))
    #return HttpResponse(serializers.serialize("json", [dog_object]), content_type="application/json")

@login_required(login_url='/authentication/login/')
def get_dog_detail(request, id) :
    dog_object = DogDescription.objects.get(pk = int(id))
    context = {
        "id" : dog_object.id,
        "name" : dog_object.name.upper()
    }
    return render(request, "get_dog_detail.html", context)
