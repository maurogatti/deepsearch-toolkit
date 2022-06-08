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


class ProjectDefaultValues(object):
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
        'ccs_project': 'ProjectDefaultValuesCcsProject',
        'dataflow': 'ProjectDefaultValuesDataflow'
    }

    attribute_map = {
        'ccs_project': 'ccs_project',
        'dataflow': 'dataflow'
    }

    def __init__(self, ccs_project=None, dataflow=None, local_vars_configuration=None):  # noqa: E501
        """ProjectDefaultValues - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ccs_project = None
        self._dataflow = None
        self.discriminator = None

        if ccs_project is not None:
            self.ccs_project = ccs_project
        if dataflow is not None:
            self.dataflow = dataflow

    @property
    def ccs_project(self):
        """Gets the ccs_project of this ProjectDefaultValues.  # noqa: E501


        :return: The ccs_project of this ProjectDefaultValues.  # noqa: E501
        :rtype: ProjectDefaultValuesCcsProject
        """
        return self._ccs_project

    @ccs_project.setter
    def ccs_project(self, ccs_project):
        """Sets the ccs_project of this ProjectDefaultValues.


        :param ccs_project: The ccs_project of this ProjectDefaultValues.  # noqa: E501
        :type: ProjectDefaultValuesCcsProject
        """

        self._ccs_project = ccs_project

    @property
    def dataflow(self):
        """Gets the dataflow of this ProjectDefaultValues.  # noqa: E501


        :return: The dataflow of this ProjectDefaultValues.  # noqa: E501
        :rtype: ProjectDefaultValuesDataflow
        """
        return self._dataflow

    @dataflow.setter
    def dataflow(self, dataflow):
        """Sets the dataflow of this ProjectDefaultValues.


        :param dataflow: The dataflow of this ProjectDefaultValues.  # noqa: E501
        :type: ProjectDefaultValuesDataflow
        """

        self._dataflow = dataflow

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
        if not isinstance(other, ProjectDefaultValues):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDefaultValues):
            return True

        return self.to_dict() != other.to_dict()
