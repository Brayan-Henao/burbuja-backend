from marshmallow import Schema, fields, validate


class RegistroUsuarioEsquema(Schema):

    correo = fields.Email(
        required=True
    )

    contrasena = fields.String(
        required=True,
        validate=validate.Length(min=6)
    )