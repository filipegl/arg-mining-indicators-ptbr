from nltk import tokenize 
from Model.graficoRelacao import GraficoRelacao

class Redacao:
    '''Classe da redacao'''
    def __init__(self):
        self.titulo = ''
        self.texto = ''
        self.sentencas = []
        self.paragrafos = []
        self.marcacao = []
        self.relacao = []

    def get_quantidade_de_marcacao(self):
        '''Recupera quantidade de marcações na redação (tese, argumento e PI)'''
        return len(self.marcacao)

    def get_quantidade_de_sentencas(self):
        '''Recupera quantidade de sentencas'''
        #print(len(self.sentencas))
        return len(self.sentencas)
   
    def get_palavras(self):
        return tokenize.word_tokenize(self.texto, language='portuguese') 
   
    def get_quantidade_palavras(self):
        palavras = tokenize.word_tokenize(self.texto, language='portuguese') 
        return len(palavras)

    def get_quantidade_do_rotulo(self, rotulo):
        quantidade_do_rotulo = 0
        for sentenca in self.sentencas:
            if sentenca.rotulo == rotulo:
                quantidade_do_rotulo += 1
        return quantidade_do_rotulo

    def criarGraficoRelacao(self):
        grafico_relacao = GraficoRelacao()
        for relacao in self.relacao:
            grafico_relacao.set_relacao(relacao)
        grafico_relacao.criar_grafico()
