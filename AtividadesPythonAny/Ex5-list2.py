print("************")
print("    NÚMEROS PRIMOS  ")
print("************")

num1 = int(input("Digite o valor do número:"))
if (num1 % 4 == 0 or num1 % 6 ==0 or num1 % 10 == 0):
        print ("O seu número não é primo")
else :
        print ("O seu número é primo")