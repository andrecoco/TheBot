import json
import requests
import time
import random
import re
import math
import AuxiliaryFunctions as auxf
import db
import os
from Pymoe import Anilist
import florto

from telegram import InlineQueryResultGif, InputTextMessageContent, InlineQueryResultPhoto

def db_test(update, context):
    if(auxf.check_admin(update.message.from_user.id)):
        update.message.reply_text(db.test())
    else:
        update.message.reply_text("Você não tem permissão para executar esse comando.")

def db_printa_msgs(update, context):
    if(auxf.check_admin(update.message.from_user.id)):
        update.message.reply_text(db.printa_mensagens())
    else:
        update.message.reply_text("Você não tem permissão para executar esse comando.")

def db_insere_msg(update, context):
    db.insere_mensagem(update)

def db_restart(update, context):
    if(auxf.check_admin(update.message.from_user.id)):
        update.message.reply_text("Setting Up DB...")
        db.setup()
    else:
        update.message.reply_text("Você não tem permissão para executar esse comando.")

def db_clear_resumo(update, context):
    if(auxf.check_admin(update.message.from_user.id)):
        update.message.reply_text("Limpando Resumo...")
        db.limpa_resumo()
    else:
        update.message.reply_text("Você não tem permissão para executar esse comando.")

def insert_transparent_image(update, context):
    if(auxf.check_admin(update.message.from_user.id)):
        if(update.message.reply_to_message is None):
            print("Dê reply em uma imagem pls!")
            return
        name = update.message.text
        if(name is None):
            update.message.reply_text("Manda o nome da imagem aí irmão.")
            return
        db.insere_img_transparente(update)
    else:
        update.message.reply_text("Você não tem permissão para executar esse comando.")

# Test function
def get_transparent_image(update, context):
    if(auxf.check_admin(update.message.from_user.id)):
        name = update.message.text.replace('/get_ti', '').strip()
        fileid = db.get_transparent_image(name)
        print("File id: ", fileid, str(fileid))
        update.message.reply_document(document=str(fileid), quote=True)
    else:
        update.message.reply_text("Você não tem permissão para executar esse comando.")

def merge_transparent_image(update, context):
    if(auxf.check_admin(update.message.from_user.id) or auxf.is_private_chat(update)):
        media = update.message.reply_to_message.photo
        if(media is not None and len(media) > 0):
            media = media[-1].file_id
        else:
            print("De reply numa foto!")
            return
        florto.paste_image(media, context)
        image = open('./res/new.png', 'rb')
        print(os.system('file ./res/front'))
        print(os.system('file ./res/back'))
        update.message.reply_photo(photo=image)
        florto.clear()
    else:
        update.message.reply_text("Você não tem permissão para executar esse comando.")

def anime_recomendation(update, context):
    instance = Anilist()
    texto = update.message.text.strip().replace('/anime', '')
    if(len(texto) > 0):
        results = instance.search.anime(texto)
        animes = results['data']['Page']['media']
        anime = auxf.retiraLista(animes)
        
        #NSFW Filter
        
        if(anime['isAdult']):
            Ok = False
            for anime in animes:
                if(not anime['isAdult']):
                    Ok = True
                    break
            if(not Ok):
                update.message.reply_text("Só veio +18, procure outra coisa pls")
                return

        media_link = anime['coverImage']['large']
        text = anime['title']['romaji']
        update.message.reply_photo(photo=media_link, quote=True, caption=text)
    else:
        update.message.reply_text("Digite algum termo pls\ngetanime *termo*")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Opa, eae? (eu so mandei essa mensagem por educacao, eu ainda nao sei conversar)")

def barbixas(update, context):
    arquivo = open('videosBarbixas.json', encoding='utf-8')
    lista = json.load(arquivo)["videos"]
    index = random.randrange(0, 502) #GERA NUMERO 0-501
    #titulo = lista[index]["titulo"]
    link = "https://www.youtube.com/watch?v=" + lista[index]["id"]
    update.message.reply_text(link)
    
def resumo(update, context):
    try:
        text, media_id = db.resumo(update.message.chat.id)
        if(media_id is None):
            update.message.reply_text(text)
        else:
            update.message.reply_photo(photo=media_id, quote=True, caption=text)
    except Exception as error :
        print("Error during Commands.resumo() function" +  str(error))

