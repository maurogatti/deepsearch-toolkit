# coding: utf-8

"""
    Corpus Processing Service (CPS) API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deepsearch.cps.apis.public.configuration import Configuration


class EntityAnnotation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'match': 'str',
        'range': 'list[int]',
        'subtype': 'str',
        'type': 'str'
    }

    attribute_map = {
        'match': 'match',
        'range': 'range',
        'subtype': 'subtype',
        'type': 'type'
    }

    def __init__(self, match=None, range=None, subtype=None, type=None, local_vars_configuration=None):  # noqa: E501
        """EntityAnnotation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._match = None
        self._range = None
        self._subtype = None
        self._type = None
        self.discriminator = None

        self.match = match
        self.range = range
        if subtype is not None:
            self.subtype = subtype
        self.type = type

    @property
    def match(self):
        """Gets the match of this EntityAnnotation.  # noqa: E501


        :return: The match of this EntityAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this EntityAnnotation.


        :param match: The match of this EntityAnnotation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and match is None:  # noqa: E501
            raise ValueError("Invalid value for `match`, must not be `None`")  # noqa: E501

        self._match = match

    @property
    def range(self):
        """Gets the range of this EntityAnnotation.  # noqa: E501

        2-Tuple representing the low and high indexes of the matching substring  # noqa: E501

        :return: The range of this EntityAnnotation.  # noqa: E501
        :rtype: list[int]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this EntityAnnotation.

        2-Tuple representing the low and high indexes of the matching substring  # noqa: E501

        :param range: The range of this EntityAnnotation.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and range is None:  # noqa: E501
            raise ValueError("Invalid value for `range`, must not be `None`")  # noqa: E501

        self._range = range

    @property
    def subtype(self):
        """Gets the subtype of this EntityAnnotation.  # noqa: E501


        :return: The subtype of this EntityAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this EntityAnnotation.


        :param subtype: The subtype of this EntityAnnotation.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

    @property
    def type(self):
        """Gets the type of this EntityAnnotation.  # noqa: E501


        :return: The type of this EntityAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityAnnotation.


        :param type: The type of this EntityAnnotation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, EntityAnnotation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityAnnotation):
            return True

        return self.to_dict() != other.to_dict()
