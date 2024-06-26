dolar = 5.43
euro = 5.83

print("$$$$$$$$$$$$$$$$$$$$$$$$$")
print("CONVERSOR DE DOLAR E EURO")
print("€€€€€€€€€€€€€€€€€€€€€€€€€")

real = float(input("Digite o valor a ser convertido: "))

converter = str(input("Digite se você quer converter para EURO ou DOLAR: "))

if converter == "EURO"or "Euro" or "euro":
    print("Seu valor em euro é: ", real/euro)
elif converter == "DOLAR" or "Dolar" or "dolar":
    print("Seu valor em Dolar é: ", real/dolar)


