#!/usr/bin/env python3
"""
OKF v0.2 and Knowledge Vault Conformance Validator
Validates:
1. Root index.md carrying okf_version: "0.2"
2. Reserved files (index.md, log.md) adhering to OKF rules (no invalid frontmatter)
3. Non-reserved markdown files having parseable YAML frontmatter with non-empty 'type'
4. Tags in frontmatter matching canonical tags in 04-Meta/taxonomy.md
5. Internal markdown link integrity (relative links point to existing files)
"""

import sys
import os
import re
from pathlib import Path
import yaml

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent

RESERVED_BASENAMES = {"index.md", "log.md"}
IGNORED_DIRS = {".git", ".obsidian", ".trash"}

def extract_frontmatter(content: str):
    """Returns (frontmatter_dict, body_text) or (None, content)"""
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    fm_raw = parts[1]
    body = parts[2]
    try:
        data = yaml.safe_load(fm_raw)
        return (data if isinstance(data, dict) else {}), body
    except Exception as e:
        return e, body

def get_taxonomy_tags(vault_root: Path) -> set:
    taxonomy_file = vault_root / "04-Meta" / "taxonomy.md"
    if not taxonomy_file.exists():
        return set()
    text = taxonomy_file.read_text(encoding="utf-8")
    # Matches bullet points like `- \`operating-systems\`: ...` or `- `tag`: ...`
    tags = set(re.findall(r"-\s+`([a-z0-9\-]+)`:", text))
    return tags

def validate_vault(vault_root: Path):
    errors = []
    warnings = []
    checked_files = 0

    canonical_tags = get_taxonomy_tags(vault_root)

    # 1. Check Root index.md
    root_index = vault_root / "index.md"
    if not root_index.exists():
        errors.append("Missing bundle root index.md")
    else:
        fm, _ = extract_frontmatter(root_index.read_text(encoding="utf-8"))
        if not isinstance(fm, dict) or fm.get("okf_version") != "0.2":
            errors.append("Root index.md must include frontmatter with okf_version: '0.2'")

    # 2. Iterate all Markdown files
    for root, dirs, files in os.walk(vault_root):
        # Exclude ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

        for f in files:
            if not f.endswith(".md"):
                continue

            file_path = Path(root) / f
            rel_path = file_path.relative_to(vault_root)
            checked_files += 1

            try:
                content = file_path.read_text(encoding="utf-8")
            except Exception as e:
                errors.append(f"{rel_path}: Failed to read file: {e}")
                continue

            fm, body = extract_frontmatter(content)

            # Check reserved vs non-reserved
            if f in RESERVED_BASENAMES:
                if f == "index.md" and file_path == root_index:
                    pass # Root index.md permitted to have okf_version
                elif fm is not None:
                    errors.append(f"{rel_path}: Reserved file '{f}' must not contain YAML frontmatter")
            else:
                if fm is None:
                    errors.append(f"{rel_path}: Missing YAML frontmatter")
                elif isinstance(fm, Exception):
                    errors.append(f"{rel_path}: YAML parse error: {fm}")
                else:
                    note_type = fm.get("type")
                    if not note_type or not str(note_type).strip():
                        errors.append(f"{rel_path}: Missing or empty 'type' field in frontmatter")

                    # Check tags against taxonomy
                    tags = fm.get("tags")
                    if tags and isinstance(tags, list) and canonical_tags:
                        for tag in tags:
                            if tag not in canonical_tags:
                                warnings.append(
                                    f"{rel_path}: Tag '{tag}' is not in 04-Meta/taxonomy.md (requires user approval)"
                                )

            # Check internal markdown links in body (skip templates as they contain mock links)
            if "templates" not in file_path.parts:
                # Strip fenced code blocks and inline code
                cleaned_body = re.sub(r"```[\s\S]*?```", "", body)
                cleaned_body = re.sub(r"`[^`\n]+`", "", cleaned_body)

                links = re.findall(r"\[.*?\]\((.*?)\)", cleaned_body)
                for link in links:
                    link = link.strip().split("#")[0] # remove fragment anchor
                    if not link or link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:"):
                        continue
                    # Resolve link
                    if link.startswith("/"):
                        target = vault_root / link.lstrip("/")
                    else:
                        target = file_path.parent / link

                    # Target can be a directory or file (with or without .md if obsidian style)
                    if not target.exists() and not (target.with_suffix(".md")).exists():
                        warnings.append(f"{rel_path}: Broken internal link -> '{link}'")

    print(f"\n==========================================")
    print(f"OKF v0.2 Knowledge Vault Validation Report")
    print(f"Checked files: {checked_files}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"==========================================\n")

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  [!] {w}")
        print()

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  [X] {e}")
        print("\nResult: FAILED\n")
        return 1
    else:
        print("Result: PASSED (OKF v0.2 conformant)\n")
        return 0

if __name__ == "__main__":
    sys.exit(validate_vault(VAULT_ROOT))
