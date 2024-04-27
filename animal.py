class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def som(self):
        return f"{self.especie}: Auuuuuuuu"
    
    def som2(self):
        return f"{self.especie}: Miauuuuu"
    
    def info(self):
        return f"O {self.nome} é um animal doméstico"
    
    def info2(self):
        return f"O {self.nome} é um animal que está nem aí pro dono"
        
if __name__ == "__main__":
    animal1 = Animal("Mike", 1, "Cachorro")
    animal2 = Animal("Bernardo", 3, "Gato")

    print(animal1.som())
    print(animal1.info())
    print(animal2.som2())
    print(animal2.info2())