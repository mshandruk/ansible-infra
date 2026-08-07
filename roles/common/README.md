# common

Common system configuration for linux hosts.

## Requirements

- Debian 13+
- Ubuntu 22.04+

> Older distributions may work but are not regularly tested.

## Features

- Configure timezone
- Configure locales
- Install common packages

## Role Variables

| Variable          | Default         | Description         |
|-------------------|-----------------|---------------------|
| `common_timezone` | `Etc/UTC`       | System timezone     |
| `common_locales`  | ["en_US.UTF-8"] | Locales to generate |
| `common_packages` | []              | Packages to install |

## Dependencies

None.

## Example Playbook

`playbooks/common.yml`

```yaml
---
- name: Apply common system configuration
  hosts: all
  become: true
  roles:
    - common
```

```bash
ansible-playbook -i <inventory> playbooks/common.yml
```

## Author

Maxim Shandruk
