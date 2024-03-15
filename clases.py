# #clase = es igual a una plantilla
# # ?toda clase tiene atributos y comportamiento
# # las funciones de las clases son metodos por que solamente trabajan dentro de una clase mientras que las funciones se ejecutar en todo codigo


# # todo lo que esta dentro es de propio de la clase
# class Mueble:
#     precio=0.0
#     color="Blanco"
#     especificaciones=[]
#     tipo=""

#     #para referenciar un atributo de la misma clase a un metodo usamos la palabra self
#     def indicar_tipo(self):
#         return "El tipo es de: {}".format(self.tipo)
    

# # instanciar es hacer una copia de toda muestra plantilla de la clase atributos y metodos
# mueble1=Mueble()
# mueble1.tipo="sofa-cama"
# mueble1.indicar_tipo()

# print(mueble1.indicar_tipo())

#^ CLASES CON CONSTRUCTOR

# datos=atributos
# funciones=metodos

# class Persona:
#     # al colocar aqui los atributos lo que sucede es que nos van a pedir valores por defecto y como colocar un valor si tiene que ser dinamico para ellos aremos otro ejemplo del constructor
#     nombre
#     fecha_naciemiento

class Persona:
    # un constructor es un metodo propio de las clases que se llamara cuando se cree una instancia de la clase
    # este es un constructor propio de python 
    #metodo que se usar para definir constructores de clase
    def __init__(self,nombre,fecha_nacimiento):
        # de esta manera creamos un atributo dinamico que se almacenara en la clase con los valores que enviamos
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
    def saludar(self):
        print(f"Hola {self.nombre}")

    # Las __str__() El método debe devolver una cadena que le gustaría representar el objeto. 
    #  https://realpython.com/python-magic-methods/#:~:text=In%20Python%2C%20special%20methods%20are,hand%2C%20so%20it%20looks%20like%20.
    # metodo que sirve para que cuando vayamos  a llamar  a imprimir  el objeto, se modifique  por algo  mas entendible
    def __str__(self):
        return self.nombre + " instancia del objeto"


persona1=Persona("Jhonatan","17-08-1992")
persona2=Persona("wilfredo","1-10-1999")

# con el constructor igual podemos acceder a sus atributos el constructor solamente nos permite crear los atributos dinamicos
print(f"nombre de la persona1 {persona1.nombre}")
print(f"nombre de la persona2 {persona2.nombre}")
persona1.saludar()
persona2.saludar()

# cuando imprimimos esta clase nos muestra un mensaje bien raro que no se puede comprender para escapar de esos necesitamos usar los metodos magicos de python 
print(persona1)
