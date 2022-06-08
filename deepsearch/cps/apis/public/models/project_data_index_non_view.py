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


class ProjectDataIndexNonView(object):
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
        'description': 'str',
        'name': 'str',
        'schema_key': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'schema_key': 'schema_key'
    }

    def __init__(self, description=None, name=None, schema_key='generic', local_vars_configuration=None):  # noqa: E501
        """ProjectDataIndexNonView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._schema_key = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        if schema_key is not None:
            self.schema_key = schema_key

    @property
    def description(self):
        """Gets the description of this ProjectDataIndexNonView.  # noqa: E501

        Description of the Index  # noqa: E501

        :return: The description of this ProjectDataIndexNonView.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectDataIndexNonView.

        Description of the Index  # noqa: E501

        :param description: The description of this ProjectDataIndexNonView.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 254):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `254`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this ProjectDataIndexNonView.  # noqa: E501

        Name of the data index  # noqa: E501

        :return: The name of this ProjectDataIndexNonView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectDataIndexNonView.

        Name of the data index  # noqa: E501

        :param name: The name of this ProjectDataIndexNonView.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def schema_key(self):
        """Gets the schema_key of this ProjectDataIndexNonView.  # noqa: E501

        Schema key  # noqa: E501

        :return: The schema_key of this ProjectDataIndexNonView.  # noqa: E501
        :rtype: str
        """
        return self._schema_key

    @schema_key.setter
    def schema_key(self, schema_key):
        """Sets the schema_key of this ProjectDataIndexNonView.

        Schema key  # noqa: E501

        :param schema_key: The schema_key of this ProjectDataIndexNonView.  # noqa: E501
        :type: str
        """
        allowed_values = ["deepsearch-doc", "deepsearch-db", "generic"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and schema_key not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `schema_key` ({0}), must be one of {1}"  # noqa: E501
                .format(schema_key, allowed_values)
            )

        self._schema_key = schema_key

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
        if not isinstance(other, ProjectDataIndexNonView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDataIndexNonView):
            return True

        return self.to_dict() != other.to_dict()
