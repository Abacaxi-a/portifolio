from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('',views.home_page,name='pagina_inicial'),
    #path('projetos/',views.projetos_page,name='projetos')
]