def meme_generator(update, context):
    query = update.inline_query.query

    if(len(query) == 0):
        return

    #get args
    memeIDs = {
        #"1":112126428, #Distracted Boyfriend
        "1":129242436,  #Change my mind
        "2":87743020,   #Two Buttons
        "3":100777631,  #Is this a pidgeon
        "4":61579,      #One does not simply
        "5":155067746,  #Surprised Pikachu
        "6":89853322, #Obama Medal
    }
    args = [s.strip() for s in query.split("\n")]
    
    #print(args)
    
    if(args[-1] != '!'):
        return
    
    #user needs to pass at least 4 args (ID, upper text, bottom text, !)
    if(len(args) < 3):
        results = ""
        return

    ID = memeIDs.get(args[0], "-1")
    if(ID == -1):
        return
    
    #print(ID)
    if(args[2] == "!"):
        args[2] = ""

    data = {
        "template_id" : ID,
        "username" : "bot_memeGen",
        "password" : "qE^1h13Qi$VHUNO4",
        "text0" : args[1],
        "text1" : args[2]
    }
    req = requests.post("https://api.imgflip.com/caption_image", data = data)
    print("Meme_Gen - " + str(req))
    info = req.json()
    print(info)
    if(info["success"] == "False"):
        print("failure in meme_gen")

    url = info["data"]["url"]
    print(url)
    
    results = [
        InlineQueryResultPhoto(
            id = 0,
            photo_url=url,
            thumb_url=url)
    ]

    update.inline_query.answer(results)

def shame(update, context):
    txt = "vergonha (shilap) vergonha (plim plim plim) vergonha (shilap)"
    
    update.message.delete() #apaga o comando, pra ficar mais clean
    
    if(update.message.reply_to_message != None):
        idMessageReplied = update.message.reply_to_message.message_id    
        update.message.reply_text(txt, reply_to_message_id=idMessageReplied)
    else:
        update.message.reply_text(txt, quote=False)

def inline_function(update, context):
    query = update.inline_query.query

    if(len(query) == 0):
        return

    links = list()
    if("hug" in query):
        title = "hug"
        links.append(str(getGifLink("hug")))
        links.append(str(getGifLink("hug")))
        links.append(str(getGifLink("hug")))
        links.append(str(getGifLink("hug")))
    elif("wink" in query):
        title = "wink"
        links.append(str(getGifLink("wink")))
        links.append(str(getGifLink("wink")))
        links.append(str(getGifLink("wink")))
        links.append(str(getGifLink("wink")))
    elif("pat" in query):
        title = "pat"
        links.append(str(getGifLink("pat")))
        links.append(str(getGifLink("pat")))
        links.append(str(getGifLink("pat")))
        links.append(str(getGifLink("pat")))
    else:
        return

    results = list()
    
    results.append(
        InlineQueryResultGif(
            id=0,
            title=title,
            caption=title,
            gif_url=links[0],
            thumb_url=links[0]
        )
    )
    
    results.append(
        InlineQueryResultGif(
            id=1,
            title=title,
            caption=title,
            gif_url=links[1],
            thumb_url=links[1]
        )
    )
    
    results.append(
        InlineQueryResultGif(
            id=2,
            title=title,
            caption=title,
            gif_url=links[2],
            thumb_url=links[2]
        )
    )

    results.append(
        InlineQueryResultGif(
            id=3,
            title=title,
            caption=title,
            gif_url=links[3],
            thumb_url=links[3]
        )
    )
    update.inline_query.answer(results, cache_time=1)

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
    text = update.message.text
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
    #check if the user replied to some message
    if(update.message.reply_to_message != None):
        idUserReplied = update.message.reply_to_message.message_id
        update.message.reply_animation(animation=getGifLink("hug"), reply_to_message_id=idUserReplied)
    else:
        update.message.reply_animation(animation=getGifLink("hug"), quote=True)

def wink(update, context):
    #check if the user replied to some message
    if(update.message.reply_to_message != None):
        idUserReplied = update.message.reply_to_message.message_id
        update.message.reply_animation(animation=getGifLink("wink"), reply_to_message_id=idUserReplied)
    else:
        update.message.reply_animation(animation=getGifLink("wink"), quote=True)

def pat(update, context):
    #check if the user replied to some message
    if(update.message.reply_to_message != None):
        idUserReplied = update.message.reply_to_message.message_id
        update.message.reply_animation(animation=getGifLink("pat"), reply_to_message_id=idUserReplied)
    else:
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
    randomNumber = random.randrange(0, 51) #GERA NUMERO 0 - 50
    if(randomNumber == 35):
        msgs.append("...")
    else:
        msgs.append("POOOOOWW")
    
    #Envia os 'pras'
    for i in range(numMsgs):
        update.message.reply_text(msgs[i], quote=False)

    #Envia o POW ou '...'
    s = random.randrange(1, 5) #GERA NUMERO 1 - 4
    time.sleep(s)
    update.message.reply_text(msgs[len(msgs) - 1], quote=False)

def weather(update, context):
    #https://rapidapi.com/community/api/open-weather-map
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    city = "Aracruz" + ",br"
    querystring = {"id":"2172797","lang":"pt","units":"metric","mode":"xml%2C html","q":city}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "a60147ee0amshb90cc40b579f78ap1b711ejsn3a0fec8b9f69"
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    desc = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    t_max = response["main"]["temp_min"]
    t_min = response["main"]["temp_max"]
    local = response["name"]
    print(local)
    print(str(desc).title())
    print("Temperatura - " + str(temp))
    print("Minima - " + str(t_min) + " Maxima - " + str(t_max))

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
