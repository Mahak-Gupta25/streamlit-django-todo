
from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages

import requests

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

def app(request):
    return render(request, 'todo/app.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}!")
            return redirect("login")
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,"todo/register.html", context)
