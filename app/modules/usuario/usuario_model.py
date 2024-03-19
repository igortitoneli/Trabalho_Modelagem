from dataclasses import asdict, dataclass
from sqlalchemy import Integer, String
from ...common.util.db import db
from sqlalchemy.orm import mapped_column, Mapped


@dataclass
class Usuario(db.Model):

    # Aqui estará declarado o modelo do banco de dados da tabela usuario em sqlalchemy

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    curso: Mapped[str] = mapped_column(String, nullable=False)
    matricula: Mapped[str] = mapped_column(String(11), nullable=False)

    def to_dict(self):
        return asdict(self)

    def save(self):
        db.session.add(self)
        db.session.commit()
