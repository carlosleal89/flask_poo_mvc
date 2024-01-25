# Traduzo

Uma ferramenta de tradução de textos entre vários idiomas, utilizando Python com o Framework Flask, para criar uma aplicação Server Side. Ou seja, o Back-end (pela controller) fornecerá diretamente a camada View, para a pessoa usuária.

## Funcionalidades Principais
- Traduza textos entre os principais idiomas;

## Tecnologias Utilizadas
- **Backend:** Python, Flask e Jinja2;
- **Banco de dados:** MongoDB;
- Google Translate API;


## Como Executar o Projeto:
  **Clone o Repositório:**
  
    git clone git@github.com:carlosleal89/flask_poo_mvc.git

  **Crie o ambiente virtual:**

    python3 -m venv .venv && source .venv/bin/activate

  **Instale as Dependências:**

    python3 -m pip install -r dev-requirements.txt

## Docker
- Caso não tenha o Docker instalado em seu sistema, acesse https://www.docker.com/get-started/
  
  1. **Execute o banco e Flask pelo Docker Compose:**
     
         docker compose up translate

  2. **Popule o banco com os dados dos idiomas:**

         docker compose exec -it translate python3 src/run_seeds.py

  3. **Acesse o projeto pelo link**
         
         http://127.0.0.1:8000/

## As seguintes habilidades foram praticadas nesse projeto:
- Implementar uma API utilizando arquitetura em camadas MVC;
- Utilizar o Docker para projetos Python;
- Conhecimentos de Orientação a Objetos no desenvolvimento WEB.
- Testes para APIs para garantir a implementação dos endpoints;
- Interagir com um banco de dados não relacional MongoDB;
- Desenvolver páginas web Server Side.
      