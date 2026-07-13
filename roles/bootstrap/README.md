# bootstrap

Prepare a new linux host for ansible automation.

## Requirements

- Debian 13+
- Ubuntu 22.04+

> Older distributions may work but are not regularly tested.

## Role Variables

| Variable                  | Default                 | Description                      |
| ------------------------- | ----------------------- | -------------------------------- |
| `bootstrap_user`          | `ansible`               | Automation user name             |
| `bootstrap_sudo_nopasswd` | `true`                  | Allow passwordless sudo          |
| `bootstrap_ssh_key_path`  | `~/.ssh/id_ed25519.pub` | Path to the local SSH public key |

## Features

- create automation user
- configure sudo
- install SSH public key

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  become: true
  roles:
    - bootstrap
```

## License

MIT

## Author Information

© 2026 Maxim Shandruk
