def agregar(x, y):
    try:
        return x + y
    except TypeError:
        return "Error: El tipo de dato ingresado no es válido."

def restar(x, y):
    try:
        return x - y
    except TypeError:
        return "Error: El tipo de dato ingresado no es válido."

def multiplicar(x, y):
    try:
        return x * y
    except TypeError:
        return "Error: El tipo de dato ingresado no es válido."

def dividir(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError
        return x / y
    except TypeError:
        return "Error: El tipo de dato ingresado no es válido."
    except ZeroDivisionError:
        return "Error: No se puede realizar la división por cero."
