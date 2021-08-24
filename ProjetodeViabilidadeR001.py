from PySimpleGUI import PySimpleGUI as sg





# Frames
sg.theme('Reddit')
Frame1_construção = [

    [sg.T('Área Construida'), sg.Input(0, key='areaconstruida', size=(15, 1))],
    [sg.T('Valor da Obra   '), sg.Input(0, key='valorobra', size=(15, 1))]
]

Frame2_lote = [

    [sg.T('Metragem (m²)'), sg.Input(0, key='metragem', size=(15, 1))],
    [sg.T('Valor Do Lote '), sg.Input(0, key='valorlote', size=(15, 1))]
]

Frame3_encargos = [

    [sg.T('Imposto     '), sg.Input(0, key='imposto', size=(15, 1)), sg.T('(%)')],
    [sg.T('Corretagem'), sg.Input(0, key='corretagem', size=(15, 1)), sg.T('(%)')],
    [sg.T('Projetos     '), sg.Input(0, key='projetos', size=(15, 1))],
    [sg.T('Imagens     '), sg.Input(0, key='imagens', size=(15, 1))]
]

# Layout Geral Despesas

tabdespesas_layout = [
    [sg.Frame('Construção', Frame1_construção, font='Any 12', title_color='blue'),
     sg.Frame('Lotes', Frame2_lote, font='Any 12', title_color='blue')],
    [sg.Frame('Encargos', Frame3_encargos, font='Any 12', title_color='blue')]
]

# layout Receitas

tabreceitas_layout = [
    [sg.T('Início das Vendas'), sg.Input(6, key='iniciovendas', size=(10, 1)), sg.T(' º Mês')],
    [sg.T('Valor de venda (m²)'), sg.Input(0, key='Venda', size=(10, 1))],
    [sg.T('Número de unidades'), sg.Input(0, key='nunidades', size=(10, 1))],
]

# Layout Inf. Gerais
sg.theme('Reddit')
tabinfgeral_layout = [
    [sg.T('Mês de Início      '), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], key='mes_inicio'), sg.T('          Duração'),
     sg.Input(13, key='duração', size=(10, 1)), sg.T('(Meses)')],
    [sg.T('Ano'), sg.Input(2021, key='ano', size=(10, 1)), sg.T('TMA      '), sg.I(0, key='TMA', size=(10, 1)),
     sg.T('(%)')],

    [sg.Text(' ')],
    [sg.TabGroup([[sg.Tab('Despesas', tabdespesas_layout), sg.Tab('Receitas', tabreceitas_layout)]])]
]

# Fluxo de caixa

