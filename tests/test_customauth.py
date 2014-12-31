# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Unit tests for customauth identity behavior."""

import time
import unittest

import mock
from customauth.middleware import HappyHourIdentity


class TestCustomAuth(unittest.TestCase):
    class DummyUser(object):
        def __init__(self):
            self.name = "Username"
            self.password = "secret"

    @mock.patch('time.localtime')
    @mock.patch('keystone.common.utils.check_password')
    def test_check_password(self, mock_checkpassword, mock_localtime):
        user_ref = self.DummyUser()
        cls = HappyHourIdentity()

        # Grant access when hour == 22
        mock_localtime.return_value = time.strptime("22", "%H")
        self.assertTrue(cls._check_password('token', user_ref))

        # Fallback to parent check_password otherwise
        mock_localtime.return_value = time.strptime("23", "%H")
        cls._check_password('token', user_ref)
        mock_checkpassword.assert_called_once_with('token', 'secret')
