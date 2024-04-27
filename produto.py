class Produto:
    def __init__(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque
    
    def nome(self):
        return self.nome

    def preço(self):
        return self.preço

    def estoque(self):
        return self.estoque
    
if __name__ == '__main__':
    produto1 = Produto('camisa do sport', 50, 5)
    produto2 = Produto('bermuda', 30, 10)
    produto3 = Produto('kenner', 15, 8)

    print(produto1.preço())
    print(produto2.estoque())
    print(produto3.nome())