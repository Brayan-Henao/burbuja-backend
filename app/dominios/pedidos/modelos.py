from datetime import datetime

from app.extensiones import db




class Pedido(db.Model):

    __tablename__ = "pedidos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "usuarios.id"
        ),
        nullable=False
    )

    total = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    direccion_envio = db.Column(
        db.String(255),
        nullable=False
    )

    estado = db.Column(
        db.String(50),
        default="pendiente"
    )

    fecha_creacion = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    items = db.relationship(
        "PedidoItem",
        backref="pedido",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):

        return {
            "id": self.id,
            "usuario_id": (
                self.usuario_id
            ),
            "total": self.total,
            "direccion_envio": (
                self.direccion_envio
            ),
            "fecha_creacion": (
                self.fecha_creacion.isoformat()
            ),
            "items": [
                item.to_dict()
                for item in self.items
        ]
        }