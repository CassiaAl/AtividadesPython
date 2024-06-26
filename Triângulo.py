
num1 = 0
num2 = 0
num3 = 0

# Exibindo o menu
print("=======================")
print("DESCUBRA SEU TRIÂNGULO!")
print("=======================")

# Solicitando os lados do triângulo
num1 = int(input("Digite o número de um dos lados: "))
num2 = int(input("Digite o número do 2º lado: "))
num3 = int(input("Digite o número do 3º lado: "))

# Classificando o triângulo
match (num1, num2, num3):
    case (a, b, c) if a == b == c:
        print("Seu triângulo é equilátero!")
    case (a, b, c) if a != b and a != c and b != c:
        print("Seu triângulo é escaleno!")
    case _:
        print("Seu triângulo é isósceles!")
