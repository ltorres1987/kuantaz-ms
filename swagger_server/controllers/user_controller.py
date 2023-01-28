import connexion
import six

from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.frameworks.db.sqlalchemy import SQLAlchemyClient
from swagger_server.repository.user_repository import UserRepository
from swagger_server.use_case.user_use_case import UserUsecase
from swagger_server.models.response400 import Response400
from swagger_server.utils.logging import log as logging
from swagger_server import util
from flask.views import MethodView
from timeit import default_timer


class UserView(MethodView):
    """Create service"""

    def __init__(self):
        sqlalchemy_client = SQLAlchemyClient()
        user_repository = UserRepository(sqlalchemy_client)
        sqlalchemy_client.create_tables()
        user_usecase = UserUsecase(user_repository)
        self.user_usecase = user_usecase
        self.msg_log = 'funcion: %r - paquete : %r - mensaje: %r '

    def get_user(self):
        """Lista users

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_user"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.user_usecase.get_user()

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

    def get_user_by_rut(self, user_rut):
        """Lista users by Rut

        Args:
            user_rut (integer): user_rut

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_user_by_rut"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.user_usecase.get_user_by_rut(user_rut)

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
