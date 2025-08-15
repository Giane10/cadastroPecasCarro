# Criação da classe Peça

class Peca:
    def __init__(self, in_RegId: int, in_nome: str, in_fabric: str, in_preco: int):
        self.RegId: int = in_RegId
        self.nome: str = in_nome
        self.fabric: str = in_fabric
        self.preco: int = in_preco

    def MostraReg(self):
        print()  # pular uma linha
        print(f'Registro #{self.RegId}')
        print(f'O nome da peça é {self.nome}')
        print(f'O nome do fabricante da {self.nome} é {self.fabric}')
        print(f'O Valor da peça {self.nome} do fabricante {self.fabric} é ${self.preco}')
        print()  # pular uma linha




