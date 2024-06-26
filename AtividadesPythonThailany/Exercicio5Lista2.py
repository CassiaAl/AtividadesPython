print("******************")
print("   Número Primo")
print("******************\n")

numprimo = int(input("Digite o número que deseja verificar se é primo:\n "))

if numprimo % 6 == 0 or numprimo % 4 == 0 or numprimo % 10 == 0 or numprimo % 9 == 0:
    print("O número ",numprimo," não é primo")

else:
    print("O número ", numprimo, " é primo")