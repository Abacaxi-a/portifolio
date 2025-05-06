from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def home_page(request):
    return redirect('http://localhost:3000/')



