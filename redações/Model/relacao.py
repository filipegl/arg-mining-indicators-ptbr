class Relacao:
    def __init__(self, nome, arg1, arg2):
        self.nome = nome
        self.arg1 = arg1
        self.arg2 = arg2

    def __str__(self):
        return self.nome
