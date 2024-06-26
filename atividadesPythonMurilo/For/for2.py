import time
print('Contando de 0 a 100 com while...')
time.sleep(3)
i = int(0)
while(i<=100):
    print(i)
    i = i+1
print('\nContando de 0 a 10 com for...')
time.sleep(3)
numero = int(0)
for numero in [0,1,2,3,4,5,6,7,8,9,10]:
    print(numero)