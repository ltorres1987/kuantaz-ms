import os
from swagger_server.entity.institution_entity import Institution
from swagger_server.utils import utils
from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData
from swagger_server.models.response_project_and_responsible import ResponseProjectAndResponsible
from swagger_server.models.response_project_and_responsible_data import ResponseProjectAndResponsibleData
from swagger_server.models.response_project_and_responsible_detail import ResponseProjectAndResponsibleDetail


class InstitutionUsecase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def add_institution(self, body):
        """Agrega una nueva institución

        Args:
           body (string): body 

        Returns:
            dict: modelo de datos ResponseInstitution
        """

        data = body.to_dict()

        data["created_at"] = utils.get_current_datetime()
        data["status"] = "A"

        institution = Institution.from_dict(data)
        institution = self.institution_repository.create_institution(institution)

        data_response = ResponseInstitutionData(
            id=institution.id,
            name=institution.name,
            description=institution.description,
            address=institution.address,
            created_user=institution.created_user,
            created_at=institution.created_at,
            updated_user=institution.updated_user,
            updated_at=institution.updated_at,
            status=institution.status
        )

        response = ResponseInstitution(
            code=0,
            message=f"institution created succesfully",
            data=data_response
        )

        return response

    def get_institution(self):
        """Lista instituciones

        Returns:
            dict: modelo de datos ResponseInstitution
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        if not institutions:
            raise ValueError(f"No existe datos para la consulta")

        for institution in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=institution.id,
                    name=institution.name,
                    description=institution.description,
                    address=institution.address,
                    created_user=institution.created_user,
                    created_at=institution.created_at,
                    updated_user=institution.updated_user,
                    updated_at=institution.updated_at,
                    status=institution.status
                )
            )

        response = ResponseInstitution(
            code=0,
            message=f"institution obtained succesfully",
            data=data_response
        )

        return response

    def get_institution_by_id(self, institution_id):
        """Busca una institución por ID

        Args:
           institution_id (integer): institution id

        Returns:
            dict: modelo de datos ResponseInstitution
        """

        institution = self.institution_repository.get_institution_by_id(institution_id)

        if not institution:
            raise ValueError(f"institution of ID {institution_id} doesn't exist.")

        data_response = ResponseInstitutionData(
            id=institution.id,
            name=institution.name,
            description=institution.description,
            address=institution.address,
            created_user=institution.created_user,
            created_at=institution.created_at,
            updated_user=institution.updated_user,
            updated_at=institution.updated_at,
            status=institution.status
        )

        response = ResponseInstitution(
            code=0,
            message=f"institution obtained succesfully",
            data=data_response
        )

        return response

    def update_institution(self, body):
        """Actualiza una institución existente

        Args:
           body (string): body 

        Returns:
            dict: modelo de datos ResponseInstitution
        """

        institution_id = body.id

        institution = self.institution_repository.get_institution_by_id(institution_id)

        if not institution:
            raise ValueError(f"institution of ID {institution_id} doesn't exist.")

        data = body.to_dict()
        data["updated_at"] = utils.get_current_datetime()

        institution = self.institution_repository.update_institution(institution_id, data)

        data_response = ResponseInstitutionData(
            id=institution.id,
            name=institution.name,
            description=institution.description,
            address=institution.address,
            created_user=institution.created_user,
            created_at=institution.created_at,
            updated_user=institution.updated_user,
            updated_at=institution.updated_at,
            status=institution.status
        )

        response = ResponseInstitution(
            code=0,
            message=f"institution of ID {institution_id} updated succesfully.",
            data=data_response
        )

        return response

    def delete_institution(self, institution_id):
        """Elimina una institución

        Args:
           institution_id (integer): institution id

        Returns:
            dict: modelo de datos ResponseInstitution
        """

        institution = self.institution_repository.get_institution_by_id(institution_id)

        if not institution:
            raise ValueError(f"institution of ID {institution_id} doesn't exist.")

        data = {
            "updated_at": utils.get_current_datetime(),
            "status": "I"
        }

        self.institution_repository.update_institution(institution_id, data)

        response = ResponseInstitution(
            code=0,
            message=f"institution of ID {institution_id} deleted succesfully.",
            data={}
        )

        return response

    def get_institution_with_address(self):
        """Lista instituciones con la direccion de google maps

        Returns:
            dict: modelo de datos ResponseInstitution
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        if not institutions:
            raise ValueError(f"No existe datos para la consulta")

        # ruta de google maps
        google_maps = os.environ["GOOGLE_MAPS"]

        for institution in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=institution.id,
                    name=institution.name[0: 3],
                    description=institution.description,
                    address=f"{google_maps}{institution.address}",
                    created_user=institution.created_user,
                    created_at=institution.created_at,
                    updated_user=institution.updated_user,
                    updated_at=institution.updated_at,
                    status=institution.status
                )
            )

        response = ResponseInstitution(
            code=0,
            message=f"institution obtained succesfully",
            data=data_response
        )

        return response

    def get_institution_by_project_responsible(self, institution_id):
        """Busca una institución por ID

        Args:
           institution_id (integer): institution id

        Returns:
            dict: modelo de datos ResponseProjectAndResponsible
        """

        institution = self.institution_repository.get_institution_by_id(institution_id)

        if not institution:
            raise ValueError(f"institution of ID {institution_id} doesn't exist.")

        # detalle de proyectos
        proyects = []
        for detail in institution.pry_detail:
            proyects.append(
                ResponseProjectAndResponsibleDetail(
                    id=detail.id,
                    name=detail.name,
                    description=detail.description,
                    responsible=f"{detail.user_detail.first_name} - {detail.user_detail.last_name}"
                )
            )

        data_response = ResponseProjectAndResponsibleData(
            id=institution.id,
            name=institution.name,
            description=institution.description,
            address=institution.address,
            created_user=institution.created_user,
            created_at=institution.created_at,
            updated_user=institution.updated_user,
            updated_at=institution.updated_at,
            status=institution.status,
            proyects=proyects
        )

        response = ResponseProjectAndResponsible(
            code=0,
            message=f"institution obtained succesfully",
            data=data_response
        )

        return response
