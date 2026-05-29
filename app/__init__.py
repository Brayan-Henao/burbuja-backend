from flask import Flask

from app.configuracion import (
    Configuracion
)

from app.extensiones import (
    db,
    migrate
)

from app.dominios.usuarios.controladores import (
    usuarios_bp
)

from app.dominios.usuarios.modelos import (
    Usuario
)

from app.dominios.productos.modelos import (
    Producto
)

from app.dominios.productos.accesorio_modelos import (
    Accesorio
)

from app.dominios.pedidos.modelos import (
    Pedido
)

from app.dominios.pedidos.pedido_item_modelos import (
    PedidoItem
)

from app.dominios.productos.controladores import (
    productos_bp
)

from app.dominios.pedidos.controladores import (
    pedidos_bp
)




def crear_app():

    app = Flask(__name__)

    app.config.from_object(
        Configuracion
    )

    db.init_app(app)

    migrate.init_app(
        app,
        db
    )

    app.register_blueprint(
        usuarios_bp,
        url_prefix="/api/v1/usuarios"
    )

    app.register_blueprint(
        productos_bp,
        url_prefix="/api/v1/productos"
    )

    app.register_blueprint(
        pedidos_bp,
        url_prefix="/api/v1/pedidos"
    )

    @app.route("/health")
    def health():

        return {
            "status": "ok",
            "mensaje": (
                "Burbuja backend funcionando"
            )
        }

    return app