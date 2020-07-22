# Module Documentation
This module is quite simple.
All it does is allow you to provide a name for a user and move them within the Active Directory environment.

## Example
```
- name: Move a user to the Disabled Users OU
  win_move_user:
    name: dummy_user@testdomain.com
    path: OU=Disabled Users,DC=domain,DC=com
```
This is a very simple module that I put very little effort in perfecting.  If issues arise feel free to open them or fork and modify at your own discretion.