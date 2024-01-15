import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') #Decorador indica la ruta por la cual desde la web van a poder acceder 
def get_list(): 
    return [1, 2, 3, 4]

@app.get('/contacto', response_class = HTMLResponse) #Decorador indica la ruta por la cual desde la web van a poder acceder 
def get_list(): 
    return """
        <h1> Hola soy una pagina </h1>
        <p> Soy un parrafo </p>
    """

def run():
    store.get_categories()


if __name__ == '__main__':
    run()
