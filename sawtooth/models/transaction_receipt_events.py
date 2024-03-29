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

from swagger_client.models.transaction_receipt_attributes import TransactionReceiptAttributes  # noqa: F401,E501


class TransactionReceiptEvents(object):
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
        'event_type': 'str',
        'attributes': 'list[TransactionReceiptAttributes]',
        'data': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'attributes': 'attributes',
        'data': 'data'
    }

    def __init__(self, event_type=None, attributes=None, data=None):  # noqa: E501
        """TransactionReceiptEvents - a model defined in Swagger"""  # noqa: E501

        self._event_type = None
        self._attributes = None
        self._data = None
        self.discriminator = None

        if event_type is not None:
            self.event_type = event_type
        if attributes is not None:
            self.attributes = attributes
        if data is not None:
            self.data = data

    @property
    def event_type(self):
        """Gets the event_type of this TransactionReceiptEvents.  # noqa: E501


        :return: The event_type of this TransactionReceiptEvents.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this TransactionReceiptEvents.


        :param event_type: The event_type of this TransactionReceiptEvents.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def attributes(self):
        """Gets the attributes of this TransactionReceiptEvents.  # noqa: E501


        :return: The attributes of this TransactionReceiptEvents.  # noqa: E501
        :rtype: list[TransactionReceiptAttributes]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TransactionReceiptEvents.


        :param attributes: The attributes of this TransactionReceiptEvents.  # noqa: E501
        :type: list[TransactionReceiptAttributes]
        """

        self._attributes = attributes

    @property
    def data(self):
        """Gets the data of this TransactionReceiptEvents.  # noqa: E501


        :return: The data of this TransactionReceiptEvents.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TransactionReceiptEvents.


        :param data: The data of this TransactionReceiptEvents.  # noqa: E501
        :type: str
        """

        self._data = data

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
        if not isinstance(other, TransactionReceiptEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
