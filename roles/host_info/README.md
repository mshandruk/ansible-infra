# host_info

Deploys the host_info web application.

## Requirements

- Debian 13+

> Older distributions may work but are not regularly tested.

## Role Variables

> Default variable values can be found in `defaults/main.yml`.

## Features

- Installing the web application.
- Configuring Nginx: (creating the host_info site and disabling default site).
- Configuring the systemd unit.

## Dependencies

This role depends on the nginx role (managed via meta/main.yml)

## Example

### Playbook

playbooks/deploy_host_info.yml

```yaml
---
- name: Deploy host info application
  hosts: host_info_servers
  roles:
    - common
    - host_info
```

### Inventory

inventories/lab/hosts.yml

```yml
all:
  children:
    host_info_servers:
      hosts:
        vm-web-01:
```

## Author

Maxim Shandruk
