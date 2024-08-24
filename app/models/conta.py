# Classe básica de conta

class Conta(object):

    def __init__(self,nome_conta:str,saldo_inicial:float):
        self.nome_conta = nome_conta
        self.saldo_inicial = 0
    
    def adicionarTransacao(self,transacao):
        pass

    def calcularSaldoAtual(self):
        pass