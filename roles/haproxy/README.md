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
    host_info_servers:
      hosts:
        vm-web-01:
        vm-web-02:
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
    mode: "http"
    bind: "*:8404"
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

- name: host_info
  frontends:
  - name: host_info
    mode: "http"
    bind: "*:8443"
    timeouts:
      client: "30s"
    options:
      httplog: ""
    default_backend: "host_info_pool"
  backends:
  - name: host_info_pool
    mode: "http"
    backend_port: 80
    balance: "roundrobin"
    retries: 1
    timeouts:
      connect: "400ms"
      check: "400ms"
      server: "30s"
    options:
      redispatch: 1
      httpchk: "GET /"
    ansible_group: "host_info_servers"
    server_check_params: "check inter 500ms fall 2 rise 1"

```

## Author

Maxim Shandruk
