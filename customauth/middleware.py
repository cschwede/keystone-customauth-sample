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

import time

from keystone.identity.backends import sql
from keystone.openstack.common import log


class HappyHourIdentity(sql.Identity):
    def __init__(self, *args, **kwargs):
        super(HappyHourIdentity, self).__init__(*args, **kwargs)
        self.logger = log.getLogger(__name__)

    def _check_password(self, token, user_ref):
        """ Sample password checker.

        During Happy hour everbody is granted access independent of the given
        password. """

        self.logger.info("check_password: %s", user_ref.name)

        # Modify this according to your needs. Successful password verification
        # should return True
        if time.localtime().tm_hour == 22:
            return True

        # Fall back to SQL authentication
        return super(HappyHourIdentity, self)._check_password(token, user_ref)
