lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

lista.append(11)
print(lista)

soma = max(lista) + min(lista)

print(soma)

nova = lista.copy()
nova.append(23)
print(nova)

lista.remove(2)
print(lista)
