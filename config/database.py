
class Database(object):

    def __init__(self,chave,valor):
        self.chave = chave
        self.valor = valor

    def estrutura(self):
        banco = {}