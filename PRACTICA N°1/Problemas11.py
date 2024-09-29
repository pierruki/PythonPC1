lista = [1, 1, 2, 3, 4, 4, 5, 1]

lista_sin = []

for elemento in lista:
    
    if elemento not in lista_sin:
        
        lista_sin.append(elemento)

print(lista_sin)