# coding: utf-8

"""
InterfaceStats.py

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


class InterfaceStats(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InterfaceStats - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observed_time': 'datetime',  # (required parameter)
            'observed_time_in_ms': 'int',  # (required parameter)
            'last_reset_time': 'datetime',  # (required parameter)
            'last_reset_time_in_ms': 'int',  # (required parameter)
            'interface_id': 'str',  # (required parameter)
            'array_id': 'str',  # (required parameter)
            'array_wwn': 'str',  # (required parameter)
            'channel_type': 'str',  # (required parameter)
            'channel_number': 'int',  # (required parameter)
            'read_ops': 'float',  # (required parameter)
            'read_bytes': 'float',  # (required parameter)
            'read_time_total': 'float',  # (required parameter)
            'read_time_max': 'float',  # (required parameter)
            'write_ops': 'float',  # (required parameter)
            'write_bytes': 'float',  # (required parameter)
            'write_time_total': 'float',  # (required parameter)
            'write_time_max': 'float',  # (required parameter)
            'other_ops': 'float',  # (required parameter)
            'other_time_total': 'float',  # (required parameter)
            'other_time_max': 'float',  # (required parameter)
            'read_time_total_sq': 'float',  # (required parameter)
            'write_time_total_sq': 'float',  # (required parameter)
            'other_time_total_sq': 'float',  # (required parameter)
            'queue_depth_total': 'float',  # (required parameter)
            'queue_depth_max': 'float',  # (required parameter)
            'channel_error_counts': 'float'
        }

        self.attribute_map = {
            'observed_time': 'observedTime',  # (required parameter)
            'observed_time_in_ms': 'observedTimeInMS',  # (required parameter)
            'last_reset_time': 'lastResetTime',  # (required parameter)
            'last_reset_time_in_ms': 'lastResetTimeInMS',  # (required parameter)
            'interface_id': 'interfaceId',  # (required parameter)
            'array_id': 'arrayId',  # (required parameter)
            'array_wwn': 'arrayWwn',  # (required parameter)
            'channel_type': 'channelType',  # (required parameter)
            'channel_number': 'channelNumber',  # (required parameter)
            'read_ops': 'readOps',  # (required parameter)
            'read_bytes': 'readBytes',  # (required parameter)
            'read_time_total': 'readTimeTotal',  # (required parameter)
            'read_time_max': 'readTimeMax',  # (required parameter)
            'write_ops': 'writeOps',  # (required parameter)
            'write_bytes': 'writeBytes',  # (required parameter)
            'write_time_total': 'writeTimeTotal',  # (required parameter)
            'write_time_max': 'writeTimeMax',  # (required parameter)
            'other_ops': 'otherOps',  # (required parameter)
            'other_time_total': 'otherTimeTotal',  # (required parameter)
            'other_time_max': 'otherTimeMax',  # (required parameter)
            'read_time_total_sq': 'readTimeTotalSq',  # (required parameter)
            'write_time_total_sq': 'writeTimeTotalSq',  # (required parameter)
            'other_time_total_sq': 'otherTimeTotalSq',  # (required parameter)
            'queue_depth_total': 'queueDepthTotal',  # (required parameter)
            'queue_depth_max': 'queueDepthMax',  # (required parameter)
            'channel_error_counts': 'channelErrorCounts'
        }

        self._observed_time = None
        self._observed_time_in_ms = None
        self._last_reset_time = None
        self._last_reset_time_in_ms = None
        self._interface_id = None
        self._array_id = None
        self._array_wwn = None
        self._channel_type = None
        self._channel_number = None
        self._read_ops = None
        self._read_bytes = None
        self._read_time_total = None
        self._read_time_max = None
        self._write_ops = None
        self._write_bytes = None
        self._write_time_total = None
        self._write_time_max = None
        self._other_ops = None
        self._other_time_total = None
        self._other_time_max = None
        self._read_time_total_sq = None
        self._write_time_total_sq = None
        self._other_time_total_sq = None
        self._queue_depth_total = None
        self._queue_depth_max = None
        self._channel_error_counts = None

    @property
    def observed_time(self):
        """
        Gets the observed_time of this InterfaceStats.
        End time for this collection as measured by the number of seconds since baseTime.

        :return: The observed_time of this InterfaceStats.
        :rtype: datetime
        :required/optional: required
        """
        return self._observed_time

    @observed_time.setter
    def observed_time(self, observed_time):
        """
        Sets the observed_time of this InterfaceStats.
        End time for this collection as measured by the number of seconds since baseTime.

        :param observed_time: The observed_time of this InterfaceStats.
        :type: datetime
        """
        self._observed_time = observed_time

    @property
    def observed_time_in_ms(self):
        """
        Gets the observed_time_in_ms of this InterfaceStats.


        :return: The observed_time_in_ms of this InterfaceStats.
        :rtype: int
        :required/optional: required
        """
        return self._observed_time_in_ms

    @observed_time_in_ms.setter
    def observed_time_in_ms(self, observed_time_in_ms):
        """
        Sets the observed_time_in_ms of this InterfaceStats.


        :param observed_time_in_ms: The observed_time_in_ms of this InterfaceStats.
        :type: int
        """
        self._observed_time_in_ms = observed_time_in_ms

    @property
    def last_reset_time(self):
        """
        Gets the last_reset_time of this InterfaceStats.


        :return: The last_reset_time of this InterfaceStats.
        :rtype: datetime
        :required/optional: required
        """
        return self._last_reset_time

    @last_reset_time.setter
    def last_reset_time(self, last_reset_time):
        """
        Sets the last_reset_time of this InterfaceStats.


        :param last_reset_time: The last_reset_time of this InterfaceStats.
        :type: datetime
        """
        self._last_reset_time = last_reset_time

    @property
    def last_reset_time_in_ms(self):
        """
        Gets the last_reset_time_in_ms of this InterfaceStats.


        :return: The last_reset_time_in_ms of this InterfaceStats.
        :rtype: int
        :required/optional: required
        """
        return self._last_reset_time_in_ms

    @last_reset_time_in_ms.setter
    def last_reset_time_in_ms(self, last_reset_time_in_ms):
        """
        Sets the last_reset_time_in_ms of this InterfaceStats.


        :param last_reset_time_in_ms: The last_reset_time_in_ms of this InterfaceStats.
        :type: int
        """
        self._last_reset_time_in_ms = last_reset_time_in_ms

    @property
    def interface_id(self):
        """
        Gets the interface_id of this InterfaceStats.
        Interface that generated this group.

        :return: The interface_id of this InterfaceStats.
        :rtype: str
        :required/optional: required
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """
        Sets the interface_id of this InterfaceStats.
        Interface that generated this group.

        :param interface_id: The interface_id of this InterfaceStats.
        :type: str
        """
        self._interface_id = interface_id

    @property
    def array_id(self):
        """
        Gets the array_id of this InterfaceStats.


        :return: The array_id of this InterfaceStats.
        :rtype: str
        :required/optional: required
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """
        Sets the array_id of this InterfaceStats.


        :param array_id: The array_id of this InterfaceStats.
        :type: str
        """
        self._array_id = array_id

    @property
    def array_wwn(self):
        """
        Gets the array_wwn of this InterfaceStats.


        :return: The array_wwn of this InterfaceStats.
        :rtype: str
        :required/optional: required
        """
        return self._array_wwn

    @array_wwn.setter
    def array_wwn(self, array_wwn):
        """
        Sets the array_wwn of this InterfaceStats.


        :param array_wwn: The array_wwn of this InterfaceStats.
        :type: str
        """
        self._array_wwn = array_wwn

    @property
    def channel_type(self):
        """
        Gets the channel_type of this InterfaceStats.
        Channel Type enumeration Drive side, host side, or management.

        :return: The channel_type of this InterfaceStats.
        :rtype: str
        :required/optional: required
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """
        Sets the channel_type of this InterfaceStats.
        Channel Type enumeration Drive side, host side, or management.

        :param channel_type: The channel_type of this InterfaceStats.
        :type: str
        """
        allowed_values = ["hostside", "driveside", "management", "__UNDEFINED"]
        if channel_type not in allowed_values:
            raise ValueError(
                "Invalid value for `channel_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._channel_type = channel_type

    @property
    def channel_number(self):
        """
        Gets the channel_number of this InterfaceStats.
        Channel numerical ID.

        :return: The channel_number of this InterfaceStats.
        :rtype: int
        :required/optional: required
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """
        Sets the channel_number of this InterfaceStats.
        Channel numerical ID.

        :param channel_number: The channel_number of this InterfaceStats.
        :type: int
        """
        self._channel_number = channel_number

    @property
    def read_ops(self):
        """
        Gets the read_ops of this InterfaceStats.
        Number of read operations.

        :return: The read_ops of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._read_ops

    @read_ops.setter
    def read_ops(self, read_ops):
        """
        Sets the read_ops of this InterfaceStats.
        Number of read operations.

        :param read_ops: The read_ops of this InterfaceStats.
        :type: float
        """
        self._read_ops = read_ops

    @property
    def read_bytes(self):
        """
        Gets the read_bytes of this InterfaceStats.
        Number of bytes read.

        :return: The read_bytes of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._read_bytes

    @read_bytes.setter
    def read_bytes(self, read_bytes):
        """
        Sets the read_bytes of this InterfaceStats.
        Number of bytes read.

        :param read_bytes: The read_bytes of this InterfaceStats.
        :type: float
        """
        self._read_bytes = read_bytes

    @property
    def read_time_total(self):
        """
        Gets the read_time_total of this InterfaceStats.
        Total time in microseconds spent in read operations.

        :return: The read_time_total of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._read_time_total

    @read_time_total.setter
    def read_time_total(self, read_time_total):
        """
        Sets the read_time_total of this InterfaceStats.
        Total time in microseconds spent in read operations.

        :param read_time_total: The read_time_total of this InterfaceStats.
        :type: float
        """
        self._read_time_total = read_time_total

    @property
    def read_time_max(self):
        """
        Gets the read_time_max of this InterfaceStats.
        Max time in microseconds spent processing one read operation.

        :return: The read_time_max of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._read_time_max

    @read_time_max.setter
    def read_time_max(self, read_time_max):
        """
        Sets the read_time_max of this InterfaceStats.
        Max time in microseconds spent processing one read operation.

        :param read_time_max: The read_time_max of this InterfaceStats.
        :type: float
        """
        self._read_time_max = read_time_max

    @property
    def write_ops(self):
        """
        Gets the write_ops of this InterfaceStats.
        Number of write operations.

        :return: The write_ops of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._write_ops

    @write_ops.setter
    def write_ops(self, write_ops):
        """
        Sets the write_ops of this InterfaceStats.
        Number of write operations.

        :param write_ops: The write_ops of this InterfaceStats.
        :type: float
        """
        self._write_ops = write_ops

    @property
    def write_bytes(self):
        """
        Gets the write_bytes of this InterfaceStats.
        Number of bytes write.

        :return: The write_bytes of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._write_bytes

    @write_bytes.setter
    def write_bytes(self, write_bytes):
        """
        Sets the write_bytes of this InterfaceStats.
        Number of bytes write.

        :param write_bytes: The write_bytes of this InterfaceStats.
        :type: float
        """
        self._write_bytes = write_bytes

    @property
    def write_time_total(self):
        """
        Gets the write_time_total of this InterfaceStats.
        Total time in microseconds spent in write operations.

        :return: The write_time_total of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._write_time_total

    @write_time_total.setter
    def write_time_total(self, write_time_total):
        """
        Sets the write_time_total of this InterfaceStats.
        Total time in microseconds spent in write operations.

        :param write_time_total: The write_time_total of this InterfaceStats.
        :type: float
        """
        self._write_time_total = write_time_total

    @property
    def write_time_max(self):
        """
        Gets the write_time_max of this InterfaceStats.
        Max time in microseconds spent processing one write operation.

        :return: The write_time_max of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._write_time_max

    @write_time_max.setter
    def write_time_max(self, write_time_max):
        """
        Sets the write_time_max of this InterfaceStats.
        Max time in microseconds spent processing one write operation.

        :param write_time_max: The write_time_max of this InterfaceStats.
        :type: float
        """
        self._write_time_max = write_time_max

    @property
    def other_ops(self):
        """
        Gets the other_ops of this InterfaceStats.
        Number of non-read-write operations.

        :return: The other_ops of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._other_ops

    @other_ops.setter
    def other_ops(self, other_ops):
        """
        Sets the other_ops of this InterfaceStats.
        Number of non-read-write operations.

        :param other_ops: The other_ops of this InterfaceStats.
        :type: float
        """
        self._other_ops = other_ops

    @property
    def other_time_total(self):
        """
        Gets the other_time_total of this InterfaceStats.
        Total time in microseconds spent in non-read-write ops.

        :return: The other_time_total of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._other_time_total

    @other_time_total.setter
    def other_time_total(self, other_time_total):
        """
        Sets the other_time_total of this InterfaceStats.
        Total time in microseconds spent in non-read-write ops.

        :param other_time_total: The other_time_total of this InterfaceStats.
        :type: float
        """
        self._other_time_total = other_time_total

    @property
    def other_time_max(self):
        """
        Gets the other_time_max of this InterfaceStats.
        Max time in microseconds spent processing one non-read-write op.

        :return: The other_time_max of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._other_time_max

    @other_time_max.setter
    def other_time_max(self, other_time_max):
        """
        Sets the other_time_max of this InterfaceStats.
        Max time in microseconds spent processing one non-read-write op.

        :param other_time_max: The other_time_max of this InterfaceStats.
        :type: float
        """
        self._other_time_max = other_time_max

    @property
    def read_time_total_sq(self):
        """
        Gets the read_time_total_sq of this InterfaceStats.
        Sum of the squares of microseconds spent in read operations.

        :return: The read_time_total_sq of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._read_time_total_sq

    @read_time_total_sq.setter
    def read_time_total_sq(self, read_time_total_sq):
        """
        Sets the read_time_total_sq of this InterfaceStats.
        Sum of the squares of microseconds spent in read operations.

        :param read_time_total_sq: The read_time_total_sq of this InterfaceStats.
        :type: float
        """
        self._read_time_total_sq = read_time_total_sq

    @property
    def write_time_total_sq(self):
        """
        Gets the write_time_total_sq of this InterfaceStats.
        Sum of the squares of microseconds spent in write operations.

        :return: The write_time_total_sq of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._write_time_total_sq

    @write_time_total_sq.setter
    def write_time_total_sq(self, write_time_total_sq):
        """
        Sets the write_time_total_sq of this InterfaceStats.
        Sum of the squares of microseconds spent in write operations.

        :param write_time_total_sq: The write_time_total_sq of this InterfaceStats.
        :type: float
        """
        self._write_time_total_sq = write_time_total_sq

    @property
    def other_time_total_sq(self):
        """
        Gets the other_time_total_sq of this InterfaceStats.
        Sum of the squares of microseconds spent in non-read-write operations.

        :return: The other_time_total_sq of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._other_time_total_sq

    @other_time_total_sq.setter
    def other_time_total_sq(self, other_time_total_sq):
        """
        Sets the other_time_total_sq of this InterfaceStats.
        Sum of the squares of microseconds spent in non-read-write operations.

        :param other_time_total_sq: The other_time_total_sq of this InterfaceStats.
        :type: float
        """
        self._other_time_total_sq = other_time_total_sq

    @property
    def queue_depth_total(self):
        """
        Gets the queue_depth_total of this InterfaceStats.
        Total channel queue depth.

        :return: The queue_depth_total of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._queue_depth_total

    @queue_depth_total.setter
    def queue_depth_total(self, queue_depth_total):
        """
        Sets the queue_depth_total of this InterfaceStats.
        Total channel queue depth.

        :param queue_depth_total: The queue_depth_total of this InterfaceStats.
        :type: float
        """
        self._queue_depth_total = queue_depth_total

    @property
    def queue_depth_max(self):
        """
        Gets the queue_depth_max of this InterfaceStats.
        Maximum channel queue depth.

        :return: The queue_depth_max of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._queue_depth_max

    @queue_depth_max.setter
    def queue_depth_max(self, queue_depth_max):
        """
        Sets the queue_depth_max of this InterfaceStats.
        Maximum channel queue depth.

        :param queue_depth_max: The queue_depth_max of this InterfaceStats.
        :type: float
        """
        self._queue_depth_max = queue_depth_max

    @property
    def channel_error_counts(self):
        """
        Gets the channel_error_counts of this InterfaceStats.
        The total number of errors detected on this channel.

        :return: The channel_error_counts of this InterfaceStats.
        :rtype: float
        :required/optional: required
        """
        return self._channel_error_counts

    @channel_error_counts.setter
    def channel_error_counts(self, channel_error_counts):
        """
        Sets the channel_error_counts of this InterfaceStats.
        The total number of errors detected on this channel.

        :param channel_error_counts: The channel_error_counts of this InterfaceStats.
        :type: float
        """
        self._channel_error_counts = channel_error_counts

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
