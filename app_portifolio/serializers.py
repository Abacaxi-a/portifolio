from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer): #TODO:entender
    class Meta:
        model = Post
        fields = '__all__'