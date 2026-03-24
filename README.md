# 🗺️ Points of Interest API (Desafio GPS)

API REST desenvolvida para gerenciar e pesquisar **Pontos de Interesse (POIs)** baseados em coordenadas GPS em um plano bidimensional. O projeto foi desenvolvido como solução para o desafio de backend [Pontos de Interesse por GPS](https://github.com/backend-br/desafios/blob/master/points-of-interest/PROBLEM.md).

## 🚀 Tecnologias Utilizadas

* **Python 3.11.9**
* **FastAPI** (Framework web)
* **Uvicorn** (Servidor ASGI)
* **SQLite** (Banco de dados relacional leve)
* **SQLAlchemy** (ORM para persistência de dados)

## 📋 Descrição do problema

O desafio proposto consiste em gerenciar Pontos de Interesse (POIs) para um serviço de localização GPS. O sistema deve ser capaz de:
1. **Cadastrar** novos pontos com nome e coordenadas (X, Y) não negativas.
2. **Listar** todos os pontos cadastrados.
3. **Buscar por Proximidade**: Dado um ponto de referência (X, Y) e uma distância máxima (dmax), o sistema deve retornar todos os POIs que estejam dentro dessa distância.

## 💡 Solução

A solução foi desenvolvida utilizando o framework **FastAPI** e o banco de dados **SQLite**, pela sua praticidade em ambientes de desenvolvimento, mapeado através do **SQLAlchemy (ORM)**. Para controle de versões e migrações foi implementado o **Alembic**, que garante integridade do esquema do banco e permite evoluções futuras.

### 📐 Busca por Proximidade
Essa solução consiste no cálculo da **Distância Euclidiana**. Para cada busca, a API processa as coordenadas armazenadas e aplica a fórmula matemática:

<div align="center">
    
$d = \sqrt{(xPoi - xRef)^2 + (yPoi - yRef)^2}$
    
</div>


Apenas os registros onde **d ≤ dmax** são retornados, garantindo precisão na busca em um plano bidimensional, conforme solicitado pelo desafio.

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
| **GET** | /poi/procurar-proximos | Busca POIs por proximidade (necessário: x, y, dmax). |
| **POST** | /poi/cadastrar-ponto | Cadastra um novo ponto de interesse. |
| **DELETE** | /poi/{id_ponto} | Apaga um ponto de interesse (necessário: id). |