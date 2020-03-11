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
import BotCommands as botc

#LIDA COM OS COMANDOS
def lidaMensagemPrivado(data, text):
	if(True):
		return
	PARAMS = {'message':text}
	url = 'https://some-random-api.ml/chatbot'
	r = requests.get(url, params=PARAMS)
	print(r) 
	dados = r.json()
	print(dados)
	respostaChat = dados['response']
	r = com.enviaMensagem(data, respostaChat, False)
	print(r)
	return

#LIDA COM AS MENSAGENS, E DECIDE O QUE RESPONDER
def lidaMensagemGrupo(mensagem, text):
	print(text)
	if("triste" in text.lower()):
		num = random.randrange(0, 2) #GERA NUMERO 0 ou 1
		if(num == 1):
			url = get_doge_image_url()
			r = com.enviaImagemCaption(mensagem, url, "Poxa... Fica triste nao, olha a foto desse cachorro!", True)
		else:
			url = get_cat_image_url()
			r = com.enviaImagemCaption(mensagem, url, "Poxa... Fica triste nao, olha a foto desse gato!", True)
		print(r)
		return

	#if("?" in text):
	#	r = com.enviaMensagem(mensagem, "42", True)
	#	print(r)
	return

#RECEBE UMA LISTA DE TODAS AS MENSAGENS E PROCESSA ELAS
def processaMensagens(mensagens):
	update_id = None
	#Passa por todas as mensagens
	for mensagem in mensagens:
		#print(mensagem)

		#PEGA AS INFORMACOES DA MSG
		message_id = auxf.extract_values(mensagem, 'message_id')
		
		try:
			chat_id = auxf.extract_values(mensagem['message']['chat'], 'id')
		except Exception as e:
			chat_id = auxf.extract_values(mensagem['edited_message']['chat'], 'id')

		try:
			username = auxf.extract_values(mensagem['message']['from'], 'username')
		except Exception as e:
			username = auxf.extract_values(mensagem['edited_message']['from'], 'username')

		try:
			isGroupMessage = "group" in auxf.extract_values(mensagem['message']['chat'], 'type')
		except Exception as e:
			isGroupMessage = "group" in auxf.extract_values(mensagem['edited_message']['chat'], 'type')

		isBotCommand = "bot_command" in auxf.extract_values(mensagem, 'type')
		
		#SE O CAMPO reply_to_message existir, entao eh um reply
		try:
			try:
				aux = mensagem['message']['reply_to_message']
			except Exception as e:
				aux = mensagem['edited_message']['reply_to_message']
			isReply = True
		except Exception as e:
			isReply = False

		textList = auxf.extract_values(mensagem, 'text')

		#print(message_id)
		#print(chat_id)
		#print(username)
		#print(isGroupMessage)
		#print(isBotCommand)
		#print(isReply)
		#print(textList)

		#PEGA O TEXTO CERTO DA MSG
		#se nao tiver texto, ignora
		if(textList == []):
			continue

		if(isReply):
			if(len(textList) > 1): #CONFERE SE A RESPOSTA TEM TEXTO
				text = textList[1]
			else:
				continue
		else:
			text = textList[0]

		if(isBotCommand):
			botc.botCommands(mensagem, text)

		if(isGroupMessage):
			lidaMensagemGrupo(mensagem, text)
		else:
			#TODO - lidaMensagemPrivado()
			lidaMensagemGrupo(mensagem, text)
	update_id = auxf.extract_values(mensagens[-1], "update_id")
	return update_id[0]

########################################################################

offset = 0
update_id = None

while(True):	
	try:
		#RECEBE UPDATE
		r = com.recebeUpdate(offset)

		#EXTRAI INFORMACAO
		data = r.json()

		if(data["ok"] != True):
			print("Erro ao conseguir update!")
			time.sleep(5)
			continue

		#SEPARA TODAS AS MENSAGENS RECEBIDAS E ARMAZENA PARA PROCESSAMENTO
		mensagens = data["result"]
		
		if(mensagens == []):
			print("sem mensagens")
			time.sleep(1)
			continue

		#print(f"Processando {len(mensagens)} mensagens!")
		offset = processaMensagens(mensagens) + 1
	except Exception as e:
		print("1 - " + str(e))
