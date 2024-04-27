class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def perimetro(self):
        return (self.altura * 2) + (self.largura * 2)
    
    def area(self):
        return self.altura * self.largura
    
if __name__ == "__main__":
    altura = float(input("Digite uma altura para o retângulo: "))
    largura = float(input("Digita, agora, uma largura para o retângulo: "))
    retangulo = Retangulo(altura, largura)

    print(f"A área do retângulo com os tamanhos colocados é {retangulo.area():.1f}cm")
    print(f"O perímetro do retângulo com os tamanhos informados é {retangulo.perimetro():.1f}cm")
