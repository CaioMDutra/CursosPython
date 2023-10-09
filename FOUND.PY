countainer = [1,2,3,4,5,6,7,]

choice = int(input("Escolha um número: "))

for i, item in enumerate(countainer):
    if item == choice:
        print(f"Encontrado o número {choice} na posição {i}")
    else:
        print(f"Não encontrado na posição {i}")