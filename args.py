'''
Entendendo o *args
'''

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1,2,3,4,5,6,7,8,9,0]

print(soma_todos_numeros(*numeros))
