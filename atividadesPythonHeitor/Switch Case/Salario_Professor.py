print("*********************")
print("  Salário Professor  ")
print("*********************")

nivel1 = 12.75
nivel2 = 17.65
nivel3 = 25.45
diasuteis = 22
hora = 8

nivelprof = str(input("Você é professor de qual nível [1/2/3]: "))

match nivelprof:
    case "1":
        print(f"O seu salário é equivalente a R$ {nivel1 * diasuteis * hora}")

    case "2":
        print(f"O seu salário é equivalente a R$ {nivel2 * diasuteis * hora}")

    case "3":
        print(f"O seu salário é equivalente a R$ {nivel3 * diasuteis * hora}")
