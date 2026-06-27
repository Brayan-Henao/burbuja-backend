from flask import (
    Blueprint,
    request,
    jsonify
)

from app.seguridad import (
    token_requerido
)

from app.dominios.pedidos.servicios import (
    PedidoServicio
)


pedidos_bp = Blueprint(
    "pedidos",
    __name__
)


@pedidos_bp.route(
    "/",
    methods=["POST"]
)
@token_requerido
def crear_pedido(usuario):

    datos = request.get_json()

    pedido = (
        PedidoServicio.crear_pedido(
            usuario,
            datos
        )
    )

    return jsonify({
        "success": True,
        "message": (
            "Pedido creado correctamente"
        ),
        "data": pedido.to_dict()
    }), 201


@pedidos_bp.route(
    "/mis-pedidos",
    methods=["GET"]
)
@token_requerido
def listar_mis_pedidos(usuario):

    pedidos = (
        PedidoServicio.listar_pedidos_usuario(
            usuario
        )
    )

    return jsonify({
        "success": True,
        "data": pedidos
    }), 200

@pedidos_bp.route(
    "/<int:pedido_id>",
    methods=["GET"]
)
@token_requerido
def obtener_pedido(
    usuario,
    pedido_id
):

    pedido = (
        PedidoServicio.obtener_pedido(
            pedido_id
        )
    )

    return jsonify({
        "success": True,
        "data": pedido
    }), 200