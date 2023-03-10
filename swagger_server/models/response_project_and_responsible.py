# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_project_and_responsible_data import ResponseProjectAndResponsibleData  # noqa: F401,E501
from swagger_server import util


class ResponseProjectAndResponsible(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None, message: str=None, data: List[ResponseProjectAndResponsibleData]=None):  # noqa: E501
        """ResponseProjectAndResponsible - a model defined in Swagger

        :param code: The code of this ResponseProjectAndResponsible.  # noqa: E501
        :type code: str
        :param message: The message of this ResponseProjectAndResponsible.  # noqa: E501
        :type message: str
        :param data: The data of this ResponseProjectAndResponsible.  # noqa: E501
        :type data: List[ResponseProjectAndResponsibleData]
        """
        self.swagger_types = {
            'code': str,
            'message': str,
            'data': List[ResponseProjectAndResponsibleData]
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message',
            'data': 'data'
        }
        self._code = code
        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseProjectAndResponsible':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseProjectAndResponsible of this ResponseProjectAndResponsible.  # noqa: E501
        :rtype: ResponseProjectAndResponsible
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this ResponseProjectAndResponsible.


        :return: The code of this ResponseProjectAndResponsible.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ResponseProjectAndResponsible.


        :param code: The code of this ResponseProjectAndResponsible.
        :type code: str
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ResponseProjectAndResponsible.


        :return: The message of this ResponseProjectAndResponsible.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseProjectAndResponsible.


        :param message: The message of this ResponseProjectAndResponsible.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> List[ResponseProjectAndResponsibleData]:
        """Gets the data of this ResponseProjectAndResponsible.


        :return: The data of this ResponseProjectAndResponsible.
        :rtype: List[ResponseProjectAndResponsibleData]
        """
        return self._data

    @data.setter
    def data(self, data: List[ResponseProjectAndResponsibleData]):
        """Sets the data of this ResponseProjectAndResponsible.


        :param data: The data of this ResponseProjectAndResponsible.
        :type data: List[ResponseProjectAndResponsibleData]
        """

        self._data = data
