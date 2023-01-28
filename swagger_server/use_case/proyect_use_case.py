import os
from swagger_server.entity.proyect_entity import Proyect
from swagger_server.utils import utils
from swagger_server.models.response_proyect import ResponseProyect
from swagger_server.models.response_proyect_data import ResponseProyectData
from swagger_server.models.response_proyect_date_to_finish import ResponseProyectDateToFinish
from swagger_server.models.response_proyect_date_to_finish_data import ResponseProyectDateToFinishData
from datetime import datetime


class ProyectUsecase:

    def __init__(self, proyect_repository):
        self.proyect_repository = proyect_repository

    def get_proyect(self):
        """Lista proyectos

        Returns:
            dict: modelo de datos ResponseProyect
        """

        data_response = []
        proyects = self.proyect_repository.get_proyect()

        if not proyects:
            raise ValueError(f"No existe datos para la consulta")

        for proyect in proyects:
            data_response.append(
                ResponseProyectData(
                    id=proyect.id,
                    name=proyect.name,
                    description=proyect.description,
                    responsible=f"{proyect.user_detail.first_name} - {proyect.user_detail.last_name}",
                    start_date=proyect.start_date,
                    end_date=proyect.end_date,
                    created_user=proyect.created_user,
                    created_at=proyect.created_at,
                    updated_user=proyect.updated_user,
                    updated_at=proyect.updated_at,
                    status=proyect.status
                )
            )

        response = ResponseProyect(
            code=0,
            message=f"proyect obtained succesfully",
            data=data_response
        )

        return response

    def get_proyect_date_to_finish(self):
        """Lista proyectos

        Returns:
            dict: modelo de datos ResponseProyect
        """

        data_response = []
        proyects = self.proyect_repository.get_proyect()

        if not proyects:
            raise ValueError(f"No existe datos para la consulta")

        for proyect in proyects:
            date_finish = proyect.end_date - proyect.start_date

            data_response.append(
                ResponseProyectDateToFinishData(
                    id=proyect.id,
                    name=proyect.name,
                    description=proyect.description,
                    responsible=f"{proyect.user_detail.first_name} - {proyect.user_detail.last_name}",
                    date_finish=str(date_finish),
                    start_date=proyect.start_date,
                    end_date=proyect.end_date,
                    created_user=proyect.created_user,
                    created_at=proyect.created_at,
                    updated_user=proyect.updated_user,
                    updated_at=proyect.updated_at,
                    status=proyect.status
                )
            )

        response = ResponseProyectDateToFinish(
            code=0,
            message=f"proyect obtained succesfully",
            data=data_response
        )

        return response
