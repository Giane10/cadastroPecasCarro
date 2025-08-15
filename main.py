# Início da definição da classe 'peca' ######################################

class Peca:
    def __init__(self, in_Id: int, in_nome: str, in_fabric: str, in_preco: int):
        self.Id: int = in_Id
        self.nome: str = in_nome
        self.fabric: str = in_fabric
        self.preco: int = in_preco

    def MostraRegistro(self):
        print()  # pular uma linha
        print(f'Registro #{self.Id}')
        print(f'Peça: {self.nome}')
        print(f'Fabricante: {self.fabric}')
        print(f'Preço: ${self.preco}')
        print()  # pular uma linha

    # Método que retorna os valores das variáveis internas da classe
    def GetRegistro(self):
        return {'Id': self.Id, 'nome': self.nome, 'fabricante': self.fabric, 'preço': self.preco}


# FIM da classe 'peca' #######################################

# Início do Main ###################################################################

# Rotina para inserção dos dados das peças
registro = ['zero']
Reg_Id = 0

while True:
    print('Selecione uma ação: ')
    print('1 - Adicionar Peça')
    print('2 - Mostrar todas as peças')
    print('3 - Mostrar peça por nome')
    print('4 - Sair')
    opcao = input('>>> ')

    if opcao == '1':

        Reg_Id += 1
        while True:
            nomeReg = input('Inserir o nome da peça >> ')
            fabricReg = input('Inserir o fabricante >> ')

            while True:
                try:
                    precoReg = int(input('Inserir o preço >> '))
                    break
                except:
                    print('inserir apenas números !')
                    continue

            regPeca = Peca(in_Id=Reg_Id, in_nome=nomeReg, in_fabric=fabricReg, in_preco=precoReg)
            registro.append(regPeca)
            registro[Reg_Id].MostraRegistro()
            break

    elif opcao == '2':
        for i in range(1, len(registro)):
            registro[i].MostraRegistro()

    elif opcao == '3':
        nome_peca = input("Digite o nome da peça que deseja visualizar: ")
        encontrada = False
        for i in range(1, len(registro)):
            regGot = registro[i].GetRegistro()
        # print(regGot) # printa a variável que recebe a resposta do
        # método GetRegistro() para debug
            if regGot['nome'].lower() == nome_peca.lower():
                print("\nRegistro da peça:")
                registro[i].MostraRegistro()
                encontrada = True
                break

        if not encontrada:
            print(f"\nA peça '{nome_peca}' não foi encontrada.")

    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Opção inválida, tente novamente !')

# FIM do Main ###################################################################
