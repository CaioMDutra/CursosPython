lista = [1,2,3,4,5,6,7,8,9]

res = [dado * 10 for dado in lista]

print(res)


quadrado = [num * num for num in lista]

print(quadrado)

def caixa_alta(nome):
    return nome.replace(nome[0], nome[0].upper())

amigos = ['loco', 'léo','bia','mario','ste','cassio']

amigos = [caixa_alta(amigo)for amigo in amigos]

print(amigos)

lista2 = ['1','2','3','4','5','6','7','8','9']

list_num = [int(num) for num in lista2]

print(list_num)
