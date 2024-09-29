# Problema 1: Números divisibles por 7 y múltiplos de 5
resultado = []
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        resultado.append(i)

print("Números divisibles por 7 y múltiplos de 5:",resultado)