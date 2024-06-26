
dolar = float(5.30)
euro = float(5.60)
escolha = str(input("Escolha sua forma de converção 'D' de dólar ou 'E' de euro: "))

print('Valor para converter: ')

match escolha:
    case 'D':
        valoreal = float(input('Escreva o valor em Reais: R$ '))
        print('O valor convertido em euros seria' ,valoreal / dolar, 'esse' )

    case 'E':
        valoreal = float(input('Escreva o valor em Reais: R$'))
        print('O valor convertido em dólar seria' ,valoreal / euro, 'esse')
