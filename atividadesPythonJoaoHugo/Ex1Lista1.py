def calcular_area_retangulo():

    #By: João Hugo
    #Data: 24/06

    print("---------------------------------")
    print("       Área do Retângulo         ")
    print("---------------------------------")

    # Variável da base
    base = float(input("Coloque o valor da base: "))

    # Variável da altura
    altura = float(input("Insira o valor da altura: "))

    # Cálculo da área do retângulo
    area = base * altura

    # Exibindo o resultado
    print(f"A área do retângulo é: {area}")

# Chamando função
calcular_area_retangulo()