from django.db import models

class Aluno(models.Model):
    registro_aluno = models.PositiveIntegerField()
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    secao = models.CharField(max_length=50)

def __str__(self):
    return f'Aluno: {self.nome} {self.sobrenome}'