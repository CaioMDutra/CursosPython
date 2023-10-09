def expo(num=2, expo=2):
    return num ** expo

print(expo(7,9))
print(expo(21))
print(expo())

def info(nome= 'Caio', instrutor=False):
    if nome == 'Caio' and instrutor:
        return 'Bem vindo instrutor Caio'
    elif nome == 'Caio':
        return 'Eu pensei que vc era instrutor'
    return f'Olá {nome}'

print(info(instrutor=True))
print(info(instrutor=False))
print(info())
print(info('Stephanie'))
print(info('Caio', instrutor=True))
print(info('Caio', instrutor=False))
