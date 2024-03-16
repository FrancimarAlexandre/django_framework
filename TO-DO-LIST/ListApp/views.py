from django.shortcuts import render
from .models import Tarefa
# Create your views here.

# visualizar a tarefa
def view_tarefa(request):
    tarefa = Tarefa.objects.all()
    return render(request,'viewtarefa.html',{'contexto':tarefa})



# tela home

def home(request):
    if request.method == 'POST':
        
        tarefa = Tarefa()
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.data_tarefa = request.POST.get('data_tarefa')
        tarefa.save()
    return render(request,'home.html')