print("***************")
print("   Salario ")
print("***************")

nivel_1 = 12.75
nivel_2 = 17.65
nivel_3 = 25.45

dias = 22

hora = 8

nivel_professor = str(input("Informe qual o nivel do professor: 1/2/3\n"))

match nivel_professor:
    case"1":
        print(f"O seu salário é equivalente a R$ {nivel_1 * dias * hora}")
    case "2":
        print(f"O seu salário é equivalente a R$ {nivel_2 * dias * hora}")
    case "3":
        print(f"O seu salário é equivalente a R$ {nivel_2 * dias * hora}")

