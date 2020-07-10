#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2020, Colton Hughes <coltonhughes05@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'version': '1.0'}

DOCUMENTATION = """
---
module: win_move_user
version_added: "2.9"
short_description: Move users between OUs
description:
    - Move user objects in Active Directory between Organizational Units
options:
    name:
        description:
            - The users identifying name of the user. This can be their sAMAccount name, UserPrincipalName, SID, DistinguishedName.
    path:
        description:
            - The path for the object to be moved to.
author: Colton Hughes
"""

EXAMPLES = """
# Move a test user to a new OU
---
- name: Move test user to my_ou organizationl unit
  win_move_user:
    name: taccount
    path: "OU=my_ou,DC=DOMAIN,DC=COM"
"""

RETURN = """
original_path:
    description: The users original path (minus the user CN)
    returned: always
    type: string
    sample: "OU=TEST,DC=DOMAIN,DC=COM"
new_path:
    description: The new path to the user (minus the user CN)
    returned: always
    type: string
    sample: "CN=Users,DC=DOMAIN,DC=COM"
"""