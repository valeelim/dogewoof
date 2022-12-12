from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
from django.db.models import Sum
from .models import ContactUs, Donation
from .forms import DonationForm
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime

import json

def index(request):
    form = DonationForm()
    donationSum = Donation.objects.aggregate(Sum('amount'))
    return render(request, 'index.html', {
        'total_donation': 0 if donationSum['amount__sum'] == None else donationSum['amount__sum'],
        'form': form
    })

@csrf_exempt
def contactUs(request):
    if request.method == 'POST':
        newContactUs = ContactUs(
            user=request.user,
            date=datetime.now(),
            subject=request.POST.get('subject'),
            description=request.POST.get('description'),
        )
        newContactUs.save()
        return JsonResponse({'message': 'success'})
    return render(request, 'index.html', {})

@csrf_exempt
def getContactUs(request):
    data = []
    for obj in ContactUs.objects.all():
        print(obj.date)
        data.append({
            'username': str(obj.user),
            'date': obj.date.strftime("%d %b %Y %I:%M %p"),
            'subject': obj.subject,
            'description': obj.description
        })
    return JsonResponse(data, safe=False)
        
@csrf_exempt
def makeDonation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            newDonation = Donation(
                user=request.user,
                amount=amount
            )
            newDonation.save()
            return JsonResponse({
                'donated_amount': amount
            })
    return HttpResponseRedirect(reverse('home:index'))

def getDonation(request):
    donationSum = Donation.objects.aggregate(Sum('amount'))
    return JsonResponse({
        'total': donationSum,
    })

def getAllDonations(request):
    data = []
    for obj in Donation.objects.all().order_by('-amount'):
        data.append({
            "username": str(obj.user), 
            "amount": int(obj.amount)
        })
    return JsonResponse(data, safe=False)

