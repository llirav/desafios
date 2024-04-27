# João Vinicius

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f"{self.modelo} está ligando"
    
    def desligar(self):
        return f"{self.modelo} está desligando"
    
    def acelerar(self):
        return f"{self.modelo} está acelerando"
    
if __name__ == '__main__':
    carro1 = Carro("BMW", "X1", 2018, "Vermelha")
    carro2 = Carro("Fiat", "UNO", 2021, "Prata")
    carro3 = Carro("Audi", "A3", 2015, "All Black")

    print(carro1.ligar())
    print(carro2.desligar())
    print(carro3.acelerar())