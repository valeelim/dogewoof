import os
from django.shortcuts import render
from userprofile.models import UserProfile
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from userprofile.forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.

def show_profile(request):

    data = []
    for obj in UserProfile.objects.all():
        data.append({
            'username' :str(obj.user),
            'bio' : str(obj.bio),
            'address' :  str(obj.address),
            'dogtype' :  str(obj.dogtype),
            'saldo' :  int(obj.saldo),
            'phone' :  str(obj.phone),
        })
    return JsonResponse(data, safe=False)


def edit_profile(request):
    profile = request.user.userprofile
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        print(form.is_valid())

        if form.is_valid() :
            obj = form.save(commit=False)

            if obj.picture:
                obj.save(update_fields=['picture'])

            if obj.bio:
                obj.save(update_fields=['bio'])

            if obj.phone:
                obj.save(update_fields=['phone'])

            if obj.address:
                obj.save(update_fields=['address'])

            if obj.dogtype:
                obj.save(update_fields=['dogtype'])
            
            
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
