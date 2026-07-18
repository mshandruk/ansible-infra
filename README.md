# ansible-infra

Collection of Ansible playbooks and roles for managing Linux infrastructure.

---

## Requirements

- Linux
- Git
- Ansible
- sshpass _(optional, for password authentication)_

---

## Preparing the Control Node

Install the required packages on the machine where Ansible will be executed.

### Debian / Ubuntu

```bash
apt update
apt install -y ansible sshpass git
```

---

## Project Layout

```text
.
├── ansible.cfg
├── inventories/
├── playbooks/
└── roles/
```

| Directory      | Description            |
| -------------- | ---------------------- |
| `inventories/` | Inventory files        |
| `playbooks/`   | Entry-point playbooks  |
| `roles/`       | Reusable Ansible roles |

---

## Target Definition

`<target>` may be either:

- an inventory file or directory
- a single host (for example `192.168.1.10,`)

Examples:

```bash
-i inventories/lab
```

```bash
-i 192.168.1.10,
```

---

## Inventory

Show inventory tree

```bash
ansible-inventory -i <target> --graph
```

Show variables for a host

```bash
ansible-inventory -i <target> --host <host>
```

---

## Connectivity

Ping all hosts

```bash
ansible all -i <target> -m ping
```

Ping using a specific user

```bash
ansible all -i <target> -m ping -u <user>
```

Ping using password authentication

```bash
ansible all -i <target> -m ping -u <user> -k
```

---

## Playbooks

### Bootstrap

Prepare a host for Ansible automation.

Connect as **root**:

```bash
ansible-playbook playbooks/bootstrap.yml \
    -i <target> \
    -u root \
    -k
```

Connect as a **sudo** user:

```bash
ansible-playbook playbooks/bootstrap.yml \
    -i <target> \
    -u <user> \
    -k \
    -b \
    -K
```

### Upload SSH Public Key

Install the local SSH public key into the remote user's `authorized_keys`.

```bash
ansible-playbook playbooks/upload-sshkey.yml \
    -i <target> \
    -u <user> \
    -k
```

Run for a single host

```bash
ansible-playbook playbooks/upload-sshkey.yml \
    -i <target> \
    -l <host> \
    -u <user> \
    -k
```

### Upgrade System

```bash
ansible-playbook playbooks/upgrade-system.yml \
    -i <target>
```

---

## Diagnostics

Syntax check

```bash
ansible-playbook playbooks/bootstrap.yml --syntax-check
```

List tasks

```bash
ansible-playbook playbooks/bootstrap.yml --list-tasks
```

Dry run

```bash
ansible-playbook playbooks/bootstrap.yml --check
```

Show file differences

```bash
ansible-playbook playbooks/bootstrap.yml --diff
```

Gather all system facts

```bash
ansible all -i <target> -m setup
```

Show operating system information only

```bash
ansible all \
    -i <target> \
    -m setup \
    -a "filter=ansible_distribution*"
```

---

## References

- Ansible Best Practices
  https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html
- Alternative Directory Layout
  https://docs.ansible.com/ansible/latest/tips_tricks/sample_setup.html#alternative-directory-layout
