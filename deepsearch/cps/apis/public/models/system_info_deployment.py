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


class SystemInfoDeployment(object):
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
        'disable_kg_actions': 'bool',
        'disclaimer': 'str',
        'linked_ccs_api': 'SystemInfoDeploymentLinkedCcsApi',
        'name': 'str',
        'should_show_warning': 'bool'
    }

    attribute_map = {
        'disable_kg_actions': 'disable_kg_actions',
        'disclaimer': 'disclaimer',
        'linked_ccs_api': 'linked_ccs_api',
        'name': 'name',
        'should_show_warning': 'should_show_warning'
    }

    def __init__(self, disable_kg_actions=None, disclaimer=None, linked_ccs_api=None, name=None, should_show_warning=None, local_vars_configuration=None):  # noqa: E501
        """SystemInfoDeployment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._disable_kg_actions = None
        self._disclaimer = None
        self._linked_ccs_api = None
        self._name = None
        self._should_show_warning = None
        self.discriminator = None

        if disable_kg_actions is not None:
            self.disable_kg_actions = disable_kg_actions
        if disclaimer is not None:
            self.disclaimer = disclaimer
        if linked_ccs_api is not None:
            self.linked_ccs_api = linked_ccs_api
        if name is not None:
            self.name = name
        if should_show_warning is not None:
            self.should_show_warning = should_show_warning

    @property
    def disable_kg_actions(self):
        """Gets the disable_kg_actions of this SystemInfoDeployment.  # noqa: E501


        :return: The disable_kg_actions of this SystemInfoDeployment.  # noqa: E501
        :rtype: bool
        """
        return self._disable_kg_actions

    @disable_kg_actions.setter
    def disable_kg_actions(self, disable_kg_actions):
        """Sets the disable_kg_actions of this SystemInfoDeployment.


        :param disable_kg_actions: The disable_kg_actions of this SystemInfoDeployment.  # noqa: E501
        :type: bool
        """

        self._disable_kg_actions = disable_kg_actions

    @property
    def disclaimer(self):
        """Gets the disclaimer of this SystemInfoDeployment.  # noqa: E501


        :return: The disclaimer of this SystemInfoDeployment.  # noqa: E501
        :rtype: str
        """
        return self._disclaimer

    @disclaimer.setter
    def disclaimer(self, disclaimer):
        """Sets the disclaimer of this SystemInfoDeployment.


        :param disclaimer: The disclaimer of this SystemInfoDeployment.  # noqa: E501
        :type: str
        """

        self._disclaimer = disclaimer

    @property
    def linked_ccs_api(self):
        """Gets the linked_ccs_api of this SystemInfoDeployment.  # noqa: E501


        :return: The linked_ccs_api of this SystemInfoDeployment.  # noqa: E501
        :rtype: SystemInfoDeploymentLinkedCcsApi
        """
        return self._linked_ccs_api

    @linked_ccs_api.setter
    def linked_ccs_api(self, linked_ccs_api):
        """Sets the linked_ccs_api of this SystemInfoDeployment.


        :param linked_ccs_api: The linked_ccs_api of this SystemInfoDeployment.  # noqa: E501
        :type: SystemInfoDeploymentLinkedCcsApi
        """

        self._linked_ccs_api = linked_ccs_api

    @property
    def name(self):
        """Gets the name of this SystemInfoDeployment.  # noqa: E501


        :return: The name of this SystemInfoDeployment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemInfoDeployment.


        :param name: The name of this SystemInfoDeployment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def should_show_warning(self):
        """Gets the should_show_warning of this SystemInfoDeployment.  # noqa: E501


        :return: The should_show_warning of this SystemInfoDeployment.  # noqa: E501
        :rtype: bool
        """
        return self._should_show_warning

    @should_show_warning.setter
    def should_show_warning(self, should_show_warning):
        """Sets the should_show_warning of this SystemInfoDeployment.


        :param should_show_warning: The should_show_warning of this SystemInfoDeployment.  # noqa: E501
        :type: bool
        """

        self._should_show_warning = should_show_warning

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
        if not isinstance(other, SystemInfoDeployment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemInfoDeployment):
            return True

        return self.to_dict() != other.to_dict()
