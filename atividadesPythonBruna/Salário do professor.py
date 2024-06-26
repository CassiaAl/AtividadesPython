nivel = input('Escolha o nível entre 1,2,3: ')
nivel1 = 12.75
nivel2 = 17.65
nivel3 = 25.45

match nivel:
    case '1':
        horas_aula = float(input('Digite a quantidade de horas dadas: '))
        print(horas_aula*12.75)

    case '2':
        horas_aula = float(input('Digite a quantidade de horas dadas: '))
        print(horas_aula * 17.65)

    case '3':
        horas_aula = float(input('Digite a quantidade de horas dadas: '))
        print(horas_aula * 25.45)
