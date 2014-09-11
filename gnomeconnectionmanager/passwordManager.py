# passwordManager.py
#
# Copyright (C) 2014 - Sebastian Jordan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Todo:
# Add a try except block to check for gnomekeyring bindings
# make a new module and define inputbox in it.
#   We can use the procedures defined in the main program

"""
We want to implement a module so that the gnome_connection_manager
stores its passwords for connections in the gnome keyring
"""

import gnomekeyring as gk
import gtk
from msgDialogs import inputbox

# constants

class NoPassSetException(Exception):
	def __init__(self):
		self.msg = "No Password set"

class PasswordManager:

	def __init__(self, keyring_name):
		"""
		Initialize a new instance of PasswordManager bound to the specified
		keyring.

		Throws a NoPassSetException if a new keyring should be created but no
		password is set by the user.
		"""
		self.keyring_name = keyring_name
		if not self._keyring_exists:
			# We want to create a new keyring and therefore we need
			# a password. We open an inputbox to ask the user for a
			# new password. We will ask twice because we need a validation
			# that the user entered the password correct.
			PASSWORD_MSG = "Enter a new password for the keyring to be created"
			PASSWORD_MSG_RETRY = "The passwords don't match. Please retry"
			while True:
				# We ask the user for a new password. We will ask twice for a
				# password so we can validate that the user made no typo.
				# If the user aborts the process we raise a NoPassSetException
				frist_attempt = inputbox("Create new keyring for gcm", PASSWORD_MSG)
				if first_attempt == False:
					raise NoPassSetException
				second_attempt = inputbox("Create new keyring for gcm", "Re-enter your password!")
				password_correct = (first_attempt == second_attempt)
				if password_correct:
					newpassword = first_attempt
					break
				else:
					PASSWORD_MSG = PASSWORD_MSG_RETRY
			gk.create_sync(self.keyring_name, newpassword)
			gk.set_lock_timeout(self.keyring_name, 60)
			gk.set_lock_on_idle(self.keyring_name, True)

	def decrypt(self, id):
		return False

	def encrypt(self, password):


	def _keyring_exists(self):
		existing_keys = gk.list_keyring_names_sync()
		return (keyring_name in existing_keys)

	def delete_key(self, keyid):
		gk.item_delete_sync(self.keyring_name, keyid)
		
	def delete_keyring(self):
		gk.delete_sync(self.keyring_name)

	def save_host(self, connection_id, attributes):
		false
		
	def create_sync(self, server_info):
		gk.item_create_sync(
			'GKApp', 
			gk.ITEM_NETWORK_PASSWORD, 
			server_info["user"] + "@" + server_info["host"] + ":" + server_info["port"], # This is the description and a unique identifier of the keyring item 
			server_info.pop("pass"), # This is the complete information about the stored connection without the password 
			server_info["pass"], # This is the password of the stored connection
			True) # update if exists with same description and attributes
