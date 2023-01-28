import os
from swagger_server.entity.user_entity import User
from swagger_server.utils import utils
from swagger_server.models.response_user import ResponseUser
from swagger_server.models.response_user_data import ResponseUserData
from swagger_server.models.response_user_by_rut import ResponseUserByRut
from swagger_server.models.response_user_by_rut_data import ResponseUserByRutData
from swagger_server.models.response_user_by_rut_detail import ResponseUserByRutDetail


class UserUsecase:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user(self):
        """Lista users

        Returns:
            dict: modelo de datos ResponseUser
        """

        data_response = []
        users = self.user_repository.get_user()

        if not users:
            raise ValueError(f"No existe datos para la consulta")

        for user in users:
            data_response.append(
                ResponseUserData(
                    id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    rut=user.rut,
                    birth_date=user.birth_date,
                    position=user.position,
                    age=user.age,
                    created_user=user.created_user,
                    created_at=user.created_at,
                    updated_user=user.updated_user,
                    updated_at=user.updated_at,
                    status=user.status
                )
            )

        response = ResponseUser(
            code=0,
            message=f"user obtained succesfully",
            data=data_response
        )

        return response

    def get_user_by_rut(self, user_rut):
        """Lista users by Rut

        Args:
           user_rut (integer): user_rut

        Returns:
            dict: modelo de datos ResponseUser
        """

        user = self.user_repository.get_user_by_rut(user_rut)

        if not user:
            raise ValueError(f"user_rut of ID {user_rut} doesn't exist.")

        # detalle de proyectos
        proyects = []
        for detail in user.proyect_detail:
            proyects.append(
                ResponseUserByRutDetail(
                    id=detail.id,
                    name=detail.name,
                    description=detail.description
                )
            )

        data_response = ResponseUserByRutData(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            rut=user.rut,
            birth_date=user.birth_date,
            position=user.position,
            age=user.age,
            created_user=user.created_user,
            created_at=user.created_at,
            updated_user=user.updated_user,
            updated_at=user.updated_at,
            status=user.status,
            proyects=proyects)

        response = ResponseUserByRut(
            code=0,
            message=f"user obtained succesfully",
            data=data_response
        )

        return response
