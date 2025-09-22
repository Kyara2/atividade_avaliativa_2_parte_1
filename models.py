from datetime import date

class Pedido:
    def __init__(self, cliente):
        self.id = None
        self.cliente = cliente
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)

    def __str__(self):
        s = f"cliente: {self.cliente},  id: {self.id}, Itens:[\n"
        for item in self.itens:
            s += item.__str__() + " , \n"
        s+=']\n'  
        return s


class ItemPedido:
    def __init__(self, produto, quantidade, preco, categoria):
        self.id = None
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria

    def __str__(self):
        s = f"Item pedido: produto: {self.produto}, quantidade: {self.quantidade}, preco: {self.preco}, categoria: {self.categoria}\n"
        return s