from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='pagina_inicial'),
    path('teste/',views.teste,name='teste')
]
