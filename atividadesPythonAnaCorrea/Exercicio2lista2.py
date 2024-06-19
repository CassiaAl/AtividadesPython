def main():
    # Solicita ao usuário para inserir o peso e a altura
    peso = float(input("Digite o peso (em kg): \n"))
    altura = float(input("Digite a altura (em metros): \n"))

    # Calcula o IMC
    IMC = peso / (altura * altura)

    # Exibe o resultado
    print(f"O IMC é: {IMC:.2f}")

if __name__ == "__main__":
    main()