import json
import requests
import time
#https://docs.python.org/3/library/random.html
import random
import re
import math

#Import modules
import FuncoesAuxiliares as auxf
import FuncoesComunicacao as com

#LIDA COM OS COMANDOS DO BOT
def botCommands(mensagem, text):
	#TODO -> (DEIXAR MAIS ORGANIZADO ISSO, TALVEZ SWITCH-CASE)

	if("dorimetor" in text):
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

		r = com.enviaMensagem(mensagem, saida, True)
		print(r)
		return 

	if("dorimes" in text):
		r = com.enviaImagem(mensagem, 'https://imgur.com/IaP4h8q', False)
		print(r)
		return
	
	if("rolld20" in text):
		num = random.randrange(1, 21) #GERA NUMERO 1-20
		#username = auxf.extract_values(mensagem, 'username')
		r = com.enviaMensagem(mensagem, str(num), True)
		print(r)
		return
	
	if("doge" in text):
		r = com.enviaImagem(mensagem, get_doge_image_url(), False)
		print(r)
		return

	if("cat" in text):
		r = com.enviaImagem(mensagem, get_cat_image_url(), False)
		print(r)
		return

	if("dolar" in text):
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
		
		rand = random.randrange(0, 65) #GERA NUMERO 0 - 64
		if(rand == 32): #VER SE PEGA O SHINY
			url = auxf.extract_values(pokemon, "front_shiny")[0]
		else:
			url = auxf.extract_values(pokemon, "front_default")[0]
		
		nome = auxf.extract_values(pokemon, "name")[0]
		print(nome)
		print(url)

		texto = nome.title() + "\nDólar R$" + str(num/100)
		
		com.enviaImagemCaption(mensagem, url, texto, False)
		return

	if("euro" in text):
		try:
			moeda = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL').json()
		except Exception as e:
			print(e)
			return

		alta = auxf.extract_values(moeda, 'high')
		baixa = auxf.extract_values(moeda, 'low')
		nome = auxf.extract_values(moeda, 'name')
		texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
		com.enviaMensagem(mensagem, texto, False)
		return

	if("libra" in text):
		try:
			moeda = requests.get('https://economia.awesomeapi.com.br/all/GBP-BRL').json()
		except Exception as e:
			print(e)
			return

		alta = auxf.extract_values(moeda, 'high')
		baixa = auxf.extract_values(moeda, 'low')
		nome = auxf.extract_values(moeda, 'name')
		texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
		com.enviaMensagem(mensagem, texto, False)
		return

	if("iene" in text):
		try:
			moeda = requests.get('https://economia.awesomeapi.com.br/all/JPY-BRL').json()
		except Exception as e:
			print(e)
			return

		alta = auxf.extract_values(moeda, 'high')
		baixa = auxf.extract_values(moeda, 'low')
		nome = auxf.extract_values(moeda, 'name')
		texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
		com.enviaMensagem(mensagem, texto, False)
		return

	if("bitcoin" in text):
		try:
			moeda = requests.get('https://economia.awesomeapi.com.br/all/BTC-BRL').json()
		except Exception as e:
			print(e)
			return

		alta = auxf.extract_values(moeda, 'high')
		baixa = auxf.extract_values(moeda, 'low')
		nome = auxf.extract_values(moeda, 'name')
		texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
		com.enviaMensagem(mensagem, texto, False)
		return

	if("litecoin" in text):
		try:
			moeda = requests.get('https://economia.awesomeapi.com.br/all/LTC-BRL').json()
		except Exception as e:
			print(e)
			return

		alta = auxf.extract_values(moeda, 'high')
		baixa = auxf.extract_values(moeda, 'low')
		nome = auxf.extract_values(moeda, 'name')
		texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
		com.enviaMensagem(mensagem, texto, False)
		return

	if("ethereum" in text):
		try:
			moeda = requests.get('https://economia.awesomeapi.com.br/all/ETH-BRL').json()
		except Exception as e:
			print(e)
			return

		alta = auxf.extract_values(moeda, 'high')
		baixa = auxf.extract_values(moeda, 'low')
		nome = auxf.extract_values(moeda, 'name')
		texto = nome[0] + "\nAlta: R$" + str(alta[0]) + "\nBaixa: R$" + str(baixa[0])
		com.enviaMensagem(mensagem, texto, False)
		return

	if("charada" in text):
		url = 'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria'
		headers = {'Accept': 'application/json'}
		r = requests.post(url, headers=headers)
		print(r)

		dados = r.json()
		pergunta = dados['pergunta'] 
		resposta = dados['resposta']
		tudoJunto = pergunta + '\n' + resposta
		r = com.enviaMensagem(mensagem, tudoJunto, False)
		print(r)
		return
	
	if("hug" in text):
		r = com.enviaAnimation(mensagem, getGifLink("hug"), True)
		print(r)
		return
	
	if("wink" in text):
		r = com.enviaAnimation(mensagem, getGifLink("wink"), True)
		print(r)
		return
	
	if("pat" in text):
		r = com.enviaAnimation(mensagem, getGifLink("pat"), True)
		print(r)
		return
	
	if("meme" in text):
		if(True): #DISABLED - TA DANDO ERRO
			return
		meme = getMeme();
		image = meme['image']
		caption = meme['caption']
		r = com.enviaImagemCaption(mensagem, image, caption, False) 
		print(r)
		return 

	if("sabedoria" in text):
		listaRespostas = ["Difícil dizer....", "Não tenho certeza", "Depende de como você olha né...", "Sim", "Não", "Claro que não!", "Claro!", "Com certeza", "Sei não ein..."]
		#VERIFICA SE TEM PERGUNTA
		if("?" not in text):
			resposta = "Por favor me faça uma pergunta... (aquelas frases que tem '?')"
		else:
			resposta = retiraLista(listaRespostas);
		
		r = com.enviaMensagem(mensagem, resposta, True)
		print(r)
		return

	if("acende" in text):
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
			r = com.enviaMensagem(mensagem, msgs[i], False)

		#Envia o POW ou '...'
		s = random.randrange(1, 5) #GERA NUMERO 1 - 4
		time.sleep(s)
		r = com.enviaMensagem(mensagem, msgs[len(msgs) - 1], False)

	return

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