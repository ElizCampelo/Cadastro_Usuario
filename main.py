import PySimpleGUI as sg
class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        layout = [
            [sg.Text('Nome: '), sg.Input(key = 'nome')],
            [sg.Text('Idade: '), sg.Input(key = 'idade')],
            [sg.Text('Quais provedores de E-mail São Aceitos:?')],
            [sg.Checkbox('Gmail', key = 'gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox("Yahoo",key='yahoo')],
            [sg.Text('Aceita Cartão')],
            [sg.Radio('Sim', 'Cartões', key='aceitaCartao'), sg.Radio('Não', 'Cartões', key='naoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(50,20),key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(60,20))]
        ]
        self.janela= sg.Window('Dados do Usuário').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Outlook: {aceita_outlook}')
            print(f"Aceita Yahoo: {aceita_yahoo}")
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não Aceita Cartão: {nao_aceita_cartao}')
            print(f'velocidade Script: {velocidade_script}')

tela=TelaPython()
tela.Iniciar()
