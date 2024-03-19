# herencia en python de alguna clase superior hemos sacado algo de ella
class Vehiculo:
    
    def __init__(self,marca,modelo,numero_ruedas):
        self.marca=marca
        self.modelo=modelo
        self.numero_ruedas=numero_ruedas
    
    def acelerar(sef):
        print("el auto esta acelerando")
    
    def estado(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nNro de ruedad: {self.numero_ruedas}"

# nuetra clase Auto esta heredando todo de Vehiculo
# la herencia se da en todo aspecto desde atributos hasta metodos si creas el mismo metodo en otra clase se va sobre escribir 
class Auto(Vehiculo):
    def __init__(self,sunroof,marca,modelo):
        self.sunroof=sunroof
        # conesto podemos heredar los atributos del padre y debo mandarlo los valores para nuestro constructor padre osea vehiculo en el mismo orden
        #con super() accedo ala clase y con el . a sus atributos o metodos
        super().__init__(marca,modelo,4)

    def estado(self):
        resultado_padre=super().estado()
        return resultado_padre + f"\nSunroof: {self.sunroof}"

class Camion(Vehiculo):
    def __init__(self,numero_cambios,marca,modelo):
        self.numero_cambios=numero_cambios
        super().__init__(marca,modelo,8)

#atributos de auto heredado
objAuto =Auto(True,"Chevrolet","Alto")
print(f"Este es la marca del Auto: {objAuto.marca}")
print(f"Este es el modelo del Auto: {objAuto.modelo}")
print(f"Este es el numero de ruedas: {objAuto.numero_ruedas}")
print(f"Este es el sunroof: {objAuto.sunroof}")
print(objAuto.estado())
print("+++++++++++++++")

#atributos de Camion (numero_cambios,marca,modelo)
objCamion=Camion(15,"Toyota","Bajo")
# print(f"Este es la marca del Camion: {objCamion.marca}")
# print(f"Este es el modelo del Camion: {objCamion.modelo}")
# print(f"Este es el numero de ruedas: {objCamion.numero_ruedas}")
# print(f"Este es el numero_cambios: {objCamion.numero_cambios}")
# objCamion.estado()

#en python no funciona el poliformismo no funciona de la misma manera que los otros lenguajes
#que cuando colocamos 2 metodos con el mismo nombre y diferentes resultado se sobreescribe todo con el final
# En programación orientada a objetos, polimorfismo es la capacidad que tienen los objetos de una clase en ofrecer respuesta distinta e independiente en función de los parámetros (diferentes implementaciones) utilizados durante su invocación. Dicho de otro modo el objeto como entidad puede contener valores de diferentes tipos durante la ejecución del programa.

# poliformismo=podemos crear 3 metodos con el mismo nombre pero cada metodo recibe parametros diferentes por lo cual cada metodo tendra diferentes operaciones xk se rige deacuerdo a los parametros enviados no al nombre del metodo
# en cambio en python nos regimos en el nombre del metodo y se va sobre escribir hasta el ultimo metodo que hemos creado con sus parametros

