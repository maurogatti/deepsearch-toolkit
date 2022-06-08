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


class ModelConfiguration(object):
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
        'configurations': 'dict(str, object)',
        'created_at': 'float',
        'created_by': 'str',
        'description': 'str',
        'model_config_key': 'str',
        'name': 'str',
        'proj_key': 'str',
        'public': 'bool',
        'supported_annotations': 'object'
    }

    attribute_map = {
        'configurations': 'configurations',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'description': 'description',
        'model_config_key': 'model_config_key',
        'name': 'name',
        'proj_key': 'proj_key',
        'public': 'public',
        'supported_annotations': 'supported_annotations'
    }

    def __init__(self, configurations=None, created_at=None, created_by=None, description=None, model_config_key=None, name=None, proj_key=None, public=None, supported_annotations=None, local_vars_configuration=None):  # noqa: E501
        """ModelConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._configurations = None
        self._created_at = None
        self._created_by = None
        self._description = None
        self._model_config_key = None
        self._name = None
        self._proj_key = None
        self._public = None
        self._supported_annotations = None
        self.discriminator = None

        if configurations is not None:
            self.configurations = configurations
        self.created_at = created_at
        self.created_by = created_by
        self.description = description
        self.model_config_key = model_config_key
        self.name = name
        self.proj_key = proj_key
        self.public = public
        if supported_annotations is not None:
            self.supported_annotations = supported_annotations

    @property
    def configurations(self):
        """Gets the configurations of this ModelConfiguration.  # noqa: E501


        :return: The configurations of this ModelConfiguration.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this ModelConfiguration.


        :param configurations: The configurations of this ModelConfiguration.  # noqa: E501
        :type: dict(str, object)
        """

        self._configurations = configurations

    @property
    def created_at(self):
        """Gets the created_at of this ModelConfiguration.  # noqa: E501


        :return: The created_at of this ModelConfiguration.  # noqa: E501
        :rtype: float
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelConfiguration.


        :param created_at: The created_at of this ModelConfiguration.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this ModelConfiguration.  # noqa: E501


        :return: The created_by of this ModelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ModelConfiguration.


        :param created_by: The created_by of this ModelConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this ModelConfiguration.  # noqa: E501


        :return: The description of this ModelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelConfiguration.


        :param description: The description of this ModelConfiguration.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def model_config_key(self):
        """Gets the model_config_key of this ModelConfiguration.  # noqa: E501


        :return: The model_config_key of this ModelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._model_config_key

    @model_config_key.setter
    def model_config_key(self, model_config_key):
        """Sets the model_config_key of this ModelConfiguration.


        :param model_config_key: The model_config_key of this ModelConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model_config_key is None:  # noqa: E501
            raise ValueError("Invalid value for `model_config_key`, must not be `None`")  # noqa: E501

        self._model_config_key = model_config_key

    @property
    def name(self):
        """Gets the name of this ModelConfiguration.  # noqa: E501


        :return: The name of this ModelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelConfiguration.


        :param name: The name of this ModelConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def proj_key(self):
        """Gets the proj_key of this ModelConfiguration.  # noqa: E501


        :return: The proj_key of this ModelConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this ModelConfiguration.


        :param proj_key: The proj_key of this ModelConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and proj_key is None:  # noqa: E501
            raise ValueError("Invalid value for `proj_key`, must not be `None`")  # noqa: E501

        self._proj_key = proj_key

    @property
    def public(self):
        """Gets the public of this ModelConfiguration.  # noqa: E501


        :return: The public of this ModelConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ModelConfiguration.


        :param public: The public of this ModelConfiguration.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and public is None:  # noqa: E501
            raise ValueError("Invalid value for `public`, must not be `None`")  # noqa: E501

        self._public = public

    @property
    def supported_annotations(self):
        """Gets the supported_annotations of this ModelConfiguration.  # noqa: E501


        :return: The supported_annotations of this ModelConfiguration.  # noqa: E501
        :rtype: object
        """
        return self._supported_annotations

    @supported_annotations.setter
    def supported_annotations(self, supported_annotations):
        """Sets the supported_annotations of this ModelConfiguration.


        :param supported_annotations: The supported_annotations of this ModelConfiguration.  # noqa: E501
        :type: object
        """

        self._supported_annotations = supported_annotations

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
        if not isinstance(other, ModelConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelConfiguration):
            return True

        return self.to_dict() != other.to_dict()
