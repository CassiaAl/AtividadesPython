print("**********************")
print("  Programa Maior 2.0")
print("**********************")

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Agora digite o segundo número: "))

num3 = float(input("Agora digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O primeiro número (", num1, ") é maior que o segundo número(", num2, ") e o terceiro número (",num3,")")

elif num2 > num1 and num2 > num3:
    print("O segundo número (", num2, ") é maior que o primeiro número(", num1, ") e o terceiro número (",num3,")")

elif num3 > num1 and num3 > num2:
    print("O terceiro número (", num3, ") é maior que o primeiro número(", num1, ") e o segundo número (",num2,")")