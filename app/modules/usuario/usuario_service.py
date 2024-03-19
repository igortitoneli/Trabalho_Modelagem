from app.modules.usuario.dto.create_user_dto import CreateUserDTO
from app.modules.usuario.usuario_repository import UsuarioRepository


class UsuarioService:

    # Esta clase será responsavel por chamar o UsuarioRepository ou
    # qualquer outro repository de modo que o conjunto dessas funçoes
    # execute uma regra de negocio

    @classmethod
    def create(cls, data: CreateUserDTO):
        cls.usuario_not_exist_or_raise(data.matricula)
        usuario = UsuarioRepository.create(data)
        return usuario.to_dict()

    @staticmethod
    def usuario_not_exist_or_raise(matricula: str) -> None:
        user = UsuarioRepository.get_by_matricula(matricula)
        if user:
            raise Exception(f"Matricula <{matricula}> já esta cadastrada. ")
