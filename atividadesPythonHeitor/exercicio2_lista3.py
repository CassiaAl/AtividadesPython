def permite_entrada(idade):
    if idade >= 18:
        print("Você tem permissão para entrar na festa - Seja Bem-Vindo")

    else:
        print("Você não tem permissão para entrar na festa, ainda é necessário esperar ", 18 - idade, "ano/anos")


print("*******************")
print("  Permite Entrada")
print("*******************")

idade = int(input("Digite sua idade para verificarmos se você tem permissão: "))

permite_entrada(idade)