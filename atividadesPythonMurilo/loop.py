a = int(0)
def loop():
    global a
    print(a)
    a = a + 1

    loop()
loop()
