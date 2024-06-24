print("*****************************************")
print("     PROGRAMA Conversão PYTHON        ")
print("*****************************************")

reais = float(input("Informe a quantidade de reais para conversão: R$ "))
cotacao = float(input ("Informe se a conversão será para dolar (1) ou euro (2):  "))
if ( cotacao == 1):
    print("A conversão de real para Dolar é ", reais / 5.43)

elif ( cotacao == 2):
     print("A conversão de real para Euro é ", reais/5.83)

