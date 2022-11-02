import os
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/autentikasi')
def show_profile(request, username):

    user_data = Profile.objects.get(user=request.user)

    bio = user_data.bio
    phone = user_data.phone

    if bio == None:
        bio = "-"

    if phone == None:
        phone = "-"

    context = {
        'user' : request.user,
        'image' : user_data.image,
        'bio' : bio,
        'saldo' : user_data.saldo,
        'phone' : phone,
        'form1' : ProfileForm,
        'form2' : TopUpForm,
    }
    
    return render(request, 'profile.html', context)

@login_required(login_url='/autentikasi')
def show_topup(request):

    return render(request, 'topup.html')

def edit_profile(request):
    user = request.user.profile
    if request.POST:
        form = ProfileForm(request.POST, request.FILES, instance=user)
        print(form.is_valid())

        if form.is_valid():
            obj = form.save(commit=False)

            if obj.image:
                obj.save(update_fields=['image'])

            if obj.bio:
                obj.save(update_fields=['bio'])

            if obj.phone:
                obj.save(update_fields=['phone'])
            
            return HttpResponse("success")
    
    

def edit_saldo(request):
    user = request.user.userprofile
    if request.POST:
        new_saldo = request.POST['saldo']
        print(f'new saldo {new_saldo}')
        user_data = Profile.objects.get(user=request.user)
        print(f'user saldo {user_data.saldo}')

        user_data.saldo += int(new_saldo)

        user_data.save()
            
        return HttpResponseRedirect('/profile')

            

def show_json(request):
    profileobj = Profile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", profileobj), content_type="application/json")