import random
tigrinho = random.randint(1, 100)
import os
import time

print("**********************")
print("   Jogo Adivinhação")
print("**********************")

tentativas = 10

while tentativas > 0 :
    print("Você tem ", tentativas, "tentativas")
    num = int(input("Digite um número inteiro de 1 a 100 e tente acertar o número da sorte: "))
    os.system("cls")
    if num == tigrinho:
        os.system("cls")
        print("Parabéns você acertou o número da sorte (",tigrinho,")")
        time.sleep(10)
        break

    elif num > tigrinho:
        print("O número digitado (" ,num, ") é maior que o número da sorte!")

    else:
        print("O número digitado (", num, ") é menor que o número da sorte!")

    tentativas -= 1

if tentativas == 0:
    os.system("cls")
    print("Você esgotou todas as tentativas. O número da sorte era", tigrinho)
    time.sleep(10)