import random
def jogo_adivinhacao():
    numero_secreto = random.randint(1,10)
    tentativas = 0
    max_tentativas = 5

    print("bem vindo ao jogo de advinhação")
    print("Tente advinhar o número entre 1 e 100")

    while tentativas < max_tentativas:
        tentativa = int(input("Digite o seu palpide:"))

        if tentativa < numero_secreto:
            print("O número secreto é maior.")
        elif tentativa > numero_secreto:
            print("O número secreto é menor.")
        else:
            print(f"Parabéns! você acertou o numero secreto que era {numero_secreto}.")
            break
        tentativas += 1
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

    else:
        print(f"Você exedeu o mmáximo de número de tentativas. O número secreto era {numero_secreto}.")

    jogo_adivinhacao()