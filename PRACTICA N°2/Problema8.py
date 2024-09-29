# Problema 8: Factorial de un número
def f(num):
    if num == 0 or num == 1:
        return 1
    return num * f(num - 1)

def mostrar():
    num = int(input("Ingrese un número para calcular su factorial: "))
    print(f"El factorial de {num} es: {f(num)}")

mostrar()
