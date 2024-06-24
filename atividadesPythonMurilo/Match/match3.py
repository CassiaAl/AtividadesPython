nivel1 = float(12.75)
nivel2 = float(17.65)
nivel3 = float(25.45)
nivel = input('escolha entre nivel 1, 2 ou 3: ')
match nivel:
    case "1":
        horas=float(input('Digite o tanto de horas trabalhadas: '))
        print(nivel1*horas," Reais")
    case "2":
        horas = float(input('Digite o tanto de horas trabalhadas: '))
        print(nivel2 * horas, " Reais")
    case "3":
        horas = float(input('Digite o tanto de horas trabalhadas: '))
        print(nivel3 * horas, " Reais")
