from swagger_server.utils.utils import format_date


# Entidad representando a un product.


class User:

    def __init__(
            self, id, first_name, last_name, rut, birth_date, position, age, created_user, created_at=None,
            updated_user=None, updated_at=None,
            status=None
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.rut = rut
        self.birth_date = birth_date
        self.position = position
        self.age = age

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
        first_name = dict.get("first_name")
        last_name = dict.get("last_name")
        rut = dict.get("rut")
        birth_date = dict.get("birth_date")
        position = dict.get("position")
        age = dict.get("age")

        created_user = dict.get("created_user")
        created_at = dict.get("created_at")
        updated_user = dict.get("updated_user")
        updated_at = dict.get("updated_at")
        status = dict.get("status")

        return User(cod, first_name, last_name, rut, birth_date, position, age, created_user, created_at, updated_user,
                    updated_at, status)
