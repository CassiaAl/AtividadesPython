dol = float(5.42)

print('Conversão')
escolha = str(input('Escolha "Dolar" para converter para dolar ou "Real" para converter para real:\n'))
match escolha:
    case "Dolar":
        x=float(input('Digite o valor em reais, R$'))
        print('$',x*dol,' Dolares')
    case "Real":
        x=float(input('Digite o valor em dolar, R$'))
        print('R$',x/dol,)