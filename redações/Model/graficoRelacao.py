
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

class GraficoRelacao:
    '''Classe para gráfico da estrutura argumentativa da redação'''

    def __init__(self):
        self.arg_from = []
        self.arg_to = []

    def set_relacao(self, relacao):
        '''setar relações para construção do gráfico'''
        self.arg_from.append(relacao.arg1)
        self.arg_to.append(relacao.arg2)

    def criar_grafico(self):
        '''Criar gráfico das relações'''
        data_frame = pd.DataFrame({'from':self.arg_from, 'to':self.arg_to})

        grafico = nx.from_pandas_edgelist(data_frame, 'from', 'to', create_using=nx.DiGraph() )

        nx.draw(grafico, with_labels=True, node_size=1500, alpha=0.3, arrows=True)

        plt.show()
