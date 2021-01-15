# assert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f"{palabra} no es string"
            assert len(palabra) > 0, "No se permiten strings vacios"

            primeras_letras.append(palabra[0])

        except AssertionError as e:
            print(e)

    return primeras_letras


lista = ["Jose", 3.142, '', 2, "01c2j913cJEQWIOJEOQW", 0.0000000000001]
print("Primeras letras validas son: ", primera_letra(lista))