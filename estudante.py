class Estudante:
    def __init__(self, nome, idade, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota2 + self.nota1) / 2

if __name__ == "__main__":
    nome = input("Digite seu nome: ").strip()
    idade = int(input("Digite sua idade: "))
    nota1 = float(input("Digite sua primeira nota: "))
    nota2 = float(input("Digite sua segunda nota: "))
    estudante = Estudante(nome, idade, nota1, nota2)

    print(f"""Aluno: {estudante.nome}
Idade: {estudante.idade}
1° nota: {estudante.nota1}
2° nota: {estudante.nota2}
Média: {estudante.media()}""")
    
    if estudante.media() >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")