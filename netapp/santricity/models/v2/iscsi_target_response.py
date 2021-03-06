# coding: utf-8

"""
IscsiTargetResponse.py

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


class IscsiTargetResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        IscsiTargetResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'auth_method': 'str',  # (required parameter)
            'chap_secret': 'str',  # (required parameter)
            'iqn': 'str',  # (required parameter)
            'alias': 'str'
        }

        self.attribute_map = {
            'auth_method': 'authMethod',  # (required parameter)
            'chap_secret': 'chapSecret',  # (required parameter)
            'iqn': 'iqn',  # (required parameter)
            'alias': 'alias'
        }

        self._auth_method = None
        self._chap_secret = None
        self._iqn = None
        self._alias = None

    @property
    def auth_method(self):
        """
        Gets the auth_method of this IscsiTargetResponse.
        Authentication type (None or CHAP)

        :return: The auth_method of this IscsiTargetResponse.
        :rtype: str
        :required/optional: required
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """
        Sets the auth_method of this IscsiTargetResponse.
        Authentication type (None or CHAP)

        :param auth_method: The auth_method of this IscsiTargetResponse.
        :type: str
        """
        allowed_values = ["none", "chap", "__UNDEFINED"]
        if auth_method not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._auth_method = auth_method

    @property
    def chap_secret(self):
        """
        Gets the chap_secret of this IscsiTargetResponse.
        CHAP secret/password.

        :return: The chap_secret of this IscsiTargetResponse.
        :rtype: str
        :required/optional: required
        """
        return self._chap_secret

    @chap_secret.setter
    def chap_secret(self, chap_secret):
        """
        Sets the chap_secret of this IscsiTargetResponse.
        CHAP secret/password.

        :param chap_secret: The chap_secret of this IscsiTargetResponse.
        :type: str
        """
        self._chap_secret = chap_secret

    @property
    def iqn(self):
        """
        Gets the iqn of this IscsiTargetResponse.
        iSCSI Qualified Name (iqn)

        :return: The iqn of this IscsiTargetResponse.
        :rtype: str
        :required/optional: required
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """
        Sets the iqn of this IscsiTargetResponse.
        iSCSI Qualified Name (iqn)

        :param iqn: The iqn of this IscsiTargetResponse.
        :type: str
        """
        self._iqn = iqn

    @property
    def alias(self):
        """
        Gets the alias of this IscsiTargetResponse.
        The iSCSI target alias.

        :return: The alias of this IscsiTargetResponse.
        :rtype: str
        :required/optional: required
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this IscsiTargetResponse.
        The iSCSI target alias.

        :param alias: The alias of this IscsiTargetResponse.
        :type: str
        """
        self._alias = alias

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