# Despesas não Contábeis
desplayout = [
    [sg.Text('Descrição'), sg.Text('                                                                     Valor'),
     sg.T('      Contabilizar a partir de')],
    [sg.Input(key='desc1'), sg.Input(0, key='vdesc1', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração1'), ],
    [sg.Input(key='desc2'), sg.Input(0, key='vdesc2', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração2'), ],
    [sg.Input(key='desc3'), sg.Input(0, key='vdesc3', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração3'), ],
    [sg.Input(key='desc4'), sg.Input(0, key='vdesc4', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração4'), ],
    [sg.Input(key='desc5'), sg.Input(0, key='vdesc5', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração5'), ],
    [sg.Input(key='desc6'), sg.Input(0, key='vdesc6', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração6'), ],
    [sg.Input(key='desc7'), sg.Input(0, key='vdesc7', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração7'), ],
    [sg.Input(key='desc8'), sg.Input(0, key='vdesc8', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração8'), ],
    [sg.Input(key='desc9'), sg.Input(0, key='vdesc9', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração9'), ],
    [sg.Input(key='desc10'), sg.Input(0, key='vdesc10', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração10'), ],
    [sg.Input(key='desc11'), sg.Input(0, key='vdesc11', size=(10, 1)), sg.Combo(
        ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro'], size=(18, 1), key='duração11'), ],
]
# Layout Principal

sg.theme('Reddit')
layout = [
    [sg.Text('NOME DA EMPRESA'), sg.Input(key='nome_empresa')],
    [sg.Text('EMPREENDIMENTO  '), sg.Input(key='empreendimento')],

    [sg.Text(' ')],

    [sg.TabGroup(
        [[sg.Tab('Informações Gerais', tabinfgeral_layout), sg.Tab('Despesas Não Contabilizadas', desplayout)]])],
    [sg.Button('Prosseguir'), sg.Button('Sair')]
]


janela1= sg.Window('Estudo de Viabilidade', layout=layout, finalize=True)

values = janela1.Read()
nome_empresa = str(values['nome_empresa'])
empreendimento = str(values['empreendimento'])
mes_inicio = str(values['mes_inicio'])
duração = int(values['duração'])
ano = int(values['ano'])
iniciovendas = int(values['iniciovendas'])
TMA = float(values['TMA'])
areaconstruida = float(values['areaconstruida'])
valorobra = float(values['valorobra'])
metragem = float(values['metragem'])
valorlote = float(values['valorlote'])
imposto = float(values['imposto'])
corretagem = float(values['corretagem'])
projetos = float(values['projetos'])
imagens = float(values['imagens'])
Venda = float(values['Venda'])
desc1 = (values['desc1'])
vdesc1 = float(values['vdesc1'])
duração1 = str(values['duração1'])
desc2 = str(values['desc2'])
vdesc2 = float(values['vdesc2'])
duração2 = str(values['duração2'])
desc3 = str(values['desc3'])
vdesc3 = float(values['vdesc3'])
duração3 = str(values['duração3'])
desc4 = str(values['desc4'])
vdesc4 = float(values['vdesc4'])
duração4 = str(values['duração4'])
desc5 = str(values['desc5'])
vdesc5 = float(values['vdesc5'])
duração5 = str(values['duração5'])
desc6 = str(values['desc6'])
vdesc6 = float(values['vdesc6'])
duração6 = str(values['duração6'])
desc7 = str(values['desc7'])
vdesc7 = float(values['vdesc7'])
duração7 = str(values['duração7'])
desc8 = str(values['desc8'])
vdesc8 = float(values['vdesc8'])
duração8 = str(values['duração8'])
desc9 = str(values['desc9'])
vdesc9 = float(values['vdesc9'])
duração9 = str(values['duração9'])
desc10 = str(values['desc10'])
vdesc10 = float(values['vdesc10'])
duração10 = str(values['duração10'])
desc11 = str(values['desc11'])
vdesc11 = float(values['vdesc11'])
duração11 = str(values['duração11'])


from RepetiçõesMensaisObra import ciclo_mes as cm
from RepetiçõesMensaisVenda import ciclo_mesvenda as cmv


layout_fcaixaobra = [
[sg.T('Mês'),sg.T('                   Porcentagem concluída')],
    [sg.T('')],
    cm(mes_inicio,duração,ano),
[sg.Button ('Voltar'), sg.Button('Próximo')],
]



layout_fcaixavenda = [
[sg.T('Mês'),sg.T('                   Unidades Vendidas')],
    cmv(mes_inicio,duração,ano,iniciovendas),
[sg.Button ('Anterior'), sg.Button('Gerar Relatório')]
]

janela3= sg.Window('Fluxo de Venda', layout=layout_fcaixavenda, finalize=True)





janela1,janela2,janela3 = janela_1(),None,None


while True:  # Event Loop
    window,event, values = sg.read_all_windows()

    if window == janela1 and event == 'Prosseguir':

        janela2= sg.Window('Fluxo de Obra', layout=layout_fcaixaobra, finalize=True)
        janela1.Hide()

    if window == janela2 and event == 'Voltar':
        janela1
        janela2.Hide()
    if window == janela2 and event == 'Próximo':
        janela3= sg.Window('Fluxo de Venda', layout=layout_fcaixavenda, finalize=True)
        janela2.Hide()
    if window == janela3 and event == 'Anterior':
        janela2
        janela3.Hide()
    if window == janela1 and event == 'Sair' or sg.WIN_CLOSED:
        break