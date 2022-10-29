from urllib import request
from django.shortcuts import redirect, render
from supplies.models import Product

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required

from supplies.models import Product
from supplies.forms import ProductForm 
from django.http import HttpResponse
from django.core import serializers

from django.http import HttpResponseRedirect 
from django.urls import reverse 


@login_required(login_url='/authentication/login/')
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('supplies:show_supplies')
        else:
            messages.info(request, 'Wrong Username or Password, try again!')
    context = {}
    return render(request, 'login.html', context)

def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        contact = request.POST.get('contact')
        print(f'============ {title}')
        print(f'============ {price}')
        print(f'============ {contact}')

        new_product = Product(
            title=title, 
            price=price,
            contact=contact,
            user=request.user,
        )
        new_product.save()
    return redirect('supplies:show_supplies')

# def create_product(request):
#     form = Product()
#     if request.method == 'POST':
#         form = ProductForm (request.POST)
#         if form.is_valid():
#             data = Product(
#                 title = form.cleaned_data["form_tittle"],
#                 price = form.cleaned_data["form_price"],
#                 contact = form.cleaned_data["form_contact"],
#                 user = request.user,
#             )
#             data.save()
#             messages.success(request, 'Your product successfully uploaded!')
#             return redirect('supplies:show_supplies')
#     context = {"form": form}
#     return render(request, 'create_product.html', context)

def show_supplies(request):
    data = Product.objects.all()
    context = {
        'data_product': data,
    }
    return render(request, 'supplies.html', context)
    
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
 
 
 
 
 
    
# bakal ke page favorite (judul cart jangan lupa diganti Favorite!!!!)
# def cart(request):
#     context = {}
#     return render(request, 'cart.html', context)
    
# bakal ke page info product beserta kontak penjualnya
def view_product(request):
    context = {}
    return render(request, 'view_product.html', context)





# def logout_user(request):
#     logout(request)
#     messages.info(request, 'Successfully logout, see ya!^^')
#     return redirect('todolist:login')


