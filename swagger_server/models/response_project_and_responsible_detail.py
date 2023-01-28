# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseProjectAndResponsibleDetail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, description: str=None, responsible: str=None):  # noqa: E501
        """ResponseProjectAndResponsibleDetail - a model defined in Swagger

        :param id: The id of this ResponseProjectAndResponsibleDetail.  # noqa: E501
        :type id: int
        :param name: The name of this ResponseProjectAndResponsibleDetail.  # noqa: E501
        :type name: str
        :param description: The description of this ResponseProjectAndResponsibleDetail.  # noqa: E501
        :type description: str
        :param responsible: The responsible of this ResponseProjectAndResponsibleDetail.  # noqa: E501
        :type responsible: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'description': str,
            'responsible': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'responsible': 'responsible'
        }
        self._id = id
        self._name = name
        self._description = description
        self._responsible = responsible

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseProjectAndResponsibleDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseProjectAndResponsibleDetail of this ResponseProjectAndResponsibleDetail.  # noqa: E501
        :rtype: ResponseProjectAndResponsibleDetail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ResponseProjectAndResponsibleDetail.


        :return: The id of this ResponseProjectAndResponsibleDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ResponseProjectAndResponsibleDetail.


        :param id: The id of this ResponseProjectAndResponsibleDetail.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this ResponseProjectAndResponsibleDetail.


        :return: The name of this ResponseProjectAndResponsibleDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ResponseProjectAndResponsibleDetail.


        :param name: The name of this ResponseProjectAndResponsibleDetail.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this ResponseProjectAndResponsibleDetail.


        :return: The description of this ResponseProjectAndResponsibleDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this ResponseProjectAndResponsibleDetail.


        :param description: The description of this ResponseProjectAndResponsibleDetail.
        :type description: str
        """

        self._description = description

    @property
    def responsible(self) -> str:
        """Gets the responsible of this ResponseProjectAndResponsibleDetail.


        :return: The responsible of this ResponseProjectAndResponsibleDetail.
        :rtype: str
        """
        return self._responsible

    @responsible.setter
    def responsible(self, responsible: str):
        """Sets the responsible of this ResponseProjectAndResponsibleDetail.


        :param responsible: The responsible of this ResponseProjectAndResponsibleDetail.
        :type responsible: str
        """

        self._responsible = responsible
