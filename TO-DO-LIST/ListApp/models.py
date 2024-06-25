from django.db import models

# Create your models here.



class Tarefa(models.Model):
    titulo = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.TextField()
    data_tarefa = models.DateField()
    data_concluido = models.DateTimeField(null=True, blank=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
