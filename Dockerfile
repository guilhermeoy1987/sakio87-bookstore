# Usa uma imagem oficial do Python
FROM python:3.13-slim

# Define variáveis de ambiente para evitar arquivos .pyc e buffer de log
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Fiz os hosts permitidos para o Django não dar erro de 'NoneType'
# Adicionamos .onrender.com aqui também como garantia de ambiente
ENV DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1] .onrender.com"

# Define o diretório de trabalho
WORKDIR /app

# --- MUDANÇA AQUI: INSTALAÇÃO DO GIT E DEPENDÊNCIAS DE BUILD ---
# Adicionamos gcc, libpq-dev e python3-dev para o psycopg2 conseguir compilar
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
# --------------------------------------------------------------

# Copia e instala dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app/

# O Render vai gerenciar a porta automaticamente, mas deixamos exposta a variável de ambiente
EXPOSE 8000

# ⚡ AJUSTE AQUI: Roda as migrações e inicia com Gunicorn usando a porta dinâmica do Render
CMD ["sh", "-c", "python manage.py migrate && gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT"]