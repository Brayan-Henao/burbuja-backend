from app.extensiones import db

from app.dominios.productos.modelos import (
    Producto
)


class ProductoRepositorio:

    @staticmethod
    def obtener_todos():

        return Producto.query.all()

    @staticmethod
    def obtener_por_id(producto_id):

        return Producto.query.get(
            producto_id
        )

    @staticmethod
    def crear(producto):

        db.session.add(producto)

        db.session.commit()

        return producto