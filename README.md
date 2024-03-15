# django_framework
Repositório dedicado à explicação do framework Django
# Instalação
     pip install django
# Estrutura básica de um projeto django
  - Criar um novo projeto :
    -     django-admin startproject nome_do_projeto
# São gerados automaticamente alguns arquivos 
## manage.py
  - É um utilitário de linha de comando que permite interagir com este projeto Django de várias maneiras. Você o usa para executar comandos disponíveis no Django, como criar aplicativos dentro do projeto, trabalhar com bancos de dados e iniciar o servidor de desenvolvimento.
## nome_do_projeto/
  - Esta é a pasta raiz do seu projeto, nomeada após o nome que você deu ao criar o projeto. Ela contém:

    # __init__.py
    Um arquivo vazio que diz ao Python que este diretório deve ser considerado um pacote Python.
    # settings.py
    Contém as configurações do seu projeto Django, incluindo configurações de banco de dados, configurações de localização (idioma e fuso horário), e outras configurações específicas do projeto.
    # urls.py
    Responsável por declarar as rotas URL do seu projeto e direcioná-las para as respectivas views. Funciona como uma "tabela de conteúdos" para o seu projeto web, direcionando os usuários para o conteúdo apropriado.
    # asgi.py e wsgi.py
    São pontos de entrada para servidores web compatíveis com ASGI (Asynchronous Server Gateway Interface) ou WSGI (Web Server Gateway Interface), respectivamente. Isso permite que seu projeto Django seja servido em produção.
    # admin.py
    Embora não seja gerado automaticamente na pasta do projeto, este arquivo é criado dentro de cada aplicativo Django. É usado para configurar o site administrativo do Django, uma interface poderosa e automatizada para administrar seu site.
