# kvm

Ansible role for install and configure KVM hypervisor on Linux servers.

## Requirements

- Debian 13+
- Ubuntu 22.04+

> Older distributions may work but are not regularly tested.

## Role Variables

| Variable          | Default | Description                                           |
| ----------------- | ------- | ----------------------------------------------------- |
| `kvm_admin`       | root    | System user to be added to `libvirt` and `kvm` groups |
| `kvm_install_gui` | false   | Install graphical managment tools (`virt-manager`)    |

## Features

- Installs KVM hypervisor components, CLI managment tools (`virt-install`), and optional GUI (`virt-manager`)
- Grant KVM management permissions to the specified administrator user.
- Configure kvm aministrator

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Install KVM
  hosts: kvm
  roles:
    - kvm
```

## Author

Maxim Shandruk
