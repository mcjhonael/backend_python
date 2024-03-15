# pertenece a la parte privada de la clase y que  no puede ser vista  desde ningun programa o clase

# class Vehiculo:
#     def __init__(self,largo,ancho,cilindrada,enMarcha=False):
#         self.largo=largo
#         self.ancho=ancho
#         self.cilindrada=cilindrada
#         self.enMarcha=enMarcha
#         # indicamos que todos los vehiculos tendran x defecto el valor de alarma activada
#         # agregamos que cuando queramos indicar que un atributo va ser privado (no puede ser accedido desde afuera de la clase) se le pone antes del nombre __
#         # self.alarma=True 
#         self.__alarma=True

#     #metodo que se encarge de apagar la alarma
#     def toggle_alarma(self):
        
#         if self.__alarma==True:
#             self.__alarma=False
#         else:
#             self.__alarma=True
#         print(self.__alarma)

#     # este metodo se encargara de cambiar enMarcha su estado 
#     # antes de ser encendido debes verificar 1ro la alarma
#     def encender(self,estado=True):
#         resultado=self.__verificar_alarma()
#         if resultado:
#             print("el vehiculo puede andar correctamente")
#             self.enMarcha=estado
#         else:
#             print("quieren robar el carro 🚨🚨🚨🚨🚨")

#     #este es un metodo privado
#     # si la alarma esta prendida entonces retorna false 
#     def __verificar_alarma(self):
#         if self.__alarma==True:
#             return False
#         else:
#             return True

#     # def __str__(self):
#         # return f"El carro tiene un largo de {self.largo} un ancho de {self.ancho} una capacidad de cilindrada de {self.cilindrada} y su marcha es {self.enMarcha}"
    
# objVehiculo=Vehiculo(2.20,1.65,1500)

# # print(objVehiculo)
# # print(objVehiculo.__alarma)
# # print(objVehiculo.__verificar_alarma)
# # objVehiculo.toggle_alarma()
# # objVehiculo.toggle_alarma()
# # objVehiculo.toggle_alarma()
# print(objVehiculo.encender())


class Persona:
    
    def __init__(self,nombre,apellido,correo,password):
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.password=self.__encriptar_password(password)

    def __encriptar_password(self,password): 
        return "gergerg"+password+"sgfewrkgmekrng"
    
objPersona=Persona(nombre='jhonatan',apellido='maquera',correo='mc.jhonael@gmail.com',password="maricielo")
# cuando llamo al atributo se activa el metodo __encriptar_password y manda ese return 
print(objPersona.password)