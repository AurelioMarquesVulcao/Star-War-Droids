from django.db import models


class Demanda(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    rua_entrega = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    tel_contato = models.CharField(max_length=9)
    user = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
