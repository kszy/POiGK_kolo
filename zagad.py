lista = [27]

for i in range(29):
    if lista[i] % 2 == 0:
        lista.append(lista[i] / 2)
    else:
        lista.append(lista[i] * 3 + 1)

print(lista[-1])
