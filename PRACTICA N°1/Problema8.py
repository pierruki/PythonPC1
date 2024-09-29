# Determina si es hora de desayunar, almorzar o cenar
time = input("Introduce la hora en formato hh:mm: ")
hours, minutes = time.split(":")
hours = float(hours) + float(minutes)/60

if 7 <= hours <= 8:
    print("Es hora de desayunar.")
elif 12 <= hours <= 13:
    print("Es hora de almorzar.")
elif 18 <= hours <= 19:
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")
