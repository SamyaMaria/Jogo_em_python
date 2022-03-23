import random

def jogar_forca():
    mensagem_de_abertura()
    palavra_secreta = categoria_de_palavras()
    letras_acertadas = incrementa_palavras_acertadas(palavra_secreta)

    print(" A palavra tem {} letras ".format(len(palavra_secreta)))
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute_da_letra()

        if chute in palavra_secreta:
            marca_letras_acertadas(palavra_secreta,chute,letras_acertadas)
        else:
            erros += 1
            print("\nOps, você errou! Faltam {} tentativas.".format(7 - erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if enforcou:
        mensagem_perdeu(palavra_secreta)
    else:
        mensagem_ganhou()


def mensagem_de_abertura():
    print("\n*********************************")
    print("***Bem vindo ao jogo da forca !**")
    print("*********************************\n")

def categoria_de_palavras():
    categoria = input("QUAL CATEGORIA VOCÊ QUER JOGAR? \npalavras aleatórias: (a)\nfrutas: (f)\npaíses: (p)\nDIGITE A LETRA CORRESPONDENTE: ")

    if categoria == 'a':
        palavras_aleatorias()
        palavra_secreta = palavras_aleatorias()
    elif categoria == 'f':
        frutas()
        palavra_secreta = frutas()
    elif categoria == 'p':
        paises()
        palavra_secreta = paises()
    else:
        print("ESCRITA DE CARACTER ERRADA !")
    return palavra_secreta

def palavras_aleatorias():
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def frutas():
    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def paises():
    arquivo = open("paises.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def incrementa_palavras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def pede_chute_da_letra():
    chute = input("\nQual a letra? ")
    chute = chute.strip().upper()
    return chute

def marca_letras_acertadas(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1

def mensagem_perdeu(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_ganhou():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar_forca()