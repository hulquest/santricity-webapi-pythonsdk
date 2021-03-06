# coding: utf-8

"""
DdcExtent.py

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


class DdcExtent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DdcExtent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ddc_tag': 'int',  # (required parameter)
            'chunk_number': 'int',  # (required parameter)
            'controller_ref': 'str'
        }

        self.attribute_map = {
            'ddc_tag': 'ddcTag',  # (required parameter)
            'chunk_number': 'chunkNumber',  # (required parameter)
            'controller_ref': 'controllerRef'
        }

        self._ddc_tag = None
        self._chunk_number = None
        self._controller_ref = None

    @property
    def ddc_tag(self):
        """
        Gets the ddc_tag of this DdcExtent.
        The tag associated with the DDC data set being transferred.

        :return: The ddc_tag of this DdcExtent.
        :rtype: int
        :required/optional: required
        """
        return self._ddc_tag

    @ddc_tag.setter
    def ddc_tag(self, ddc_tag):
        """
        Sets the ddc_tag of this DdcExtent.
        The tag associated with the DDC data set being transferred.

        :param ddc_tag: The ddc_tag of this DdcExtent.
        :type: int
        """
        self._ddc_tag = ddc_tag

    @property
    def chunk_number(self):
        """
        Gets the chunk_number of this DdcExtent.
        The number of the DDC chunk that the client wants to retrieve. The number of the first chunk is one.

        :return: The chunk_number of this DdcExtent.
        :rtype: int
        :required/optional: required
        """
        return self._chunk_number

    @chunk_number.setter
    def chunk_number(self, chunk_number):
        """
        Sets the chunk_number of this DdcExtent.
        The number of the DDC chunk that the client wants to retrieve. The number of the first chunk is one.

        :param chunk_number: The chunk_number of this DdcExtent.
        :type: int
        """
        self._chunk_number = chunk_number

    @property
    def controller_ref(self):
        """
        Gets the controller_ref of this DdcExtent.
        A SYMbol reference identifying the controller that has the desired DDC log data.

        :return: The controller_ref of this DdcExtent.
        :rtype: str
        :required/optional: required
        """
        return self._controller_ref

    @controller_ref.setter
    def controller_ref(self, controller_ref):
        """
        Sets the controller_ref of this DdcExtent.
        A SYMbol reference identifying the controller that has the desired DDC log data.

        :param controller_ref: The controller_ref of this DdcExtent.
        :type: str
        """
        self._controller_ref = controller_ref

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

