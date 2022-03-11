import random

def jogar_forca():
    print("\n*********************************")
    print("***Bem vindo ao jogo da forca !**")
    print("*********************************\n")

    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    print(" A palavra tem {} letras ".format(len(palavra_secreta)))
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        '''str.strip: esse built in remove os espaços que podem ser deixados
           str.upper: converte o string para letra maiúscula '''

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if enforcou:
        print("\nVocê perdeu !!!")
    else:
        print("\nVocê ganhou !!!")

    print("\nFim do jogo !!!")

if __name__ == "__main__":   # para executar no promp de comando o arquivo invidualmente
    jogar_forca()            # sem precisar passar pelo que está integrado.
