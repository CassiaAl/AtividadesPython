def main():
    # Solicita a idade do usuário

    idade = int(input("Digite sua idade: "))

    # Verifica se a idade é maior que 18

    if idade >= 18:
        print("Pode entrar, sua idade é compatível com a idade autorizada.")
    else:
        # Calcula quantos anos faltam para o usuário ter 18 anos

        anos_faltam = 18 - idade
        print(f"Os anos que faltam para você poder entrar são: {anos_faltam}")
