# de la libreria flask importame la clase Flask
# todos las clases siempre son en mayuscula
# crear tu entorno virtual para garantizar la funcionalidad de tu software
from flask import Flask,request
# el atributo name permite indicarle que este sera el archivo principal de la aplicacion de ahi podra acceder a los archivos estaticos como plantillas
app=Flask(__name__)


# decorador patron de software que permite modificar el funcionamiento de una clase sin la necesidad de usar la herencia
@app.route('/',methods=["GET","POST"])
def home():
    # print(request.__dict__)
    print(request.get_json())
    return {
        "content":"",
        "message":"Hola desde mi nueva api"
    }

if __name__=="__main__":
    # para levantar el servidor debug para k el servidor se reinicie en cada modificacion que hagamos y el port el puerto donde va escuchar
    app.run(debug=True,port=5000)