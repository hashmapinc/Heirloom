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


class TransactionHeader(object):
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
        'batcher_public_key': 'str',
        'dependencies': 'list[str]',
        'family_name': 'str',
        'family_version': 'str',
        'inputs': 'list[str]',
        'nonce': 'str',
        'outputs': 'list[str]',
        'payload_sha512': 'str',
        'signer_public_key': 'str'
    }

    attribute_map = {
        'batcher_public_key': 'batcher_public_key',
        'dependencies': 'dependencies',
        'family_name': 'family_name',
        'family_version': 'family_version',
        'inputs': 'inputs',
        'nonce': 'nonce',
        'outputs': 'outputs',
        'payload_sha512': 'payload_sha512',
        'signer_public_key': 'signer_public_key'
    }

    def __init__(self, batcher_public_key=None, dependencies=None, family_name=None, family_version=None, inputs=None, nonce=None, outputs=None, payload_sha512=None, signer_public_key=None):  # noqa: E501
        """TransactionHeader - a model defined in Swagger"""  # noqa: E501

        self._batcher_public_key = None
        self._dependencies = None
        self._family_name = None
        self._family_version = None
        self._inputs = None
        self._nonce = None
        self._outputs = None
        self._payload_sha512 = None
        self._signer_public_key = None
        self.discriminator = None

        if batcher_public_key is not None:
            self.batcher_public_key = batcher_public_key
        if dependencies is not None:
            self.dependencies = dependencies
        if family_name is not None:
            self.family_name = family_name
        if family_version is not None:
            self.family_version = family_version
        if inputs is not None:
            self.inputs = inputs
        if nonce is not None:
            self.nonce = nonce
        if outputs is not None:
            self.outputs = outputs
        if payload_sha512 is not None:
            self.payload_sha512 = payload_sha512
        if signer_public_key is not None:
            self.signer_public_key = signer_public_key

    @property
    def batcher_public_key(self):
        """Gets the batcher_public_key of this TransactionHeader.  # noqa: E501


        :return: The batcher_public_key of this TransactionHeader.  # noqa: E501
        :rtype: str
        """
        return self._batcher_public_key

    @batcher_public_key.setter
    def batcher_public_key(self, batcher_public_key):
        """Sets the batcher_public_key of this TransactionHeader.


        :param batcher_public_key: The batcher_public_key of this TransactionHeader.  # noqa: E501
        :type: str
        """

        self._batcher_public_key = batcher_public_key

    @property
    def dependencies(self):
        """Gets the dependencies of this TransactionHeader.  # noqa: E501


        :return: The dependencies of this TransactionHeader.  # noqa: E501
        :rtype: list[str]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this TransactionHeader.


        :param dependencies: The dependencies of this TransactionHeader.  # noqa: E501
        :type: list[str]
        """

        self._dependencies = dependencies

    @property
    def family_name(self):
        """Gets the family_name of this TransactionHeader.  # noqa: E501


        :return: The family_name of this TransactionHeader.  # noqa: E501
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this TransactionHeader.


        :param family_name: The family_name of this TransactionHeader.  # noqa: E501
        :type: str
        """

        self._family_name = family_name

    @property
    def family_version(self):
        """Gets the family_version of this TransactionHeader.  # noqa: E501


        :return: The family_version of this TransactionHeader.  # noqa: E501
        :rtype: str
        """
        return self._family_version

    @family_version.setter
    def family_version(self, family_version):
        """Sets the family_version of this TransactionHeader.


        :param family_version: The family_version of this TransactionHeader.  # noqa: E501
        :type: str
        """

        self._family_version = family_version

    @property
    def inputs(self):
        """Gets the inputs of this TransactionHeader.  # noqa: E501


        :return: The inputs of this TransactionHeader.  # noqa: E501
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TransactionHeader.


        :param inputs: The inputs of this TransactionHeader.  # noqa: E501
        :type: list[str]
        """

        self._inputs = inputs

    @property
    def nonce(self):
        """Gets the nonce of this TransactionHeader.  # noqa: E501


        :return: The nonce of this TransactionHeader.  # noqa: E501
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """Sets the nonce of this TransactionHeader.


        :param nonce: The nonce of this TransactionHeader.  # noqa: E501
        :type: str
        """

        self._nonce = nonce

    @property
    def outputs(self):
        """Gets the outputs of this TransactionHeader.  # noqa: E501


        :return: The outputs of this TransactionHeader.  # noqa: E501
        :rtype: list[str]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TransactionHeader.


        :param outputs: The outputs of this TransactionHeader.  # noqa: E501
        :type: list[str]
        """

        self._outputs = outputs

    @property
    def payload_sha512(self):
        """Gets the payload_sha512 of this TransactionHeader.  # noqa: E501


        :return: The payload_sha512 of this TransactionHeader.  # noqa: E501
        :rtype: str
        """
        return self._payload_sha512

    @payload_sha512.setter
    def payload_sha512(self, payload_sha512):
        """Sets the payload_sha512 of this TransactionHeader.


        :param payload_sha512: The payload_sha512 of this TransactionHeader.  # noqa: E501
        :type: str
        """

        self._payload_sha512 = payload_sha512

    @property
    def signer_public_key(self):
        """Gets the signer_public_key of this TransactionHeader.  # noqa: E501


        :return: The signer_public_key of this TransactionHeader.  # noqa: E501
        :rtype: str
        """
        return self._signer_public_key

    @signer_public_key.setter
    def signer_public_key(self, signer_public_key):
        """Sets the signer_public_key of this TransactionHeader.


        :param signer_public_key: The signer_public_key of this TransactionHeader.  # noqa: E501
        :type: str
        """

        self._signer_public_key = signer_public_key

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
        if not isinstance(other, TransactionHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
