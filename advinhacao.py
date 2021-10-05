import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    rodada = 1
    pontos = 1000
    total_de_tentativas = 0

    print("Qual o nivel de dificuldade?")
    print("(1) Fácil  (2) Médio   (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 51

    for i in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(i, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute <1 or chute > 100):
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior que o número secreto")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")

            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()