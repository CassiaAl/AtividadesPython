print("*****************************")
print("  Positivo,Negativo ou nulo")
print("*****************************")

num = int(input("Digite um número inteiro para verificar o valor dele: "))

if num < 0:
    print("O número ",num," é negativo")

elif num == 0:
    print("O número ", num, " é neutro")

else:
    print("O número ", num, " é positivo")