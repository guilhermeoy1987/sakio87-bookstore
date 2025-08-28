# sakio87-bookstore

Nesse exercício faremos um novo projeto, você deve usar o projeto bookstore, que construímos durante as aulas, e adicionar o Django Rest Framework (DRF). Para isso, você usará o comando:

poetry add djangorestframework

Feito essa instalação, para garantirmos que o poetry.lock foi atualizado, utilize o comando poetry update.

Agora, no seu arquivo settings.py, você deve adicionar o DRF como um app instalado. Para isso, procure pelo INSTALLED_APPS e adicione-o, exemplo:

INSTALLED_APPS = [
 "django.contrib.admin",
 "django.contrib.auth",
 "django.contrib.contenttypes",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.staticfiles",
 'rest_framework',	
]


Realize o teste para verificar se o projeto permaneceu operativo:


poetry run python manage.py runserver

update realizado.
