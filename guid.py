# El programa simula un GUID.
# El Guid debe contener 5 secciones de 8-4-4-4-12 letras y numeros aleatorios
# @author: Gonzalo Chacaltana B <gchacaltanab@gmail.com>
import random

secciones = [8,4,4,4,12]

secciones_guid = []

def generate_seccion(longitud):
    """ Funcion para generar seccion de GUID"""
    cadena = "abcdef0123456"
    cantidad = len(cadena)
    seccion = ""
    while len(seccion)<=longitud:
        seccion = seccion + cadena[random.randint(0, cantidad -1)]
    
    return seccion

lista = []

for seccion in secciones:
    parte = generate_seccion(seccion)
    lista.append(parte.upper())

print '-'.join(lista)