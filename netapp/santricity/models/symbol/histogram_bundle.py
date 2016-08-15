# coding: utf-8

"""
HistogramBundle.py

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


class HistogramBundle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HistogramBundle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'observation_time': 'int',  # (required parameter)
            'object_ref': 'ObjectReference',  # (required parameter)
            'histogram': 'list[Histogram]'
        }

        self.attribute_map = {
            'observation_time': 'observationTime',  # (required parameter)
            'object_ref': 'objectRef',  # (required parameter)
            'histogram': 'histogram'
        }

        self._observation_time = None
        self._object_ref = None
        self._histogram = None

    @property
    def observation_time(self):
        """
        Gets the observation_time of this HistogramBundle.
        The time that the histogram was retrieved. Time is the number of seconds since midnight, January 1, 1970.

        :return: The observation_time of this HistogramBundle.
        :rtype: int
        :required/optional: required
        """
        return self._observation_time

    @observation_time.setter
    def observation_time(self, observation_time):
        """
        Sets the observation_time of this HistogramBundle.
        The time that the histogram was retrieved. Time is the number of seconds since midnight, January 1, 1970.

        :param observation_time: The observation_time of this HistogramBundle.
        :type: int
        """
        self._observation_time = observation_time

    @property
    def object_ref(self):
        """
        Gets the object_ref of this HistogramBundle.
        A reference to the object to which the histogram applies.

        :return: The object_ref of this HistogramBundle.
        :rtype: ObjectReference
        :required/optional: required
        """
        return self._object_ref

    @object_ref.setter
    def object_ref(self, object_ref):
        """
        Sets the object_ref of this HistogramBundle.
        A reference to the object to which the histogram applies.

        :param object_ref: The object_ref of this HistogramBundle.
        :type: ObjectReference
        """
        self._object_ref = object_ref

    @property
    def histogram(self):
        """
        Gets the histogram of this HistogramBundle.
        An array of histogram streams, one stream per controller.

        :return: The histogram of this HistogramBundle.
        :rtype: list[Histogram]
        :required/optional: required
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """
        Sets the histogram of this HistogramBundle.
        An array of histogram streams, one stream per controller.

        :param histogram: The histogram of this HistogramBundle.
        :type: list[Histogram]
        """
        self._histogram = histogram

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
