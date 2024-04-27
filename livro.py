class Livro:
    def __init__(self,  titulo, autor, numero_pag):
        self.titulo = titulo
        self.autor = autor
        self.numero_pag = numero_pag

    def titulo(self):
        return self.titulo
    
    def autor(self):
        return self.autor
    
    def numero_pag(self):
        return self.numero_pag
    
if __name__ == "__main__":
    titulo = input("Diga o nome do livro: ")
    autor = input("Diga, agora, o nome do autor: ")
    numero_pag = int(input("Digite a quantidade de páginas no livro: "))
    info = input("Faça uma breve descrição do livro: ")
    livro = Livro(titulo, autor, numero_pag)

    print(f"O nome do livro é {livro.titulo}")
    print(f"O autor dele é {livro.autor}")
    print(f"O número de palavras por páginas é por volta de 300")
    print(info)