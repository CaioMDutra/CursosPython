lista = [1,2,3,4,5,6,7,8,9,0]

pares = [num for num in lista if num % 2 == 0]
impares = [num for num in lista if num % 2 != 0]


print(impares)
print(pares)