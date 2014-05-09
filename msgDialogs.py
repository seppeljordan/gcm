# msgDialogs.py
#
# Copyright (C) 2014 - Sebastian Jordan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import gtk
import os

ICON_PATH = os.path.dirname(os.path.abspath(__file__)) + "/icon.png"

class EntryDialog( gtk.Dialog):
    """Create a Window that prompts the user to enter text."""
    def __init__(self, title, message, default_text='', modal=True, mask=False):
        """Create an objtect to render a simple input window

        This procedure relies heavily on the gtk bindings.

        Arguments are:
        title -- The title of the window
        message -- a text that is prompted to the user
        default_text -- The text that is in the input box by default
        modal -- modal windows block all parent widows from user input
                 until the user interacted with the modal window
        """
        gtk.Dialog.__init__(self)
        self.set_title(title)
        self.connect("destroy", self.quit)
        self.connect("delete_event", self.quit)
        if modal:
            self.set_modal(True)
        box = gtk.VBox(spacing=10)
        box.set_border_width(10)
        self.vbox.pack_start(box)
        box.show()
        if message:
            label = gtk.Label(message)
            box.pack_start(label)
            label.show()
        self.entry = gtk.Entry()
        self.entry.set_text(default_text)
        self.entry.set_visibility(not mask)
        box.pack_start(self.entry)
        self.entry.show()
        self.entry.grab_focus()
        button = gtk.Button(stock=gtk.STOCK_OK)
        button.connect("clicked", self.click)
        self.entry.connect("activate", self.click)
        button.set_flags(gtk.CAN_DEFAULT)
        self.action_area.pack_start(button)
        button.show()
        button.grab_default()
        button = gtk.Button(stock=gtk.STOCK_CANCEL)
        button.connect("clicked", self.quit)
        button.set_flags(gtk.CAN_DEFAULT)
        self.action_area.pack_start(button)
        button.show()
        self.ret = None

    def quit(self, w=None, event=None):
        self.hide()
        self.destroy()        

    def click(self, button):
        self.value = self.entry.get_text()        
        self.response(gtk.RESPONSE_OK)


def inputbox(title, text, default='', password=False):
	"""This procedure creates a small inputbox for user interaction.

        Arguments: 
        title -- string that will be displayed as window title 
        text -- string that will be displayed to the user as a prompt
        password -- boolean that defines if the input of the user will be masked
        """
	msgBox = EntryDialog(title, text, default, mask=password)
	msgBox.set_icon_from_file(ICON_PATH)
	if msgBox.run() == gtk.RESPONSE_OK:
		response = msgBox.value
	else:
		response = None
	msgBox.destroy()
	return response
