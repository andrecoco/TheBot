import json
import requests
import time
#https://docs.python.org/3/library/random.html
import random
import re
import math
import AuxiliaryFunctions as auxf

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Opa, eae? (eu so mandei essa mensagem por educacao, eu ainda nao sei conversar)")

def dorimetor(update, context):
    dicionario = {
            'A' : 'Do',
            'B' : 'Ri',
            'C' : 'Me',
            'D' : 'In',
            'E' : 'Te',
            'F' : 'Ri',
            'G' : 'Mo',
            'H' : 'Ada',
            'I' : 'Pa',
            'J' : 'Re',
            'K' : 'La',
            'L' : 'Ti',
            'M' : 'Re',
            'N' : 'La',
            'O' : 'Ti',
            'P' : 'Re',
            'Q' : 'Mo',
            'R' : 'Do',
            'S' : 'Ri',
            'T' : 'Me',
            'U' : 'A',
            'V' : 'Me',
            'W' : 'No',
            'X' : 'O',
            'Y' : 'Me',
            'Z' : 'Nare',
            'a' : 'do',
            'b' : 'ri',
            'c' : 'me',
            'd' : 'in',
            'e' : 'te',
            'f' : 'ri',
            'g' : 'mo',
            'h' : 'ada',
            'i' : 'pa',
            'j' : 're',
            'k' : 'la',
            'l' : 'ti',
            'm' : 're',
            'n' : 'la',
            'o' : 'ti',
            'p' : 're',
            'q' : 'mo',
            'r' : 'do',
            's' : 'ri',
            't' : 'me',
            'u' : 'a',
            'v' : 'me',
            'w' : 'no',
            'x' : 'o',
            'y' : 'me',
            'z' : 'nare',
            ' ' : ' '
    }
    saida = ""
    for i in range(len(text)):
        if(text[i] == '/'):
            break
        if(text[i] in dicionario):
            saida += dicionario.get(str(text[i]))
        else:
            saida += text[i]
    update.message.reply_text(mensagem, quote=True)

def dorimes(update, context):
    return
    update.message.reply_photo(photo='https://imgur.com/IaP4h8q', quote=False)

def rolld20(update, context):
        num = random.randrange(1, 21) #GERA NUMERO 1-20
        update.message.reply_text(num, quote=True)

def triste(update, context):
    num = random.randrange(0, 11) #GERA NUMERO 0 e 10
    if(num < 5):
        url = get_doge_image_url()
        text = "Poxa... Fica triste nao, olha a foto desse cachorro!"
    elif(num > 5):
        url = get_cat_image_url()
        text = "Poxa... Fica triste nao, olha a foto desse gato!"
    else:
        url = get_birb_image_url()
        text = "Poxa... Fica triste nao, olha a foto desse birb!"
    update.message.reply_photo(photo=url, quote=True, caption=text)

def doge(update, context):
    print(update.message.text)
    update.message.reply_photo(photo=get_doge_image_url(), quote=False)

def cat(update, context):
    update.message.reply_photo(photo=get_cat_image_url(), quote=False)

def birb(update, context):
    update.message.reply_photo(photo=get_birb_image_url(), quote=False)

def pokeDolar(update, context):
    #CONECTA NA API
    try:
        moeda = requests.get('https://api.hgbrasil.com/finance').json()
    except Exception as e:
        print(e)
        return

    #PEGA O VALOR
    valores = auxf.extract_values(moeda, "buy")
    cotacao = valores[0]
    num = math.floor(cotacao*100)
    print(num)

    #PEGA O POKEMON
    try:
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-form/' + str(num)).json()
    except Exception as e:
        print(e)
        return
    
    #PEGA IMAGEM E NOME
    rand = random.randrange(0, 21) #GERA NUMERO 0 - 20
    if(rand == 15): #VER SE PEGA O SHINY
        url = auxf.extract_values(pokemon, "front_shiny")[0]
        nome = "Shiny " + auxf.extract_values(pokemon, "name")[0]
    else:
        url = auxf.extract_values(pokemon, "front_default")[0]
        nome = auxf.extract_values(pokemon, "name")[0]
    
    print(nome)
    print(url)
    
    texto = nome.title() + "\nDólar R$" + str(num/100)
    update.message.reply_photo(photo=url, quote=False, caption = texto)

