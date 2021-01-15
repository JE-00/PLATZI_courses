import sys


def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, dic = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return dic[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, dic) + fibonacci_dinamico(n - 2, dic)
        dic[n] = resultado
        return resultado


if __name__ == "__main__":
    # sys.setrecursionlimit(1002) #Para ampliar las recursiones
    n = int(input("Escoge un numero: "))
    resultado = fibonacci_dinamico(n)
    print(resultado)
