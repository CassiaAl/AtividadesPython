print("******************")
print("  Leitor de sexo  ")
print("******************")

sexo = str(input("Informe seu sexo [M/F]: "))

match sexo:
    case "M":
        print("Sexo válido!")

    case "F":
        print("Sexo válido!")

    case _:
        print("Sexo inválido!")