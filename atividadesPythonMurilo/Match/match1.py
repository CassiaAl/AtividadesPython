print('"1", "2", "3"')
x = str(input("Digite uma das opções, que defina seu namorado: "))
match x:
    case '1':
        print('Opção 1, Legal')
    case '2':
        print('Opção 2, Mais ou menos')
    case '3':
        print('Opção 3, Chato')