import time

cores = ['Verde', ' Amarelo', ' Azul','Branco']

#print(cores)

cores.append('Rosa')

#print(cores)

def cantar_parabens():
    print('Parabéns pra você')
    time.sleep(4)
    print('Nesta data querida')
    time.sleep(3.5)
    print('Muitas felicidades')
    time.sleep(3.5)
    print('muitos anos de vida')
    time.sleep(2)
    

for n in range(2):
    cantar_parabens()

print('Viva o aniversáriante')
