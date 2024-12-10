print("")
num = int(input("Digite um número: "))
if num % 4 == 0 or num % 6 == 0 or num % 9 == 0 or num % 10 == 0:
    print("O número digitado não é primo!")
else:
    print("O número é primo! :)")