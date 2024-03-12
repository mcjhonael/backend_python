colores=['verde','platano','amarillo','negro']

print(colores)
# colores.remove("verde")
print(colores)
color=colores.remove("verde")
# print(colores)

print(color)

persona={
    'nombre':'jhon',
    'apellido':'maquera',
    'edad':29,
    'correo':'correo@correo.com',
    'hobbies':[
        {
            'nombre':"volar drones",
            "conocimiento":"avanzado"
        },
        {
            'nombre':"montar cicle",
            'conocimiento':"intermedio"
        }
    ]
}
#retorna un arreglo de las claves de un diccionario
print(persona.keys())

#retorna un arreglo de todos los valores de una diccionario
print(persona.values())
print(persona['nombre'])
print(persona['hobbies'][0]['nombre'])

print("limpiar la lista {}".format(persona.clear()))