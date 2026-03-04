# 🚀 FastAPI do Zero - Task Manager API

Este projeto é uma API de gerenciamento de tarefas desenvolvida durante o curso **FastAPI do Zero** do Professor Dunossauro (Eduardo Mendes). O foco foi aplicar as melhores práticas de desenvolvimento Back-end com Python moderno.

## 🛠️ Tecnologias e Ferramentas

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Assíncrono)
* **Validação:** Pydantic v2
* **Banco de Dados:** SQLAlchemy com SQLite
* **Migrações:** Alembic
* **Testes:** Pytest
* **Segurança:** JWT (JSON Web Tokens)

---

## 🧠 Aprendizados Chave

Neste repositório, apliquei conceitos essenciais para o mercado:

* **TDD (Test Driven Development):** Desenvolvimento orientado a testes
* **Clean Code:** Código organizado seguindo a PEP8 e tipagem estática
* **Injeção de Dependências:** Uso avançado do `Depends` para modularidade

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/NOME-DO-REPO.git
```

### 2. Instale as dependências (recomendado usar `poetry` ou `pip`)

```bash
pip install -r requirements.txt
```

### 3. Execute as migrações do banco

```bash
alembic upgrade head
```

### 4. Inicie o servidor

```bash
fastapi dev fast_zero/app.py
```

### 5. Acesse a documentação interativa

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🎓 Créditos

Projeto desenvolvido seguindo a metodologia do **Professor Dunossauro** no curso [FastAPI do Zero](https://github.com/dunossauro/fastapi-do-zero).

Um agradecimento especial ao mestre Eduardo Mendes pela excelente didática e por fortalecer a comunidade Python no Brasil.

---

Desenvolvido por **Matheus** – [Meu LinkedIn](https://www.linkedin.com/in/matheus-goveia)

