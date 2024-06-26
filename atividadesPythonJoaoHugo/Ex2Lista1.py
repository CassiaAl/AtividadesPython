def cauculo_de_IMC():

    #By: João Hugo
    #Data: 24/06

    print("---------------------------------")
    print("       Cálculo de IMC            ")
    print("---------------------------------")

    # Váriavel da altura
    altura = float(input("Insira o valor da sua altura: "))

    # Váriavel da massa
    massa = float(input("insira o valor de sua massa: "))

    # Cáclculo do IMC
    IMC = massa / (altura * altura)

    # Exibindo valor do IMC
    print(f"O valor do seu IMC é de: {IMC}")

# Chamando a função
cauculo_de_IMC()