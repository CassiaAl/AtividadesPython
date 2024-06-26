
idadepermitida = 18

print("//////////////////")
print("  ENTRADA FESTA!  ")
print("//////////////////")


idade = int(input("Digite sua idade: "))


match (idade):
    case _ if idade >= 18:
        print("Pode entrar na festa!")
    case _ if idade < 18:
        print(f"Infelizmente você não poderá entrar, espere: {idadepermitida - idade} ano/s")
        print("ATÉ LOGO!")
    case _ if idade >= 200:
        print("Espera... Você ainda está vivo?")
