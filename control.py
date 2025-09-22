from models import Pedido, ItemPedido


class PedidoControl:
    def __init__(self, db):
        self.db = db

    def salvar_pedido(self, pedido):
        pedido_query = "INSERT INTO pedido (cliente) VALUES (%s)"
        cursor = self.db.execute_query(pedido_query, (pedido.cliente,))
        #cursor = self.atualizar_pedido(pedido);
        if cursor:
            # print("cursor e valido")
            #if not pedido.id:
            pedido.id = cursor.lastrowid

            item_query = "INSERT INTO item_pedido (pedido_id, produto, quantidade, preco, categoria) VALUES (%s, %s, %s, %s, %s)"
            for item in pedido.itens:
                # print(f"pedido_id: {pedido.id},produto: {item.produto}, quantidade: {item.quantidade}, preco: {item.preco}, categoria: {item.categoria}")
                self.db.execute_query(item_query, (pedido.id, item.produto, item.quantidade, item.preco, item.categoria))
        else:
            print("Erro! O cursor e invalido")

   
    def atualizar_pedido(self, pedido):
        if pedido.id is None:
            raise ValueError("Pedido deve ter um ID para atualizar")

        # Deletar itens primeiro para respeitar FK
        delete_itens = "DELETE FROM item_pedido WHERE pedido_id = %s"
        self.db.execute_query(delete_itens, (pedido.id,))

        update_query = "UPDATE pedido SET cliente = %s WHERE id = %s"
        self.db.execute_query(update_query, (pedido.cliente, pedido.id))

        item_query = "INSERT INTO item_pedido (pedido_id, produto, quantidade, preco, categoria) VALUES (%s, %s, %s, %s, %s)"
        for item in pedido.itens:
            # print(f"pedido_id: {pedido.id},produto: {item.produto}, quantidade: {item.quantidade}, preco: {item.preco}, categoria: {item.categoria}")
            self.db.execute_query(item_query, (pedido.id, item.produto, item.quantidade, item.preco, item.categoria))

    def deletar_pedido(self, pedido_id):
        # Deletar itens primeiro para respeitar FK
        delete_itens = "DELETE FROM item_pedido WHERE pedido_id = %s"
        self.db.execute_query(delete_itens, (pedido_id,))

        # Deletar pedido
        delete_pedido = "DELETE FROM pedido WHERE id = %s"
        self.db.execute_query(delete_pedido, (pedido_id,))

    def listar_pedidos_com_itens(self):
        query = """
        SELECT p.id, p.cliente, i.produto, i.quantidade, i.preco, i.categoria
        FROM pedido p
        JOIN item_pedido i ON p.id = i.pedido_id
        ORDER BY p.id;
        """
        cursor = self.db.execute_query(query)
        pedidos = {}
        if cursor:
            for pedido_id, cliente, produto, quantidade, preco, categoria in cursor:
                if pedido_id not in pedidos:
                    pedidos[pedido_id] = Pedido(cliente)
                    pedidos[pedido_id].id = pedido_id
                item = ItemPedido(produto, quantidade, preco, categoria)
                pedidos[pedido_id].add_item(item)
        return list(pedidos.values())  # Retorna lista explícita