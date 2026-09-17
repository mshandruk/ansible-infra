#!/usr/bin/env bash

set -eu

BASE_URL="https://mirror.yandex.ru/rockylinux"

REPO_DIR="/etc/yum.repos.d"
REPO_FILES=(
    "rocky-addons.repo"
    "rocky-devel.repo"
    "rocky-extras.repo"
    "rocky.repo"
    "rocky-security.repo"
)

for repo_file in "${REPO_FILES[@]}"; do
    sed -i 's|^mirrorlist=|#mirrorlist=|' "$REPO_DIR/$repo_file"
    sed -i "s|^#\?baseurl=http://dl.rockylinux.org/\$contentdir\(.*\)|baseurl=${BASE_URL}\\1|" "$REPO_DIR/$repo_file"
done
