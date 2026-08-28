#!/usr/bin/env bash

set -eu

BASE_URL="https://mirror.yandex.ru/rockylinux"

for repo_file in /etc/yum.repos.d/*.repo; do
    sed -i 's|^mirrorlist=|#mirrorlist=|' "$repo_file"
    sed -i "s|^#\?baseurl=http://dl.rockylinux.org/\$contentdir\(.*\)|baseurl=${BASE_URL}\\1|" "$repo_file"
done
