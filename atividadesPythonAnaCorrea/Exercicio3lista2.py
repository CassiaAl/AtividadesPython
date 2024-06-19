def main():
    # Solicita ao usuário para inserir a quantidade de horas

    print("*******************************")
    print("****** Programa de area do retangulo")
    print("*******************************")

    horas = int(input("Digite a quantidade de horas: \n"))

    # Calcula o equivalente em minutos
    minutos = horas * 60

    # Exibe o resultado
    print(f"O equivalente em minutos é: {minutos}")

if __name__ == "__main__":
    main()