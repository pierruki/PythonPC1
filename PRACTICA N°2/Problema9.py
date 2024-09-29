# Problema 9: Eliminar vocales de una cadena
def delete_vocales(cadena):
    voc = "aeiouAEIOU"
    return ''.join([letras for letras in cadena if letras not in voc])

def eliminar():
    text = input("Ingrese una cadena de texto: ")
    print("Texto sin vocales:", delete_vocales(text))

eliminar()
