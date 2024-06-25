# Aplicativo Clientes - Desafio Desenvolvedor Python

## LIGO - Laboratório de Inovação de Goiás

## Autor
Walyson Maxwel Dias Leite
### Descrição

Este projeto é um aplicativo de gerenciamento de clientes desenvolvido como parte do desafio para desenvolvedores Python. O aplicativo é composto por dois módulos principais:

1. **Módulo Cadastro de Clientes**: Desenvolvido com Flask, permite o cadastro de clientes com nome completo, endereço (URL) e e-mail do responsável. Após a inclusão do cliente, são gerados um ID de cliente, um segredo do cliente e a data de inclusão. Os dados são persistidos em um banco de dados PostgreSQL e podem ser recuperados e exibidos. Além disso, há uma opção para gerar um JWT para o cliente.

2. **Módulo JWT**: Desenvolvido com FastAPI, é um serviço REST que recebe os dados do cliente como parâmetro e retorna um JWT contendo esses dados.

### Configuração e Execução

#### Pré-requisitos

- Docker
- Docker Compose

#### Passos para Configuração e Execução

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/walysonmaxwel/ligo-clientes
   cd ligo-clientes

2. **Configure os arquivos .env:**

Crie os arquivos .env nas pastas flask_crud_clients e fastapi_jwt copiando o conteúdo do .env.example:

3. **Construa e inicie os containers:**
```
docker compose up --build
```

4. **Acesse os serviços:**

- O módulo Flask estará disponível em: http://localhost:5000
- O módulo FastAPI estará disponível em: http://localhost:8000


5. **Estrutura do Código:**

Flask
- migrations: Lógica de migration da tabela do banco de dados pgsql
- src/__init__.py: Configura a aplicação Flask, inicializa extensões e define a criação do banco de dados.
- src/routes.py: Define as rotas para criação de usuário e jwt
- models.py: Define o modelo de cliente para o banco de dados.

FastAPI
- src/main.py: Configura a aplicação FastAPI e inclui as rotas.
- src/routes.py: Define a rota para gerar o JWT.
Docker
- docker-compose.yml
- Define os serviços para o PostgreSQL, Flask e FastAPI, incluindo suas dependências e  variáveis de ambiente.
- Dockerfile: Cada módulo (Flask e FastAPI) tem seu próprio Dockerfile que instala as dependências necessárias e configura a execução da aplicação.


### Observações
- HotReload implementado para ambas aplicações
- Foi implementada proteção CSRF na aplicação flask
- Ambiente está dentro de cointainer docker. Ps: o banco possui volume definido, caso queira wipar o banco: docker volume rm ligo-clientes_postgres_data 
- Para simplificar o projeto, o banco de dados não foi normalizado
- Para evitar dificuldades de subida de ambiente, mantive os .envs fora do .gitignore
- Por segurança, mantive client_id e client_secret fora do jwt pois são dados sensíveis que não devem ser expostos