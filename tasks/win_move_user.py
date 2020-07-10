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