soma = 0

num = int(input("Digite um valor: "))

for i in range(1, num + 1):
    soma += i
print("O resultado de 1 a ", num, " é ", soma)