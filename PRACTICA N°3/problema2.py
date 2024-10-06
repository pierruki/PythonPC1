def obt(notas):
    try:
        v = [round(float(grade.strip())) for grade in notas.split(',')]
        return v
    except ValueError:
        print("Error: Ingresar números en formato decimal, separados por comas.")
        return None

if __name__ == "__main__":
    while True:
        n = input("por favor ingresar las notas en decimal separadas por comas: ")
        s = obt(n)
        if s is not None:
            print("Lista de notas redondeadas:", s)
            break