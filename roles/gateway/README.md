# gateway

A simple internet gateway

## Requirements

- Debian 13+

> Older distributions may work but are not regularly tested.

## Role Variables

### Required Variables

| Variable    | Default | Description   |
|-------------|---------|---------------|
| `iface_lan` |         | Lan interface |
| `iface_wan` |         | Wan interface |

### Optional Variables

| Variable                | Default | Description                                         |
|-------------------------|---------|-----------------------------------------------------|
| `gateway_input_rules`   | `[]`    | List of allowed incoming rules for the INPUT chain  |
| `gateway_port_forwards` | `[]`    | List of port forwarding (DNAT) rules                |
| `gateway_forward_rules` | `[]`    | List of allowed transit rules for the FORWARD chain |

> Default variables values can be found in `defaults/main.yml`.
> Note: By default, the port for Ansible is allowed in the `filter` table's `input` chain, see templates/rules.v4.j2

## Features

- Install iptables, iptables-persistent.
- Enables IPv4 forwarding in sysctl.
- Disallow IPv6 default policy.
- Configure source NAT (masquerade) from iface_lan to iface_wan
- Manages custom INPUT, FORWARD, and DNAT rules.

## Dependencies

None.

## Example

### Playbook

playbooks/gateway.yml

```yaml
---
- hosts: gateway
  roles:
    - gateway
```

### Inventory

inventories/lab/hosts.yml

```yml
all:
  children:
    gateway:
      hosts:
        gw:
          ansible_host: 192.168.1.1
```

inventories/lab/host_vars/gw.yml

Internet gateway

```yaml
---
iface_wan: enp1s0
iface_lan: enp7s0

gateway_enable_masquerade: true
gateway_forward_rules:
  - in_interface: "{{ iface_lan }}"
    out_interface: "{{ iface_wan }}"
    comment: Allow LAN to WAN internet access
```

Port forwarding gateway

```yml
---
iface_wan: enp1s0
iface_lan: enp7s0

gateway_port_forwards:
  - protocol: tcp
    external_port: 80
    destination: 10.0.0.2
    destination_port: 8080
    in_interface: "{{ iface_wan }}"
    out_interface: "{{ iface_lan }}"
    comment: Allow access to web site
```

Allow icmp

```yaml
---
iface_wan: enp1s0
iface_lan: enp7s0

gateway_input_rules:
  - protocol: icmp
    icmp_type: echo-request
    comment: Allow echo request (ping)
```

## Author

Maxim Shandruk
