# bootstrap

Prepare a new linux host for ansible automation.

## Requirements

- Debian 13+
- Ubuntu 22.04+

### Ganerate SSH key

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_ansible -N "
```

> Older distributions may work but are not regularly tested.

## Role Variables

| Variable                  | Default                         | Description                      |
| ------------------------- | ------------------------------- | -------------------------------- |
| `bootstrap_user`          | `ansible`                       | Automation user name             |
| `bootstrap_sudo_nopasswd` | `true`                          | Allow passwordless sudo          |
| `bootstrap_ssh_key_path`  | `~/.ssh/id_ed25519_ansible.pub` | Path to the local SSH public key |

## Features

- create automation user
- configure sudo
- install SSH public key

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Bootstrap
  gather_facts: true
  hosts: all

  roles:
    - bootstrap
```

## Debian

```bash
ansible-playbook playbooks/bootstrap.yml -i <inventory> -e "ansible_user=root"
```

## Ubuntu 24.04

```bash
ansible-playbook playbooks/bootstrap.yml -i <inventory> -e "ansible_user=<some_sudo_user>" -K
```

## Ubuntu 26.04

```bash
ansible-playbook playbooks/bootstrap.yml -i <inventory> -e "ansible_user=<some_sudo_user> ansible_become_exe=/usr/bin/sudo.ws" -K
```

## License

MIT

## Author Information

© 2026 Maxim Shandruk
