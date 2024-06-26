

print ("bem-vindo a geração de cadastros")
nome = input("digite seu nome:")
print("Senhor(a)",nome)
idade = input("informe sua idade:")
print("muito bem ", nome, "você tem", idade, "anos")
idade_base1 = 18
idade1 = int (idade)
idade_base = int(idade_base1)

igual = idade_base == idade1
maior = idade_base > idade1
menor = idade_base < idade1

if (igual):
    print("pode prosseguir", nome)
if (maior) : print("você é menor de idade")
elif menor: print("você é menor de idade")




