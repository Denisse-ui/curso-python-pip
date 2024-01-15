import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #obtenemos el estatus de la peticion 
    print(r.text) #Obtenemos la información de la petición 
    print(type(r.text)) #Obtenemos el tipo de r.text
    categories = r.json() #Convertimos las categorias en formato json 
    for category in categories:
        print(category['name']) #Imprimimos el atributo del nombre de cada una de las categorias 