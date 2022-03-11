def calculadora():
    operacao = input(
        "ESCOLHA UM OPERADOR: \n'+' PARA SOMA  \n'-' PARA SUBTRAÇÃO \n'*' PARA MULTIPLICACAO \n'/' PARA DIVISAO:\n ")

    n1 = int(input("número 1: "))
    n2 = int(input("número 2: "))

    if operacao == '+':
        print("{} + {}".format(n1, n2))
        print(n1 + n2)
    elif operacao == '-':
        print("{} - {}".format(n1, n2))
        print(n1 - n2)
    elif operacao == '*':
        print("{} * {}".format(n1, n2))
        print(n1 * n2)
    elif operacao == '/':
        print("{} / {}".format(n1, n2))
        print(n1 / n2)
    else:
        print("Operacao inválida!!!!")


def again():
    continuar = input("DESEJA CONTINUAR ?\n 'y' para sim\n 'n' para nao:\n  ")

    if continuar == 'y':
        calculadora()
    elif continuar == 'n':
        print("OPERAÇÃO ENCERRADA")
    else:
        again()
        print("ERRO NA DIGITAÇÃO DA RESPOSTA!!")


if __name__ == "__main__":
    calculadora()
    again()
