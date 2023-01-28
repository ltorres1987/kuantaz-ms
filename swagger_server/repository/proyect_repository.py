from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, Date
from sqlalchemy.orm import relationship

from swagger_server.entity.user_entity import User
from swagger_server.entity.proyect_entity import Proyect
from swagger_server.entity.institution_entity import Institution


# Implementación con SQL Alchemy para el repositorio de Proyect.


class ProyectRepository:

    def __init__(self, sqlalchemy_client, test=False):
        # Mapear la tabla institutio de forma imperativa.
        # Si "test" es true, se le agrega un sufijo al nombre de la tabla,
        # para que las pruebas de integración no sobreescriban los datos existentes.

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "proyect"

        if test:
            table_name += "_test"

        self.proyect_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String(100), nullable=True),
            Column("description", String(100), nullable=True),
            Column("start_date", Date, nullable=True),
            Column("end_date", Date, nullable=True),
            Column("institutionid", Integer, ForeignKey(Institution.id), nullable=True),
            Column("usuarioid", Integer, ForeignKey(User.id), nullable=True),
            Column("created_user", String(100), nullable=True),
            Column("created_at", TIMESTAMP, nullable=True),
            Column("updated_user", String(100), nullable=True),
            Column("updated_at", TIMESTAMP, nullable=True),
            Column("status", String(1), nullable=True),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(Proyect, self.proyect_table, properties={
            'user_detail': relationship(User, backref='user_detail', lazy='joined')
        })

    def get_proyect(self):
        """Lista proyectos

        Returns:
            model: proyects
        """
        with self.session_factory() as session:
            proyects = session.query(Proyect).filter_by(status='A').all()
            return proyects
