# Playbooks

This repository provides several entry-point playbooks for common administration tasks.

## Recommended workflow

For a newly installed host, the recommended order is:

1. **bootstrap** – prepare the host for Ansible automation.
2. **common** – configure common system settings.
3. Run one or more infrastructure-specific playbooks as needed:
      - **docker**
      - **gateway**
      - **kvm**
4. **upgrade-system** – keep installed packages up to date.
5. **upload-sshkey** *(optional)* – install an additional SSH public key.

## Available playbooks

| Playbook             | Description                                    |
|----------------------|------------------------------------------------|
| `bootstrap.yml`      | Prepare a new host for Ansible automation.     |
| `common.yml`         | Apply common Linux configuration.              |
| `docker.yml`         | Install and configure Docker.                  |
| `gateway.yml`        | Configure a Linux gateway.                     |
| `kvm.yml`            | Configure a KVM virtualization host.           |
| `upgrade-system.yml` | Upgrade installed system packages.             |