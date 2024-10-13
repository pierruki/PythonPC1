import random
from pyfiglet import Figlet
figlet = Figlet()
fuente = input("Escriba el nombre de una fuente (o presione Enter para elegir una al azar): ")
fuentes_disponibles = figlet.getFonts()
if not fuente:
    fuente = random.choice(fuentes_disponibles)
else:
    if fuente not in fuentes_disponibles:
        print(f"La fuente '{fuente}' no está disponible. Se seleccionará una fuente al azar.")
        fuente = random.choice(fuentes_disponibles)
figlet.setFont(font=fuente)
texto = input("Escriba el texto que desea convertir en arte ASCII: ")
print(figlet.renderText(texto))

