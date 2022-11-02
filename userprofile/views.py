import os
from django.shortcuts import render
from userprofile.models import UserProfile
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from userprofile.forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/autentikasi')
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
        'user' : request.user.username,
        'picture' : user_data.picture,
        'bio' : bio,
        'address' : address,
        'dogtype' : dogtype,
        'saldo' : user_data.saldo,
        'phone' : phone,
        'email' : request.user.email,
        'form1' : ProfileForm,
        'form2' : TopUpForm,
    }
    
    return render(request, 'profile.html', context)

@login_required(login_url='/autentikasi')
def show_topup(request):

    return render(request, 'topup.html')

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
    user = request.user.userprofile
    if request.POST:
        new_saldo = request.POST['saldo']
        print(f'new saldo {new_saldo}')
        user_data = UserProfile.objects.get(user=request.user)
        print(f'user saldo {user_data.saldo}')

        user_data.saldo += int(new_saldo)

        user_data.save()
            
        return HttpResponseRedirect('/profile')
            # if obj.saldo:
            #     obj.save(update_fields=['saldo'])

            

def show_json(request):
    profileobj = UserProfile.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", profileobj), content_type="application/json")