# TheBot
Um Bot que meio que faz um monte de coisas basicamente inúteis, porém possivelmente interessantes.

Acho que o mais fácil é rodar no Heroku, usando webhook.
Eu tô usando o addon "Heroku Postgres", pra guardar as coisas.

## Como Configurar
No heroku é preciso colocar essa variáveis de ambiente.

ADMIN -> ID do Telegram dos usuários com permissão para executar todos os comandos (separados por vírgula).

DATABASE_URL -> URL do banco de dados (se usar o addon nele tem lá essa URL)

HEROKU_LINK -> O link do webapp do Heroku (usado pra setar o webhook)

TOKEN -> O token do Bot do Telegram
