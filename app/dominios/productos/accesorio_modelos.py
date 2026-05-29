from app.extensiones import db


class Accesorio(db.Model):

    __tablename__ = "accesorios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nombre = db.Column(
        db.String(100),
        nullable=False
    )

    descripcion = db.Column(
        db.Text,
        nullable=False
    )

    precio_extra = db.Column(
        db.Float,
        default=0
    )

    activo = db.Column(
        db.Boolean,
        default=True
    )

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "productos.id"
        ),
        nullable=False
    )

    def to_dict(self):

        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": (
                self.descripcion
            ),
            "precio_extra": (
                self.precio_extra
            ),
            "activo": self.activo
        }