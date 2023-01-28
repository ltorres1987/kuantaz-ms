from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, Date
from sqlalchemy.orm import relationship

from swagger_server.entity.user_entity import User
from swagger_server.entity.proyect_entity import Proyect


# Implementación con SQL Alchemy para el repositorio de institutio.


class UserRepository:

    def __init__(self, sqlalchemy_client, test=False):
        # Mapear la tabla institutio de forma imperativa.
        # Si "test" es true, se le agrega un sufijo al nombre de la tabla,
        # para que las pruebas de integración no sobreescriban los datos existentes.

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "usuario"

        if test:
            table_name += "_test"

        self.user_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key=True),
            Column("first_name", String(100), nullable=True),
            Column("last_name", String(100), nullable=True),
            Column("rut", String(100), nullable=True),
            Column("birth_date", Date, nullable=True),
            Column("position", String(100), nullable=True),
            Column("age", Integer, nullable=True),
            Column("created_user", String(100), nullable=True),
            Column("created_at", TIMESTAMP, nullable=True),
            Column("updated_user", String(100), nullable=True),
            Column("updated_at", TIMESTAMP, nullable=True),
            Column("status", String(1), nullable=True),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(User, self.user_table, properties={
            'proyect_detail': relationship(Proyect, backref='proyect_detail', lazy='joined')
        })

    def get_user(self):
        """Lista users

        Returns:
            model: users
        """
        with self.session_factory() as session:
            users = session.query(User).filter_by(status='A').all()
            return users

    def get_user_by_rut(self, user_rut):
        """Lista users by Rut

        Args:
           user_rut (integer): user_rut

        Returns:
            model: user
        """
        with self.session_factory() as session:
            user = session.query(User).filter_by(rut=user_rut, status='A').first()
            return user
