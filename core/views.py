from django.shortcuts import render
import os

# Create your views here.

def home(request):
    return render(request,'core/home.html')

