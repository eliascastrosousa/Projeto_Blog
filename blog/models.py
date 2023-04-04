from django.db import models

class Post(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    artigo = models.TextField()
    image =  models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome
