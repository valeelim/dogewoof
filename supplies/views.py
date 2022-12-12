from urllib import request
from django.shortcuts import redirect, render
from supplies.models import Product

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required

from supplies.forms import ProductForm 
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from django.http import HttpResponseRedirect 
from django.urls import reverse 
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/authentication/login/')

def show_supplies(request):
    data = Product.objects.all()
    context = {
        'data_product': data,
    }
    return render(request, 'supplies.html', context)

@csrf_exempt    
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
 
@csrf_exempt 
def add_product(request):
    if request.method == 'POST':
        form = ProductForm( request.POST)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            return render(request, 'supplies.html', {'form': form})        
        else:
            form = ProductForm()
    return render(request, 'supplies.html', {'form': form})  
 
@csrf_exempt      
def add(request):
    if request.method == 'POST':
        Product(title=request.POST.get('title'), price=request.POST.get('price'), description=request.POST.get('description'), contact=request.POST.get('contact')).save()
        return JsonResponse({'message': 'success'})
    return render(request, "create.html")