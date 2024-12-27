from django.shortcuts import render,redirect

# Create your views here.

def home_page(response):
    return render(response,'pages/home.html')
