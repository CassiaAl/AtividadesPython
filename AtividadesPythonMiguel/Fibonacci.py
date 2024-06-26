
a = 1
b = 2
def fibonacci():
    global a, b
    print("----------------------")
    print("SEQUENCIA DE FIBONACCI")
    print("----------------------")

    print("A sequencia até o vigésimo termo é: \n", a, ", ", b, ", ", end="")

    for i in range(2, 20):
        c = a + b
        print(c, ", ", end="")
        a = b
        b = c

fibonacci()
