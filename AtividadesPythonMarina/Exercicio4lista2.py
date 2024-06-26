print("*****************************************")
print("     PROGRAMA número maior PYTHON        ")
print("*****************************************")

def maior(x,y):
  if x>y:
    print("O primeiro valor digitado,",x,", é maior que o segundo,",y,".")
  elif x==y:
    print("Ambos os valores digitados são iguais",x,"=",y,".")
  else:
    print("O segundo valor digitado,",y,", é maior que o primeiro,",x,".")
x=int(input("Digite o primeiro número: "))
y=int(input("Digite o segundo número: "))
maior(x,y)
