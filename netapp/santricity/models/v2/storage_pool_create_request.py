# coding: utf-8

"""
StoragePoolCreateRequest.py

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


class StoragePoolCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoragePoolCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'raid_level': 'str',  # (required parameter)
            'disk_drive_ids': 'list[str]',  # (required parameter)
            'erase_secured_drives': 'bool',  
            'name': 'str'
        }

        self.attribute_map = {
            'raid_level': 'raidLevel',  # (required parameter)
            'disk_drive_ids': 'diskDriveIds',  # (required parameter)
            'erase_secured_drives': 'eraseSecuredDrives',  
            'name': 'name'
        }

        self._raid_level = None
        self._disk_drive_ids = None
        self._erase_secured_drives = None
        self._name = None

    @property
    def raid_level(self):
        """
        Gets the raid_level of this StoragePoolCreateRequest.
        The RAID configuration for the new storage pool.

        :return: The raid_level of this StoragePoolCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._raid_level

    @raid_level.setter
    def raid_level(self, raid_level):
        """
        Sets the raid_level of this StoragePoolCreateRequest.
        The RAID configuration for the new storage pool.

        :param raid_level: The raid_level of this StoragePoolCreateRequest.
        :type: str
        """
        allowed_values = ["raidUnsupported", "raidAll", "raid0", "raid1", "raid3", "raid5", "raid6", "raidDiskPool", "__UNDEFINED"]
        if raid_level not in allowed_values:
            raise ValueError(
                "Invalid value for `raid_level`, must be one of {0}"
                .format(allowed_values)
            )
        self._raid_level = raid_level

    @property
    def disk_drive_ids(self):
        """
        Gets the disk_drive_ids of this StoragePoolCreateRequest.
        The identifiers of the disk drives to use for creating the storage pool.

        :return: The disk_drive_ids of this StoragePoolCreateRequest.
        :rtype: list[str]
        :required/optional: required
        """
        return self._disk_drive_ids

    @disk_drive_ids.setter
    def disk_drive_ids(self, disk_drive_ids):
        """
        Sets the disk_drive_ids of this StoragePoolCreateRequest.
        The identifiers of the disk drives to use for creating the storage pool.

        :param disk_drive_ids: The disk_drive_ids of this StoragePoolCreateRequest.
        :type: list[str]
        """
        self._disk_drive_ids = disk_drive_ids

    @property
    def erase_secured_drives(self):
        """
        Gets the erase_secured_drives of this StoragePoolCreateRequest.
        Security-enabled drives that were previously part of a secured storage pool must be erased before they can be re-used. Enable to automatically erase such drives.

        :return: The erase_secured_drives of this StoragePoolCreateRequest.
        :rtype: bool
        :required/optional: optional
        """
        return self._erase_secured_drives

    @erase_secured_drives.setter
    def erase_secured_drives(self, erase_secured_drives):
        """
        Sets the erase_secured_drives of this StoragePoolCreateRequest.
        Security-enabled drives that were previously part of a secured storage pool must be erased before they can be re-used. Enable to automatically erase such drives.

        :param erase_secured_drives: The erase_secured_drives of this StoragePoolCreateRequest.
        :type: bool
        """
        self._erase_secured_drives = erase_secured_drives

    @property
    def name(self):
        """
        Gets the name of this StoragePoolCreateRequest.
        The user-label to assign to the new storage pool.

        :return: The name of this StoragePoolCreateRequest.
        :rtype: str
        :required/optional: required
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragePoolCreateRequest.
        The user-label to assign to the new storage pool.

        :param name: The name of this StoragePoolCreateRequest.
        :type: str
        """
        self._name = name

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
