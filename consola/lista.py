print("Inicio")

entradas = []

while True:
    entrada = input('>')
    if entrada.lower() == 'x':
        break
    entradas.append(entrada)

print("Saliendo")
print("Entradas registradas:", entradas)