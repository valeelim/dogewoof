from django.shortcuts import render
from .forms import Form
from .models import FAQ
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def mainpage(request):
    form = Form()
    data = FAQ.objects.all()
    context = {
        'title':'Frequentyly Asked Questions',
        'data': data,
        'form': form
    }
    return render(request, "mainpage.html", context)

@login_required(login_url='/authentication/login/')
def input_question(request):
    form = Form(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

        return redirect('faq:mainpage')
    
    context = {'form':form}
    return render(request, "add_question.html", context)


def json_forum(request):
        data = FAQ.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")




