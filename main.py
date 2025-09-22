from database import Database
from models import Pedido, ItemPedido
from control import PedidoControl

if __name__ == "__main__":
    db = Database(host='localhost', user='kyara', password='password', database='db_pedidos')
    control = PedidoControl(db)

    # primeiro pedido
    pedido_kyara=Pedido(cliente="Kyara")
    
    # itens do primeiro pedido
    item_tv = ItemPedido("TV", 1, 3000, "eletronicos")
    pedido_kyara.add_item(item_tv);
    item_celular = ItemPedido("Celular", 2, 2000, "mobile")
    pedido_kyara.add_item(item_celular);
    # print(pedido_kyara)

    control.salvar_pedido(pedido_kyara)

    # segundo pedido
    pedido_jose=Pedido(cliente="jose")
    #control.atualizar_pedido(pedido_jose)
    
    # itens do segundo pedido
    item_cadeira = ItemPedido("Cadeira", 5, 600, "moveis")
    pedido_jose.add_item(item_cadeira);
    item_banana = ItemPedido("Banana", 10, 10, "comida")
    pedido_jose.add_item(item_banana);
    # print(pedido_jose)

    control.salvar_pedido(pedido_jose)

    print("\n=============Lista de pedidos apos salvar o pedido da kyara e do jose: ============= \n")

    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}")


    control.deletar_pedido(pedido_kyara.id);

    print("\n=============Lista de pedidos apos deletar o pedido da kyara: ============= \n")
    pedidos = control.listar_pedidos_com_itens()

    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}")


    pedido_jose.cliente = "Mateus";
    pedido_mateus = pedido_jose
    item_pokemon = ItemPedido("Cartas Pokemon", 100, 50.0, "brinquedos")
    pedido_mateus.add_item(item_pokemon);

    control.atualizar_pedido(pedido_mateus)

    print("\n=============Lista de pedidos apos atualizar o pedido do Jose -> Mateus: ============= \n")
    pedidos = control.listar_pedidos_com_itens()

    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}")




    db.close()
