from datetime import datetime

from app.extensiones import db


class Usuario(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    correo = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    contrasena = db.Column(
        db.String(255),
        nullable=False
    )

    rol = db.Column(
        db.String(20),
        default="usuario"
    )

    fecha_creacion = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {
            "id": self.id,
            "correo": self.correo,
            "rol": self.rol,
            "fecha_creacion": (
                self.fecha_creacion.isoformat()
                if self.fecha_creacion
                else None
            )
        }