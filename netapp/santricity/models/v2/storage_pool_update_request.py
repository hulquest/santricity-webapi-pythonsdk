# coding: utf-8

"""
StoragePoolUpdateRequest.py

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


class StoragePoolUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoragePoolUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',  
            'secure_pool': 'bool',  
            'reserved_drive_count': 'int',  
            'pool_priority': 'DiskPoolPriorityUpdateRequest',  
            'pool_threshold': 'DiskPoolThresholdUpdateRequest'
        }

        self.attribute_map = {
            'name': 'name',  
            'secure_pool': 'securePool',  
            'reserved_drive_count': 'reservedDriveCount',  
            'pool_priority': 'poolPriority',  
            'pool_threshold': 'poolThreshold'
        }

        self._name = None
        self._secure_pool = None
        self._reserved_drive_count = None
        self._pool_priority = None
        self._pool_threshold = None

    @property
    def name(self):
        """
        Gets the name of this StoragePoolUpdateRequest.
        The new user-label to assign to the storage pool.

        :return: The name of this StoragePoolUpdateRequest.
        :rtype: str
        :required/optional: optional
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragePoolUpdateRequest.
        The new user-label to assign to the storage pool.

        :param name: The name of this StoragePoolUpdateRequest.
        :type: str
        """
        self._name = name

    @property
    def secure_pool(self):
        """
        Gets the secure_pool of this StoragePoolUpdateRequest.
        Convert to a secure Storage Pool if all of the drives that constitute      the Pool are security capable

        :return: The secure_pool of this StoragePoolUpdateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._secure_pool

    @secure_pool.setter
    def secure_pool(self, secure_pool):
        """
        Sets the secure_pool of this StoragePoolUpdateRequest.
        Convert to a secure Storage Pool if all of the drives that constitute      the Pool are security capable

        :param secure_pool: The secure_pool of this StoragePoolUpdateRequest.
        :type: bool
        """
        self._secure_pool = secure_pool

    @property
    def reserved_drive_count(self):
        """
        Gets the reserved_drive_count of this StoragePoolUpdateRequest.
        Set the number of drives reserved by the storage pool for reconstruction operations      (only for RAID Type: raidDiskPool)

        :return: The reserved_drive_count of this StoragePoolUpdateRequest.
        :rtype: int
        :required/optional: optional
        """
        return self._reserved_drive_count

    @reserved_drive_count.setter
    def reserved_drive_count(self, reserved_drive_count):
        """
        Sets the reserved_drive_count of this StoragePoolUpdateRequest.
        Set the number of drives reserved by the storage pool for reconstruction operations      (only for RAID Type: raidDiskPool)

        :param reserved_drive_count: The reserved_drive_count of this StoragePoolUpdateRequest.
        :type: int
        """
        self._reserved_drive_count = reserved_drive_count

    @property
    def pool_priority(self):
        """
        Gets the pool_priority of this StoragePoolUpdateRequest.
        Set the reconstruction and background operation priorities (only for RAID Type: raidDiskPool)

        :return: The pool_priority of this StoragePoolUpdateRequest.
        :rtype: DiskPoolPriorityUpdateRequest
        :required/optional: optional
        """
        return self._pool_priority

    @pool_priority.setter
    def pool_priority(self, pool_priority):
        """
        Sets the pool_priority of this StoragePoolUpdateRequest.
        Set the reconstruction and background operation priorities (only for RAID Type: raidDiskPool)

        :param pool_priority: The pool_priority of this StoragePoolUpdateRequest.
        :type: DiskPoolPriorityUpdateRequest
        """
        self._pool_priority = pool_priority

    @property
    def pool_threshold(self):
        """
        Gets the pool_threshold of this StoragePoolUpdateRequest.
        Set the reconstruction and background operation priorities (only for RAID Type: raidDiskPool)

        :return: The pool_threshold of this StoragePoolUpdateRequest.
        :rtype: DiskPoolThresholdUpdateRequest
        :required/optional: optional
        """
        return self._pool_threshold

    @pool_threshold.setter
    def pool_threshold(self, pool_threshold):
        """
        Sets the pool_threshold of this StoragePoolUpdateRequest.
        Set the reconstruction and background operation priorities (only for RAID Type: raidDiskPool)

        :param pool_threshold: The pool_threshold of this StoragePoolUpdateRequest.
        :type: DiskPoolThresholdUpdateRequest
        """
        self._pool_threshold = pool_threshold

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

