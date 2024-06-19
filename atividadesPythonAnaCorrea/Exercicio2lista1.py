
def main():
    soma = 0
    numero = 0

    print("*******************************")
    print("****** Programa de soma *******")
    print("*******************************")

    numero = int(input("Digite o número para a soma: \n"))

    for i in range(1, numero + 1):
        soma += i

    print(f"O resultado da soma dos números de 1 a {numero} = {soma}")


if __name__ == "__main__":
    main()
