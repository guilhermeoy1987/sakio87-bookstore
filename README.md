# sakio87-bookstore
🧪 Cobertura de Testes e Validação de Fluxos (Bookstore API)
Data: 2026 | Foco: Qualidade de Código e Robustez de Sistema
Desenvolvimento focado na branch novoteste2, representando uma evolução na suíte de testes da aplicação. O objetivo principal foi expandir a cobertura de testes para cenários mais complexos, garantindo que a API mantenha sua integridade mesmo sob condições de uso variadas.

✅ Testes de Regras de Negócio: Implementação de verificações para garantir que o sistema não permita operações inválidas (ex: cadastrar livros com preços negativos ou campos obrigatórios vazios).

✅ Simulação de Requisições Complexas: Uso de ferramentas de teste do Django para simular diferentes métodos HTTP (POST, PUT, PATCH, DELETE) em endpoints protegidos, validando a resposta do servidor.

✅ Integridade do Banco de Dados: Testes que confirmam se as operações realizadas via API estão sendo persistidas corretamente no banco de dados e se os relacionamentos entre Autores e Livros permanecem consistentes.

✅ Refino de Mensagens de Erro: Validação de que a API retorna mensagens de erro claras e informativas em formato JSON quando uma requisição falha, melhorando a experiência para os desenvolvedores de Front-end.

Stack: Python, Django Rest Framework (Testing), Git.
