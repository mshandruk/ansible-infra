# nginx

Deploy and configure nginx.

## Requirements

- Debian 13+

> Older distributions may work but are not regularly tested.

## Role Variables

> Default variables values can be found in `defaults/main.yml`.

## Features

- Install nginx package.
- Ensure nginx service is enabled and started.

## Dependencies

None.

## Handlers

These handlers can be notified by consumer roles/playbooks.

- `Reload nginx` - Safetly reloads the Nginx configuration without breaking active client connections.
- `Restart nginx` - Full restart nginx service.

## Example

### Inventory

inventories/lab/hosts.yml

```yaml
all:
  children:
    web_servers:
      hosts:
        vm-web-01:
        vm-web-02:
```


### Playbook

Deploy nginx web server:

```yaml
---
- name: Deploy nginx web server
  hosts: web_servers
  roles:
  - nginx
```

 Deploy nginx web server with additional nginx module:

```yaml
---
- name: Deploy nginx web server
  hosts: web_servers
  vars:
    nginx_additional_packages:
    - libnginx-mod-http-geoip2 # Debian package

  roles:
  - nginx

```


## Author

Maxim Shandruk
