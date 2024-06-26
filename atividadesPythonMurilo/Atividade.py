resul = float(0)
def inicio():
    global resul
    x = (float(input('Digite um numero: ')))
    y = (float(input('Digite outro numero: ')))
    resul = resul + x + y
    print('Resultado = ', resul)
    inicio()
inicio()
