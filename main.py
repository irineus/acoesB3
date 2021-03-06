# https://www.youtube.com/watch?v=NkrwHaY3oBY&t=99s


from alpha_vantage.timeseries import TimeSeries
from portfolio import Portfolio


# def ler_cotacao(ativo):
#    cotação = web.DataReader(f'{ativo}.SA', data_source='yahoo', start='01/01/2020', end='01/01/2022')
#    print(cotacao)
#     cotacao["Adj Close"].plot()
#     plt.show()


def main():
    api_key = "6IVMPQEIHN2R3JJ"
    ts = TimeSeries(key=api_key, output_format="pandas")

    p = Portfolio('Stock Portfolio')
    p.parse_portfolio()

    for stock in p.stocks:
        print(stock.ticker)
        print(stock.shares)
        print(stock.buyPrice)


#    tabelas_acoes = {}

#    for ação in carteira["Ativo"]:
#        data, meta_data = ts.get_daily_adjusted(f"{ação}.SAO", outputsize="full")
#        print(data)
#        tabela_ações[ação] = data
#        carteira.loc[carteira["Ativo"] == ação, "Cotação"]


main()

# janela = Tk()
# janela.title("Cotações Ibovespa")

# texto_orientacao = Label(janela, text="Clique no botão para ver as cotações")
# texto_orientacao.grid(column=0, row=0)

# botao = Button(janela, text="Buscar cotações do Ibovespa", command=atualizar_cotacoes())
# botao.grid(column=0, row=1)


# janela.mainloop()
