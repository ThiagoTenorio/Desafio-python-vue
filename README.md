# Django REST API para Processamento de Arquivos CSV

Esta é uma API construída com Django REST Framework que lê dados de um arquivo CSV, armazena as informações em um banco de dados PostgreSQL e disponibiliza os dados através de um endpoint.

## Funcionalidades

- Carregamento de dados de um arquivo CSV localizado na raiz do projeto.
- Armazenamento de três colunas (col1, col2, col3) no banco de dados PostgreSQL.
- Endpoint para acessar os dados armazenados.

## Requisitos

- Python 3.x
- PostgreSQL
- Django
- Django REST Framework

## Passos para Execução

### Primeiro Passo - Clonar o Repositório

Clone o repositório para sua máquina local utilizando o seguinte comando:

```bash
git clone https://github.com/ThiagoTenorio/Desafio-python-vue.git
```

### Segundo Passo - Criar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **No Windows:**

```bash
venv\Scripts\activate
```

- **No macOS/Linux:**

```bash
source venv/bin/activate
```

### Terceiro Passo - Instalar as Dependências

Instale as dependências do projeto a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Quarto Passo - Navegar até o Diretório do App

Acesse o diretório onde está localizado o projeto:

```bash
cd extration
```

### Quinto Passo - Executar o Servidor

Inicie o servidor Django com o seguinte comando:

```bash
python manage.py runserver
```

## Como Usar

1. **Carregar o Arquivo CSV:**
   Envie uma requisição POST para o endpoint `http://localhost:8000/api/data-excel/` para processar o arquivo CSV. O arquivo CSV deve estar localizado na raiz do projeto.

2. **Listar os Dados:**
   Acesse o endpoint `http://localhost:8000/api/data-excel/list/` para visualizar os dados armazenados no banco de dados.

## Estrutura do Projeto

```plaintext
myproject/
│
├── data/                 # App que processa o CSV
│   ├── migrations/       # Migrações do banco de dados
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Modelos do banco de dados
│   ├── serializers.py    # Serializers para a API
│   ├── tests.py
│   └── views.py         # Views da API
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py       # Configurações do projeto
│   ├── urls.py           # URLs do projeto
│   └── wsgi.py
│
├── manage.py             # Script para gerenciar o projeto
└── requirements.txt      # Dependências do projeto
```
