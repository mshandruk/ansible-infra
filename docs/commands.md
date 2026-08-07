# Commands

## Inventory

Show inventory tree

```bash
ansible-inventory -i <target> --graph
```

Show variables for a host

```bash
ansible-inventory -i <target> --host <host>
```

The inventory is responsible for:

- defining hosts and groups;
- connection variables (for example `ansible_user`);
- infrastructure-specific variable overrides.

Role defaults should **not** be modified directly. Override them in `group_vars/` or `host_vars/`.

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

## Syntax

Syntax check

```bash
ansible-playbook playbooks/<some.yml> --syntax-check
```

Lint

```bash
ansible-lint playbooks/<some.yml>
```

## Tasks

List tasks

```bash
ansible-playbook playbooks/<some.yml> --list-tasks
```

Dry run

```bash
ansible-playbook playbooks/<some.yml> --check
```

Show file differences

```bash
ansible-playbook playbooks/<some.yml> --diff
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
