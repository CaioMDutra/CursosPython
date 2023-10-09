
tupla = tuple(range(22+1))

print(tupla)



dados = (input('Qual seu nome? '),
        input("Qual sua profisssão? "),
        input("Qual sua empresa? "))

nome, profissao, empresa = dados

print(f'O {nome} trabalha como {profissao}, na empresa {empresa}! Parabéns Caio, você é de MAIS +++++')    




print(len(dados))
print('Caio' in dados)

for i, nome in enumerate(dados):
    print(i, nome)