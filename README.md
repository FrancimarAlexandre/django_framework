# django_framework
Repositório dedicado à explicação do framework Django
# Resumo
 O Django oferece uma estrutura que facilita o desenvolvimento de sites seguros e escaláveis. Compreender a função de cada arquivo e componente é crucial para aproveitar ao máximo o que o framework oferece. Essa visão geral cobre os aspectos essenciais, mas o Django tem muito mais a explorar, incluindo formulários, autenticação de usuários, sinais, e muito mais. Recomendo consultar a <a hreft = "https://docs.djangoproject.com/en/5.0/">documentação</a> oficial do Django para obter informações detalhadas e atualizadas.

# Instalação
     pip install django
# Estrutura básica de um projeto django
### Um projeto Django é composto por um ou mais aplicativos, que são módulos do projeto. Cada aplicativo contém funcionalidades específicas do projeto
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




# Estrutura básica de um aplicativo django
  - criar um novo aplicativo
    -      python manage.py startapp nome_do_app

### Dentro de um projeto Django, você pode ter um ou vários aplicativos. Cada aplicativo contém um conjunto de arquivos similares:

# migrations/:
  -  Diretório que contém as migrações de banco de dados – arquivos que descrevem como fazer e desfazer as alterações feitas na estrutura do banco de dados.
# models.py:
  -  Define a estrutura dos dados do aplicativo, usando classes Python. Essas definições são convertidas pelo Django em tabelas de banco de dados.
# views.py: 
  - Contém a lógica de apresentação. As views recebem requisições web e retornam respostas. As respostas podem ser páginas HTML, redirecionamentos, arquivos para download, JSON para APIs, entre outros.
# tests.py:
  - Usado para escrever testes para o seu aplicativo.
# apps.py:
  - Usado para configurar metadados do aplicativo.
# admin.py:
  - Como mencionado anteriormente, é usado para configurar o site administrativo para o seu aplicativo.


# comandos usados no Django:
 ## django-admin startproject nome_do_projeto
   - Este comando cria um novo projeto Django. Ele gera a estrutura inicial do diretório do projeto, incluindo configurações básicas.
 ## python manage.py startapp nome_da_app
   - Usado para criar uma nova aplicação Django dentro do projeto. Cada aplicação pode conter seu próprio conjunto de modelos, vistas, formulários e testes.
 ## python manage.py runserver
   - Inicia um servidor de desenvolvimento local no endereço http://127.0.0.1:8000/. Este comando é muito útil para desenvolvimento e teste rápido.
 ## python manage.py createsuperuser
   - Cria um usuário administrador (superuser), permitindo acesso ao Django Admin, uma interface auto-gerada para administração de conteúdo do site.
 ## python manage.py makemigrations
   - Identifica mudanças feitas nos modelos (models) e prepara arquivos de migração, que são scripts para ajustar o esquema do banco de dados.
 ## python manage.py migrate
   - Aplica as migrações ao banco de dados. Este comando atualiza o banco de dados com as novas alterações feitas nos modelos.
 ## python manage.py collectstatic
   - Coleta arquivos estáticos das apps e de outros lugares em uma localização central que pode ser servida em produção.
 ## python manage.py test
   - Roda os testes definidos nas aplicações do projeto Django. É uma forma essencial de verificar a integridade do código ao fazer mudanças.
 ## python manage.py shell
   - Abre o shell interativo do Django, que é um Python shell com o ambiente do Django configurado. É útil para interagir diretamente com os componentes do Django, como modelos e consultas ao banco de dados.
 ## python manage.py dbshell
   - Fornece acesso ao shell do banco de dados, útil para consultas diretas ao banco de dados ou para administração.
 ## python manage.py dumpdata
   - Usado para criar um backup dos dados do banco de dados. Gera saída em vários formatos (incluindo JSON e XML).
 ## python manage.py loaddata
   - Carrega dados no banco de dados a partir de um arquivo. É usado frequentemente em conjunto com o comando dumpdata
