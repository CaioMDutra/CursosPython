def quadrado(num):
       return num ** 2

print(quadrado(int(input('Digite um numero. '))))

def cantar_parabens(voce):
    print('Parabéns pra você')
    
    print('Nesta data querida')
   
    print('Muitas felicidades')
    
    print('muitos anos de vida')

    print(f'Viva {voce}')

cantar_parabens('Julia')


def soma_impares(nums):
    total = 0
    for num in nums:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1,2,3,4,5,6,7,8,9,0]
print(soma_impares(lista))
    