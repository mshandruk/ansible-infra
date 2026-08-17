# Inventory

## Directory Structure

```text
inventories/
└── example/
    ├── hosts.yml
    ├── group_vars/
    │   └── all.yml
    └── host_vars/
```

## Creating an Inventory

Copy the example inventory:

```bash
cp -r inventories/example inventories/<name>
```

## Variables

### Role defaults

```text
roles/<role>/defaults/main.yml
```

### Group variables

```text
inventories/<inventory>/group_vars/
```

### Host variables

```text
inventories/<inventory>/host_vars/
```

### Role Defaults

Role defaults are defined in: `roles/<role>/defaults/main.yml`

They provide default values that can be overridden by inventory variables.

---
[← Back to project README](../README.md)