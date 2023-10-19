import requests
import pandas as pd
from datetime import datetime
from tkinter import *

def pegar_cotacoes_DOL():

    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    Texto_cotacao['text'] = f'''
    dol: {cotacao_dolar}'''


def pegar_cotacoes_EURO():

    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    Texto_cotacao['text'] = f'''
    euro : {cotacao_euro}'''

def pegar_cotacoes_BTC():

    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]
    Texto_cotacao['text'] = f'''
    bct : {cotacao_btc}'''





# JANELA
janela = Tk ()
janela.title ('cotação das moedas :D')

#TXT 1
textodeorientação = Label (janela, text = 'selecione uma moeda')
textodeorientação.grid (column=1, row= 0, padx= 10, pady= 10)

#BOTÃO EURO
botao_euro = Button (janela, text= "Euro", command=pegar_cotacoes_EURO)
botao_euro.grid (column=0, row= 1, padx= 10)


#BOTÃO dol
botao_dol = Button (janela, text= "dol", command=pegar_cotacoes_DOL)
botao_dol.grid (column=1, row= 1, padx= 10)

#BOTÃO btc
botao_btc = Button (janela, text= "btc", command=pegar_cotacoes_BTC)
botao_btc.grid (column=2, row= 1, padx= 10)

#TEXTO DE COTAÇÃO
Texto_cotacao =Label (janela, text ="")
Texto_cotacao.grid  (column=1, row= 2, padx= 10, pady= 10)



janela.mainloop ()