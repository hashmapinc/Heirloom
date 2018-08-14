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


class BatchStatusesInnerInvalidTransactions(object):
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
        'id': 'str',
        'message': 'str',
        'extended_data': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'extended_data': 'extended_data'
    }

    def __init__(self, id=None, message=None, extended_data=None):  # noqa: E501
        """BatchStatusesInnerInvalidTransactions - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._message = None
        self._extended_data = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if extended_data is not None:
            self.extended_data = extended_data

    @property
    def id(self):
        """Gets the id of this BatchStatusesInnerInvalidTransactions.  # noqa: E501


        :return: The id of this BatchStatusesInnerInvalidTransactions.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchStatusesInnerInvalidTransactions.


        :param id: The id of this BatchStatusesInnerInvalidTransactions.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this BatchStatusesInnerInvalidTransactions.  # noqa: E501


        :return: The message of this BatchStatusesInnerInvalidTransactions.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BatchStatusesInnerInvalidTransactions.


        :param message: The message of this BatchStatusesInnerInvalidTransactions.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def extended_data(self):
        """Gets the extended_data of this BatchStatusesInnerInvalidTransactions.  # noqa: E501


        :return: The extended_data of this BatchStatusesInnerInvalidTransactions.  # noqa: E501
        :rtype: str
        """
        return self._extended_data

    @extended_data.setter
    def extended_data(self, extended_data):
        """Sets the extended_data of this BatchStatusesInnerInvalidTransactions.


        :param extended_data: The extended_data of this BatchStatusesInnerInvalidTransactions.  # noqa: E501
        :type: str
        """
        if extended_data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', extended_data):  # noqa: E501
            raise ValueError("Invalid value for `extended_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._extended_data = extended_data

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
        if not isinstance(other, BatchStatusesInnerInvalidTransactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
