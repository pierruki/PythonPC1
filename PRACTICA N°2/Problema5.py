# Problema 5: Suma de números primos menores que 100
def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma():
    suma = sum(i for i in range(2, 100) if primo(i))
    print(f"La suma de los números primos menores que 100 es: {suma}")

suma()
