from PySimpleGUI import PySimpleGUI as sg


lista = []
def ciclo_mesvenda (mes_inicio,duração,ano,iniciovendas):


    if mes_inicio == 'Janeiro':
        key= 1

    if mes_inicio == 'Fevereiro':
        key= 2

    if mes_inicio == 'Março':
        key= 3

    if mes_inicio == 'Abril':
        key= 4

    if mes_inicio == 'Maio':
        key= 5

    if mes_inicio == 'Junho':
        key= 6

    if mes_inicio == 'Julho':
        key= 7

    if mes_inicio == 'Agosto':
        key= 8

    if mes_inicio == 'Setembro':
        key= 9

    if mes_inicio == 'Outubro':
        key= 10

    if mes_inicio == 'Novembro':
        key= 11

    if mes_inicio == 'Dezembro':
        key= 12

    if mes_inicio == 'test 13':
        key=13

    if mes_inicio == 'test0':
        key=0

    if mes_inicio == 'test-1':
        key=-1

    for key in range (key+iniciovendas, key+duração):
            if key >12:
                key = key-13
                key=key+1

                if key== 1:
                    cont=1
                    if cont == 1:
                        ano=ano+1

            if key > 12:
                key = key - 13
                key = key + 1

                if key == 1:
                    cont = 1
                    if cont == 1:
                        ano = ano + 1

            if key > 12:
                key = key - 13
                key = key + 1

                if key == 1:
                    cont = 1
                    if cont == 1:
                        ano = ano + 1
            if key > 12:
                key = key - 13
                key = key + 1

                if key == 1:
                    cont = 1
                    if cont == 1:
                        ano = ano + 1



            t1 = [sg.T('Janeiro de ' + str(ano)), sg.Input(key='nunidadesJaneiro' + str(ano),size=(10,1))],
            t2 = [sg.T('Fevereiro de ' + str(ano)), sg.Input(key='nunidadesFevereiro' + str(ano),size=(10,1))],
            t3 = [sg.T('Março de ' + str(ano)), sg.Input(key='nunidadesMarço' + str(ano),size=(10,1))],
            t4 = [sg.T('Abril de ' + str(ano)), sg.Input(key='nunidadesAbril' + str(ano),size=(10,1))],
            t5 = [sg.T('Maio de ' + str(ano)), sg.Input(key='nunidadesMaio' + str(ano),size=(10,1))],
            t6 = [sg.T('Junho de ' + str(ano)), sg.Input(key='nunidadesJunho' + str(ano),size=(10,1))],
            t7 = [sg.T('Julho de ' + str(ano)), sg.Input(key='nunidadesJulho' + str(ano),size=(10,1))],
            t8 = [sg.T('Agosto de ' + str(ano)), sg.Input(key='nunidadesAgosto' + str(ano),size=(10,1))],
            t9 = [sg.T('Setembro de ' + str(ano)), sg.Input(key='nunidadesSetembro' + str(ano),size=(10,1))],
            t10 = [sg.T('Outubro de ' + str(ano)), sg.Input(key='nunidadesOutubro' + str(ano),size=(10,1))],
            t11 = [sg.T('Novembro de ' + str(ano)), sg.Input(key='nunidadesNovembro' + str(ano),size=(10,1))],
            t12 = [sg.T('Dezembro de ' + str(ano)), sg.Input(key='nunidadesDezembro' + str(ano),size=(10,1))],



            if key == 1:
                lista.append(t1)

            if key == 2:
                lista.append(t2)

            if key == 3:
                lista.append(t3)

            if key == 4:
                lista.append(t4)

            if key == 5:
                lista.append(t5)

            if key == 6:
                lista.append(t6)

            if key == 7:
                lista.append(t7)

            if key == 8:
                lista.append(t8)

            if key == 9:
                lista.append(t9)

            if key == 10:
                lista.append(t10)

            if key == 11:
                lista.append(t11)

            if key == 12:
                lista.append(t12)


    return lista