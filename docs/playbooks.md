# Playbooks

Entry-point playbooks for managing Linux hosts and infrastructure services.

## Recommended Workflow

For a newly installed host, run the playbooks in the following order:

```text
bootstrap
    ↓
common
    ↓
infrastructure-specific playbook
    ↓
upgrade-system
```

## Available Playbooks

| Playbook         | Description                                           |
|------------------|-------------------------------------------------------|
| `bootstrap`      | Prepare a newly installed host for Ansible automation |
| `common`         | Configure settings shared by managed hosts            |
| `docker`         | Install and configure Docker                          |
| `gateway`        | Deploy and configure the network gateway server       |
| `kvm`            | Deploy and configure a KVM virtualization host        |
| `haproxy`        | Install and configure the HAProxy load balancer       |
| `upgrade-system` | Update installed system packages                      |
| `nginx`          | Deploy nginx web server                               |

## Running a Playbook

General form:

```bash
ansible-playbook \
  -i inventories/<inventory>/hosts.yml \
  playbooks/<playbook>.yml
```

Replace `<inventory>` and `<playbook>` with the appropriate values for your environment.

See [Commands Reference](commands.md) for commonly used commands.

---

[← Back to project README](../README.md)