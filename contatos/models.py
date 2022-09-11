from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Contato(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to='fotos_contatos/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.nome
2