#Funcoes de enviar/receber mensagens
import re
import requests
import time
import json

#Import modules
import FuncoesAuxiliares as auxf

#URL
URL = #Insira a URL da API com o token aqui

def recebeUpdate(offset):
	#PARAMETROS
	#OFFSET eh para so pegar as mensagens novas (deve ser maior do que o update_id da ultima msg processada)
	PARAMS = {'offset':offset}

	#MANDA O GET REQUEST
	try:
		r = requests.get(url = URL + '/getUpdates', params = PARAMS)
	except Exception as e:
		time.sleep(5)
		return e
	return r

#ENVIA MENSAGEM, COM REPLY OU NAO
def enviaMensagem(data, resposta, reply):
	messageid = auxf.extract_values(data, 'message_id')
	chatid = auxf.extract_values(data, 'id') #PODE TER PROBLEMA!!!!! (TEM VARIOS IDs)
	if(reply != True):
		#PREPARA A MENSAGEM DE VOLTA
		data = {'chat_id':chatid[1],
				'text':resposta}
	else:
		#PREPARA A MENSAGEM DE VOLTA
		data = {'chat_id':chatid[1],
			'text':resposta,
			'reply_to_message_id':messageid}
	
	#ENVIA A MSG DE VOLTA
	try:
		r = requests.post(url = URL + '/sendMessage', data = data)
	except Exception as e:
		time.sleep(5)
		return e
	
	return r

def enviaImagem(data, url, reply):	
	messageid = auxf.extract_values(data, 'message_id')
	chatid = auxf.extract_values(data, 'id') #PODE TER PROBLEMA!!!!! (TEM VARIOS IDs)
	#PREPARA A MSG
	if(reply != True):
		data = {'chat_id':chatid[1],
				'photo':url}
	else:
		data = {'chat_id':chatid[1],
				'photo':url,
				'reply_to_message_id':messageid}
	#ENVIA
	try:
		r = requests.post(url = URL + '/sendPhoto', data = data)
	except Exception as e:
		time.sleep(5)
		return e
	return r

#ENVIA IMAGEM COM LEGENDA
def enviaImagemCaption(data, url, caption, reply):
	messageid = auxf.extract_values(data, 'message_id')
	chatid = auxf.extract_values(data, 'id') #PODE TER PROBLEMA!!!!! (TEM VARIOS IDs)
	
	#PREPARA A MSG
	#VE SE EH PARA SER UMA RESPOSTA OU NAO
	if(reply != True):
		data = {'chat_id':chatid[1],
			'photo':url,
			'caption':caption}
	else:
		data = {'chat_id':chatid[1],
			'photo':url,
			'caption':caption,
			'reply_to_message_id':messageid}
	#ENVIA
	try:
		r = requests.post(url = URL + '/sendPhoto', data = data)
	except Exception as e:
		time.sleep(5)
		return e
	return r

#ENVIA UM GIF OU VIDEO
def enviaAnimation(dados, url, reply):
	messageid = auxf.extract_values(dados, 'message_id')
	chatid = auxf.extract_values(dados, 'id') #PODE TER PROBLEMA!!!!! (TEM VARIOS IDs)
	
	#PREPARA A MENSAGEM
	#VERIFICA SE EH UMA RESPOSTA
	if(reply != True):
		DATA = {'chat_id':chatid[1],
				'animation':url}
	else:
		DATA = {'chat_id':chatid[1],
				'animation':url,
				'reply_to_message_id':messageid}
	
	#ENVIA
	try:
		r = requests.post(url = URL + '/sendAnimation', data = DATA)
	except Exception as e:
		time.sleep(5)
		return e
	return r

def enviaAnimationCaption(dados, url, reply, caption):
	messageid = auxf.extract_values(dados, 'message_id')
	chatid = auxf.extract_values(dados, 'id') #PODE TER PROBLEMA!!!!! (TEM VARIOS IDs)
	
	#PREPARA A MENSAGEM
	#VERIFICA SE EH UMA RESPOSTA
	if(reply != True):
		DATA = {'chat_id':chatid[1],
				'animation':url,
				'caption':caption}
	else:
		DATA = {'chat_id':chatid[1],
				'animation':url,
				'caption':caption,
				'reply_to_message_id':messageid}
	
	#ENVIA
	try:
		r = requests.post(url = URL + '/sendAnimation', data = DATA)
	except Exception as e:
		time.sleep(5)
		return e
	return r
