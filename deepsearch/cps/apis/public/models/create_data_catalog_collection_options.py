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


class CreateDataCatalogCollectionOptions(object):
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
        'collection_name': 'str'
    }

    attribute_map = {
        'collection_name': 'collection_name'
    }

    def __init__(self, collection_name=None, local_vars_configuration=None):  # noqa: E501
        """CreateDataCatalogCollectionOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._collection_name = None
        self.discriminator = None

        self.collection_name = collection_name

    @property
    def collection_name(self):
        """Gets the collection_name of this CreateDataCatalogCollectionOptions.  # noqa: E501


        :return: The collection_name of this CreateDataCatalogCollectionOptions.  # noqa: E501
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        """Sets the collection_name of this CreateDataCatalogCollectionOptions.


        :param collection_name: The collection_name of this CreateDataCatalogCollectionOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and collection_name is None:  # noqa: E501
            raise ValueError("Invalid value for `collection_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                collection_name is not None and len(collection_name) > 24):
            raise ValueError("Invalid value for `collection_name`, length must be less than or equal to `24`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                collection_name is not None and len(collection_name) < 4):
            raise ValueError("Invalid value for `collection_name`, length must be greater than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                collection_name is not None and not re.search(r'^(?:\w|-)+$', collection_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `collection_name`, must be a follow pattern or equal to `/^(?:\w|-)+$/`")  # noqa: E501

        self._collection_name = collection_name

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
        if not isinstance(other, CreateDataCatalogCollectionOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDataCatalogCollectionOptions):
            return True

        return self.to_dict() != other.to_dict()
