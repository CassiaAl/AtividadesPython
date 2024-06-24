print("********************")
print("  Programa Cotacao")
print("********************")

valor = float(input("Digite o valor que você possui em reais: "))

moeda = str(input("Digite para qual moeda deseja converter [Dolar/Euro]: "))

match moeda:
    case "Dolar":
        print(f"O valor que você possui convertido para Dólar é ${valor/5.42}")

    case "Euro":
        print(f"O valor que você possui convertido para Euro é ${valor / 5.81}")

