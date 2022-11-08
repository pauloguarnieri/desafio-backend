#### Quiz API

> API de gerenciamento de quiz, contando com cadastro de usuarios (players e admins), categorias especificas e sistema de rankeamento de jogadores.

## Ferramentas de gerenciamento de projeto utilizadas

#

| Ferramenta | Link                      |
| ---------- | ------------------------- |
| GitHub     | https://github.com/       |
| Diagrams   | https://app.diagrams.net/ |
| Trello     | https://trello.com/       |

##  Diagrama ER


Diagrama ER da API definindo bem as relações entre as tabelas do banco de dados.

  * o diagrama se encontra na pasta raiz do projeto (DER.jpg)


##  Autenticação

Django Rest Token Authentication.

##  Endpoints

- Accounts
  - POST - api/accounts/player/register/  (registro de player)
  - POST - api/accounts/admin/register/  (registro de admin)
- Accounts - Login
  - POST - api/accounts/login/ (login)
- Categorys
  - GET - api/categories/ (lista categorias existentes)
- Questions
  - POST - api/questions/ (registra uma nova question)
- QUIZ
  - POST - api/quiz/ (recebe um novo quiz)