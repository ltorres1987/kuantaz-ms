import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.frameworks.db.sqlalchemy import SQLAlchemyClient
from swagger_server.repository.institution_repository import InstitutionRepository
from swagger_server.use_case.institution_use_case import InstitutionUsecase
from swagger_server.models.response400 import Response400
from swagger_server.models.request_institution_add import RequestInstitutionAdd
from swagger_server.models.request_institution_upd import RequestInstitutionUpd
from swagger_server.utils.logging import log as logging
from swagger_server import util
from flask.views import MethodView
from timeit import default_timer


class InstitutionView(MethodView):
    """Create service"""

    def __init__(self):
        sqlalchemy_client = SQLAlchemyClient()
        institution_repository = InstitutionRepository(sqlalchemy_client)
        sqlalchemy_client.create_tables()
        institution_usecase = InstitutionUsecase(institution_repository)
        self.institution_usecase = institution_usecase
        self.msg_log = 'funcion: %r - paquete : %r - mensaje: %r '

    def add_institution(self):
        """Agrega una nueva institución

        Args:
            body (dict | bytes): objeto diccionario tipo RequestInstitutionAdd

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "add_institution"
        package_name = __name__
        log = logging()

        if connexion.request.is_json:

            body = RequestInstitutionAdd.from_dict(connexion.request.get_json())

            message = f"start request: {function_name}"
            log.info(self.msg_log, function_name, package_name, message)

            try:

                response = self.institution_usecase.add_institution(body)

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

    def get_institution(self):
        """Lista instituciones

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_institution"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.institution_usecase.get_institution()

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

    def get_institution_by_id(self, institution_id):
        """Busca una institución por ID

        Args:
            institution_id (integer): institution id

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_institution_by_id"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.institution_usecase.get_institution_by_id(institution_id)

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

    def update_institution(self):
        """Actualiza una institución existente

        Args:
            body (dict | bytes): objeto diccionario tipo RequestInstitutionUpd

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "update_institution"
        package_name = __name__
        log = logging()

        if connexion.request.is_json:

            body = RequestInstitutionUpd.from_dict(connexion.request.get_json())

            message = f"start request: {function_name}"
            log.info(self.msg_log, function_name, package_name, message)

            try:

                response = self.institution_usecase.update_institution(body)

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

    def delete_institution(self, institution_id):
        """Elimina una institución

        Args:
            institution_id (integer): institution id

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "delete_institution"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.institution_usecase.delete_institution(institution_id)

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

    def get_institution_with_address(self):
        """Lista instituciones con la direccion de google maps

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_institution_with_address"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.institution_usecase.get_institution_with_address()

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

    def get_institution_by_project_responsible(self, institution_id):
        """Busca una institución por ID

        Args:
            institution_id (integer): institution id

        Return:
             dict: modelo de datos Response400
        """

        start_time = default_timer()
        function_name = "get_institution_by_project_responsible"
        package_name = __name__
        log = logging()

        message = f"start request: {function_name}"
        log.info(self.msg_log, function_name, package_name, message)

        try:

            response = self.institution_usecase.get_institution_by_project_responsible(institution_id)

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
