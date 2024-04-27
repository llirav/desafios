class Pedido:
    def __init__(self, itens, total, status):
        self.itens = itens
        self.total = total
        self.status = status

if __name__ == "__main__":
    total = 0
    cont = "sim"

    while cont == "sim":
        produto = int(input("""----------PRODUTOS----------
1 - Leite            - R$3,00
2 - Feijão           - R$6,50
3 - Arroz            - R$5,00
4 - Farinha de Trigo - R$3,50
Digite o o número do produto que deseja: """))
        
        itens = int(input("Digite a quantidade que deseja deste item: "))

        if produto == 1:
            total += 3 * itens
        elif produto == 2:
            total += 6.5 * itens
        elif produto == 3:
            total += 5 * itens
        elif produto == 4:
            total += 3.5 * itens
        
        cont = input("Deseja continuar? ").lower()

    print(f"O valor total do pedido foi R${total}")
    
