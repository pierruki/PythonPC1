# Problema 7: Números perfectos menores que 1000
def num_perfect(numero):
    divisores = [i for i in range(1, numero) if numero % i == 0]
    return sum(divisores) == numero

def mostrar_num():
    perfectos = [i for i in range(1, 1000) if num_perfect(i)]
    print("Números perfectos menores que 1000:", perfectos)

mostrar_num()
