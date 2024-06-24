def main():
    num1 = float(input("Escreva o valor para conversão: "))
    operacao = int(input("Informe se a conversão será para dólar (5) ou euro (10): "))

    if operacao == 5:
        print(f"A conversão de real para dólar é: {num1 / 5.20:.2f}")
    elif operacao == 10:
        print(f"A conversão de real para euro é: {num1 / 5.50:.2f}")


if __name__ == "__main__":
    main()
