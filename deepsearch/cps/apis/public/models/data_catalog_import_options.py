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


class DataCatalogImportOptions(object):
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
        'options': 'ProjectProjKeyDataCataloguesFromMongoOptions',
        'target': 'ProjectProjKeyDataCataloguesFromMongoTarget'
    }

    attribute_map = {
        'options': 'options',
        'target': 'target'
    }

    def __init__(self, options=None, target=None, local_vars_configuration=None):  # noqa: E501
        """DataCatalogImportOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._options = None
        self._target = None
        self.discriminator = None

        self.options = options
        self.target = target

    @property
    def options(self):
        """Gets the options of this DataCatalogImportOptions.  # noqa: E501


        :return: The options of this DataCatalogImportOptions.  # noqa: E501
        :rtype: ProjectProjKeyDataCataloguesFromMongoOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DataCatalogImportOptions.


        :param options: The options of this DataCatalogImportOptions.  # noqa: E501
        :type: ProjectProjKeyDataCataloguesFromMongoOptions
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def target(self):
        """Gets the target of this DataCatalogImportOptions.  # noqa: E501


        :return: The target of this DataCatalogImportOptions.  # noqa: E501
        :rtype: ProjectProjKeyDataCataloguesFromMongoTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this DataCatalogImportOptions.


        :param target: The target of this DataCatalogImportOptions.  # noqa: E501
        :type: ProjectProjKeyDataCataloguesFromMongoTarget
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

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
        if not isinstance(other, DataCatalogImportOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataCatalogImportOptions):
            return True

        return self.to_dict() != other.to_dict()
