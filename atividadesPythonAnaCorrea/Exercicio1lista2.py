main():
    # Solicita ao usuário para inserir a base e a altura do retângulo

print("*******************************")
print("****** Programa de area do retangulo")
print("*******************************")

 base = float(input("Digite o valor da base do retângulo: \n"))
    altura = float(input("Digite o valor da altura do retângulo: \n"))

    # Calcula a área do retângulo
    area = base * altura

    # Exibe o resultado
    print(f"A área do retângulo é: {area}")

if __name__ == "__main__":
    main()