#!/usr/bin/env python3
"""
Parse README.md (Single Source of Truth) and merge with metadata.json
to generate docs/data/prompts.json for the gallery website.

README format expected:
  ## Prompts: Category Name
  ### Subcategory
  - [Title](https://tygwan.github.io/awesome-stitch-design/#slug) - Description.

metadata.json provides supplementary data keyed by slug:
  { "slug": { "prompt": "...", "device": "Desktop", "featured": false, "discussionNumber": 1 } }

Contributor is extracted from git log -- the PR author who first added the
line containing the slug. Falls back to the default contributor.
"""

import json
import re
import subprocess
import sys
import os

CATEGORY_MAP = {
    "prompts: marketing and public": "marketing",
    "prompts: product and app": "product",
    "prompts: commerce": "commerce",
    "prompts: utility": "utility",
    "prompts: admin": "admin",
}

DEFAULT_CONTRIBUTOR = {"username": "tygwan", "name": "coffin"}


def parse_readme(readme_path):
    """Parse README.md and extract prompt entries."""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    entries = []
    current_category = None
    current_subcategory = None

    for line in content.split("\n"):
        # Match ## Prompts: Category Name
        h2_match = re.match(r"^## Prompts:\s*(.+)$", line)
        if h2_match:
            cat_name = h2_match.group(1).strip()
            key = f"prompts: {cat_name.lower()}"
            current_category = CATEGORY_MAP.get(key)
            current_subcategory = None
            continue

        # Match ### Subcategory
        h3_match = re.match(r"^### (.+)$", line)
        if h3_match:
            current_subcategory = h3_match.group(1).strip()
            continue

        # Reset category on non-prompt H2
        if re.match(r"^## (?!Prompts:)", line):
            current_category = None
            current_subcategory = None
            continue

        # Match list items: - [Title](url/#slug) - Description.
        if current_category:
            item_match = re.match(
                r"^- \[(.+?)\]\(https://tygwan\.github\.io/awesome-stitch-design/#(.+?)\) - (.+)$",
                line,
            )
            if item_match:
                title = item_match.group(1)
                slug = item_match.group(2)
                description = item_match.group(3).rstrip(".")
                entries.append(
                    {
                        "id": slug,
                        "title": title,
                        "description": description + ".",
                        "category": current_category,
                        "subcategory": current_subcategory,
                    }
                )

    return entries


def get_contributor_from_git(slug, readme_path="README.md"):
    """
    Find the PR author who first added a line containing the slug to README.md.

    Uses `git log --diff-filter=A -S` to find the commit that introduced the slug,
    then extracts the author. Returns None if not found or git is unavailable.
    """
    try:
        # Search for the commit that added a line containing the slug anchor
        result = subprocess.run(
            [
                "git", "log", "--diff-filter=A", "--format=%an",
                "-S", f"#{slug})", "--", readme_path,
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            # Take the earliest commit (last line) that added this slug
            authors = result.stdout.strip().split("\n")
            author = authors[-1].strip()
            if author and author != "github-actions[bot]":
                return {"username": author, "name": author}
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    return None


def merge_with_metadata(entries, metadata_path, use_git=True):
    """Merge parsed entries with metadata.json supplementary data."""
    metadata = {}
    if os.path.exists(metadata_path):
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)

    prompts = []
    for entry in entries:
        slug = entry["id"]
        meta = metadata.get(slug, {})

        # Determine contributor: git log -> metadata -> default
        contributor = None
        if use_git:
            contributor = get_contributor_from_git(slug)
        if not contributor:
            meta_contributor = meta.get("contributor")
            if meta_contributor:
                if isinstance(meta_contributor, dict):
                    contributor = meta_contributor
                else:
                    contributor = {"username": meta_contributor, "name": meta_contributor}
        if not contributor:
            contributor = DEFAULT_CONTRIBUTOR.copy()

        prompt_data = {
            "id": slug,
            "title": entry["title"],
            "description": entry["description"],
            "prompt": meta.get("prompt", ""),
            "image": f"previews/{entry['category']}/{slug}.png",
            "category": entry["category"],
            "subcategory": entry.get("subcategory", ""),
            "device": meta.get("device", "Desktop"),
            "discussionNumber": meta.get("discussionNumber", None),
            "featured": meta.get("featured", False),
            "contributor": contributor,
        }
        prompts.append(prompt_data)

    return {"prompts": prompts}


def main():
    readme_path = "README.md"
    metadata_path = "docs/data/metadata.json"
    output_path = "docs/data/prompts.json"

    # Check if we're in a git repo
    use_git = os.path.isdir(".git")

    entries = parse_readme(readme_path)
    print(f"Parsed {len(entries)} prompt entries from README.md")

    result = merge_with_metadata(entries, metadata_path, use_git=use_git)
    print(f"Generated {len(result['prompts'])} prompts with metadata")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Written to {output_path}")


if __name__ == "__main__":
    main()
