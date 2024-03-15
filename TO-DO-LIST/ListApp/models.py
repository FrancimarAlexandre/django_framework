from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length = 55)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add = True)
    data_tarefa = models.DateField(auto_now_add = False)
    data_concluido = models.DateField(null=True)
    atualizacao = models.DateField(null = True)
    concluida = models.BooleanField(default = False)

    def __str__(self):
        return self.titulo