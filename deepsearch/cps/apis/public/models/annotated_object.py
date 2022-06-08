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


class AnnotatedObject(object):
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
        'image': 'AnnotatedImage',
        'table': 'AnnotatedTable',
        'text': 'AnnotatedTextLines'
    }

    attribute_map = {
        'image': 'image',
        'table': 'table',
        'text': 'text'
    }

    def __init__(self, image=None, table=None, text=None, local_vars_configuration=None):  # noqa: E501
        """AnnotatedObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._image = None
        self._table = None
        self._text = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if table is not None:
            self.table = table
        if text is not None:
            self.text = text

    @property
    def image(self):
        """Gets the image of this AnnotatedObject.  # noqa: E501


        :return: The image of this AnnotatedObject.  # noqa: E501
        :rtype: AnnotatedImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this AnnotatedObject.


        :param image: The image of this AnnotatedObject.  # noqa: E501
        :type: AnnotatedImage
        """

        self._image = image

    @property
    def table(self):
        """Gets the table of this AnnotatedObject.  # noqa: E501


        :return: The table of this AnnotatedObject.  # noqa: E501
        :rtype: AnnotatedTable
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this AnnotatedObject.


        :param table: The table of this AnnotatedObject.  # noqa: E501
        :type: AnnotatedTable
        """

        self._table = table

    @property
    def text(self):
        """Gets the text of this AnnotatedObject.  # noqa: E501


        :return: The text of this AnnotatedObject.  # noqa: E501
        :rtype: AnnotatedTextLines
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AnnotatedObject.


        :param text: The text of this AnnotatedObject.  # noqa: E501
        :type: AnnotatedTextLines
        """

        self._text = text

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
        if not isinstance(other, AnnotatedObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnnotatedObject):
            return True

        return self.to_dict() != other.to_dict()
