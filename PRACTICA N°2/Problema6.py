# Problema 6: Serie de Fibonacci entre 0 y 50
def serie_fibocci(limite):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= limite:
        fib.append(fib[-1] + fib[-2])
    return fib

def mostrar_fib():
    serie = serie_fibocci(50)
    print("Serie de Fibonacci hasta 50:", serie)

mostrar_fib()
