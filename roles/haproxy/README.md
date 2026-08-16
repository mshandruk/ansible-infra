# haproxy

Deploy and configure Haproxy load balancer

## Requirements

- Debian 13+

> Older distributions may work but are not regularly tested.

## Role Variables

> Default variables values can be found in `defaults/main.yml`.

## Features

- Install haproxy.
- Configure by inventory.

## Dependencies

None.

## Example

### Playbook

playbooks/haproxy.yml

```yaml
---
- name: Deploy haproxy load balancer
  hosts: haproxy
  roles:
  - haproxy
```

### Inventory

inventories/lab/hosts.yml

```yml
all:
  hosts:
    haproxy:

  children:
    uptime_site:
      hosts:
        vm-web-05:
        vm-web-06:
```

inventories/lab/host_vars/haproxy.yml

```yaml
haproxy_configs:
- name: stats
  userlists:
  - name: stats-users
    users:
    - name: admin
      password: "admin"
      password_hash_alg: "sha512"
      password_secure_salt: "SecureSalt123"
  frontends:
  - name: stats-in
    bind: "*:8404"
    mode: "http"
    http_request_rules:
    - 'auth realm "HAProxy Statistics" if ! { http_auth(stats-users) }'
    default_backend: "stats-out"
  backends:
  - name: stats-out
    mode: "http"
    stats:
    - "enable"
    - "uri /"
    - "refresh 10s"

- name: uptime_site
  defaults:
    mode: "http"
    log: "global"
    retries: 1
    timeouts:
      connect: "400ms"
      check: "400ms"
      client: "30s"
      server: "30s"
    options:
      redispatch: 1
  frontends:
  - name: http_front
    bind: "*:8443"
    default_backend: "uptime_site_pool"
  backends:
  - name: uptime_site_pool
    balance: "roundrobin"
    options:
      httpchk: "HEAD /"
    ansible_group: "uptime_site"
    backend_port: 80
    server_check_params: "check inter 500ms fall 2 rise 1"

```

## Author

Maxim Shandruk
