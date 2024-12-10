valor = float(input("Digite o valor para a conversão: "))
operacao = float(input("Digite 1 para dólar e 2 para euro: "))
if(operacao==1):
    print("O valor de ", valor ," em dólar é: ", valor*5.38)
if(operacao==2):
    print("O valor de ", valor ," em euro é : ", valor*5.78)