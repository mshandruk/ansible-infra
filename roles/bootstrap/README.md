# bootstrap

Prepare a new linux host for ansible automation.

## Requirements

- Debian 13+
- Ubuntu 22.04+

> Older distributions may work but are not regularly tested.

## Features

- Create automation user.
- Configure sudo.
- Install SSH public key.

## Generate SSH key

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519_ansible -N ""
```

## Role Variables

| Variable                   | Default                                    | Description                                  |
|----------------------------|--------------------------------------------|----------------------------------------------|
| `bootstrap_user`           | `ansible`                                  | Automation user name                         |
| `bootstrap_sudo_nopasswd`  | `true`                                     | Allow passwordless sudo                      |
| `bootstrap_authorized_key` | "{{ lookup('file', ansible_public_key) }}" | Public key installed for the automation user |

## Initial bootstrap

For the initial bootstrap only, override ansible_user with an existing administrative account (for example, root or a
sudo-enabled user). After the role completes successfully, configure your inventory to connect as the automation user
created by this role.

### Debian

```bash
ansible-playbook playbooks/bootstrap.yml -i <inventory> -e "ansible_user=root" -k
```

### Ubuntu 24.04

```bash
ansible-playbook playbooks/bootstrap.yml -i <inventory> -e "ansible_user=<some_sudo_user>" -k -K
```

### Ubuntu 26.04

```bash
ansible-playbook playbooks/bootstrap.yml -i <inventory> -e "ansible_user=<some_sudo_user> ansible_become_exe=/usr/bin/sudo.ws" -k -K
```

After bootstrapping, update your inventory to connect as the automation user created by this role. Example
`group_vars/all.yml`:

```yaml
# SSH

ansible_user: ansible
ansible_public_key: "{{ lookup('env', 'HOME') }}/.ssh/id_ed25519_ansible.pub"
```

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Bootstrap
  gather_facts: true
  hosts: all
  become: true

  roles:
    - bootstrap
```

## License

MIT

## Author Information

© 2026 Maxim Shandruk
