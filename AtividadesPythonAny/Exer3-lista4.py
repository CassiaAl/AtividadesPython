print("**************")
print("     PROGRAMA SOMA    ")
print("**************")

n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, n + 1):
    soma += i

print(f"A soma de todos os números inteiros de 1 a {n} é: {soma}")