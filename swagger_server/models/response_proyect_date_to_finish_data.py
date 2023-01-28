# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseProyectDateToFinishData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, description: str=None, responsible: str=None, date_finish: int=None, start_date: str=None, end_date: str=None, created_user: str=None, created_at: str=None, updated_user: str=None, updated_at: str=None, status: str=None):  # noqa: E501
        """ResponseProyectDateToFinishData - a model defined in Swagger

        :param id: The id of this ResponseProyectDateToFinishData.  # noqa: E501
        :type id: int
        :param name: The name of this ResponseProyectDateToFinishData.  # noqa: E501
        :type name: str
        :param description: The description of this ResponseProyectDateToFinishData.  # noqa: E501
        :type description: str
        :param responsible: The responsible of this ResponseProyectDateToFinishData.  # noqa: E501
        :type responsible: str
        :param date_finish: The date_finish of this ResponseProyectDateToFinishData.  # noqa: E501
        :type date_finish: int
        :param start_date: The start_date of this ResponseProyectDateToFinishData.  # noqa: E501
        :type start_date: str
        :param end_date: The end_date of this ResponseProyectDateToFinishData.  # noqa: E501
        :type end_date: str
        :param created_user: The created_user of this ResponseProyectDateToFinishData.  # noqa: E501
        :type created_user: str
        :param created_at: The created_at of this ResponseProyectDateToFinishData.  # noqa: E501
        :type created_at: str
        :param updated_user: The updated_user of this ResponseProyectDateToFinishData.  # noqa: E501
        :type updated_user: str
        :param updated_at: The updated_at of this ResponseProyectDateToFinishData.  # noqa: E501
        :type updated_at: str
        :param status: The status of this ResponseProyectDateToFinishData.  # noqa: E501
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'description': str,
            'responsible': str,
            'date_finish': int,
            'start_date': str,
            'end_date': str,
            'created_user': str,
            'created_at': str,
            'updated_user': str,
            'updated_at': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'responsible': 'responsible',
            'date_finish': 'dateFinish',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'created_user': 'createdUser',
            'created_at': 'createdAt',
            'updated_user': 'updatedUser',
            'updated_at': 'updatedAt',
            'status': 'status'
        }
        self._id = id
        self._name = name
        self._description = description
        self._responsible = responsible
        self._date_finish = date_finish
        self._start_date = start_date
        self._end_date = end_date
        self._created_user = created_user
        self._created_at = created_at
        self._updated_user = updated_user
        self._updated_at = updated_at
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseProyectDateToFinishData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseProyectDateToFinishData of this ResponseProyectDateToFinishData.  # noqa: E501
        :rtype: ResponseProyectDateToFinishData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ResponseProyectDateToFinishData.


        :return: The id of this ResponseProyectDateToFinishData.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ResponseProyectDateToFinishData.


        :param id: The id of this ResponseProyectDateToFinishData.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this ResponseProyectDateToFinishData.


        :return: The name of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ResponseProyectDateToFinishData.


        :param name: The name of this ResponseProyectDateToFinishData.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this ResponseProyectDateToFinishData.


        :return: The description of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ResponseProyectDateToFinishData.


        :param description: The description of this ResponseProyectDateToFinishData.
        :type description: str
        """

        self._description = description

    @property
    def responsible(self) -> str:
        """Gets the responsible of this ResponseProyectDateToFinishData.


        :return: The responsible of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._responsible

    @responsible.setter
    def responsible(self, responsible: str):
        """Sets the responsible of this ResponseProyectDateToFinishData.


        :param responsible: The responsible of this ResponseProyectDateToFinishData.
        :type responsible: str
        """

        self._responsible = responsible

    @property
    def date_finish(self) -> int:
        """Gets the date_finish of this ResponseProyectDateToFinishData.


        :return: The date_finish of this ResponseProyectDateToFinishData.
        :rtype: int
        """
        return self._date_finish

    @date_finish.setter
    def date_finish(self, date_finish: int):
        """Sets the date_finish of this ResponseProyectDateToFinishData.


        :param date_finish: The date_finish of this ResponseProyectDateToFinishData.
        :type date_finish: int
        """

        self._date_finish = date_finish

    @property
    def start_date(self) -> str:
        """Gets the start_date of this ResponseProyectDateToFinishData.


        :return: The start_date of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: str):
        """Sets the start_date of this ResponseProyectDateToFinishData.


        :param start_date: The start_date of this ResponseProyectDateToFinishData.
        :type start_date: str
        """

        self._start_date = start_date

    @property
    def end_date(self) -> str:
        """Gets the end_date of this ResponseProyectDateToFinishData.


        :return: The end_date of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: str):
        """Sets the end_date of this ResponseProyectDateToFinishData.


        :param end_date: The end_date of this ResponseProyectDateToFinishData.
        :type end_date: str
        """

        self._end_date = end_date

    @property
    def created_user(self) -> str:
        """Gets the created_user of this ResponseProyectDateToFinishData.


        :return: The created_user of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user: str):
        """Sets the created_user of this ResponseProyectDateToFinishData.


        :param created_user: The created_user of this ResponseProyectDateToFinishData.
        :type created_user: str
        """

        self._created_user = created_user

    @property
    def created_at(self) -> str:
        """Gets the created_at of this ResponseProyectDateToFinishData.


        :return: The created_at of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this ResponseProyectDateToFinishData.


        :param created_at: The created_at of this ResponseProyectDateToFinishData.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def updated_user(self) -> str:
        """Gets the updated_user of this ResponseProyectDateToFinishData.


        :return: The updated_user of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._updated_user

    @updated_user.setter
    def updated_user(self, updated_user: str):
        """Sets the updated_user of this ResponseProyectDateToFinishData.


        :param updated_user: The updated_user of this ResponseProyectDateToFinishData.
        :type updated_user: str
        """

        self._updated_user = updated_user

    @property
    def updated_at(self) -> str:
        """Gets the updated_at of this ResponseProyectDateToFinishData.


        :return: The updated_at of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: str):
        """Sets the updated_at of this ResponseProyectDateToFinishData.


        :param updated_at: The updated_at of this ResponseProyectDateToFinishData.
        :type updated_at: str
        """

        self._updated_at = updated_at

    @property
    def status(self) -> str:
        """Gets the status of this ResponseProyectDateToFinishData.


        :return: The status of this ResponseProyectDateToFinishData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this ResponseProyectDateToFinishData.


        :param status: The status of this ResponseProyectDateToFinishData.
        :type status: str
        """

        self._status = status