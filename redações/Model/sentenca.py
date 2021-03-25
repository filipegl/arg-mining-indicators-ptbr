
from nltk import tokenize   

class Sentenca:

    def __init__(self, identificador, texto, rotulo):
        self.identificador = identificador
        self.texto = texto
        self.rotulo = rotulo
        self.recursos = []
        self.analise_cogroo = ''

    def __repr__(self):
        return self.texto

    def getValoresDosRecursos(self):
        self.ordenaRecursos(self.recursos)
        recursos = [recurso.valor for recurso in self.recursos]
        return recursos

    def getQuantidadePalavras(self):
        palavras_tokenize = tokenize.word_tokenize(self.texto, language='portuguese')
        return len(palavras_tokenize)
    
    def ordenaRecursos(self, recursos):
        return sorted(recursos, key=lambda x: x.identificador)

    def getRotulo(self):
        if self.rotulo == 'Tese':
            return 1
        if self.rotulo == 'Argumento':
            return 2
        if self.rotulo == 'PI':
            return 3
        return 0
