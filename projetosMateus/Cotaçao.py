print("***************")
print("   Cotação ")
print("***************")

transformacao = str(input("Digite o qual moeda voçê quer converter: Dolar ou Euro \n"))

reais = float(input("Informe o valor em reais: "))

match transformacao:
    case "Dolar":
        print(f"seu valor de reais em dolar é R$ {reais/5.42}")

    case "Euro":
        print(f"seu valor de reais em euros é R$ {reais/5.81}")



