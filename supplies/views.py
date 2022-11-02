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
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'supplies.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ProductForm()
    return render(request, 'supplies.html', {'form': form})        


def ubah_status(request, id):
    data = Product.objects.get(pk=id) 
    if (not data.is_finished):
        data.is_finished = True
    data.save()
    return redirect('supplies:show_supplies')

def hapus_task(request, id):
    Product.objects.get(pk=id).delete()
    return redirect('supplies:show_supplies')