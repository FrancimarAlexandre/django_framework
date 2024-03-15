from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
# CREATE
def home(request):
    if request.method == 'POST':
        usuario = Usuario()
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.senha = request.POST.get('password')
        usuario.idade = request.POST.get('age')  # Corrigido para atribuir à instância
        usuario.save()  # Corrigido para salvar a instância correta
    return render(request,'home.html')
 

# READ
def viewusers(request):
    usuario = Usuario.objects.all()
    return render(request,'users.html',{'contexto':usuario})

# DELETE
def deleteusers(request,id):
    usuario = Usuario.objects.filter(pk = id).delete()
    return redirect(viewusers)

# UPDATE
def editusers(request,id):
    return render(request,'editusers.html')