import psycopg2
import urllib.parse as urlparse
import os
import AuxiliaryFunctions as auxf
from datetime import datetime

def close_connection(cursor, connection):
    if(connection):
        cursor.close()
        connection.close()
    return True

def connect_to_db():
    try:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port

        connection = psycopg2.connect(
                    dbname=dbname,
                    user=user,
                    password=password,
                    host=host,
                    port=port
                    )
        return connection
    except:
        return None

def test():
    connection = connect_to_db()
    if(connection == None):
        return "Error while connecting to PostgreSQL" +  str(error)

    try:
        cursor = connection.cursor()
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        output = "You are connected to - " + str(record) + "\n\n"
        
        output += "Lista de Tabelas:\n"
        cursor.execute("""SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'""")
        for table in cursor.fetchall():
            output += str(table) + "\n"

    except (Exception, psycopg2.Error) as error :
        output = "Error during test() function" +  str(error)
    
    finally:
        close_connection(cursor, connection)
        return output

def limpa_resumo():
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM mensagens *;")
        connection.commit()
    except (Exception, psycopg2.Error) as error :
        output = "Error during test() function" +  str(error)
    
    finally:
        close_connection(cursor, connection)

def setup_resumo(cursor, connection):
    #Media guarda o file_id se existir
    #Mensagem guarda o text, se existir
    try:
        #create table if not exists
        create_table_query = '''CREATE TABLE IF NOT EXISTS MENSAGENS(
            ID             SERIAL       PRIMARY KEY         ,
            CHATID         TEXT                    NOT NULL ,
            MENSAGEM       TEXT                             ,
            MEDIA          TEXT                             ,
            DATA           TIMESTAMP               NOT NULL
        );'''
        cursor.execute(create_table_query)

        #delete old entries
        delete_old_entries_query = '''DELETE FROM mensagens WHERE DATA < (now() - '24 hours'::interval);'''
        cursor.execute(delete_old_entries_query)
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        print("Error while creating PostgreSQL resumo table", error)
        return False
    return True

def setup_transparente(cursor, connection):
    # Guarda imagens transparentes pro comando merge
    try:
        #create table if not exists
        create_table_query = '''CREATE TABLE IF NOT EXISTS IMGTRANSPARENTE(
            ID             SERIAL       PRIMARY KEY         ,
            CHATID         TEXT                    NOT NULL ,
            NOME           TEXT                             ,
            FILEID         TEXT                    NOT NULL ,
            DATA           TIMESTAMP               NOT NULL
        );'''
        cursor.execute(create_table_query)

        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error :
        print("Error while creating PostgreSQL transparente_img table", error)
        return False
    return True

def setup(): #create the tables if necessary, and clean old entries
    connection = connect_to_db()
    if(connection == None):
        print("Error while connecting to PostgreSQL" +  str(error))
        return False

    cursor = connection.cursor()
    setup_resumo(cursor, connection)
    setup_transparente(cursor, connection)
    close_connection(cursor, connection)
    return True

def insere_img_transparente(update):
    chatid = update.message.chat.id
    name = update.message.text
    fileid = update.message.photo
    if(media is not None and len(media) > 0):
        fileid = fileid[0].file_id
    else:
        fileid = None
    '''else:
        media = update.message.sticker
        if(media is not None):
           media = media.file_id'''
    
    if(fileid is None and name is None):
        return

    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO IMGTRANSPARENTE (CHATID, NOME, FILEID, DATA) VALUES (%s,%s,%s, current_timestamp)"""
        record_to_insert = (chatid, name, fileid)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into imagem_transparente table")

    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into imagem_transparente table", error)

    finally:
        close_connection(cursor, connection)

    return True

def get_transparent_image(update):
    chatid = update.message.chat.id
    name = update.message.text
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM 
                            IMGTRANSPARENTE
                        WHERE
                            CHATID = %s
                        AND
                            NAME = %s''', [chat_id, name])
        fileid = cursor.fetchall() 

    except (Exception, psycopg2.Error) as error :
        fileid = "Error while fetching data from PostgreSQL" + str(error)
    
    finally:
        return fileid

#For now, ignore stickers
def insere_mensagem(update):
    chatid = update.message.chat.id
    text = update.message.text
    media = update.message.photo
    if(media is not None and len(media) > 0):
        media = media[0].file_id
    else:
        media = None
    '''else:
        media = update.message.sticker
        if(media is not None):
           media = media.file_id'''
    
    if(media is None and text is None):
        return

    try:
        connection = connect_to_db()
        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO mensagens (CHATID, MENSAGEM, MEDIA, DATA) VALUES (%s,%s,%s, current_timestamp)"""
        record_to_insert = (chatid,text, media)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print (count, "Record inserted successfully into mensagens table")

    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into mensagens table", error)

    finally:
        close_connection(cursor, connection)

    return True

def printa_mensagens():
    try:
        output = "Saida: \n"
        connection = connect_to_db()
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * FROM mensagens ORDER BY ID DESC LIMIT 5;"
        cursor.execute(postgreSQL_select_Query)
        mensagens = cursor.fetchall() 

        for row in mensagens:
            output += "Id       = " + str(row[0]) + "\n"
            output += "ChatId   = " + str(row[1]) + "\n"
            output += "Mensagem = " + str(row[2]) + "\n"
            output += "Media    = " + str(row[3]) + "\n"
            output += "Data     = " + str(row[4]) + "\n" 
            output += "\n"

    except (Exception, psycopg2.Error) as error :
        output = "Error while fetching data from PostgreSQL" + str(error)
    
    finally:
        return output   

def resumo(chat_id):
    chat_id = str(chat_id)
    try:
        media_id = None
        texto_da_msg = "Resumo:\n"
        
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM 
                            mensagens
                        WHERE
                            CHATID = %s
                        ORDER BY 
                            RANDOM()
                        LIMIT 5;''', [chat_id])
        mensagens = cursor.fetchall()
        
        for mensagem in mensagens:
            if(str(mensagem[2]) != 'None'):
                texto_da_msg += "- " + str(mensagem[2]) + "\n"
            elif(str(mensagem[3]) != 'None'):
                media_id = str(mensagem[3])

    except (Exception, psycopg2.Error) as error :
        print("Error during db.resumo() function" +  str(error))
    finally:
        close_connection(cursor, connection)
        return texto_da_msg, media_id