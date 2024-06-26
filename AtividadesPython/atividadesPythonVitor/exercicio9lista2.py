print("*****************")
print("  Positivo soma")
print("*****************")

num = int(input("Digite um número positivo: "))
total = num

while num > 0:
        print("O total é ",total)
        num = int(input("Digite um número novamente: "))
        total = total + num
