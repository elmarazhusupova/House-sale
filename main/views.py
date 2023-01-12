from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    banner = Banner.objects.all()
    about = AboutApartment.objects.all()
    content = {'banner': banner, 'about':about}
    return render(request, 'index.html', content)



def about(request):
    about = AboutApartment.objects.all()
    content = {'about': about}
    return render(request,'about.html', content)
