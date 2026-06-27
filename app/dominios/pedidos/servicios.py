from app.extensiones import db

from app.dominios.pedidos.modelos import (
    Pedido
)

from app.dominios.pedidos.pedido_item_modelos import (
    PedidoItem
)

from app.dominios.pedidos.repositorios import (
    PedidoRepositorio
)


class PedidoServicio:

    @staticmethod
    def crear_pedido(usuario, datos):

        items = datos["items"]

        total = 0

        nuevo_pedido = Pedido(

            usuario_id=usuario.id,

            direccion_envio=datos[
                "direccion_envio"
            ]
        )

        db.session.add(nuevo_pedido)

        db.session.flush()

        for item in items:

            subtotal = item["subtotal"]

            total += subtotal

            nuevo_item = PedidoItem(

                pedido_id=nuevo_pedido.id,

                producto_id=item[
                    "producto_id"
                ],

                accesorio_id=item.get(
                    "accesorio_id"
                ),

                color=item.get(
                    "color"
                ),

                grabado=item.get(
                    "grabado",
                    False
                ),

                texto_grabado=item.get(
                    "texto_grabado"
                ),

                tarjeta=item.get(
                    "tarjeta",
                    False
                ),

                mensaje_tarjeta=item.get(
                    "mensaje_tarjeta"
                ),

                subtotal=subtotal
            )

            db.session.add(
                nuevo_item
            )

        nuevo_pedido.total = total

        db.session.commit()

        return nuevo_pedido

    @staticmethod
    def listar_pedidos_usuario(usuario):

        pedidos = (
            PedidoRepositorio.obtener_por_usuario(
                usuario.id
            )
        )

        return [
            pedido.to_dict()
            for pedido in pedidos
        ]
    
    @staticmethod
    def obtener_pedido(pedido_id):

        pedido = (
            PedidoRepositorio.obtener_por_id(
                pedido_id
            )
        )

        if not pedido:

            raise ValueError(
                "Pedido no encontrado"
            )

        return pedido.to_dict()