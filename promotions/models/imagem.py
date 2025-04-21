from django.db import models

class Imagem(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="media/", verbose_name="Imagem", help_text="Faça o upload da imagem") 

    def __str__(self):
        return self.nome
