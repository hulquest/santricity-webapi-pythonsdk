# coding: utf-8

"""
StorageSystemCreateRequest.py

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


class StorageSystemCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StorageSystemCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',  
            'controller_addresses': 'list[str]',  # (required parameter)
            'password': 'str',  
            'wwn': 'str',  
            'enable_trace': 'bool',  
            'meta_tags': 'list[KeyValue]'
        }

        self.attribute_map = {
            'id': 'id',  
            'controller_addresses': 'controllerAddresses',  # (required parameter)
            'password': 'password',  
            'wwn': 'wwn',  
            'enable_trace': 'enableTrace',  
            'meta_tags': 'metaTags'
        }

        self._id = None
        self._controller_addresses = None
        self._password = None
        self._wwn = None
        self._enable_trace = None
        self._meta_tags = None

    @property
    def id(self):
        """
        Gets the id of this StorageSystemCreateRequest.
        ID to assign to the storage system.  This must be left null or be unique.  If null, a unique ID will be assigned

        :return: The id of this StorageSystemCreateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StorageSystemCreateRequest.
        ID to assign to the storage system.  This must be left null or be unique.  If null, a unique ID will be assigned

        :param id: The id of this StorageSystemCreateRequest.
        :type: str
        """
        self._id = id

    @property
    def controller_addresses(self):
        """
        Gets the controller_addresses of this StorageSystemCreateRequest.
        A list of controller IP addresses or host names.

        :return: The controller_addresses of this StorageSystemCreateRequest.
        :rtype: list[str]
        :required/optional: required
        """
        return self._controller_addresses

    @controller_addresses.setter
    def controller_addresses(self, controller_addresses):
        """
        Sets the controller_addresses of this StorageSystemCreateRequest.
        A list of controller IP addresses or host names.

        :param controller_addresses: The controller_addresses of this StorageSystemCreateRequest.
        :type: list[str]
        """
        self._controller_addresses = controller_addresses

    @property
    def password(self):
        """
        Gets the password of this StorageSystemCreateRequest.
        The SYMbol password for the storage system.

        :return: The password of this StorageSystemCreateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this StorageSystemCreateRequest.
        The SYMbol password for the storage system.

        :param password: The password of this StorageSystemCreateRequest.
        :type: str
        """
        self._password = password

    @property
    def wwn(self):
        """
        Gets the wwn of this StorageSystemCreateRequest.
        The world wide name for the storage system.  This is only needed for   in-band management with an in-band agent that is managing more than a single storage system.

        :return: The wwn of this StorageSystemCreateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """
        Sets the wwn of this StorageSystemCreateRequest.
        The world wide name for the storage system.  This is only needed for   in-band management with an in-band agent that is managing more than a single storage system.

        :param wwn: The wwn of this StorageSystemCreateRequest.
        :type: str
        """
        self._wwn = wwn

    @property
    def enable_trace(self):
        """
        Gets the enable_trace of this StorageSystemCreateRequest.
        Enable trace logging for SYMbol calls to the storage system.

        :return: The enable_trace of this StorageSystemCreateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._enable_trace

    @enable_trace.setter
    def enable_trace(self, enable_trace):
        """
        Sets the enable_trace of this StorageSystemCreateRequest.
        Enable trace logging for SYMbol calls to the storage system.

        :param enable_trace: The enable_trace of this StorageSystemCreateRequest.
        :type: bool
        """
        self._enable_trace = enable_trace

    @property
    def meta_tags(self):
        """
        Gets the meta_tags of this StorageSystemCreateRequest.
        Optional meta tags to associate to this storage system

        :return: The meta_tags of this StorageSystemCreateRequest.
        :rtype: list[KeyValue]
        :required/optional: optional
        """
        return self._meta_tags

    @meta_tags.setter
    def meta_tags(self, meta_tags):
        """
        Sets the meta_tags of this StorageSystemCreateRequest.
        Optional meta tags to associate to this storage system

        :param meta_tags: The meta_tags of this StorageSystemCreateRequest.
        :type: list[KeyValue]
        """
        self._meta_tags = meta_tags

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