def euro(update, context):
    try:
        moeda = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL').json()
    except Exception as e:
        print(e)
        return

    alta = auxf.extract_values(moeda, 'high')
    baixa = auxf.extract_values(moeda, 'low')
    nome = auxf.extract_values(moeda, 'name')
    texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
    update.message.reply_text(texto, quote=False)

def libra(update, context):
    try:
        moeda = requests.get('https://economia.awesomeapi.com.br/all/GBP-BRL').json()
    except Exception as e:
        print(e)
        return

    alta = auxf.extract_values(moeda, 'high')
    baixa = auxf.extract_values(moeda, 'low')
    nome = auxf.extract_values(moeda, 'name')
    texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
    update.message.reply_text(texto, quote=False)

def iene(update, context):
    try:
        moeda = requests.get('https://economia.awesomeapi.com.br/all/JPY-BRL').json()
    except Exception as e:
        print(e)
        return

    alta = auxf.extract_values(moeda, 'high')
    baixa = auxf.extract_values(moeda, 'low')
    nome = auxf.extract_values(moeda, 'name')
    texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
    update.message.reply_text(texto, quote=False)

def bitcoin(update, context):
    try:
        moeda = requests.get('https://economia.awesomeapi.com.br/all/BTC-BRL').json()
    except Exception as e:
        print(e)
        return

    alta = auxf.extract_values(moeda, 'high')
    baixa = auxf.extract_values(moeda, 'low')
    nome = auxf.extract_values(moeda, 'name')
    texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
    update.message.reply_text(texto, quote=False)

def litecoin(update, context):
    try:
        moeda = requests.get('https://economia.awesomeapi.com.br/all/LTC-BRL').json()
    except Exception as e:
        print(e)
        return

    alta = auxf.extract_values(moeda, 'high')
    baixa = auxf.extract_values(moeda, 'low')
    nome = auxf.extract_values(moeda, 'name')
    texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
    update.message.reply_text(texto, quote=False)

def ethereum(update, context):
    try:
        moeda = requests.get('https://economia.awesomeapi.com.br/all/ETH-BRL').json()
    except Exception as e:
        print(e)
        return

    alta = auxf.extract_values(moeda, 'high')
    baixa = auxf.extract_values(moeda, 'low')
    nome = auxf.extract_values(moeda, 'name')
    texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
    update.message.reply_text(texto, quote=False)

def charada(update, context):
    url = 'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria'
    headers = {'Accept': 'application/json'}
    r = requests.post(url, headers=headers)
    print(r)

    dados = r.json()
    pergunta = dados['pergunta'] 
    resposta = dados['resposta']
    tudoJunto = pergunta + '\n' + resposta
    update.message.reply_text(tudoJunto, quote=False)

def hug(update, context):
    update.message.reply_animation(animation=getGifLink("hug"), quote=True)

def wink(update, context):
    update.message.reply_animation(animation=getGifLink("wink"), quote=True)

def pat(update, context):
    update.message.reply_animation(animation=getGifLink("pat"), quote=True)

def meme(update, context):
    if(True): #DISABLED COMMAND - TA DANDO ERRO
        return
    meme = getMeme();
    image = meme['image']
    caption = meme['caption']
    update.message.reply_photo(photo=image, quote=False, caption=caption)

def sabedoria(update, context):
    listaRespostas = ["Difícil dizer....", "Não tenho certeza", "Depende de como você olha né...", "Sim", "Não", "Claro que não!", "Claro!", "Com certeza", "Sei não ein..."]
    #VERIFICA SE TEM PERGUNTA
    if("?" not in update.message.text):
        resposta = "Por favor me faça uma pergunta na mesma mensagem do comando... ( perguntas sao aquelas frases que tem '?')"
    else:
        resposta = auxf.retiraLista(listaRespostas);

    update.message.reply_text(resposta, quote=True)

