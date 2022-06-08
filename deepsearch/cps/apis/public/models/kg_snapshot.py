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


class KgSnapshot(object):
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
        'data_flow': 'object',
        'is_current': 'bool',
        'name': 'str',
        'project_task_id': 'str',
        'task_type': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'data_flow': 'data_flow',
        'is_current': 'is_current',
        'name': 'name',
        'project_task_id': 'project_task_id',
        'task_type': 'task_type',
        'timestamp': 'timestamp'
    }

    def __init__(self, data_flow=None, is_current=None, name=None, project_task_id=None, task_type=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """KgSnapshot - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data_flow = None
        self._is_current = None
        self._name = None
        self._project_task_id = None
        self._task_type = None
        self._timestamp = None
        self.discriminator = None

        self.data_flow = data_flow
        if is_current is not None:
            self.is_current = is_current
        if name is not None:
            self.name = name
        if project_task_id is not None:
            self.project_task_id = project_task_id
        if task_type is not None:
            self.task_type = task_type
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def data_flow(self):
        """Gets the data_flow of this KgSnapshot.  # noqa: E501


        :return: The data_flow of this KgSnapshot.  # noqa: E501
        :rtype: object
        """
        return self._data_flow

    @data_flow.setter
    def data_flow(self, data_flow):
        """Sets the data_flow of this KgSnapshot.


        :param data_flow: The data_flow of this KgSnapshot.  # noqa: E501
        :type: object
        """

        self._data_flow = data_flow

    @property
    def is_current(self):
        """Gets the is_current of this KgSnapshot.  # noqa: E501


        :return: The is_current of this KgSnapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_current

    @is_current.setter
    def is_current(self, is_current):
        """Sets the is_current of this KgSnapshot.


        :param is_current: The is_current of this KgSnapshot.  # noqa: E501
        :type: bool
        """

        self._is_current = is_current

    @property
    def name(self):
        """Gets the name of this KgSnapshot.  # noqa: E501


        :return: The name of this KgSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KgSnapshot.


        :param name: The name of this KgSnapshot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_task_id(self):
        """Gets the project_task_id of this KgSnapshot.  # noqa: E501


        :return: The project_task_id of this KgSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._project_task_id

    @project_task_id.setter
    def project_task_id(self, project_task_id):
        """Sets the project_task_id of this KgSnapshot.


        :param project_task_id: The project_task_id of this KgSnapshot.  # noqa: E501
        :type: str
        """

        self._project_task_id = project_task_id

    @property
    def task_type(self):
        """Gets the task_type of this KgSnapshot.  # noqa: E501


        :return: The task_type of this KgSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this KgSnapshot.


        :param task_type: The task_type of this KgSnapshot.  # noqa: E501
        :type: str
        """

        self._task_type = task_type

    @property
    def timestamp(self):
        """Gets the timestamp of this KgSnapshot.  # noqa: E501


        :return: The timestamp of this KgSnapshot.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this KgSnapshot.


        :param timestamp: The timestamp of this KgSnapshot.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

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
        if not isinstance(other, KgSnapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KgSnapshot):
            return True

        return self.to_dict() != other.to_dict()
