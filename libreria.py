#^ librerias
#para trabajar con librerias utilizamos pypi.org aqui encontramos todos las liberias de 
#pip gestor de paquete para instalar de python
#pip install camelcase

#de la libreria camelcase importame su clase Camelcase
from camelcase import CamelCase

#siempre debemos instanciar una clase 
#recibe como parametro la palabra que no desea que se convierta a camelcase
instancia=CamelCase("alumnos")

texto="hola alumnos buenas noches ya se viene el break"

#usar la instancia y le aplicamos el metodo hump que recibe la oracion a transformar
resultado=instancia.hump(texto)

#muestra el resultado
print(resultado)

