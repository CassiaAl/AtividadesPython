from unittest import case

print("***************")
print("Leitor de sexo ")
print("***************")

sexo = str(input("Informe seu sexo [M/F]: "))

match sexo:
    case "M":
        print("Masculino.")
    case "F":
        print("Feminino.")
    case _:
        print("Sexo invalido.")