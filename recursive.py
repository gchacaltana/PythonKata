# Programa que devuelve cadena invertida en secciones de cabeza y cola.
# @author: Gonzalo Chacaltana B <gchacaltanab@gmail.com>
def invertirCadena(cadena):
    """ Funcion para invertir cadena en cabeza y cola
    """
    cabeza = cadena[0:1]
    cola = cadena[1:len(cadena)]
    return cola + cabeza


cadena = raw_input("Ingresa una cadena: ")
print invertirCadena(cadena)

