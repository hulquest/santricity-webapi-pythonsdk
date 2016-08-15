# coding: utf-8

"""
DeviceAsupDevice.py

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


class DeviceAsupDevice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DeviceAsupDevice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'wwn': 'str',  # (required parameter)
            'name': 'str',  # (required parameter)
            'asup_capable': 'bool',  # (required parameter)
            'asup_enabled': 'bool',  # (required parameter)
            'on_demand_capable': 'bool',  # (required parameter)
            'scheduled': 'bool',  # (required parameter)
            'daily_schedule_time': 'int',  # (required parameter)
            'weekly_schedule_time': 'int',  # (required parameter)
            'weekly_day_of_week': 'str'
        }

        self.attribute_map = {
            'wwn': 'wwn',  # (required parameter)
            'name': 'name',  # (required parameter)
            'asup_capable': 'asupCapable',  # (required parameter)
            'asup_enabled': 'asupEnabled',  # (required parameter)
            'on_demand_capable': 'onDemandCapable',  # (required parameter)
            'scheduled': 'scheduled',  # (required parameter)
            'daily_schedule_time': 'dailyScheduleTime',  # (required parameter)
            'weekly_schedule_time': 'weeklyScheduleTime',  # (required parameter)
            'weekly_day_of_week': 'weeklyDayOfWeek'
        }

        self._wwn = None
        self._name = None
        self._asup_capable = None
        self._asup_enabled = None
        self._on_demand_capable = None
        self._scheduled = None
        self._daily_schedule_time = None
        self._weekly_schedule_time = None
        self._weekly_day_of_week = None

    @property
    def wwn(self):
        """
        Gets the wwn of this DeviceAsupDevice.
        Device's world-wide-name

        :return: The wwn of this DeviceAsupDevice.
        :rtype: str
        :required/optional: required
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """
        Sets the wwn of this DeviceAsupDevice.
        Device's world-wide-name

        :param wwn: The wwn of this DeviceAsupDevice.
        :type: str
        """
        self._wwn = wwn

    @property
    def name(self):
        """
        Gets the name of this DeviceAsupDevice.
        Device's name

        :return: The name of this DeviceAsupDevice.
        :rtype: str
        :required/optional: required
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceAsupDevice.
        Device's name

        :param name: The name of this DeviceAsupDevice.
        :type: str
        """
        self._name = name

    @property
    def asup_capable(self):
        """
        Gets the asup_capable of this DeviceAsupDevice.
        ASUP capable

        :return: The asup_capable of this DeviceAsupDevice.
        :rtype: bool
        :required/optional: required
        """
        return self._asup_capable

    @asup_capable.setter
    def asup_capable(self, asup_capable):
        """
        Sets the asup_capable of this DeviceAsupDevice.
        ASUP capable

        :param asup_capable: The asup_capable of this DeviceAsupDevice.
        :type: bool
        """
        self._asup_capable = asup_capable

    @property
    def asup_enabled(self):
        """
        Gets the asup_enabled of this DeviceAsupDevice.
        ASUP enabled

        :return: The asup_enabled of this DeviceAsupDevice.
        :rtype: bool
        :required/optional: required
        """
        return self._asup_enabled

    @asup_enabled.setter
    def asup_enabled(self, asup_enabled):
        """
        Sets the asup_enabled of this DeviceAsupDevice.
        ASUP enabled

        :param asup_enabled: The asup_enabled of this DeviceAsupDevice.
        :type: bool
        """
        self._asup_enabled = asup_enabled

    @property
    def on_demand_capable(self):
        """
        Gets the on_demand_capable of this DeviceAsupDevice.
        ASUP OnDemand capable

        :return: The on_demand_capable of this DeviceAsupDevice.
        :rtype: bool
        :required/optional: required
        """
        return self._on_demand_capable

    @on_demand_capable.setter
    def on_demand_capable(self, on_demand_capable):
        """
        Sets the on_demand_capable of this DeviceAsupDevice.
        ASUP OnDemand capable

        :param on_demand_capable: The on_demand_capable of this DeviceAsupDevice.
        :type: bool
        """
        self._on_demand_capable = on_demand_capable

    @property
    def scheduled(self):
        """
        Gets the scheduled of this DeviceAsupDevice.
        Device has ASUP daily/weekly schedule

        :return: The scheduled of this DeviceAsupDevice.
        :rtype: bool
        :required/optional: required
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """
        Sets the scheduled of this DeviceAsupDevice.
        Device has ASUP daily/weekly schedule

        :param scheduled: The scheduled of this DeviceAsupDevice.
        :type: bool
        """
        self._scheduled = scheduled

    @property
    def daily_schedule_time(self):
        """
        Gets the daily_schedule_time of this DeviceAsupDevice.
        ASUP daily scheduled time

        :return: The daily_schedule_time of this DeviceAsupDevice.
        :rtype: int
        :required/optional: required
        """
        return self._daily_schedule_time

    @daily_schedule_time.setter
    def daily_schedule_time(self, daily_schedule_time):
        """
        Sets the daily_schedule_time of this DeviceAsupDevice.
        ASUP daily scheduled time

        :param daily_schedule_time: The daily_schedule_time of this DeviceAsupDevice.
        :type: int
        """
        self._daily_schedule_time = daily_schedule_time

    @property
    def weekly_schedule_time(self):
        """
        Gets the weekly_schedule_time of this DeviceAsupDevice.
        ASUP weekly scheduled time

        :return: The weekly_schedule_time of this DeviceAsupDevice.
        :rtype: int
        :required/optional: required
        """
        return self._weekly_schedule_time

    @weekly_schedule_time.setter
    def weekly_schedule_time(self, weekly_schedule_time):
        """
        Sets the weekly_schedule_time of this DeviceAsupDevice.
        ASUP weekly scheduled time

        :param weekly_schedule_time: The weekly_schedule_time of this DeviceAsupDevice.
        :type: int
        """
        self._weekly_schedule_time = weekly_schedule_time

    @property
    def weekly_day_of_week(self):
        """
        Gets the weekly_day_of_week of this DeviceAsupDevice.
        ASUP weekly scheduled day of week

        :return: The weekly_day_of_week of this DeviceAsupDevice.
        :rtype: str
        :required/optional: required
        """
        return self._weekly_day_of_week

    @weekly_day_of_week.setter
    def weekly_day_of_week(self, weekly_day_of_week):
        """
        Sets the weekly_day_of_week of this DeviceAsupDevice.
        ASUP weekly scheduled day of week

        :param weekly_day_of_week: The weekly_day_of_week of this DeviceAsupDevice.
        :type: str
        """
        allowed_values = ["notSpecified", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "__UNDEFINED"]
        if weekly_day_of_week not in allowed_values:
            raise ValueError(
                "Invalid value for `weekly_day_of_week`, must be one of {0}"
                .format(allowed_values)
            )
        self._weekly_day_of_week = weekly_day_of_week

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
