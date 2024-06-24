dolar = 5.29
euro = 5.63

# Imprimindo o cabeçalho do programa
print("****************")
print("Conversor de Dólar e Euro")
print("****************")

# Solicitando ao usuário o valor em reais para conversão

valor_real = float(input("Digite o valor que deseja converter: "))

# Perguntando ao usuário para qual moeda ele deseja converter

print("Escolha para qual moeda será convertido:")
print("-1 US$ Dólar\n-2 € Euro")
escolha = int(input())

# Verificando a escolha do usuário e fazendo a conversão

if escolha == 1:
    # Convertendo para Dólar
    valor_convertido = valor_real * dolar
    print("A quantia é: US$", valor_convertido)
elif escolha == 2:
    # Convertendo para Euro
    valor_convertido = valor_real * euro
    print("A quantia é: €", valor_convertido)
else:
    # Se o usuário escolher uma opção inválida
    print("Opção inválida! Por favor, escolha 1 para Dólar ou 2 para Euro.")
