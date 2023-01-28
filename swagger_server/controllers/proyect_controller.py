import connexion
import six

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.frameworks.db.sqlalchemy import SQLAlchemyClient
from swagger_server.repository.proyect_repository import ProyectRepository
from swagger_server.use_case.proyect_use_case import ProyectUsecase
from swagger_server.models.response400 import Response400
from swagger_server.utils.logging import log as logging
from swagger_server import util
from flask.views import MethodView
from timeit import default_timer


class ProyectView(MethodView):
    """Create service"""

    def __init__(self):
        sqlalchemy_client = SQLAlchemyClient()
        proyect_repository = ProyectRepository(sqlalchemy_client)
        sqlalchemy_client.create_tables()
        proyect_usecase = ProyectUsecase(proyect_repository)
        self.proyect_usecase = proyect_usecase
        self.msg_log = 'funcion: %r - paquete : %r - mensaje: %r '

    def get_proyect(self):
        """Lista proyectos

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_proyect"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.proyect_usecase.get_proyect()

        except Exception as ex:

            message = str(ex)
            log.critical(self.msg_log, function_name, package_name, message)

            response = Response400(
                code=-1,
                message=message
            )
        finally:
            end_time = default_timer()
            message = f"end request: {function_name} - Procesada en : {round((end_time - start_time) * 1000)} milisegundos "
            log.info(self.msg_log, function_name, package_name, message)

        return response

    def get_proyect_date_to_finish(self):
        """Lista proyectos

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_proyect_date_to_finish"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.proyect_usecase.get_proyect_date_to_finish()

        except Exception as ex:

            message = str(ex)
            log.critical(self.msg_log, function_name, package_name, message)

            response = Response400(
                code=-1,
                message=message
            )
        finally:
            end_time = default_timer()
            message = f"end request: {function_name} - Procesada en : {round((end_time - start_time) * 1000)} milisegundos "
            log.info(self.msg_log, function_name, package_name, message)

        return response
