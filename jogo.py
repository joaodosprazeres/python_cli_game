import advinhacao
import forca

def jogar():
    print("****************************************")
    print("********ESCOLHA SEU JOGO****************")
    print("****************************************")

    print("(1) FORCA    (2) ADVINHACAO")

    jogo = int(input("Qual jogo?  "))

    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        advinhacao.jogar()

if(__name__ == "__main__"):
    jogar()