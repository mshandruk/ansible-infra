# ansible-infra

Collection of Ansible playbooks and roles for managing Linux infrastructure.

## Documentation

* [Quick Start](docs/quickstart.md)
* [Playbooks](docs/playbooks.md)
* [Commands Reference](docs/commands.md)

## Project Layout

```text
.
├── ansible.cfg
├── inventories/
├── playbooks/
└── roles/
```

| Directory      | Description            |
|----------------|------------------------|
| `inventories/` | Inventory files        |
| `playbooks/`   | Entry-point playbooks  |
| `roles/`       | Reusable Ansible roles |

## Roles

Each role is responsible for a single area of system configuration.

| Role                                   | Description                            |
|----------------------------------------|----------------------------------------|
| [bootstrap](roles/bootstrap/README.md) | Prepare a host for Ansible automation. |
| [common](roles/common/README.md)       | Configure common system settings.      |
| [docker](roles/docker/README.md)       | Install and configure Docker.          |
| [gateway](roles/gateway/README.md)     | Deploy the net gateway server.         |
| [kvm](roles/kvm/README.md)             | Deploy the KVM virtualization host.    |
| [haproxy](roles/haproxy/README.md)             | Deploy the Haproxy load balancer.    |

Role defaults are stored in:

```text
roles/<role>/defaults/main.yml
```

Inventory-specific values should be overridden using:

```text
inventories/<inventory>/group_vars/
inventories/<inventory>/host_vars/
```

## Inventory

The repository contains an example inventory layout.

```text
inventories/
├── example/
│   ├── hosts.yml
│   ├── group_vars/
│   │   └── all.yml
│   └── host_vars/
```

Copy the example inventory and customize it for your own environment.

## References

- Ansible Best Practices
  https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html
- Alternative Directory Layout
  https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html#alternative-directory-layout
