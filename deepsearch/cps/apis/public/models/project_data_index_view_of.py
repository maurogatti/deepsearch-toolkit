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


class ProjectDataIndexViewOf(object):
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
        'index_key': 'str',
        'instance_id': 'str',
        'proj_key': 'str',
        'query_options': 'ElasticIndexSearchQueryOptions'
    }

    attribute_map = {
        'index_key': 'index_key',
        'instance_id': 'instance_id',
        'proj_key': 'proj_key',
        'query_options': 'query_options'
    }

    def __init__(self, index_key=None, instance_id=None, proj_key=None, query_options=None, local_vars_configuration=None):  # noqa: E501
        """ProjectDataIndexViewOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index_key = None
        self._instance_id = None
        self._proj_key = None
        self._query_options = None
        self.discriminator = None

        self.index_key = index_key
        if instance_id is not None:
            self.instance_id = instance_id
        if proj_key is not None:
            self.proj_key = proj_key
        self.query_options = query_options

    @property
    def index_key(self):
        """Gets the index_key of this ProjectDataIndexViewOf.  # noqa: E501

        Data index key  # noqa: E501

        :return: The index_key of this ProjectDataIndexViewOf.  # noqa: E501
        :rtype: str
        """
        return self._index_key

    @index_key.setter
    def index_key(self, index_key):
        """Sets the index_key of this ProjectDataIndexViewOf.

        Data index key  # noqa: E501

        :param index_key: The index_key of this ProjectDataIndexViewOf.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and index_key is None:  # noqa: E501
            raise ValueError("Invalid value for `index_key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                index_key is not None and len(index_key) > 64):
            raise ValueError("Invalid value for `index_key`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                index_key is not None and len(index_key) < 1):
            raise ValueError("Invalid value for `index_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._index_key = index_key

    @property
    def instance_id(self):
        """Gets the instance_id of this ProjectDataIndexViewOf.  # noqa: E501

        Instance id key, if the source is a data asset  # noqa: E501

        :return: The instance_id of this ProjectDataIndexViewOf.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ProjectDataIndexViewOf.

        Instance id key, if the source is a data asset  # noqa: E501

        :param instance_id: The instance_id of this ProjectDataIndexViewOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                instance_id is not None and len(instance_id) > 64):
            raise ValueError("Invalid value for `instance_id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instance_id is not None and len(instance_id) < 1):
            raise ValueError("Invalid value for `instance_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def proj_key(self):
        """Gets the proj_key of this ProjectDataIndexViewOf.  # noqa: E501

        Project id key, if the source is a project data index  # noqa: E501

        :return: The proj_key of this ProjectDataIndexViewOf.  # noqa: E501
        :rtype: str
        """
        return self._proj_key

    @proj_key.setter
    def proj_key(self, proj_key):
        """Sets the proj_key of this ProjectDataIndexViewOf.

        Project id key, if the source is a project data index  # noqa: E501

        :param proj_key: The proj_key of this ProjectDataIndexViewOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                proj_key is not None and len(proj_key) > 64):
            raise ValueError("Invalid value for `proj_key`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                proj_key is not None and len(proj_key) < 1):
            raise ValueError("Invalid value for `proj_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._proj_key = proj_key

    @property
    def query_options(self):
        """Gets the query_options of this ProjectDataIndexViewOf.  # noqa: E501


        :return: The query_options of this ProjectDataIndexViewOf.  # noqa: E501
        :rtype: ElasticIndexSearchQueryOptions
        """
        return self._query_options

    @query_options.setter
    def query_options(self, query_options):
        """Sets the query_options of this ProjectDataIndexViewOf.


        :param query_options: The query_options of this ProjectDataIndexViewOf.  # noqa: E501
        :type: ElasticIndexSearchQueryOptions
        """
        if self.local_vars_configuration.client_side_validation and query_options is None:  # noqa: E501
            raise ValueError("Invalid value for `query_options`, must not be `None`")  # noqa: E501

        self._query_options = query_options

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
        if not isinstance(other, ProjectDataIndexViewOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDataIndexViewOf):
            return True

        return self.to_dict() != other.to_dict()
