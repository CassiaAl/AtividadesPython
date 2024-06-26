print("********************************")
print("    COTAÇÃO     ")
print("********************************")

Moeda = str(input("Informe se a conversão desejada é para dólar ou euro (escreva 1 para dólar e 2 para euro):"))
Valor = float(input("Informe o valor desejado para a conversão:"))

if Moeda == 1:
    print ("A conversão de real para dólar é", Valor%5.27)
elif Moeda == 2:
    print ("A conversão de real para euro é", Valor%5.60)