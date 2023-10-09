from random import random

def joga_moeda():
    #valor = random() (só para mostrar que não preciso crar uma variavel para random)
    #if valor > 0.5:
    if random() > 0.5:
        return 'Cara'
    return'Corroa'

print(joga_moeda())


def par_ou_impar():
    num  = int(input('Digite um numero '))
    if num % 2 == 0:
        return 'Numero par'
    return 'Numero impar'

print(par_ou_impar())


