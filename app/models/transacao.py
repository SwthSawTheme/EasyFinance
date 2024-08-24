# Classe básica de transação

class Transacao(object):

    def __init__(self,valor:float,data:str,descricao:str,tipo:tuple,categoria):
        self.valor = valor
        self.data = data
        self.descricao = descricao
        self.tipo = () # TipoTransacao (enumeração: RECEITA, DESPESA)
        self.categoria = categoria
