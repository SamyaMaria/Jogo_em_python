import adivinhacao
import forca

def escolher_jogo():

    print("\n*********************************")
    print("*******ESCOLHA UM JOGO!**********")
    print("*********************************")

    print("\nQUAL JOGO VOCê QUER JOGAR? ")

    jogo = int(input("(1) ADIVINHAÇÃO   (2) FORCA : "))

    if (jogo == 1):
        print("   \nJOGANDO ADIVINHAÇÃO!! ")
        adivinhacao.jogar_adivinhacao() #nome do arquivo . função que vai ser executada
    elif (jogo == 2):
        print("   \nJOGANDO FORCA!! ")
        forca.jogar_forca()

if (__name__ == "__main__" ):
    escolher_jogo()

