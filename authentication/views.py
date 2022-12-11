from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
            }, status=401)
    return render(request, 'login.html', {})

@csrf_exempt
def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('yay')
            form.save()
            return JsonResponse({
                "status": True,
                'message': 'User successfully registered',
            }, status=200)
        return JsonResponse({
            "status": False,
            'message': 'Something went wrong',
        }, status=400)
    context = {'form': form}
    return render(request, 'register.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    # response = HttpResponseRedirect(reverse('authentication:login'))
    # response.delete_cookie('username')
    return JsonResponse({
        "status": True,
        "message": "Successfully logged out"
    }, status=200)



