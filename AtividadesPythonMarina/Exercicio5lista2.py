print("*****************************************")
print("     PROGRAMA PRIMO PYTHON        ")
print("*****************************************")

numero = int(input("Digite um número:"))
if numero < 0:
    print("Número inválido. Digite apenas valores positivos")
if numero == 0 or numero == 1:
    print(f"{numero} é um caso especial.")
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print(f"{numero} não é primo, pois 2 é o único número par primo.")
    else:
        x = 3
        while x < numero:
            if numero % x == 0:
                break
            x = x + 2
        if x == numero:
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo, pois é divisível por {x}")

