# coding: utf-8

"""
MinihubTypeData.py

 The Clear BSD License

 Copyright (c) – 2016, NetApp, Inc. All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

 * Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pprint import pformat
from six import iteritems


class MinihubTypeData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MinihubTypeData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'minihub_type': 'str',  # (required parameter)
            'parent_controller': 'str'
        }

        self.attribute_map = {
            'minihub_type': 'minihubType',  # (required parameter)
            'parent_controller': 'parentController'
        }

        self._minihub_type = None
        self._parent_controller = None

    @property
    def minihub_type(self):
        """
        Gets the minihub_type of this MinihubTypeData.
        This enumeration is used to identify the type of a minihub.

        :return: The minihub_type of this MinihubTypeData.
        :rtype: str
        :required/optional: required
        """
        return self._minihub_type

    @minihub_type.setter
    def minihub_type(self, minihub_type):
        """
        Sets the minihub_type of this MinihubTypeData.
        This enumeration is used to identify the type of a minihub.

        :param minihub_type: The minihub_type of this MinihubTypeData.
        :type: str
        """
        allowed_values = ["hostside", "driveside", "__UNDEFINED"]
        if minihub_type not in allowed_values:
            raise ValueError(
                "Invalid value for `minihub_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._minihub_type = minihub_type

    @property
    def parent_controller(self):
        """
        Gets the parent_controller of this MinihubTypeData.
        This field is present only if the minihubType value is equal to MINIHUB_TYPE_HOSTSIDE. It contains the detailed information about the controller the minihub is associated with.

        :return: The parent_controller of this MinihubTypeData.
        :rtype: str
        :required/optional: optional
        """
        return self._parent_controller

    @parent_controller.setter
    def parent_controller(self, parent_controller):
        """
        Sets the parent_controller of this MinihubTypeData.
        This field is present only if the minihubType value is equal to MINIHUB_TYPE_HOSTSIDE. It contains the detailed information about the controller the minihub is associated with.

        :param parent_controller: The parent_controller of this MinihubTypeData.
        :type: str
        """
        self._parent_controller = parent_controller

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        if self is None:
           return None
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if self is None or other is None:
            return None
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

