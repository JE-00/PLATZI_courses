"""
Excepciones comunes:
ImportError: una importación falla;
IndexError: una lista se indexa con un número fuera de rango;
NameError: se usa una variable desconocida;
SyntaxError: el código no se puede analizar correctamente
TypeError: se llama a una función en un valor de un tipo inapropiado;
ValueError: se llama a una función en un valor del tipo correcto, pero con un valor inapropiado;
"""
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(20))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))
