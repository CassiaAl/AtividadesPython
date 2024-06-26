def comparacao_de_numeros():

    # By: João Hugo
    # Data: 24/06

    print("---------------------------------")
    print("       Comparador de Números     ")
    print("---------------------------------")

    num1 = int(input("Insira o primeiro número: "))

    num2 = int(input("Insira o segundo número: "))

    if num1 > num2:
        print(num1, "é maior que", num2)

    else:
        print("O número", num1, "é menor ou igual a", num2)

comparacao_de_numeros()