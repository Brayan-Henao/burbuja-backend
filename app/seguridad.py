from functools import wraps

import jwt

from flask import request, jsonify, current_app

from app.dominios.usuarios.repositorios import (
    UsuarioRepositorio
)


def token_requerido(func):

    @wraps(func)
    def decorador(*args, **kwargs):

        token = None

        auth_header = request.headers.get(
            "Authorization"
        )

        if auth_header and auth_header.startswith(
            "Bearer "
        ):

            token = auth_header.split(" ")[1]

        if not token:

            return jsonify({
                "success": False,
                "error": "Token requerido"
            }), 401

        try:

            payload = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )
            
            usuario = (
                UsuarioRepositorio.obtener_por_id(
                    payload["usuario_id"]
                )
            )
            
            if not usuario:

                return jsonify({
                    "success": False,
                    "error": "Usuario no encontrado"
                }), 401

        except jwt.ExpiredSignatureError:

            return jsonify({
                "success": False,
                "error": "Token expirado"
            }), 401

        except jwt.InvalidTokenError:

            return jsonify({
                "success": False,
                "error": "Token inválido"
            }), 401

        return func(usuario, *args, **kwargs)

    return decorador

def admin_requerido(func):

    @wraps(func)
    def decorador(usuario, *args, **kwargs):

        if usuario.rol != "admin":

            return jsonify({
                "success": False,
                "error": (
                    "Acceso solo para administradores"
                )
            }), 403

        return func(
            usuario,
            *args,
            **kwargs
        )

    return decorador