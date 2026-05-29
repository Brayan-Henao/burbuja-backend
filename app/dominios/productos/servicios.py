from app.dominios.productos.modelos import (
    Producto
)

from app.dominios.productos.repositorios import (
    ProductoRepositorio
)


class ProductoServicio:

    @staticmethod
    def crear_producto(datos):

        nuevo_producto = Producto(

            nombre=datos["nombre"],

            descripcion=datos[
                "descripcion"
            ],

            precio=datos["precio"],

            imagen=datos["imagen"],

            colores=datos.get(
                "colores"
            ),

            permite_grabado=datos.get(
                "permite_grabado",
                False
            ),

            max_caracteres_grabado=datos.get(
                "max_caracteres_grabado"
            ),

            precio_extra_grabado=datos.get(
                "precio_extra_grabado",
                0
            ),

            permite_tarjeta=datos.get(
                "permite_tarjeta",
                False
            ),

            activo=datos.get(
                "activo",
                True
            )
        )

        return ProductoRepositorio.crear(
            nuevo_producto
        )

    @staticmethod
    def listar_productos():

        productos = (
            ProductoRepositorio.obtener_todos()
        )

        return [
            producto.to_dict()
            for producto in productos
        ]