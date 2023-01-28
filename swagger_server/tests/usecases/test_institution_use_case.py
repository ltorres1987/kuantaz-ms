import pytest

from datetime import datetime
from unittest.mock import Mock

from swagger_server.entity.institution_entity import Institution
from swagger_server.use_case.institution_use_case import InstitutionUsecase


@pytest.fixture
def repository_mock():
    return Mock()


@pytest.fixture
def manage_institution_usecase(repository_mock):
    return InstitutionUsecase(repository_mock)


class TestInstitutionUsecase:

    def test_get_institution(self, manage_institution_usecase):
        # Definir que el mock del repositorio retorne tres institution.

        mock_institutions = [
            Institution(1, "Instituto 1", "Descripcion 1", "address 1", "admin"),
            Institution(2, "Instituto 2", "Descripcion 2", "address 2", "admin"),
            Institution(3, "Instituto 3", "Descripcion 3", "address 3", "admin"),
        ]

        manage_institution_usecase.institution_repository.get_institution.return_value = mock_institutions

        # Obtener los institution desde el caso de uso, y afirmar que se haya
        # retornado la cantidad correcta de institution.

        institutions = manage_institution_usecase.get_institution()

        assert len(institutions.data) == len(mock_institutions)
