print("******************")
print("  Programa Maior")
print("******************")

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Agora digite o segundo número: "))

if num1 > num2:
    print("O primeiro número (", num1 , ") é maior que o segundo número(", num2 ,")")

elif num2 > num1:
    print("O segundo número (", num2, ") é maior que o primeiro número (", num1 , ")")

else:
    print("O primeiro número (", num1, ") é igual ao segundo número (", num2 ,")")