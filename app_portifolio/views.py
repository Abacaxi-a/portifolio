from django.shortcuts import render,redirect

# Create your views here.

def home_page(request):
    return render(request,'pages/home.html')


def projetos_page(request):
    return render(request,'pages/projetos.html')


