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


class LoadKgcDataInputDataflow(object):
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
        'config': 'object',
        'data_flow': 'list[object]'
    }

    attribute_map = {
        'config': 'config',
        'data_flow': 'data-flow'
    }

    def __init__(self, config=None, data_flow=None, local_vars_configuration=None):  # noqa: E501
        """LoadKgcDataInputDataflow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config = None
        self._data_flow = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if data_flow is not None:
            self.data_flow = data_flow

    @property
    def config(self):
        """Gets the config of this LoadKgcDataInputDataflow.  # noqa: E501


        :return: The config of this LoadKgcDataInputDataflow.  # noqa: E501
        :rtype: object
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this LoadKgcDataInputDataflow.


        :param config: The config of this LoadKgcDataInputDataflow.  # noqa: E501
        :type: object
        """

        self._config = config

    @property
    def data_flow(self):
        """Gets the data_flow of this LoadKgcDataInputDataflow.  # noqa: E501


        :return: The data_flow of this LoadKgcDataInputDataflow.  # noqa: E501
        :rtype: list[object]
        """
        return self._data_flow

    @data_flow.setter
    def data_flow(self, data_flow):
        """Sets the data_flow of this LoadKgcDataInputDataflow.


        :param data_flow: The data_flow of this LoadKgcDataInputDataflow.  # noqa: E501
        :type: list[object]
        """

        self._data_flow = data_flow

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
        if not isinstance(other, LoadKgcDataInputDataflow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoadKgcDataInputDataflow):
            return True

        return self.to_dict() != other.to_dict()
