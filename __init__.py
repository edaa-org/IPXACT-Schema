# ==================================================================================================================== #
#               ___ ______  __    _    ____ _____                                                                      #
#   _ __  _   _|_ _|  _ \ \/ /   / \  / ___|_   _|                                                                     #
#  | '_ \| | | || || |_) \  /   / _ \| |     | |                                                                       #
#  | |_) | |_| || ||  __//  \  / ___ \ |___  | |                                                                       #
#  | .__/ \__, |___|_|  /_/\_\/_/   \_\____| |_|                                                                       #
#  |_|    |___/                                                                                                        #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2017-2025 Patrick Lehmann - Bötzingen, Germany                                                             #
# Copyright 2016-2016 Patrick Lehmann - Dresden, Germany                                                               #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""
This package is a resource package containing various data files.

.. rubric:: Common Files

* :file:`README.md`
* :file:`LICENSE.md`
* :file:`NOTICE.md`

.. rubric:: XML Schema Files

* :file:`ipxact-1.0/`

  * :file:`README.md`
  * :file:`index.xsd`
  * :file:`***.xsd`

* :file:`ipxact-1.1/`

  * :file:`README.md`
  * :file:`index.xsd`
  * :file:`***.xsd`

* :file:`ipxact-1.2/`

  * :file:`README.md`
  * :file:`index.xsd`
  * :file:`***.xsd`

* :file:`ipxact-1.4/`

  * :file:`README.md`
  * :file:`index.xsd`
  * :file:`***.xsd`

* :file:`ipxact-1.5/`

  * :file:`README.md`
  * :file:`index.xsd`
  * :file:`***.xsd`

* :file:`ieee-1685-2009/`

  * :file:`README.md`
  * :file:`index.xsd`
  * :file:`***.xsd`

* :file:`ieee-1685-2014/`

  * :file:`README.md`
  * :file:`index.xsd`
  * :file:`***.xsd`

* :file:`ieee-1685-2022/`

  * :file:`README.md`
  * :file:`LICENSE`
  * :file:`NOTICE`
  * :file:`index.xsd`
  * :file:`***.xsd`

"""
from sys import modules

from pyTooling.Common import getResourceFile

__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2016-2025, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.4.0"

__module = modules[__name__]

_IPXACT_10_INDEX = getResourceFile(__module, "ipxact-1.0/index.xsd")
_IPXACT_11_INDEX = getResourceFile(__module, "ipxact-1.1/index.xsd")
_IPXACT_12_INDEX = getResourceFile(__module, "ipxact-1.2/index.xsd")
_IPXACT_14_INDEX = getResourceFile(__module, "ipxact-1.4/index.xsd")
_IPXACT_15_INDEX = getResourceFile(__module, "ipxact-1.5/index.xsd")

_IPXACT_2009_INDEX = getResourceFile(__module, "ieee-1685-2009/index.xsd")
_IPXACT_2014_INDEX = getResourceFile(__module, "ieee-1685-2014/index.xsd")
_IPXACT_2022_INDEX = getResourceFile(__module, "ieee-1685-2022/index.xsd")

__all__ = [
	"_IPXACT_10_INDEX",
	"_IPXACT_11_INDEX",
	"_IPXACT_12_INDEX",
	"_IPXACT_14_INDEX",
	"_IPXACT_15_INDEX",
	"_IPXACT_2009_INDEX",
	"_IPXACT_2014_INDEX",
	"_IPXACT_2022_INDEX"
]
