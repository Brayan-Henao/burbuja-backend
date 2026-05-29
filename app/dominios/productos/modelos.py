from app.extensiones import db

from app.dominios.productos.accesorio_modelos import (
    Accesorio
)


class Producto(db.Model):

    __tablename__ = "productos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(150),
        nullable=False
    )

    descripcion = db.Column(
        db.Text,
        nullable=False
    )

    precio = db.Column(
        db.Float,
        nullable=False
    )

    imagen = db.Column(
        db.String(255),
        nullable=False
    )

    colores = db.Column(
        db.String(255),
        nullable=True
    )

    permite_grabado = db.Column(
        db.Boolean,
        default=False
    )

    max_caracteres_grabado = db.Column(
        db.Integer,
        nullable=True
    )

    precio_extra_grabado = db.Column(
        db.Float,
        default=0
    )

    permite_tarjeta = db.Column(
        db.Boolean,
        default=False
    )

    activo = db.Column(
        db.Boolean,
        default=True
    )

    accesorios = db.relationship(
        "Accesorio",
        backref="producto",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "imagen": self.imagen,
            "colores": self.colores,
            "permite_grabado": (
                self.permite_grabado
            ),
            "max_caracteres_grabado": (
                self.max_caracteres_grabado
            ),
            "precio_extra_grabado": (
                self.precio_extra_grabado
            ),
            "permite_tarjeta": (
                self.permite_tarjeta
            ),
            "activo": self.activo,
            "accesorios": [
                accesorio.to_dict()
                for accesorio in self.accesorios
            ]
        }