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

# Editar terafa

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_tarefa = request.POST.get('data_tarefa')
        
        if titulo and descricao and data_tarefa:
            tarefa.titulo = titulo
            tarefa.descricao = descricao
            tarefa.data_tarefa = data_tarefa
            tarefa.concluida = False
            tarefa.save()
            return redirect(view_tarefa)
        else:
            return render(request, 'editartarefa.html', {'tarefa': tarefa, 'error': 'Todos os campos são obrigatórios.'})
    
    return render(request, 'editartarefa.html', {'tarefa': tarefa})