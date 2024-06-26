print("------------------------")
print("     NÚMEROS PRIMOS     ")
print("------------------------")

num1 = int(input("Digite o número para descobrir se é primo: "))

if num1 % 4 == 0 or num1 % 6 == 0 or num1 % 10 == 0:
    print("Seu número não é primo")
else:
    print("Seu número é primo")