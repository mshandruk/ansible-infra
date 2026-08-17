# Quick Start

Install the required packages on the machine where Ansible will be executed.

### Debian / Ubuntu

1. Install system depends
    ```bash
    apt update
    apt install -y sshpass git wget make
    ```

2. Install uv
    ```bash
    wget -qO- https://astral.sh/uv/install.sh | sh
    ```

3. Clone repository
      ```bash
      git clone https://github.com/mshandruk/ansible-infra.git
      ```

4. Set up the project
      ```bash
      cd ansible-infra
      make setup
      ```

5. Activate the virtual environment
    ```bash
    source .venv/bin/activate
    ```

---
[← Back to project README](../README.md)
