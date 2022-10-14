#!/usr/bin/env python
"""This module contains a derived date and time classes which with extended
ISO 8601 handling to deal with trailing "Z" characters instead of +0.
"""

# Copyright 2022, United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#
# Reuse is permitted under the terms of the license.
# The AUTHORS file and the LICENSE file are at the
# top level of this library.

import datetime


def isozformat(date_time):
    if date_time.utcoffset() == datetime.timedelta():
        return date_time.replace(tzinfo=None).isoformat() + "Z"
    else:
        raise ValueError(
            "The datetime object is either naive (not timezone aware), "
            "or has a non-zero offset from UTC.  Maybe you just want "
            "the datetime object's isoformat() function?"
        )