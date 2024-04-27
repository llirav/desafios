class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def area(self):
        if self.lado1 == self.lado2:
            s = (self.lado1 ** 2) - ((self.lado3 / 2)**2)**0.5 

        elif self.lado1 == self.lado3:
            s = (self.lado1 ** 2) - ((self.lado2 / 2)**2)**0.5

        elif self.lado2 == self.lado3:
            s = (self.lado2 ** 2) - ((self.lado1 / 2)**2)**0.5

        elif self.lado1 == self.lado2 and self.lado1 == self.lado3:
            s = (self.lado2 ** 2) - ((self.lado1 / 2)**2)**0.5

        else:
            if self.lado1 < self.lado2 and self.lado1 < self.lado3 and self.lado2 < self.lado3:
                s = (self.lado1 * self.lado2) / 2
            elif self.lado1 < self.lado2 and self.lado1 < self.lado3 and self.lado3 < self.lado2:
                s = (self.lado1 * self.lado3) / 2
            elif self.lado1 > self.lado2 and self.lado1 > self.lado3:
                s = (self.lado2 * self.lado3) / 2
            else:
                print("Isto não é um triângulo!")
        return s
        
if __name__ == "__main__":
    lado1 = float(input("Digite um valor para um lado do triângulo: "))
    lado2 = float(input("Digite outro valor para outro lado do triângulo: "))
    lado3 = float(input("Digite o último valor para outro lado do triângulo: "))

    triangulo = Triangulo(lado1, lado2, lado3)
    print(f"Perimetro: {triangulo.perimetro():.1f}")
    print(f"Area: {triangulo.area():.1f}")