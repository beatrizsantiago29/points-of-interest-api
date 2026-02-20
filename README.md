# 🗺️ Points of Interest API (Desafio GPS)

API REST desenvolvida para gerenciar e pesquisar **Pontos de Interesse (POIs)** baseados em coordenadas GPS em um plano bidimensional. O projeto foi desenvolvido como solução para o desafio de backend [Pontos de Interesse por GPS](https://github.com/backend-br/desafios/blob/master/points-of-interest/PROBLEM.md).

## 🚀 Tecnologias Utilizadas

* **Python 3.11.9**
* **FastAPI** (Framework web)
* **Uvicorn** (Servidor ASGI)
* **SQLite** (Banco de dados relacional leve)
* **SQLAlchemy** (ORM para persistência de dados)

## 🛠️ Como Instalar e Rodar

1. Clone o repositório e entre na pasta.
2. Crie o ambiente virtual e ative-o: 
    ```
    python -m venv .venv 
    .venv\Scripts\activate
    ```
3. Instale as dependências: `pip install -r requirements.txt`
4. Prepare o banco de dados (Alembic): `alembic upgrade head`
5. Execute a API: `uvicorn main:app --reload`
6. **Acesse a documentação:**
   Acesse http://127.0.0.1:8000/docs para testar os endpoints interativamente via **Swagger UI**.

## 📍 Endpoints Principais

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| **GET** | /poi | Lista todos os POIs cadastrados. |
| **POST** | /poi/cadastrar-ponto | Cadastra um novo ponto de interesse. |
| **POST** | /poi/listar-proximos | Busca POIs por proximidade (necessário: x, y, dmax). |