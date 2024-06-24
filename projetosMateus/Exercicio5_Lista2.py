print("**************************")
print("           MENU           ")
print("**************************")

num1 = float(input("Digite um numero: "))

if num1 % 6 == 0 or num1 % 9 == 0 or num1 % 10 == 0 or num1 % 4 == 0:
    print("Numero",num1," nao é  primo")

else:
    print("Numero",num1," é  primo")