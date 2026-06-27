from app.extensiones import db

from app.dominios.pedidos.modelos import (
    Pedido
)


class PedidoRepositorio:

    @staticmethod
    def guardar():

        db.session.commit()

    @staticmethod
    def crear(pedido):

        db.session.add(pedido)

        db.session.commit()

        return pedido

    @staticmethod
    def obtener_todos():

        return Pedido.query.all()

    @staticmethod
    def obtener_por_id(pedido_id):

        return Pedido.query.get(
            pedido_id
        )

    @staticmethod
    def obtener_por_usuario(usuario_id):

        return Pedido.query.filter_by(
            usuario_id=usuario_id
        ).all()