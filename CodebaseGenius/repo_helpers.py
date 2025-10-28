# repo_helpers.py
import os
import subprocess
from pathlib import Path

def clone_repo(repo_url: str, tmp_dir: str = "./tmp_repo") -> str:
    """Clone a GitHub repository to a temporary folder."""
    if os.path.exists(tmp_dir):
        subprocess.run(["rm", "-rf", tmp_dir])
    subprocess.run(["git", "clone", repo_url, tmp_dir], check=True)
    return tmp_dir

def build_file_tree(path: str) -> dict:
    """Recursively build file-tree JSON."""
    tree = {}
    path = Path(path)
    for item in path.iterdir():
        if item.name in [".git", "node_modules"]:
            continue
        if item.is_dir():
            tree[item.name] = build_file_tree(item)
        else:
            tree[item.name] = "file"
    return tree

def read_readme(path: str) -> str:
    """Read README.md or similar file."""
    readme_files = ["README.md", "README.MD", "readme.md"]
    for f in readme_files:
        fpath = Path(path) / f
        if fpath.exists():
            return fpath.read_text()
    return "No README found."
import os

def get_repo_map(repo_path):
    """
    Recursively maps the directory structure of a repository.

    Args:
        repo_path (str): Path to the cloned repository.

    Returns:
        dict: Nested dictionary representing the directory structure.
    """
    repo_map = {}

    for root, dirs, files in os.walk(repo_path):
        path = root.replace(repo_path, "").lstrip(os.sep)
        parent = repo_map
        if path:
            for part in path.split(os.sep):
                parent = parent.setdefault(part, {})
        for d in dirs:
            parent.setdefault(d, {})
        for f in files:
            parent[f] = None

    return repo_map
import os

def get_repo_map(repo_path):
    """
    Generate a dictionary representing the repository structure.
    Keys: folder paths
    Values: list of file names in each folder
    """
    repo_map = {}
    for root, dirs, files in os.walk(repo_path):
        if files:  # only include folders that have files
            # Use relative paths for readability
            relative_root = os.path.relpath(root, repo_path)
            repo_map[relative_root] = files
    return repo_map
