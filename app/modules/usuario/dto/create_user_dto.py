from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    nome: str
    idade: int
    curso: str
    matricula: str
