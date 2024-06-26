print("********************")
print("    Ano bissexto")
print("********************")

ano = int(input("Digite um ano para verificar se o mesmo é bissexto: "))

if ano % 4 == 0:
    print("O ano " ,ano, " é bissexto")

else:
    print("O ano " ,ano, " não é bissexto")
