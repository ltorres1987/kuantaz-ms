from swagger_server.utils.utils import format_date


# Entidad representando a un product.


class Institution:

    def __init__(
            self, id, name, description, address, created_user, created_at=None, updated_user=None, updated_at=None,
            status=None
    ):
        self.id = id
        self.name = name
        self.description = description
        self.address = address

        self.created_user = created_user
        self.created_at = created_at
        self.updated_user = updated_user
        self.updated_at = updated_at
        self.status = status

    @classmethod
    def from_dict(cls, dict):
        # Retorna una instancia de este objeto desde un diccionario de datos,
        # para no tener que llamar al constructor pasando los datos uno a uno.
        # Si un campo falta en el diccionario, se asume valor None.

        cod = dict.get("id")
        name = dict.get("name")
        description = dict.get("description")
        address = dict.get("address")

        created_user = dict.get("created_user")
        created_at = dict.get("created_at")
        updated_user = dict.get("updated_user")
        updated_at = dict.get("updated_at")
        status = dict.get("status")

        return Institution(cod, name, description, address, created_user, created_at, updated_user, updated_at, status)
