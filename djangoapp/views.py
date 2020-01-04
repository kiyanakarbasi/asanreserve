from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logut

from . import forms, models


def logout(request):
    auth_logut(request)
    return redirect('/')
