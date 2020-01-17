from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logut

from . import forms, models


def logout(request):

    auth_logut(request)

    return redirect('/')


def index(request):

    return render(request, 'index.html')


def travels(request):

    if 'type' in request.GET:
        travels = models.Travel.objects.filter(vehicle__vehicle_type=request.GET['type'])

    else:
        travels = models.Travel.objects.all()


    response = {
        'travels': travels
    }

    return render(request, 'travels.html', response)



def travel(request, id):
    return render()