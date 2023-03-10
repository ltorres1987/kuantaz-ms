# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_proyect_data import ResponseProyectData  # noqa: F401,E501
from swagger_server import util


class ResponseProyect(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None, message: str=None, data: List[ResponseProyectData]=None):  # noqa: E501
        """ResponseProyect - a model defined in Swagger

        :param code: The code of this ResponseProyect.  # noqa: E501
        :type code: str
        :param message: The message of this ResponseProyect.  # noqa: E501
        :type message: str
        :param data: The data of this ResponseProyect.  # noqa: E501
        :type data: List[ResponseProyectData]
        """
        self.swagger_types = {
            'code': str,
            'message': str,
            'data': List[ResponseProyectData]
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
    def from_dict(cls, dikt) -> 'ResponseProyect':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseProyect of this ResponseProyect.  # noqa: E501
        :rtype: ResponseProyect
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this ResponseProyect.


        :return: The code of this ResponseProyect.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this ResponseProyect.


        :param code: The code of this ResponseProyect.
        :type code: str
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ResponseProyect.


        :return: The message of this ResponseProyect.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ResponseProyect.


        :param message: The message of this ResponseProyect.
        :type message: str
        """

        self._message = message

    @property
    def data(self) -> List[ResponseProyectData]:
        """Gets the data of this ResponseProyect.


        :return: The data of this ResponseProyect.
        :rtype: List[ResponseProyectData]
        """
        return self._data

    @data.setter
    def data(self, data: List[ResponseProyectData]):
        """Sets the data of this ResponseProyect.


        :param data: The data of this ResponseProyect.
        :type data: List[ResponseProyectData]
        """

        self._data = data
