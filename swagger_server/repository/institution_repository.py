from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from swagger_server.entity.institution_entity import Institution
from swagger_server.entity.proyect_entity import Proyect


# Implementación con SQL Alchemy para el repositorio de institutio.


class InstitutionRepository:

    def __init__(self, sqlalchemy_client, test=False):
        # Mapear la tabla institutio de forma imperativa.
        # Si "test" es true, se le agrega un sufijo al nombre de la tabla,
        # para que las pruebas de integración no sobreescriban los datos existentes.

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "institution"

        if test:
            table_name += "_test"

        self.institution_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String(100), nullable=True),
            Column("description", String(500), nullable=True),
            Column("address", String(200), nullable=True),
            Column("created_user", String(100), nullable=True),
            Column("created_at", TIMESTAMP, nullable=True),
            Column("updated_user", String(100), nullable=True),
            Column("updated_at", TIMESTAMP, nullable=True),
            Column("status", String(1), nullable=True),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(Institution, self.institution_table, properties={
            'pry_detail': relationship(Proyect, backref='pry_detail', lazy='joined')
        })

    def create_institution(self, institution):
        """Agrega una nueva institución

        Args:
           institution (model): institution

        Returns:
            model: institution
        """
        with self.session_factory() as session:
            session.add(institution)
            session.commit()

            return institution

    def get_institution(self):
        """Lista instituciones

        Returns:
            model: institutions
        """
        with self.session_factory() as session:
            institutions = session.query(Institution).filter_by(status='A').all()
            return institutions

    def get_institution_by_id(self, institution_id):
        """Busca una institución por ID

        Args:
           institution_id (integer): institution id

        Returns:
            model: institution
        """
        with self.session_factory() as session:
            institution = session.query(Institution).filter_by(id=institution_id, status='A').first()
            return institution

    def update_institution(self, institution_id, fields):
        """Actualiza una institución existente

        Args:
           institution_id (integer): institution id
           fields (dict): dict de campos actualizar

        Returns:
            model: institution
        """

        with self.session_factory() as session:
            session.query(Institution).filter_by(id=institution_id, status='A').update(fields)
            session.commit()

            institution = session.query(Institution).filter_by(id=institution_id, status='A').first()
            return institution
