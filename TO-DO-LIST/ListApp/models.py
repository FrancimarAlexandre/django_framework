from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length = 55)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add = True)
    atualizacao = models.DateField(auto_now_add = True)
    concluida = models.BooleanField(default = 1)

    def __str__(self):
        return self.titulo