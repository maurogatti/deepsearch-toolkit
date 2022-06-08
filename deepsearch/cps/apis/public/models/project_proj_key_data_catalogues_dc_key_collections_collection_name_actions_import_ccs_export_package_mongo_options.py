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


class ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions(object):
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
        'assemble_options': 'ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsAssembleOptions',
        'incremental': 'bool',
        'inputs': 'ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsInputs',
        'package_options': 'ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions'
    }

    attribute_map = {
        'assemble_options': 'assemble_options',
        'incremental': 'incremental',
        'inputs': 'inputs',
        'package_options': 'package_options'
    }

    def __init__(self, assemble_options=None, incremental=None, inputs=None, package_options=None, local_vars_configuration=None):  # noqa: E501
        """ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assemble_options = None
        self._incremental = None
        self._inputs = None
        self._package_options = None
        self.discriminator = None

        self.assemble_options = assemble_options
        self.incremental = incremental
        if inputs is not None:
            self.inputs = inputs
        self.package_options = package_options

    @property
    def assemble_options(self):
        """Gets the assemble_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501


        :return: The assemble_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :rtype: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsAssembleOptions
        """
        return self._assemble_options

    @assemble_options.setter
    def assemble_options(self, assemble_options):
        """Sets the assemble_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.


        :param assemble_options: The assemble_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :type: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsAssembleOptions
        """
        if self.local_vars_configuration.client_side_validation and assemble_options is None:  # noqa: E501
            raise ValueError("Invalid value for `assemble_options`, must not be `None`")  # noqa: E501

        self._assemble_options = assemble_options

    @property
    def incremental(self):
        """Gets the incremental of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501


        :return: The incremental of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.


        :param incremental: The incremental of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and incremental is None:  # noqa: E501
            raise ValueError("Invalid value for `incremental`, must not be `None`")  # noqa: E501

        self._incremental = incremental

    @property
    def inputs(self):
        """Gets the inputs of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501


        :return: The inputs of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :rtype: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsInputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.


        :param inputs: The inputs of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :type: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsInputs
        """

        self._inputs = inputs

    @property
    def package_options(self):
        """Gets the package_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501


        :return: The package_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :rtype: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions
        """
        return self._package_options

    @package_options.setter
    def package_options(self, package_options):
        """Sets the package_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.


        :param package_options: The package_options of this ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions.  # noqa: E501
        :type: ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptionsPackageOptions
        """
        if self.local_vars_configuration.client_side_validation and package_options is None:  # noqa: E501
            raise ValueError("Invalid value for `package_options`, must not be `None`")  # noqa: E501

        self._package_options = package_options

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
        if not isinstance(other, ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectProjKeyDataCataloguesDcKeyCollectionsCollectionNameActionsImportCcsExportPackageMongoOptions):
            return True

        return self.to_dict() != other.to_dict()
