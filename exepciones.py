# es para capturar los errores
#cuando nuestro codigo muera abruptamente x ejemplo cuando el usuario kiera un correo y el cliente no nos lance un correo ahi resaltara un error
# otro ejemplo cuando quisieramos calcular el igv pero no tenemos el precio del productos entonces como podemmos calcular de algo que no existe y explota el algoritmo
#recuerda donde ocurra el error salta y te vota y no se ejecuta nada que este despues de eso


#intentalo 
try:
    numero=5/1
    print(f"la division es: {numero}")
    # numero=1000/0
    num=10+5
    print(f"la division de 10 {num}")
#para especificar los errores especificos
except ZeroDivisionError:
    print("Error al hacer la division")
except TypeError:
    print("no se puede sumar string con number")
#si no lo hacemos asi 
#para los errores genericos
except:
    print("hubo algun error en nuestro codigo")
#para usar un else tenemos que obligatoriamente declarar un except, y este se ejecutara cuando no ingresa  a ningun except (cuando la operacion no tuvo errores)
else:
    print("todo ok")
#no import asi la operacion salio mal o hubo errores, igual me ejecuto ojo siempre va al final de todo los except antes del else.
finally:
    print("igual me ejecuto")
print("despues de usar las exepciones")