# docker

Deploy Docker on supported Linux distributions.

## Requirements

- Debian family: Debian 13+, Ubuntu 24.04+
- RedHat family: Rocky Linux 10+

> Older distributions may work but are not regularly tested.

## Role Variables

> Default variable values can be found in `defaults/main.yml`.

`docker_user`

Optional username to add to the `docker` group.
The user must be already exist on the target host. The role does not create users.

### Docker network

In cases where default docker network overlaps with the host network, breaking host routing.

Docker network configuration is disabled by default:
`docker_configure_net: false`

To enable it:
`docker_configure_net: true`

The default network configuration is:

```yaml
docker_bip: "172.30.0.1/16"
docker_address_pool: "172.31.0.0/16"
docker_address_pool_size: 24
```

`docker_bip` - defines the address and network prefix of docker default bridge(docker0).
`docker_address_pool` - defines the address pool for automatically created user-defined docker network.
`docker_address_pool_size` - defines the prefix size of network allocated from docker_address_pool.

For example:

```text
docker create --name alpine alpine

172.30.0.0/16
└── Docker default bridge
└── docker0: 172.30.0.1
```

```text

docker network create frontend
docker network create backend

172.31.0.0/16
└── Docker network address pool
├── 172.31.0.0/24
├── 172.31.1.0/24
└── ...
```

Make sure that `docker_bip` and `docker_address_pool` do not overlap with
network used by the host.

## Features

- Installing Docker packages from docker repository.
- Adding an existing user to the `docker` group.
- Configuring docker network.

## Dependencies

None.

## Example Playbook

`playbooks/docker.yml`

```yaml
---
- name: Deploy docker
  hosts: all
  roles:
    - docker
```

### Deploy docker with defaults

```bash
ansible-playbook -i <inventory> playbooks/docker.yml
```

### Deploy and add existing user for manage docker cli

```bash
ansible-playbook -i <inventory> playbooks/docker.yml \
  -e "docker_user=<username>"
```

### Deploy docker with docker network configuration

```bash
ansible-playbook -i <inventory> playbooks/docker.yml \
  -e "docker_configure_net=true"
```

### Deploy with a custom docker network configuration

```bash
ansible-playbook -i <inventory> playbooks/docker.yml \
  -e "docker_configure_net=true" \
  -e "docker_bip=172.30.0.1/16" \
  -e "docker_address_pool=172.31.0.0/16" \
  -e "docker_address_pool_size=24"
```

## Author

Maxim Shandruk
