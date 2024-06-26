
print("*********************************")
print("       PROGRAMA IMC PYTHON       ")
print("*********************************")

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura:'))

imc = peso / (altura * 2)

print('Seu IMC é : {0}'.format(imc))

if imc <= 18.5:
    print('Você esta muito abaixo do peso!')
elif imc > 18.5 and imc <= 24.9:
    print('Você está no peso ideal!')
elif imc > 24.9 and imc <= 29.9:
    print('Voce está levemente acima do peso!')
else:
    print('Você esta com obesidade!!!')