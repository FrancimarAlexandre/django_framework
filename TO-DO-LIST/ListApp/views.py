from django.shortcuts import render,get_object_or_404,redirect
from .models import Tarefa
from datetime import datetime
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


# delete tarefa

def delete_tarefa(request,id):
    tarefa = Tarefa.objects.filter(pk = id).delete()
    return redirect(view_tarefa)

# tarefa concluída

def concluir_tarefa(request,id):
    if request.method == 'POST':
        tarefa = get_object_or_404(Tarefa,pk = id)
        tarefa.data_concluido = datetime.now()
        tarefa.concluida = True
        tarefa.save()
    return redirect(view_tarefa)

