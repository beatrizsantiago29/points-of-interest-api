from sqlalchemy import create_engine, String, Integer, Column

from sqlalchemy.orm import declarative_base

# conexao com o banco SQLite
DATABASE_URL = "sqlite:///bancoPOI.db"
db = create_engine(DATABASE_URL)

# base para os modelos
Base = declarative_base()

class POI(Base):
    __tablename__ = "pois"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    x = Column("x", Integer, nullable=False)
    y = Column("y", Integer, nullable=False)

    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y