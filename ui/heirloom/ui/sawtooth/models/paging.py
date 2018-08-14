# coding: utf-8

"""
    Sawtooth REST API

    _This HTTP pragmatic REST API is built on top of Sawtooth's existing ZMQ/Protobuf infrastructure, simplifying client interaction with the blockchain by exposing endpoints that use common HTTP/JSON standards._   # noqa: E501

    OpenAPI spec version: 0.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Paging(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start': 'str',
        'limit': 'int',
        'next_position': 'str',
        'next': 'str'
    }

    attribute_map = {
        'start': 'start',
        'limit': 'limit',
        'next_position': 'next_position',
        'next': 'next'
    }

    def __init__(self, start=None, limit=None, next_position=None, next=None):  # noqa: E501
        """Paging - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._limit = None
        self._next_position = None
        self._next = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit
        if next_position is not None:
            self.next_position = next_position
        if next is not None:
            self.next = next

    @property
    def start(self):
        """Gets the start of this Paging.  # noqa: E501


        :return: The start of this Paging.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Paging.


        :param start: The start of this Paging.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def limit(self):
        """Gets the limit of this Paging.  # noqa: E501


        :return: The limit of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Paging.


        :param limit: The limit of this Paging.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def next_position(self):
        """Gets the next_position of this Paging.  # noqa: E501


        :return: The next_position of this Paging.  # noqa: E501
        :rtype: str
        """
        return self._next_position

    @next_position.setter
    def next_position(self, next_position):
        """Sets the next_position of this Paging.


        :param next_position: The next_position of this Paging.  # noqa: E501
        :type: str
        """

        self._next_position = next_position

    @property
    def next(self):
        """Gets the next of this Paging.  # noqa: E501


        :return: The next of this Paging.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Paging.


        :param next: The next of this Paging.  # noqa: E501
        :type: str
        """

        self._next = next

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Paging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other