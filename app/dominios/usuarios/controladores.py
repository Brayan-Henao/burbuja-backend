from flask import Blueprint, request, jsonify

from marshmallow import ValidationError

from app.seguridad import (
    token_requerido
)

from app.dominios.usuarios.esquemas import (
    RegistroUsuarioEsquema
)

from app.dominios.usuarios.servicios import (
    UsuarioServicio
)


usuarios_bp = Blueprint(
    "usuarios",
    __name__
)


@usuarios_bp.route(
    "/registro",
    methods=["POST"]
)
def registro():

    datos = request.get_json()

    esquema = RegistroUsuarioEsquema()

    try:

        datos_validados = esquema.load(
            datos
        )

        usuario = (
            UsuarioServicio.crear_usuario(
                datos_validados
            )
        )

        return jsonify({
            "success": True,
            "message": (
                "Usuario creado correctamente"
            ),
            "data": usuario.to_dict()
        }), 201

    except ValidationError as error:

        return jsonify({
            "success": False,
            "errores": error.messages
        }), 400

    except ValueError as error:

        return jsonify({
            "success": False,
            "error": str(error)
        }), 400


@usuarios_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    datos = request.get_json()

    try:

        resultado = (
            UsuarioServicio.login(
                datos
            )
        )

        return jsonify({
            "success": True,
            "message": "Login exitoso",
            "data": resultado
        }), 200

    except ValueError as error:

        return jsonify({
            "success": False,
            "error": str(error)
        }), 401


@usuarios_bp.route(
    "/perfil",
    methods=["GET"]
)
@token_requerido
def perfil(usuario):

    return jsonify({
        "success": True,
        "data": usuario.to_dict()
    }), 200