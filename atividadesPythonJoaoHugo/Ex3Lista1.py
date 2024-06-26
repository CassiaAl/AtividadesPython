from datetime import datetime
def conversor_de_horas():

    #By: João Hugo
    #Data: 24/06

    print("---------------------------------")
    print("       Conversor de Hora         ")
    print("---------------------------------")


    # pedindo para inserir no formato HH/MM
    hora_str = input("insira o horário atual(no formato HH:MM): ")

     # entrada para objeto datetime
    hora = datetime.strptime(hora_str, '%H:%M')

    #Converter em minutos
    minutos = hora.hour * 60 + hora.minute

    # exibindo o resultado
    print(f"O horário atual em minutos é: {minutos}")

# chamando a função
conversor_de_horas()