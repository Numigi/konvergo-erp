#!/usr/bin/env python3
"""
Script to automatically split gitoo.yml into separate files for incremental Docker builds.
This ensures the split configs stay in sync with the main gitoo.yml file.
"""
import yaml
import os
import sys


def split_gitoo_config(input_file, output_dir):
    """Split gitoo.yml into OCA and Numigi-specific config files"""

    with open(input_file, "r") as f:
        config = yaml.safe_load(f)

    oca_repos = []
    numigi_repos = []

    for repo in config:
        url = repo.get("url", "")
        if "github.com/OCA/" in url:
            oca_repos.append(repo)
        elif "github.com/Numigi/" in url:
            numigi_repos.append(repo)
        else:
            print(f"Warning: Unknown repository organization: {url}")

    # Write OCA config
    oca_file = os.path.join(output_dir, "gitoo-oca.yml")
    with open(oca_file, "w") as f:
        yaml.dump(oca_repos, f, default_flow_style=False, sort_keys=False)

    # Write Numigi config
    numigi_file = os.path.join(output_dir, "gitoo-numigi.yml")
    with open(numigi_file, "w") as f:
        yaml.dump(numigi_repos, f, default_flow_style=False, sort_keys=False)

    print(f"Split {len(config)} repositories:")
    print(f"  - {len(oca_repos)} OCA repos -> {oca_file}")
    print(f"  - {len(numigi_repos)} Numigi repos -> {numigi_file}")


if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "gitoo.yml"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    split_gitoo_config(input_file, output_dir)
