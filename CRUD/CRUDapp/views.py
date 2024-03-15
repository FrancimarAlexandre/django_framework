from django.shortcuts import render,get_object_or_404, redirect
from .models import Usuario

# Create your views here.
# CREATE
def home(request):
    if request.method == 'POST':
        usuario = Usuario()
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.senha = request.POST.get('password')
        usuario.idade = request.POST.get('age')  
        usuario.save()  
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
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.senha = request.POST.get('password')
        usuario.idade = request.POST.get('age')
        usuario.save()
        return redirect(viewusers)
    user = {
        'id':usuario.id,
        'username':usuario.username,
        'email':usuario.email,
        'senha':usuario.senha,
        'idade':usuario.idade,
    }
    return render(request,'editusers.html',{'contexto':user})