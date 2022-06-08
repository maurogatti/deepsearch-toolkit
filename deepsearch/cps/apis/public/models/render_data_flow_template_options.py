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


class RenderDataFlowTemplateOptions(object):
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
        'target_bag': 'ProjectProjKeyKgcDataflowTemplatesDfTplKeyActionsLoadRenderTargetBag',
        'variables': 'dict(str, object)'
    }

    attribute_map = {
        'target_bag': 'target_bag',
        'variables': 'variables'
    }

    def __init__(self, target_bag=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """RenderDataFlowTemplateOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target_bag = None
        self._variables = None
        self.discriminator = None

        self.target_bag = target_bag
        self.variables = variables

    @property
    def target_bag(self):
        """Gets the target_bag of this RenderDataFlowTemplateOptions.  # noqa: E501


        :return: The target_bag of this RenderDataFlowTemplateOptions.  # noqa: E501
        :rtype: ProjectProjKeyKgcDataflowTemplatesDfTplKeyActionsLoadRenderTargetBag
        """
        return self._target_bag

    @target_bag.setter
    def target_bag(self, target_bag):
        """Sets the target_bag of this RenderDataFlowTemplateOptions.


        :param target_bag: The target_bag of this RenderDataFlowTemplateOptions.  # noqa: E501
        :type: ProjectProjKeyKgcDataflowTemplatesDfTplKeyActionsLoadRenderTargetBag
        """
        if self.local_vars_configuration.client_side_validation and target_bag is None:  # noqa: E501
            raise ValueError("Invalid value for `target_bag`, must not be `None`")  # noqa: E501

        self._target_bag = target_bag

    @property
    def variables(self):
        """Gets the variables of this RenderDataFlowTemplateOptions.  # noqa: E501


        :return: The variables of this RenderDataFlowTemplateOptions.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this RenderDataFlowTemplateOptions.


        :param variables: The variables of this RenderDataFlowTemplateOptions.  # noqa: E501
        :type: dict(str, object)
        """
        if self.local_vars_configuration.client_side_validation and variables is None:  # noqa: E501
            raise ValueError("Invalid value for `variables`, must not be `None`")  # noqa: E501

        self._variables = variables

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
        if not isinstance(other, RenderDataFlowTemplateOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RenderDataFlowTemplateOptions):
            return True

        return self.to_dict() != other.to_dict()
