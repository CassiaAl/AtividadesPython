def funcao():
    print('Soma até um valor acumulado de 100')
    resultado = float(0)
    while resultado < 100:
        x = int(input('Digite um valor para ser acumulado: '))
        resultado = resultado + x
        print(resultado)
    else:
        print('Resultado =',resultado,' Programa finalisado')

funcao()
