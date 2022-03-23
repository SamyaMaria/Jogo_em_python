import random

def jogar_adivinhacao():
    mensagem_de_abertura()
    numero_secreto = random.randrange(1, 101)  # random: para número aleatórios
    total_de_tentativas = nivel_do_jogo()

    pontos_total = 100
    for rodada in range(1, total_de_tentativas + 1):

        print("\nTentativa {} de {}" .format(rodada, total_de_tentativas))
        chute = pede_chute()

        if chute < 1 or chute > 100:
            print("Você deve digitar um número de 1 a 100 !!!")
            continue

        if chute == numero_secreto:
            print("Você acertou!! \nTOTAL DE PONTOS OBTIDOS: {} ".format(pontos_total))
            break
        else:
            if chute >  numero_secreto:
                print("VOCÊ ERROU ! Seu número foi maior que o número secreto")
                if rodada == total_de_tentativas:
                    print("\nVOCÊ PERDEU !! O número secreto era {} e seus pontos obtidos foram: {}". format(numero_secreto, pontos_total))
            elif chute <  numero_secreto:
                print("VOCÊ ERROU ! Seu número foi menor que o número secreto")
                if rodada == total_de_tentativas:
                    print("\nVOCÊ PERDEU !! O número secreto era {} e seus pontos obtidos foram: {}".format(numero_secreto, pontos_total))
        pontos = abs(numero_secreto - chute)
        pontos_total = pontos_total - pontos

    print("\nFIM DO JOGO!!!")

def mensagem_de_abertura():
    print("\n********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************\n")

def nivel_do_jogo():
    total_de_tentativas = 0
    print("ESCOLHA O NÍVEL DO JOGO ")
    print("(1) Fácil   (2) Médio  (3) Difícil")

    nivel = int(input("DIGITE O NÍVEL: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    return total_de_tentativas

def pede_chute():
    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou: ", chute)
    return chute

if __name__ == "__main__":
    jogar_adivinhacao()