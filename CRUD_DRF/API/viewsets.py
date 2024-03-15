from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuario

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

    def create_usuario(request):
        
