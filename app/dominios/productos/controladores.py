from flask import (
    Blueprint,
    request,
    jsonify
)

from app.seguridad import (
    token_requerido,
    admin_requerido
)

from app.dominios.productos.servicios import (
    ProductoServicio
)

from app.dominios.productos.accesorio_servicios import (
    AccesorioServicio
)

productos_bp = Blueprint(
    "productos",
    __name__
)


@productos_bp.route(
    "/",
    methods=["GET"]
)
def listar_productos():

    productos = (
        ProductoServicio.listar_productos()
    )

    return jsonify({
        "success": True,
        "data": productos
    }), 200


@productos_bp.route(
    "/",
    methods=["POST"]
)
@token_requerido
@admin_requerido
def crear_producto(usuario):

    datos = request.get_json()

    producto = (
        ProductoServicio.crear_producto(
            datos
        )
    )

    return jsonify({
        "success": True,
        "message": (
            "Producto creado correctamente"
        ),
        "data": producto.to_dict()
    }), 201


@productos_bp.route(
    "/<int:producto_id>/accesorios",
    methods=["POST"]
)
@token_requerido
@admin_requerido
def crear_accesorio(
    usuario,
    producto_id
):

    datos = request.get_json()

    accesorio = (
        AccesorioServicio.crear_accesorio(
            producto_id,
            datos
        )
    )

    return jsonify({
        "success": True,
        "message": (
            "Accesorio creado correctamente"
        ),
        "data": accesorio.to_dict()
    }), 201