from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Sum
from .models import ContactUs, Donation
from .forms import DonationForm

def index(request):
    form = DonationForm()
    donationSum = Donation.objects.aggregate(Sum('amount'))
    return render(request, 'index.html', {
        'total_donation': 0 if donationSum['amount__sum'] == None else donationSum['amount__sum'],
        'form': form
    })

@login_required
def contactUs(request):
    if request.method == 'POST':
        newContactUs = ContactUs(
            user=request.user,
            subject=request.POST.get('subject'),
            description=request.POST.get('description'),
        )
        newContactUs.save()
        return JsonResponse({'message': 'success'})
    return render(request, 'index.html', {})

@login_required
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
            

