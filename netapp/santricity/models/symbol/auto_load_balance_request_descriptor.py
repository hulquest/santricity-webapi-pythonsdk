# coding: utf-8

"""
AutoLoadBalanceRequestDescriptor.py

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


class AutoLoadBalanceRequestDescriptor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AutoLoadBalanceRequestDescriptor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',  # (required parameter)
            'delay_seconds': 'int'
        }

        self.attribute_map = {
            'action': 'action',  # (required parameter)
            'delay_seconds': 'delaySeconds'
        }

        self._action = None
        self._delay_seconds = None

    @property
    def action(self):
        """
        Gets the action of this AutoLoadBalanceRequestDescriptor.
        This enumeration identifies an auto load balance action being requested by the client.

        :return: The action of this AutoLoadBalanceRequestDescriptor.
        :rtype: str
        :required/optional: required
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AutoLoadBalanceRequestDescriptor.
        This enumeration identifies an auto load balance action being requested by the client.

        :param action: The action of this AutoLoadBalanceRequestDescriptor.
        :type: str
        """
        allowed_values = ["unknown", "resetStatisticsBaseline", "rebalanceLoad", "__UNDEFINED"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action`, must be one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def delay_seconds(self):
        """
        Gets the delay_seconds of this AutoLoadBalanceRequestDescriptor.
        Amount of time to delay before performing load balance operation.

        :return: The delay_seconds of this AutoLoadBalanceRequestDescriptor.
        :rtype: int
        :required/optional: optional
        """
        return self._delay_seconds

    @delay_seconds.setter
    def delay_seconds(self, delay_seconds):
        """
        Sets the delay_seconds of this AutoLoadBalanceRequestDescriptor.
        Amount of time to delay before performing load balance operation.

        :param delay_seconds: The delay_seconds of this AutoLoadBalanceRequestDescriptor.
        :type: int
        """
        self._delay_seconds = delay_seconds

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
