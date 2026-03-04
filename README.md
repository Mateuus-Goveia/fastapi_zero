```markdown
# 🚀 FastAPI do Zero - Task Manager API

Este projeto é uma API robusta de gerenciamento de tarefas, desenvolvida durante o curso **FastAPI do Zero** do
**Professor Dunossauro (Eduardo Mendes)**. O foco principal foi aplicar as melhores práticas de desenvolvimento
 Back-end com Python moderno.

## 🛠️ Tecnologias e Ferramentas
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Assíncrono)
* **Validação/Schemas:** Pydantic v2
* **Banco de Dados:** SQLite (Desenvolvimento) com SQLAlchemy (ORM)
* **Migrações:** Alembic
* **Testes Automatizados:** Pytest (Cobertura de código)
* **Segurança:** Autenticação JWT (JSON Web Tokens) e Passlib
* **Ambiente:** Taskipy (Automação de tarefas) e Docker

## 🧠 Aprendizados Chave
Neste repositório, demonstro o domínio de conceitos essenciais para o mercado:
- **TDD (Test Driven Development):** Criação de testes antes da implementação das rotas.
- **Clean Code:** Organização de código seguindo PEP8 e tipagem estática.
- **CRUD Completo:** Operações assíncronas de criação, leitura, atualização e deleção.
- **Gestão de Dependências:** Uso avançado de `Depends` do FastAPI para injeção de dependências.

## 🚀 Como executar o projeto
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/fastapi-do-zero.git](https://github.com/seu-usuario/fastapi-do-zero.git)

```

2. Instale as dependências (recomendado usar `poetry` ou `pip`):
```bash
pip install -r requirements.txt

```


3. Execute as migrações do banco:
```bash
alembic upgrade head

```


4. Inicie o servidor:
```bash
fastapi dev fast_zero/app.py

```


5. Acesse a documentação interativa em: `http://127.0.0.1:8000/docs`

## 🎓 Créditos

Projeto desenvolvido seguindo a metodologia do **Professor Dunossauro** no curso [FastAPI do Zero](https://www.google.com/search?q=https://github.com/fastapi-do-zero). 
Um agradecimento especial ao mestre Eduardo Mendes pela excelente didática e por fortalecer a comunidade Python no Brasil.

---

Desenvolvido por **Matheus** – [Meu LinkedIn](www.linkedin.com/in/matheus-goveia)

```
