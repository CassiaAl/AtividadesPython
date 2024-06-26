print("*****************************************")
print("    PROGRAMA Conversão de horas PYTHON    ")
print("*****************************************")

def converter_horas_minutos(num_horas):
    minutos = num_horas * 60
    return minutos

def convert_horas_segundos(num_horas):
    minutes = converter_horas_minutos(num_horas)
    segundos = minutes * 60
    return segundos

def converter_minutos_horas(num_nim):
    mhoras = num_nim/ 60
    return mhoras

def converter_minutos_segundos(num_nim):
    ssegundos = num_nim * 60
    return ssegundos



def converter_segundos_horas(num_segundos):
    segundos_horas = num_segundos/3600
    return segundos_horas

def convert_segundos_minutos(num_segundos):
    h_minutos = converter_segundos_horas(num_segundos)
    m_segundos = h_minutos * 60
    return m_segundos


escolha=True
while escolha:
    print("""
    1.Converter horas
    2.Converter Minutos
    3.Converter Segundos
    4.Exit/Quit/Saída
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        print('\n')
        hora = float(input('Número de horas que '
                           'pretende converter: '))
        print('\n')
        minuto = converter_horas_minutos(hora)
        segundos = convert_horas_segundos(hora)
        print(str(hora) + ' horas são '+ str(minuto)+' minutos.')
        print(str(hora) + ' horas são '
                          '' + str(segundos) + ' segundos.')
    elif escolha=="2":
      print('\n')
      minutos = float(input('Número de minutos que pretende converter: '))
      print('\n')
      mhoras=converter_minutos_horas(minutos)
      ssegundos= converter_minutos_segundos(minutos)
      print(str(minutos) + ' minutos são '
                           '' + str("{0:.2f}".format(round(mhoras, 2))) + ' horas.')
      print(str(minutos) + ' minutos são ' + str(ssegundos) + ' segundos.')

    elif escolha=="3":
        print('\n')
        segundo = float(input('Número de segundos que pretende converter: '))
        print('\n')
        shoras = converter_segundos_horas(segundo)
        sminutos = convert_segundos_minutos(segundo)
        print(str(segundo) + ' segundos são '
                             '' + str("{0:.2f}".format(round(shoras, 2))) + ' horas.')
        print(str(segundo) + ' segundos são'
                             ' ' + str("{0:.2f}".format(round(sminutos, 2))) + ' minutos.')
    elif escolha=="4":
      print("\n Adeus")
      escolha = None
    else:
       print("\n Escolha não válida.\n Tente outra vez.")