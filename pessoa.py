class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def nome(self):
        return self.nome
    
    def idade(self):
        return self.idade
    
    def sexo(self):
        return self.sexo
    
    def altura(self):
        return self.altura
    
if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ")
    altura = float(input("Digite sua altura: "))
    pessoinha = Pessoa(nome, idade, altura)

    print(f"Seu nome é {pessoinha.nome}")
    print(f"Sua idade é {pessoinha.idade}")
    print(f"Seu sexo é {sexo}")
    print(f"Sua altura é {pessoinha.altura}")