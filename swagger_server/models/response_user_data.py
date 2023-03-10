# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseUserData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, first_name: str=None, last_name: str=None, rut: str=None, birth_date: str=None, position: str=None, age: int=None, created_user: str=None, created_at: str=None, updated_user: str=None, updated_at: str=None, status: str=None):  # noqa: E501
        """ResponseUserData - a model defined in Swagger

        :param id: The id of this ResponseUserData.  # noqa: E501
        :type id: int
        :param first_name: The first_name of this ResponseUserData.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this ResponseUserData.  # noqa: E501
        :type last_name: str
        :param rut: The rut of this ResponseUserData.  # noqa: E501
        :type rut: str
        :param birth_date: The birth_date of this ResponseUserData.  # noqa: E501
        :type birth_date: str
        :param position: The position of this ResponseUserData.  # noqa: E501
        :type position: str
        :param age: The age of this ResponseUserData.  # noqa: E501
        :type age: int
        :param created_user: The created_user of this ResponseUserData.  # noqa: E501
        :type created_user: str
        :param created_at: The created_at of this ResponseUserData.  # noqa: E501
        :type created_at: str
        :param updated_user: The updated_user of this ResponseUserData.  # noqa: E501
        :type updated_user: str
        :param updated_at: The updated_at of this ResponseUserData.  # noqa: E501
        :type updated_at: str
        :param status: The status of this ResponseUserData.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'first_name': str,
            'last_name': str,
            'rut': str,
            'birth_date': str,
            'position': str,
            'age': int,
            'created_user': str,
            'created_at': str,
            'updated_user': str,
            'updated_at': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'rut': 'rut',
            'birth_date': 'birthDate',
            'position': 'position',
            'age': 'age',
            'created_user': 'createdUser',
            'created_at': 'createdAt',
            'updated_user': 'updatedUser',
            'updated_at': 'updatedAt',
            'status': 'status'
        }
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._rut = rut
        self._birth_date = birth_date
        self._position = position
        self._age = age
        self._created_user = created_user
        self._created_at = created_at
        self._updated_user = updated_user
        self._updated_at = updated_at
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseUserData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseUserData of this ResponseUserData.  # noqa: E501
        :rtype: ResponseUserData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ResponseUserData.


        :return: The id of this ResponseUserData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ResponseUserData.


        :param id: The id of this ResponseUserData.
        :type id: int
        """

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this ResponseUserData.


        :return: The first_name of this ResponseUserData.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this ResponseUserData.


        :param first_name: The first_name of this ResponseUserData.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this ResponseUserData.


        :return: The last_name of this ResponseUserData.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this ResponseUserData.


        :param last_name: The last_name of this ResponseUserData.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def rut(self) -> str:
        """Gets the rut of this ResponseUserData.


        :return: The rut of this ResponseUserData.
        :rtype: str
        """
        return self._rut

    @rut.setter
    def rut(self, rut: str):
        """Sets the rut of this ResponseUserData.


        :param rut: The rut of this ResponseUserData.
        :type rut: str
        """

        self._rut = rut

    @property
    def birth_date(self) -> str:
        """Gets the birth_date of this ResponseUserData.


        :return: The birth_date of this ResponseUserData.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: str):
        """Sets the birth_date of this ResponseUserData.


        :param birth_date: The birth_date of this ResponseUserData.
        :type birth_date: str
        """

        self._birth_date = birth_date

    @property
    def position(self) -> str:
        """Gets the position of this ResponseUserData.


        :return: The position of this ResponseUserData.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position: str):
        """Sets the position of this ResponseUserData.


        :param position: The position of this ResponseUserData.
        :type position: str
        """

        self._position = position

    @property
    def age(self) -> int:
        """Gets the age of this ResponseUserData.


        :return: The age of this ResponseUserData.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this ResponseUserData.


        :param age: The age of this ResponseUserData.
        :type age: int
        """

        self._age = age

    @property
    def created_user(self) -> str:
        """Gets the created_user of this ResponseUserData.


        :return: The created_user of this ResponseUserData.
        :rtype: str
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user: str):
        """Sets the created_user of this ResponseUserData.


        :param created_user: The created_user of this ResponseUserData.
        :type created_user: str
        """

        self._created_user = created_user

    @property
    def created_at(self) -> str:
        """Gets the created_at of this ResponseUserData.


        :return: The created_at of this ResponseUserData.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this ResponseUserData.


        :param created_at: The created_at of this ResponseUserData.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def updated_user(self) -> str:
        """Gets the updated_user of this ResponseUserData.


        :return: The updated_user of this ResponseUserData.
        :rtype: str
        """
        return self._updated_user

    @updated_user.setter
    def updated_user(self, updated_user: str):
        """Sets the updated_user of this ResponseUserData.


        :param updated_user: The updated_user of this ResponseUserData.
        :type updated_user: str
        """

        self._updated_user = updated_user

    @property
    def updated_at(self) -> str:
        """Gets the updated_at of this ResponseUserData.


        :return: The updated_at of this ResponseUserData.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: str):
        """Sets the updated_at of this ResponseUserData.


        :param updated_at: The updated_at of this ResponseUserData.
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def status(self) -> str:
        """Gets the status of this ResponseUserData.


        :return: The status of this ResponseUserData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this ResponseUserData.


        :param status: The status of this ResponseUserData.
        :type status: str
        """

        self._status = status
