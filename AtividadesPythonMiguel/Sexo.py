sexo = 0

print("_______________________")
print("SEXO VÁLIDO OU INVÁLIDO")
print("^^^^^^^^^^^^^^^^^^^^^^^")

print("Digite o seu sexo: ")
print("- 1 M\n- 2 F")

sexo = int(input())

match sexo:
    case 1:
        print("Sexo válido")
    case 2:
        print("Sexo válido")
    case _:
        print("Sexo inválido")
