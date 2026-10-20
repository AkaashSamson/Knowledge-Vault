#!/usr/bin/env bash
# Sync Knowledge Vault skills to Antigravity discovery paths:
# 1. Workspace .agents/skills/
# 2. Global ~/.gemini/config/skills/

set -euo pipefail

VAULT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SKILLS_SRC="${VAULT_DIR}/04-Meta/skills"
GLOBAL_SKILLS_DIR="${HOME}/.gemini/config/skills"
WORKSPACE_AGENTS_DIR="${VAULT_DIR}/.agents/skills"
PARENT_AGENTS_DIR="$(dirname "${VAULT_DIR}")/.agents/skills"

echo "=== Syncing Knowledge Vault Skills ==="
echo "Source: ${SKILLS_SRC}"

mkdir -p "${WORKSPACE_AGENTS_DIR}"
mkdir -p "${PARENT_AGENTS_DIR}"
mkdir -p "${GLOBAL_SKILLS_DIR}"

for skill_dir in "${SKILLS_SRC}"/*/; do
  if [ -d "${skill_dir}" ]; then
    skill_name="$(basename "${skill_dir}")"
    echo "Syncing skill: ${skill_name}"

    # 1. Local vault .agents/skills/ (relative symlink)
    ln -sfn "../../04-Meta/skills/${skill_name}" "${WORKSPACE_AGENTS_DIR}/${skill_name}"

    # 2. Parent workspace .agents/skills/ (relative symlink)
    ln -sfn "../../Knowledge-Vault/04-Meta/skills/${skill_name}" "${PARENT_AGENTS_DIR}/${skill_name}"

    # 3. Global Antigravity config
    ln -sfn "${SKILLS_SRC}/${skill_name}" "${GLOBAL_SKILLS_DIR}/${skill_name}"
  fi
done

echo "=== Skills sync complete ==="
