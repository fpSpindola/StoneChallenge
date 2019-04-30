from collections import defaultdict
from datetime import datetime
from collections import defaultdict
from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Funcionario(Base):

    __tablename__ = "funcionario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    cargo = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    last_updated_at = Column(DateTime, nullable=True)

    def as_json(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "cargo": self.cargo,
            "created_at": self.created_at,
            "last_updated_at": self.last_updated_at
        }
