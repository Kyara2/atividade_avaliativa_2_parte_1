from database import Database
from models import Pedido, ItemPedido
from control import PedidoControl

if __name__ == "__main__":
    db = Database(host='localhost', user='root', password='', database='db_pedidos')
    control = PedidoControl(db)
    #pedido=Pedido(cliente="Claudio Ulisse")
    #pedido.id=7
    #control.atualizar_pedido(pedido)
    
   # control.salvar_pedido(pedido)

    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente} - Data: {p.data_pedido}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}")

    db.close()
