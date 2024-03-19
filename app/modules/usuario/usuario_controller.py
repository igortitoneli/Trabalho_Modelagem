from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.modules.usuario.dto.create_user_dto import CreateUserDTO
from app.modules.usuario.usuario_service import UsuarioService


bp = Blueprint("usuario", __name__, url_prefix="/api/usuario")


# Esse arquivo será responsável por declarar as endpoints
# utilizando blueprint e validar os inputs pydantic


@bp.post("/create")
@jwt_required()
def change_status():
    request_data = request.get_json()
    data = CreateUserDTO.model_validate(request_data)
    return UsuarioService.create(data)
