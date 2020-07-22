#!/usr/bin/python
# -*- coding: utf-8 -*-


# Copyright 2020 Colton Hughes <colton.hughes@firemon.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


ANSIBLE_METADATA = {'status': ['stableinterface'],
                    'supported_by': 'community',
                    'version': '1.0'}

DOCUMENTATION = '''
---
module: win_move_user
version_added: "2.9.10"
short_description: Moves AD User objects between OUs and CNs
description:
     - The module win_move_user moves Active Directory User objects between OUs and CNs.
options:
  name:
    description:
      - Identifiable parameter to find the object you are wanting to move. Currently supports (sAMAccountName and UserPrincipalName)
    required: true
    default: null
    aliases: []
  path:
    description:
      - Path to where you would like to move the object to. If the path is the same as the current location the object will NOT be moved.
    required: true
    default: null
    aliases: []
author: "Colton Hughes <colton.hughes@firemon.com>"
'''

EXAMPLES = '''
- name: Move a user to the Disabled Users OU
  win_move_user:
    name: dummy_user@testdomain.com
    path: OU=Disabled Users,DC=domain,DC=com
'''
RETURN = '''
old_path:
  description: original location of AD object
  returned: always
  type: string
  sample: "CN=Users,DC=domain,DC=com"
new_path:
  description: new location of AD object
  returned: changed
  type: string
  sample: "OU=Disabled Users,DC=domain,DC=com"
'''
