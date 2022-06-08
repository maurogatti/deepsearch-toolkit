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


class RelationshipAnnotationColumn(object):
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
        'entities': 'list[str]',
        'key': 'str'
    }

    attribute_map = {
        'entities': 'entities',
        'key': 'key'
    }

    def __init__(self, entities=None, key=None, local_vars_configuration=None):  # noqa: E501
        """RelationshipAnnotationColumn - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entities = None
        self._key = None
        self.discriminator = None

        self.entities = entities
        self.key = key

    @property
    def entities(self):
        """Gets the entities of this RelationshipAnnotationColumn.  # noqa: E501


        :return: The entities of this RelationshipAnnotationColumn.  # noqa: E501
        :rtype: list[str]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this RelationshipAnnotationColumn.


        :param entities: The entities of this RelationshipAnnotationColumn.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and entities is None:  # noqa: E501
            raise ValueError("Invalid value for `entities`, must not be `None`")  # noqa: E501

        self._entities = entities

    @property
    def key(self):
        """Gets the key of this RelationshipAnnotationColumn.  # noqa: E501


        :return: The key of this RelationshipAnnotationColumn.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this RelationshipAnnotationColumn.


        :param key: The key of this RelationshipAnnotationColumn.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if not isinstance(other, RelationshipAnnotationColumn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelationshipAnnotationColumn):
            return True

        return self.to_dict() != other.to_dict()
