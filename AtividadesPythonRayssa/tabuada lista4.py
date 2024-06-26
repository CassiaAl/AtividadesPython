print("*******************************")
print("     Pograma tabuada    ")
print("*******************************")

numero = int(input("Digite um número para ver sua tabuada: "))

i = 1

print(f"\nTabuada de {numero}:")
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1