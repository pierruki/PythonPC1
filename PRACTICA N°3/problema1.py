def porcentaje(frac):
    try:
        x, y = frac.split('/')
        x = int(x)
        y = int(y)
        
        if y == 0:
            raise ZeroDivisionError("Y debe ser diferente de 0")
        if x > y:
            raise ValueError("X debe ser menor o igual a Y")
        porcent = (x / y) * 100
        if porcent <= 1:
            return 'E'
        elif porcent >= 99:
            return 'F'
        else:
            return f"{round(porcent)}%"
    except ValueError:
        print("Error: Ingresar fracción con números enteros.")
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero.")
    return None
if __name__ == "__main__":
    while True:
        frac = input("ingrear una fracción (X/Y): ")
        resultado = porcentaje(frac)
        if resultado:
            print("Resultado:", resultado)
            break