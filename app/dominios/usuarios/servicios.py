from datetime import (
    datetime,
    timedelta
)

import jwt

from flask import current_app

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.dominios.usuarios.modelos import (
    Usuario
)

from app.dominios.usuarios.repositorios import (
    UsuarioRepositorio
)


class UsuarioServicio:

    @staticmethod
    def crear_usuario(datos):

        correo = datos["correo"]

        contrasena = datos["contrasena"]

        usuario_existente = (
            UsuarioRepositorio.obtener_por_correo(
                correo
            )
        )

        if usuario_existente:

            raise ValueError(
                "El correo ya está registrado"
            )

        contrasena_hash = (
            generate_password_hash(
                contrasena
            )
        )

        nuevo_usuario = Usuario(
            correo=correo,
            contrasena=contrasena_hash
        )

        return UsuarioRepositorio.crear(
            nuevo_usuario
        )

    @staticmethod
    def login(datos):

        correo = datos["correo"]

        contrasena = datos["contrasena"]

        usuario = (
            UsuarioRepositorio.obtener_por_correo(
                correo
            )
        )

        if not usuario:

            raise ValueError(
                "Credenciales inválidas"
            )

        contrasena_correcta = (
            check_password_hash(
                usuario.contrasena,
                contrasena
            )
        )

        if not contrasena_correcta:

            raise ValueError(
                "Credenciales inválidas"
            )

        payload = {
            "usuario_id": usuario.id,
            "exp": (
                datetime.utcnow()
                + timedelta(hours=24)
            )
        }

        token = jwt.encode(
            payload,
            current_app.config[
                "SECRET_KEY"
            ],
            algorithm="HS256"
        )

        return {
            "access_token": token,
            "usuario": usuario.to_dict()
        }