def sadanimesong(update, context):
    with open('animeSadSongs.json', encoding="utf8") as j:
        listaMusicas = json.load(j)["songs"]
    size = len(listaMusicas)
    
    #faz um rand
    rand = random.randrange(0, size) #GERA NUMERO 0 - (size-1)
    nome = listaMusicas[rand]["name"]
    link = listaMusicas[rand]["link"]
    resposta = nome + '\n' + link 
    update.message.reply_text(resposta, quote=False)

def acende(update, context):
    numMsgs = random.randrange(2, 7) #GERA NUMERO 2 - 6
    msgs = []
    #Gera as msgs com o 'pra'
    for i in range (numMsgs):
        numPras = random.randrange(1, 7) #GERA NUMERO 1 - 6
        msgs.append("pra "*numPras)

    #Ve se mascou ou n
    randomNumber = random.randrange(2, 7) #GERA NUMERO 0 - 50
    if(randomNumber == 35):
        msgs.append("...")
    else:
        msgs.append("POOOOOWW")
    
    #Envia os 'pras'
    for i in range(numMsgs):
        update.message.reply_text(msgs[i], quote=False)
        break

    #Envia o POW ou '...'
    s = random.randrange(1, 5) #GERA NUMERO 1 - 4
    time.sleep(s)
    update.message.reply_text(msgs[len(msgs) - 1], quote=False)


######### FUNCOES AUXILIARES ###########
#RETORNA UMA URL DE UMA FOTO DE GATO
def get_cat_image_url():
	allowed_extension = ['jpg','jpeg','png']
	file_extension = '' 
	while file_extension not in allowed_extension:
		#contents = requests.get('http://aws.random.cat/meow').json()
		#url = contents['file']
		try:
			contents = requests.get('https://api.thecatapi.com/v1/images/search?').json()
		except Exception as e:
			print("Erro ao conseguir URL do cat!")
			return 'https://www.daviferreira.com/assets/blog/canvas-4.jpg'
		url = auxf.extract_values(contents, 'url')[0]
		file_extension = re.search("([^.]*)$",url).group(1).lower()
	return url

#RETORNA UMA URL DE UMA FOTO DE CACHORRO
def get_doge_image_url():
	allowed_extension = ['jpg','jpeg','png']
	file_extension = '' 
	while file_extension not in allowed_extension:
		try:
			contents = requests.get('https://random.dog/woof.json').json()
		except Exception as e:
			print("Erro ao conseguir URL do doge!")
			return 'https://images.pexels.com/photos/1851164/pexels-photo-1851164.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
		url = contents['url']
		file_extension = re.search("([^.]*)$",url).group(1).lower()
	return url

#RETORNA UMA URL DE UMA FOTO DE UM PASSARO
def get_birb_image_url():
	allowed_extension = ['jpg','jpeg','png']
	file_extension = '' 
	while file_extension not in allowed_extension:
		try:
			contents = requests.get('https://some-random-api.ml/img/birb').json()
		except Exception as e:
			print("Erro ao conseguir URL do doge!")
			return 'https://www.google.com.br/url?sa=i&url=https%3A%2F%2Fnl.pinterest.com%2Fpin%2F794463190487111091%2F&psig=AOvVaw0nP8Ox7Gi0zHitacdeUj2j&ust=1584747601061000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCID2g4Pbp-gCFQAAAAAdAAAAABAD'
		url = contents['link']
		file_extension = re.search("([^.]*)$",url).group(1).lower()
	return url

#retorna a url do gif
def getGifLink(type):
	url = 'https://some-random-api.ml/animu/' + type
	try:
		dados = requests.get(url).json()
	except Exception as e:
		print("Erro ao conseguir gif URL!")
		return 'https://media.tenor.com/images/53a6d2a0e9de9c45cf5391ac749cc6e8/tenor.gif'
	link = dados['link']
	return link

#Retorno um json com um meme
def getMeme():
	url = 'https://some-random-api.ml/meme'
	r = requests.get(url)
	return r.json()