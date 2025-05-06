from django.db import models

# Create your models here.
class Post(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

class Delete(models.Model):
    valor_unico = id