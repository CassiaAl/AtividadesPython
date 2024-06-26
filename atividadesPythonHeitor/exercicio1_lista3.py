def conversao(moeda):
    if moeda == "Dolar":
        print("O seu valor convertido em Dolár é equivalente a ", valor / 5.48)
    elif moeda == "Euro":
        print("O seu valor convertido em Euro é equivalente a ", valor / 5.88)

print("********************")
print("  Programa Cotação")
print("********************")

print("Bem-Vindo ao Programa Cotação!")
valor = float(input("Digite o valor em reais que você possui: "))
moeda = str(input("Digite o nome do moeda : Dolar ou Euro \n"))

conversao(moeda)