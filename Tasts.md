# Plano de Tarefas para Desenvolvimento do Projeto de Finanças Domésticas

## Task 1: Configuração Inicial

- [ ] **Configurar o Ambiente Virtual**
  - Ative o ambiente virtual que já foi criado (`.venv`).
  - Instale as dependências necessárias (se houver, como `pytest` para testes).

- [ ] **Configuração do Banco de Dados (se aplicável)**
  - Configure o arquivo `config/database.py` para estabelecer a conexão com o banco de dados.
  - Defina as configurações no arquivo `config/settings.py`.

## Task 2: Implementação dos Modelos

- [ ] **Implementar Classe `Usuario`**
  - Implemente a classe `Usuario` em `app/models/usuario.py` com atributos `nome`, `email`, `senha`.
  - Adicione um método `__init__` para inicializar esses atributos.

- [ ] **Implementar Classe `Conta`**
  - Implemente a classe `Conta` em `app/models/conta.py` com atributos `nome_conta`, `saldo_inicial`.
  - Adicione métodos para adicionar transações e calcular o saldo atual.

- [ ] **Implementar Classe `Transacao`**
  - Implemente a classe `Transacao` em `app/models/transacao.py` com atributos `valor`, `data`, `descricao`, `tipo`, `categoria`.
  - Adicione o método `__init__` para inicializar esses atributos.

- [ ] **Implementar Classe `Categoria`**
  - Implemente a classe `Categoria` em `app/models/categoria.py` com o atributo `nome_categoria`.
  - Adicione o método `__init__` para inicializar esse atributo.

- [ ] **Implementar Classe `Relatorio`**
  - Implemente a classe `Relatorio` em `app/models/relatorio.py` com atributos `periodo_inicial`, `periodo_final`.
  - Adicione métodos para gerar relatórios com base nas transações.

## Task 3: Implementação dos Controladores

- [ ] **Implementar `UsuarioController`**
  - Em `app/controllers/usuario_controller.py`, implemente métodos para criar usuários e autenticar usuários utilizando a classe `Usuario` do modelo.

- [ ] **Implementar `ContaController`**
  - Em `app/controllers/conta_controller.py`, implemente métodos para criar contas e adicionar transações utilizando as classes `Conta` e `Transacao` dos modelos.

- [ ] **Implementar `TransacaoController`**
  - Em `app/controllers/transacao_controller.py`, implemente métodos para criar transações utilizando as classes `Transacao` e `Categoria` dos modelos.

## Task 4: Implementação das Views

- [ ] **Implementar `UsuarioView`**
  - Em `app/views/usuario_view.py`, implemente métodos para capturar os dados do usuário (ex: formulário ou linha de comando) e para mostrar detalhes do usuário.

- [ ] **Implementar `ContaView`**
  - Em `app/views/conta_view.py`, implemente métodos para capturar os dados da conta e para mostrar detalhes da conta.

- [ ] **Implementar `TransacaoView`**
  - Em `app/views/transacao_view.py`, implemente métodos para capturar os dados da transação e para mostrar detalhes da transação.

## Task 5: Testes Unitários

- [ ] **Escrever Testes para `Usuario`**
  - Em `tests/test_usuario.py`, escreva testes para verificar a criação de usuários e a autenticação, utilizando a classe `Usuario` e `UsuarioController`.

- [ ] **Escrever Testes para `Conta`**
  - Em `tests/test_conta.py`, escreva testes para verificar a criação de contas e adição de transações, utilizando as classes `Conta` e `ContaController`.

- [ ] **Escrever Testes para `Transacao`**
  - Em `tests/test_transacao.py`, escreva testes para verificar a criação de transações, utilizando as classes `Transacao` e `TransacaoController`.

- [ ] **Escrever Testes para `Relatorio`**
  - Em `tests/test_relatorio.py`, escreva testes para verificar a geração de relatórios, utilizando a classe `Relatorio`.

## Task 6: Integração no `main.py`

- [ ] **Integração dos Controladores com as Views**
  - No `main.py`, use os controladores (`controllers`) e as views (`views`) para criar um fluxo de execução básico, onde:
    - O usuário é criado e autenticado.
    - Contas são criadas e transações são adicionadas.
    - Detalhes das transações e contas são exibidos.
    - Relatórios são gerados e exibidos.

## Task 7: Refatoração e Revisão

- [ ] **Refatoração**
  - Refatore o código conforme necessário para melhorar a clareza, a eficiência, e a modularidade.

- [ ] **Revisão dos Testes**
  - Revise e execute todos os testes para garantir que o sistema está funcionando conforme o esperado.
