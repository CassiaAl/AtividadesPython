print("********************************")
print("   EXERCÍCIO 2  ")
print("********************************")


numero = int(input("Digite um número para vizualizar a tabuada: "))

i = 1

print(f"\nTabuada de {numero}:")
while i <= 20:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1