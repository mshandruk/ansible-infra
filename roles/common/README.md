# common

Common system configuration for linux servers.

## Requirements

- Debian 13+
- Ubuntu 22.04+

> Older distributions may work but are not regularly tested.

## Role Variables

| Variable          | Default         | Description                  |
| ----------------- | --------------- | ---------------------------- |
| `common_timezone` | `etc/UTC`       | Timezone region              |
| `common_locales`  | ["en_US.UTF-8"] | Locales to generate          |
| `common_packages` | []              | List of packages for install |

## Features

- Configure timezone
- Configure locales
- Common package installation

## Dependencies

None.

## Example Playbook

```yaml
---
- hosts: all
  become: true
  roles:
    - common
```

## Author

Maxim Shandruk
