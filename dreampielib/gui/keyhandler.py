# Copyright 2009 Noam Yorav-Raphael
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

__all__ = ['make_keyhandler_decorator', 'handle_keypress']

"""
Help handling keypress events. The functions here should be used like this:

keyhandlers = {}
keyhandler = make_keyhandler_decorator(keyhandlers)
class Whatever:
    @keyhandler('Return', 0)
    def on_return(self):
        # Do something
    def on_keypress(self, widget, event):
        handle_keypress(self, event, keyhandlers)
"""

from gtk import gdk

# We ignore all other mods. MOD1 is usually alt, according to docs.
handled_mods = gdk.SHIFT_MASK | gdk.CONTROL_MASK | gdk.MOD1_MASK

def make_keyhandler_decorator(keyhandlers_dict):
    def keyhandler(keyval, state):
        def decorator(func):
            keyhandlers_dict[keyval, state] = func
            return func
        return decorator
    return keyhandler

def handle_keypress(self, event, keyhandlers_dict):
    r = gdk.keymap_get_default().translate_keyboard_state(
        event.hardware_keycode, event.state, event.group)
    if r is None:
        # This seems to be the case when pressing CapsLock on win32
        return
    keyval, group, level, consumed_mods = r
    state = event.state & ~consumed_mods & handled_mods
    keyval_name = gdk.keyval_name(keyval)
    try:
        func = keyhandlers_dict[keyval_name, state]
    except KeyError:
        pass
    else:
        return func(self)

