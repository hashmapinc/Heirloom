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

from swagger_client.models.link import Link  # noqa: F401,E501


class InlineResponse2009(object):
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
        'data': 'list[str]',
        'link': 'Link'
    }

    attribute_map = {
        'data': 'data',
        'link': 'link'
    }

    def __init__(self, data=None, link=None):  # noqa: E501
        """InlineResponse2009 - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._link = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if link is not None:
            self.link = link

    @property
    def data(self):
        """Gets the data of this InlineResponse2009.  # noqa: E501


        :return: The data of this InlineResponse2009.  # noqa: E501
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse2009.


        :param data: The data of this InlineResponse2009.  # noqa: E501
        :type: list[str]
        """

        self._data = data

    @property
    def link(self):
        """Gets the link of this InlineResponse2009.  # noqa: E501


        :return: The link of this InlineResponse2009.  # noqa: E501
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InlineResponse2009.


        :param link: The link of this InlineResponse2009.  # noqa: E501
        :type: Link
        """

        self._link = link

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
        if not isinstance(other, InlineResponse2009):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
