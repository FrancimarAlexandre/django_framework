from django.shortcuts import render
from . models import Usuario
# Create your views here.

def register(request):
    if request.method == 'POST':
        usuario  = Usuario()
        usuario.username = request.POST.get('username')
        usuario.email = request.POST.get('email')
        usuario.password = request.POST.get('password')
        user = usuario.save()
        if user:
            pass
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')