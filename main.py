from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

def ler_cotacao(ativo):
    cotacao = web.DataReader(f'{ativo}.SA', data_source='yahoo', start='01/01/2020', end='01/01/2022')
    print(cotacao)
    #cotacao["Adj Close"].plot()
    #plt.show()

def main():
    tabela_empresas = pd.read_excel("acoes.xlsx")
    #print(tabela_empresas)
    for empresa in tabela_empresas['Ativo']:
        print(empresa[1])
        ler_cotacao(empresa)

main()

#janela = Tk()
#janela.title("Cotações Ibovespa")

#texto_orientacao = Label(janela, text="Clique no botão para ver as cotações")
#texto_orientacao.grid(column=0, row=0)

#botao = Button(janela, text="Buscar cotações do Ibovespa", command=atualizar_cotacoes())
#botao.grid(column=0, row=1)




#janela.mainloop()