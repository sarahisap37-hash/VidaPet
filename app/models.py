from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String(100), nullable=True)
    telefone = Column(String(20), nullable=True)
    email = Column(String(100), unique=False, nullable=True)


class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_animal = Column(String(60), nullable=True)
    especie = Column(String(40), nullable=True)
    raca = Column(String(60), nullable=True)
    peso_kg = Column(Float, nullable=True)
    tutor_id = Column(Integer, ForeignKey("tutores.id"))


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_atend = Column(String(10), nullable=True)  # DD/MM/AAAA
    motivo = Column(String(200), nullable=True)
    valor_cons = Column(Float, nullable=True)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=True)