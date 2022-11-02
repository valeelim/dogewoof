from urllib import request
from django.shortcuts import redirect, render
from supplies.models import Product

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required

from supplies.forms import ProductForm 
from django.http import HttpResponse
from django.core import serializers

from django.http import HttpResponseRedirect 
from django.urls import reverse 


@login_required(login_url='/authentication/login/')

def show_supplies(request):
    data = Product.objects.filter(user=request.user).all()
    context = {
        'data_product': data,
    }
    return render(request, 'supplies.html', context)
    
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
 
def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        contact = request.POST.get('contact')
        new_task = Product(
            title=title, 
            price=price, 
            description=description,
            contact=contact, 
            user=request.user,
        )
        new_task.save()
    return redirect('supplies:show_supplies')

def ubah_status(request, id):
    data = Product.objects.get(pk=id) 
    if (not data.is_finished):
        data.is_finished = True
    data.save()
    return redirect('supplies:show_supplies')

def hapus_task(request, id):
    Product.objects.get(pk=id).delete()
    return redirect('supplies:show_supplies')