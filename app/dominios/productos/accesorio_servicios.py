from app.extensiones import db

from app.dominios.productos.accesorio_modelos import (
    Accesorio
)


class AccesorioServicio:

    @staticmethod
    def crear_accesorio(
        producto_id,
        datos
    ):

        accesorio = Accesorio(

            producto_id=producto_id,

            nombre=datos["nombre"],

            descripcion=datos.get(
                "descripcion"
            ),

            precio_extra=datos.get(
                "precio_extra",
                0
            )
        )

        db.session.add(
            accesorio
        )

        db.session.commit()

        return accesorio