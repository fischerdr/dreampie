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

#------------------------------------------------------------------------------
# String Types
#------------------------------------------------------------------------------
if py3k:
    unicode = str
    basestring = str
else:
    # These are already defined in Python 2
    pass

#------------------------------------------------------------------------------
# Numeric Types
#------------------------------------------------------------------------------
if py3k:
    long = int
else:
    # long is already defined in Python 2
    pass

#------------------------------------------------------------------------------
# Iterators
#------------------------------------------------------------------------------
if py3k:
    xrange = range
else:
    # xrange is already defined in Python 2
    pass

#------------------------------------------------------------------------------
# Dictionary Methods
#------------------------------------------------------------------------------
if py3k:
    def iteritems(d):
        return d.items()

    def iterkeys(d):
        return d.keys()

    def itervalues(d):
        return d.values()
else:
    def iteritems(d):
        return d.iteritems()

    def iterkeys(d):
        return d.iterkeys()

    def itervalues(d):
        return d.itervalues()

#------------------------------------------------------------------------------
# Input Functions
#------------------------------------------------------------------------------
if py3k:
    raw_input = input
else:
    # raw_input is already defined in Python 2
    pass

#------------------------------------------------------------------------------
# Character Functions
#------------------------------------------------------------------------------
if py3k:
    unichr = chr
else:
    # unichr is already defined in Python 2
    pass

#------------------------------------------------------------------------------
# Comparison Functions
#------------------------------------------------------------------------------
if py3k:
    def cmp(a, b):
        """
        Implementation of cmp() for Python 3.
        
        Compare the two objects a and b and return an integer according to the outcome:
        - Return a negative integer if a < b
        - Return zero if a == b
        - Return a positive integer if a > b
        """
        return (a > b) - (a < b)
else:
    # cmp is already defined in Python 2
    pass

#------------------------------------------------------------------------------
# GTK Compatibility
#------------------------------------------------------------------------------
# Define GTK compatibility variables
gtk = None
gobject = None
gtksourceview2 = None
pango = None
gdk = None
glade = None

try:
    # Try importing the old-style GTK modules
    import gobject
    import gtk
    import gtksourceview2
    import pango
    import gdk
    import glade
except ImportError:
    # If old-style imports fail, use the new GI repository
    import gi
    
    # Try different GTK source versions
    gtksource_version = None
    for version in ['4.0', '3.0', '2.0']:
        try:
            gi.require_version('GtkSource', version)
            gtksource_version = version
            break
        except (ValueError, ImportError):
            continue
    
    if gtksource_version is None:
        raise ImportError("Could not find any compatible GtkSource version")
    
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk as gtk
    from gi.repository import GObject as gobject
    from gi.repository import GtkSource as gtksourceview2
    from gi.repository import Pango as pango
    from gi.repository import Gdk as gdk
    try:
        gi.require_version('Glade', '2.0')
    except (ValueError, ImportError):
        try:
            gi.require_version('Glade', '3.0')
        except (ValueError, ImportError):
            pass
    try:
        from gi.repository import Glade as glade
    except (ImportError, ValueError):
        glade = None

#------------------------------------------------------------------------------
# Utility Functions
#------------------------------------------------------------------------------
def unicodify(s):
    """
    Convert a string to unicode in both Python 2 and 3.
    
    Args:
        s: The string to convert
        
    Returns:
        A unicode string
    """
    if py3k:
        if isinstance(s, bytes):
            return s.decode("utf-8")
        return str(s)
    else:
        if isinstance(s, str):
            return s.decode("utf-8")
        return unicode(s)
