import os
from django.shortcuts import render
from userprofile.models import UserProfile
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from userprofile.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@login_required(login_url='/authentication/login/')
def show_profile(request):

    user_data = UserProfile.objects.get(user=request.user)

    address = user_data.address
    bio = user_data.bio
    phone = user_data.phone
    dogtype = user_data.dogtype

    if bio == None:
        bio = "-"

    if address == None:
        address = "-"

    if phone == None:
        phone = "-"

    context = {
        'username' : request.user.username,
        'bio' : bio,
        'image' : user_data.picture.url,
        'address' : address,
        'dogtype' : dogtype,
        'saldo' : user_data.saldo,
        'phone' : phone,
        'email' : request.user.email,
    }
    
    
    return JsonResponse({'data':context})

@csrf_exempt
@login_required(login_url='/authentication/login/')
def edit_profile(request):
    profile = request.user.userprofile
    if request.POST:
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid() :
            obj = form.save(commit=False)

            if obj.bio:
                obj.save(update_fields=['bio'])

            if obj.phone:
                obj.save(update_fields=['phone'])

            if obj.address:
                obj.save(update_fields=['address'])

            if obj.dogtype:
                obj.save(update_fields=['dogtype'])

            return JsonResponse({
                'bio': obj.bio,
                'phone': obj.phone,
                'address': obj.address,
                'dogtype': obj.dogtype,
            })
            
    return HttpResponse("success")
    

def edit_saldo(request):
    if request.POST:
        new_saldo = request.POST['saldo']
        user_data = UserProfile.objects.get(user=request.user)
        user_data.saldo += int(new_saldo)
        user_data.save()

        return HttpResponse("success")
  
def show_json(request):
    profileobj = UserProfile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", profileobj), content_type="application/json")
