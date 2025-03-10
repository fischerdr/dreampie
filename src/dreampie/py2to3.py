#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of DreamPie.
#
# DreamPie is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DreamPie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DreamPie.  If not, see <http://www.gnu.org/licenses/>.

"""
Python 2 to Python 3 compatibility module.

This module provides compatibility definitions for Python 2 and Python 3,
allowing the same code to run on both versions with minimal changes.
"""

import sys

# Determine Python version
py3k = sys.version_info[0] == 3

# For Python 3 compatibility
if py3k:
    # String types
    unicode = str
    basestring = str

    # Numeric types
    long = int

    # Iterators
    xrange = range

    # Dict methods
    def iteritems(d):
        return d.items()

    def iterkeys(d):
        return d.keys()

    def itervalues(d):
        return d.values()

    # Input function
    raw_input = input
else:
    # Dict methods for Python 2
    def iteritems(d):
        return d.iteritems()

    def iterkeys(d):
        return d.iterkeys()

    def itervalues(d):
        return d.itervalues()

    # Keep raw_input as is
    raw_input = raw_input


# Common compatibility functions
def unicodify(s):
    """Convert a string to unicode in both Python 2 and 3."""
    if py3k:
        if isinstance(s, bytes):
            return s.decode("utf-8")
        return str(s)
    else:
        if isinstance(s, str):
            return s.decode("utf-8")
        return unicode(s)
