# Classe básica de usuário

class Usuario(object):

    def __init__(self, nome:str,email:str,senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha
