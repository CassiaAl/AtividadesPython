print("**************************************")
print("  Programa Python area do triangulo")
print("**************************************")

num1 = float(input("informe o valor do primeiro lado:"))
num2 = float(input("informe o valor do segundo lado:"))
num3 = float(input("informe o valor do terceiro lado:"))

if(num1 == num2) and (num2 == num3):
    print("esse triangulo é equlatero")

elif (num1 == num2 or num2 == num3 or num1 == num3):
    print("o triangulo é isósceles")

else:
    print("o triangulo é escaleno")