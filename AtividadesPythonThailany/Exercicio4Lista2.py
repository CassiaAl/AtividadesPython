print("*********************")
print("     Número maior    ")
print("*********************")

num1 = int(input("Digite o primeiro número inteiro: \n"))

num2 = int(input("Digite o segundo número inteiro: \n"))

if num1 > num2:
    print("O número ",num1," é maior que o número ",num2)

elif num2 > num1:
    print("O número ", num2, " é maior que o número ", num1)

else:
    print("\nO número ",num1, " e o número ",num2," são iguais")