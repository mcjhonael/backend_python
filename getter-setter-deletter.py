# sirve para modificar los valores atributos y metodos privados aunque no es recomendable

class Electrodomestico:
    
    def __init__(self):
        self.__nombre=""
        self.__color=""
        self.__precio=0.0
    
    # settear quiere decir que vas a reemplazar o cambiar el nombre
    def __setNombre(self,nombre):
        self.__nombre=nombre
    
    #get es obtener el nombre y el return para devolver lo que estas retornando
    def __getNombre(self):
        return self.__nombre
         
    # para eliminar el contenido del atributo
    def __deleteNombre(self):
        del self.__nombre

    # cuando nosotros definamos los __setter __getter para acceder a ellos debemos usar la propiedad
    # property = sirve para deefinir el comportamiento que tendra un atributo de la clase considerando ese mismo orden x favor get,set,del
    nombre=property(__getNombre,__setNombre,__deleteNombre)
    property()


objElectrodomestico=Electrodomestico()
objElectrodomestico.nombre="plancha"
print(objElectrodomestico.nombre) 
