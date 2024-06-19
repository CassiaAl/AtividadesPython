def main():
    # Solicita ao usuário para inserir dois números e uma operação

    print("*******************************")
    print("****** Programa de soma e subtração *******")
    print("*******************************")

    numero1 = int(input("Digite um número: \n"))
    numero2 = int(input("Digite um número: \n"))
    operacao = input("Digite A para + ou S para - \n").upper()  # Converte a entrada para maiúscula para facilitar a comparação

    # Realiza a operação com base na entrada do usuário
    if operacao == 'A':
        print("O resultado da conta é:", numero1 + numero2)
    elif operacao == 'S':
        print("O resultado da conta é:", numero1 - numero2)
    else:
        print("Operação inválida")

if __name__ == "__main__":
    main()

