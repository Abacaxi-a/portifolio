from django.shortcuts import render,redirect

# Create your views here.

def home_page(response):
    return render(response,'index.html')

def teste(request):
    return redirect('pagina_inicial')