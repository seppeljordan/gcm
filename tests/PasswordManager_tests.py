# PasswordManager_tests.py
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
"""
This file defines unittests for the PasswordManager Class
"""

import sys
sys.path.append('..')

import unittest2 as unittest
import passwordManager

class EncryptDecryptIdentityTest(unittest.TestCase):
	def setUp(self):
		self.pm = passwordManager.PasswordManager("test_ring")
	def test_identity(self):
		testPW = "abc"
		pw_hash = pm.encrypt(testPW)
		encryptedPW = pm.decrypt(pw_hash)
		self.assertEqual(testPW, encryptedPW, msg="Test if decryption of an encrypted password is the identity")
	def tearDown(self):
		self.pm.delete_keyring()

	
if __name__ == '__main__':
	unittest.main()