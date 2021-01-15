def factorial(n):
    """
    Calcula el factorial de n
    :param n: int > 0
    :return: n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Escriba un numero: "))
print(factorial(n))