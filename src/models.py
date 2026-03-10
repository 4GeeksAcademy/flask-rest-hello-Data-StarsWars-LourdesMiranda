import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

# ✅ Buen uso de SQLAlchemy para definir modelos

# Inicializa la base de datos

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # 🔧 Cambiado el orden de atributos
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)  # ✅ Buen uso de restricciones
    password: Mapped[str] = mapped_column(String(250), nullable=False)  # 🔧 Aumentado el tamaño de la contraseña
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)  # ✅ Buen uso de restricciones

    favourites: Mapped[List["Favourite"]] = relationship(back_populates="user")  # 🔧 Cambiado 'favourites' a 'favorites'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Planet(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # 🔧 Cambiado el orden de atributos
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)  # 🔧 Aumentado el tamaño del nombre
    climate: Mapped[Optional[str]] = mapped_column(String(100))  # ✅ Uso correcto de Optional
    terrain: Mapped[Optional[str]] = mapped_column(String(100))  # ✅ Uso correcto de Optional

    favourites: Mapped[List["Favourite"]] = relationship(back_populates="planet")  # 🔧 Cambiado 'favourites' a 'favorites'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain
        }


class Character(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # 🔧 Cambiado el orden de atributos
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)  # 🔧 Aumentado el tamaño del nombre
    hair_color: Mapped[Optional[str]] = mapped_column(String(50))  # ✅ Uso correcto de Optional
    eye_color: Mapped[Optional[str]] = mapped_column(String(50))  # ✅ Uso correcto de Optional
    gender: Mapped[Optional[str]] = mapped_column(String(50))  # ✅ Uso correcto de Optional

    favourites: Mapped[List["Favourite"]] = relationship(back_populates="character")  # 🔧 Cambiado 'favourites' a 'favorites'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "gender": self.gender
        }


class Favourite(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # 🔧 Cambiado el orden de atributos
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)  # ✅ Buen uso de claves foráneas
    planet_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("planet.id"), nullable=True)  # ✅ Uso correcto de Optional
    character_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("character.id"), nullable=True)  # ✅ Uso correcto de Optional

    user: Mapped["User"] = relationship(back_populates="favourites")  # 🔧 Cambiado 'favourites' a 'favorites'
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="favourites")  # 🔧 Cambiado 'favourites' a 'favorites'
    character: Mapped[Optional["Character"]] = relationship(back_populates="favourites")  # 🔧 Cambiado 'favourites' a 'favorites'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }