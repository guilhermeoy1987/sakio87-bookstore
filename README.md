# sakio87-bookstore #Alteraçãp para fazer token authentication.

🚀 Implementação de Infraestrutura com Docker Compose
Nesta etapa do projeto, avançamos na automação do ambiente de desenvolvimento da aplicação Sakio87 Bookstore. O foco principal foi a orquestração de múltiplos serviços e a integração com um banco de dados robusto.

🛠️ O que foi implementado:
Orquestração com Docker Compose:

Criação do arquivo docker-compose.yml para gerenciar a aplicação e o banco de dados simultaneamente.

Definição de redes internas para permitir que os containers se comuniquem pelo nome do serviço.

Integração com Banco de Dados Postgres:

Substituição (ou preparação) do banco de dados para utilizar o PostgreSQL 15.

Configuração de variáveis de ambiente (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB) para garantir a segurança e flexibilidade das credenciais.

Persistência de Dados (Volumes):

Configuração de um volume nomeado (postgres_data). Isso garante que os dados cadastrados na livraria não sejam perdidos quando os containers forem reiniciados ou removidos.

Mapeamento de Portas e Conectividade:

Exposição da porta 8000 para acesso externo à API/Aplicação.

Implementação da diretiva depends_on, garantindo que a aplicação só inicie após o banco de dados estar pronto para aceitar conexões.

📋 Fluxo de Trabalho Git:
Criação de uma branch dedicada: dockercompose.

Realização de testes de conectividade local (Docker Desktop).

# Execução bem-sucedida das migrações do Django dentro do ambiente isolado.

# API de Gerenciamento de Livraria (Bookstore API)

Data: 2026 | Foco: Desenvolvimento Backend e APIs RESTful Desenvolvimento de uma API robusta para controle de acervo e vendas, focada na construção de um sistema escalável que gerencia a comunicação entre o banco de dados e as requisições do cliente.

✅ Arquitetura Django Rest Framework (DRF): Implementação de uma estrutura profissional para criação de endpoints seguros, utilizando Serializers para a conversão eficiente de dados complexos em JSON.

✅ Modelagem de Dados: Estruturação de modelos de banco de dados para livros, autores e categorias, garantindo a integridade e o relacionamento correto entre as informações.

✅ CRUD Completo: Desenvolvimento das operações de Criação, Leitura, Atualização e Exclusão (CRUD), permitindo o gerenciamento total do inventário através de requisições HTTP.

✅ Testes de Endpoints: Validação das rotas de API para garantir que o sistema responda corretamente a diferentes cenários de entrada, priorizando a estabilidade do software.

Stack: Python, Django, Django Rest Framework e SQLite/PostgreSQL.
