# TheBot
Um Bot que meio que faz um monte de coisas basicamente inúteis, porém possivelmente interessantes.

O bot atualmente está hosteado no Heroku, utilizando webhooks para se comunicar com a API do Telegram.

Para guardar os dados necessários é utilizado o addon "Heroku Postgres"

## Como Configurar
No heroku é preciso colocar essas variáveis de ambiente.

- `ADMIN ID` - do Telegram dos usuários com permissão para executar todos os comandos (separados por vírgula).

- `DATABASE_URL` - URL do banco de dados (se usar o addon nele tem lá essa URL)

- `HEROKU_LINK` - O link do webapp do Heroku (usado pra setar o webhook)

- `TOKEN` - O token do Bot do Telegram

## Funcionalidades Disponíveis

- `/doge` - Envia uma imagem aleatória de um cachorro🐶
- `/cat` - Envia uma imagem aleatória de um gato😺
- `/birb` - Envia uma imagem aleatória de um pássaro🐦
- `/sabedoria (pergunta)?` - Recebe uma resposta muito sábia🧠
- `/rolld20` - Rola um d20🎲
- `/dolar` - Envia a cotação do dolar e uma imagem do pokemon de número equivalente💸
- `/alcoolgel` - Precauções para evitar o espalhamento do víruos COVID-19🦠

<hr>

<sub><p align="center"> Made with ❤️ by andrecoco </p></sub>
