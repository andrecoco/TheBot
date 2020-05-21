#Funcoes auxiliares utilizadas por outras
import random

#EXTRAI CAMPOS DE json
def extract_values(obj, key):
    """Recursively pull values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Return all matching values in an object."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

#RETORNA UM ELEMENTO ALEATORIO DA LISTA
def retiraLista(lista):
	tam = len(lista)
	num = random.randrange(0, tam) #GERA NUMERO 0-FinalDaLista
	return lista[num]