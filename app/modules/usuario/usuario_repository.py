from typing import Optional

from app.modules.usuario.dto.create_user_dto import CreateUserDTO
from app.modules.usuario.usuario_model import Usuario


class UsuarioRepository:

    # Essa classe será responsavel apenas por acessar o modelo usuario,
    # ou seja, aqui ficará as funções responsaveis por acessar a tabela
    # usuario do banco.

    @staticmethod
    def create(data: CreateUserDTO) -> Usuario:
        usuario = Usuario(
            nome=data.nome,
            idade=data.idade,
            curso=data.curso,
            matricula=data.matricula,
        )
        usuario.save()
        return usuario

    @staticmethod
    def get_by_matricula(matricula: str) -> Optional[Usuario]:
        return Usuario.query.filter_by(matricula=matricula).first()
