# coding: utf-8

"""
PITGroupRollbackUtilizationEstimate.py

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


class PITGroupRollbackUtilizationEstimate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PITGroupRollbackUtilizationEstimate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metadata_bytes_required': 'int',  # (required parameter)
            'cow_data_bytes_required': 'int',  # (required parameter)
            'current_bytes_available': 'int'
        }

        self.attribute_map = {
            'metadata_bytes_required': 'metadataBytesRequired',  # (required parameter)
            'cow_data_bytes_required': 'cowDataBytesRequired',  # (required parameter)
            'current_bytes_available': 'currentBytesAvailable'
        }

        self._metadata_bytes_required = None
        self._cow_data_bytes_required = None
        self._current_bytes_available = None

    @property
    def metadata_bytes_required(self):
        """
        Gets the metadata_bytes_required of this PITGroupRollbackUtilizationEstimate.
        The amount of repository capacity in bytes necessary for PiT metadata during rollback.

        :return: The metadata_bytes_required of this PITGroupRollbackUtilizationEstimate.
        :rtype: int
        :required/optional: required
        """
        return self._metadata_bytes_required

    @metadata_bytes_required.setter
    def metadata_bytes_required(self, metadata_bytes_required):
        """
        Sets the metadata_bytes_required of this PITGroupRollbackUtilizationEstimate.
        The amount of repository capacity in bytes necessary for PiT metadata during rollback.

        :param metadata_bytes_required: The metadata_bytes_required of this PITGroupRollbackUtilizationEstimate.
        :type: int
        """
        self._metadata_bytes_required = metadata_bytes_required

    @property
    def cow_data_bytes_required(self):
        """
        Gets the cow_data_bytes_required of this PITGroupRollbackUtilizationEstimate.
        The amount of repository capacity in bytes necessary for copy-on-write operations required by the rollback process to preserve all PiTs.

        :return: The cow_data_bytes_required of this PITGroupRollbackUtilizationEstimate.
        :rtype: int
        :required/optional: required
        """
        return self._cow_data_bytes_required

    @cow_data_bytes_required.setter
    def cow_data_bytes_required(self, cow_data_bytes_required):
        """
        Sets the cow_data_bytes_required of this PITGroupRollbackUtilizationEstimate.
        The amount of repository capacity in bytes necessary for copy-on-write operations required by the rollback process to preserve all PiTs.

        :param cow_data_bytes_required: The cow_data_bytes_required of this PITGroupRollbackUtilizationEstimate.
        :type: int
        """
        self._cow_data_bytes_required = cow_data_bytes_required

    @property
    def current_bytes_available(self):
        """
        Gets the current_bytes_available of this PITGroupRollbackUtilizationEstimate.
        The current remaining available capacity (in bytes) of the associated repository.

        :return: The current_bytes_available of this PITGroupRollbackUtilizationEstimate.
        :rtype: int
        :required/optional: required
        """
        return self._current_bytes_available

    @current_bytes_available.setter
    def current_bytes_available(self, current_bytes_available):
        """
        Sets the current_bytes_available of this PITGroupRollbackUtilizationEstimate.
        The current remaining available capacity (in bytes) of the associated repository.

        :param current_bytes_available: The current_bytes_available of this PITGroupRollbackUtilizationEstimate.
        :type: int
        """
        self._current_bytes_available = current_bytes_available

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

