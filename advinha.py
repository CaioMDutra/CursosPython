import random

num = random.randint(1, 5)

while True:
    try:        
        user_input = input("Tente adivinhar o número (1 a 5): ")

        choice = int(user_input)

        if choice > 5:
            print("ATENÇAO!!! Escolha um número entre 1 e 5.")
        else:
            if choice == num:
                print(f"Parabéns! Você acertou o número {num}.")
                break
            else:
                print(f"Voce errou. \nA respota correta seria {num} ")
                break

    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
