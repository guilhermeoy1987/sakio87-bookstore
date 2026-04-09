# sakio87-bookstore

🔑 Autenticação via Token em APIs (Bookstore API)
Data: 2026 | Foco: Segurança de Comunicação e Stateless Auth
Desenvolvimento focado na branch feat-auth-token, implementando o padrão de Token Authentication. Esta é uma etapa crucial para permitir que a API seja consumida de forma segura por diferentes front-ends (Web, Mobile) de maneira desacoplada e eficiente.

✅ Autenticação Stateless: Implementação do sistema de tokens onde o servidor não precisa armazenar a sessão do usuário, tornando a API mais escalável e performática.

✅ Geração Dinâmica de Tokens: Configuração da lógica para que, após o login bem-sucedido, o sistema gere uma chave única de acesso para o usuário realizar requisições subsequentes.

✅ Cabeçalhos de Autorização (Headers): Integração da lógica de validação que identifica o usuário através do campo Authorization: Token <key> enviado nas requisições HTTP.

✅ Persistência de Segurança: Configuração do banco de dados para gerenciar o ciclo de vida dos tokens, permitindo a revogação de acessos quando necessário.

Stack: Python, Django, Django Rest Framework (TokenAuth) e Git.
