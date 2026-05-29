from app.extensiones import db


class PedidoItem(db.Model):

    __tablename__ = "pedido_items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    pedido_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "pedidos.id"
        ),
        nullable=False
    )

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "productos.id"
        ),
        nullable=False
    )

    accesorio_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "accesorios.id"
        ),
        nullable=True
    )

    color = db.Column(
        db.String(100),
        nullable=True
    )

    grabado = db.Column(
        db.Boolean,
        default=False
    )

    texto_grabado = db.Column(
        db.String(255),
        nullable=True
    )

    tarjeta = db.Column(
        db.Boolean,
        default=False
    )

    mensaje_tarjeta = db.Column(
        db.String(255),
        nullable=True
    )

    subtotal = db.Column(
        db.Float,
        nullable=False
    )

    def to_dict(self):

        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "producto_id": (
                self.producto_id
            ),
            "accesorio_id": (
                self.accesorio_id
            ),
            "color": self.color,
            "grabado": self.grabado,
            "texto_grabado": (
                self.texto_grabado
            ),
            "tarjeta": self.tarjeta,
            "mensaje_tarjeta": (
                self.mensaje_tarjeta
            ),
            "subtotal": self.subtotal
        }