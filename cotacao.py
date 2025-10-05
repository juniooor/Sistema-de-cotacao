
class Cotacao:
    def __init__(self,fornecedor):
        self.fornecedor = fornecedor
        self.total_pecas = 0
        self.frete = 0
        self.prazo = 0
        self.imposto = 0
        self.total_pecas

    def adcionar_pecas(self, quantidade, preco):
        self.total_pecas += quantidade * preco

    def extras(self, frete, imposto, prazo):
        self.imposto = imposto
        self.frete = frete
        self.prazo = prazo
        self.total = self.total_pecas + imposto + frete 

    def mostrar(self, posicao):
        print(f"\n {posicao} {self.fornecedor}")
        print(f"   valor R$ {self.total:.2f}")
        print(F"  prazo:" {self.prazo })

        

    

        