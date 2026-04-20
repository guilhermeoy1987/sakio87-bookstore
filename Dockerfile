# Usa uma imagem oficial do Python
FROM python:3.13-slim

# Define variáveis de ambiente para evitar arquivos .pyc e buffer de log
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Fiz os hosts permitidos para o Django não dar erro de 'NoneType'
ENV DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"
# -------------------

# Define o diretório de trabalho
WORKDIR /app

# INSTALAÇÃO DO GIT
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app/

# Expõe a porta que o Django utiliza
EXPOSE 8000

#  Tenta rodar as migrações e depois inicia o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]