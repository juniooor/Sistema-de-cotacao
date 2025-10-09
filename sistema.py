from cotacao import Cotacao


class Sistema:

    def __init__(self):
        self.cotacoes = []

    def coletar_cotacoes(self, numero):
        print(f'\n Cotação {numero} --- ')
    
    fornecedor = input("Fornecedor: ")
    cotacao = Cotacao(fornecedor)

    num_pecas = int(input("Quantas peças?: "))

    for i in range(1, num_pecas+1):
        print(f' peça {i}')
        
