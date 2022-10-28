from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ContactUs

def index(request):
    return render(request, 'index.html', {})

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