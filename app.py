# colores=['verde','platano','amarillo','negro']

# print(colores)
# # colores.remove("verde")
# print(colores)
# color=colores.remove("verde")
# # print(colores)

# print(color)

# persona={
#     'nombre':'jhon',
#     'apellido':'maquera',
#     'edad':29,
#     'correo':'correo@correo.com',
#     'hobbies':[
#         {
#             'nombre':"volar drones",
#             "conocimiento":"avanzado"
#         },
#         {
#             'nombre':"montar cicle",
#             'conocimiento':"intermedio"
#         }
#     ]
# }
# #retorna un arreglo de las claves de un diccionario
# print(persona.keys())

# #retorna un arreglo de todos los valores de una diccionario
# print(persona.values())
# print(persona['nombre'])
# print(persona['hobbies'][0]['nombre'])

# print("limpiar la lista {}".format(persona.clear()))

# #para almacenar valores sin la necesidad de llaves
# cursos={'matematica','cta','biologia','comunicacion'}
# print(cursos)

# #?condicionales
# #?edad permitida para vacunarse entre 18 a 65
# print("####")
# print("####")
# edad=int(input("ingrese su edad para saber si puede usted vacunarse "))

# if edad < 18 :
#     print("usted no se puede vacunar")
#     print("felicidades no lo necesitas")
# elif edad<65:
#     print("necesitas 3ra dosis")
#     print("provecho!!....")
# else:
#     print("hijo ya fuiste")

# texto="eres mayor de edad" if edad>18 else "eres menor de edad"
# print(texto)

#^ciclos for iteraciones

meses=['agosto','setiembre','octubre','diciembre']

# for mes in meses:
    # print(f"los meses restantes son: {mes.upper()}")
#a diferencia de js la variable mes normal va poder ser utilizada fuera del mismo scope del for por lo cual el ultimo valor sera considerado en esa variable
# print(mes)

#podemos colocar un rango de iteraciones tbm 
#ojo que range puede tomar 3 valores
# range(n)= (n) el limite de las iteraciones desde 0 - n
# range(m,n)= (m) el numero inicial con que va empezar las iteraciones desde m - n
# range(m,n,o)= (o) es el valor de cuanto se va aumentar o decrementar en cada ciclo

#imprime del 5 - 7 - 9 
# for item in range(5,10,2):
#     print(item)

#^ el break

# for numero in range(60):
#     if numero==10:
#         print(numero)
#         break
#     print(numero)

#^salta la iteracion actual que tenemos
# for numero in range(60):
#     if numero==10:
#         continue
#     print(numero)

#^se ejecutara siempre y cuando la condicion sea verdadera

# numero=5
# while numero<10:
#     numero +=1
#     print(f"es el numero amiguito {numero}")

#^ funciones

# funciones es un bloque de codigo que se ejecuta cuantas veces  sea llamada la funcion

# print("1er ejecutable")
# aqui estamos declando la funcion 
# def saludar():
#     print("hola desde funciones")
#2do ejecutable
# print("2do ejecutable")

#aqui estamos llamando a la funcion
#3er ejecutable
# saludar()

#^funciones con parametros
# los parametros que usan las funciones o las variables creadas dentro de las funciones solamente podran ser accedidas dentro de ellas  
# def saludarNombre(nombre):
#     print(f"hola saludo a mi amigo {nombre}")
# saludarNombre("jhonael")

#^valores opciones que podemos darle a los parametros
def registro(nombre,correo=None):
    print(f"tu nombre es {nombre} y su correo {correo}")

# registro("jhonatan","mc.jhonael@gmail.com")

#^el parametro que tiene el * es un parametro especial de python que sirve para almacenar n valores y lo guardamos en la variable args
def alumnos(*args):
    # todo los valores que pasemos a este parametro se almacenaran  en una tupla en el mismo orden con el cual hemos pasado los parametros
    print(args)

# alumnos("juan","pedro","lucho",15,False)

#esta funcion se encarga de recibir 1 nombre y despues todos los valores que enviemos siempre se colocar el args al final para k encapsule todo de golpe    
def tareas(nombre,*args):
    print("OK")
    print(nombre)
    print(args)
# tareas("jhonatan",14,'jhoel',6.25)

# keywork arguments= es muy similar a los *args solo con la diferencia que los KWargs usan el nombre del parametro (nombre="jhonatan")
#los keywords agrupa todo los valores como clave y valor como un diccionario {} a diferencia de los *args
def indeterminada(**kwargs):
    print(kwargs)
indeterminada(nombre="pamela")

#^ librerias
#para trabajar con librerias utilizamos pypi.org aqui encontramos todos las liberias de 
#pip gestor de paquete para instalar de python
#pip install camelcase

from camelsace import Camelcase
