from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from dog_market.forms import *
from dog_market.models import DogItem


# Create your views here.

data_item = DogItem.objects.all()
context = {
    'itemlist': data_item,
}

@login_required(login_url='/authentication/login/')
def listing(request):
    context = {}
    all = DogItem.objects.all()
    return render(request, "listing.html", {'all':all})

@login_required(login_url='/authentication/login/')
def submit_item(request):

    if request.method == "POST":
        form = DogItemFormModel(request.POST)
        if form.is_valid():
            form.save()
    context = {}
    context['form']= DogItemFormModel()

    return render(request, "submit_item.html", context)

@login_required(login_url='/authentication/login/')
def submit_item_alt(request):

    if request.method == "POST":
        form = DogItemForm(request.POST)
        if form.is_valid():
            newitem = DogItem.objects.create(
                item_title = form.cleaned_data["item_title"],
                price = form.cleaned_data["price"],
                breed = form.cleaned_data["breed"],
                description = form.cleaned_data["description"],
                contact = form.cleaned_data["contact"],
                image = form.cleaned_data["image"],
                user = request.user,
            )
            newitem.save()

    return render(request, "submit_item_alt.html", context)
    
@login_required(login_url='/authentication/login/')
def view_item(request, itemid):
    reqitem = DogItem.objects.get(id=itemid)
    return render(request, "view_item.html", reqitem)
