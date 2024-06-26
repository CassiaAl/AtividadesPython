print("**************************")
print("     Programa cotação  ")
print("**************************")

conver = int(input("Informe se a conversão será para dólar ou euro (escreva 1 para dólar e 2 para euro):  "))
num = float(input("informe o valor para a conversão:  "))

if (conver == 1):
    print("A conversão de real para dólar é:  ", num/5.43)

elif (conver == 2):
    print("A conversão de real para euro é:  ", num/5.83)