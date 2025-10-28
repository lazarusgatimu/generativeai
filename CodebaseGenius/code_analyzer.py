import os

def analyze_codebase(repo_path):
    """
    Analyze a codebase and return a summary of Python files and their line counts.
    """
    summary = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        summary[file_path] = len(f.readlines())
                except Exception as e:
                    summary[file_path] = f"Error reading file: {e}"
    return summary

import os

def analyze_codebase(repo_path):
    """
    Analyze a codebase and return a summary of Python files and their line counts.
    """
    summary = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    summary[file_path] = len(f.readlines())
    return summary


import ast
from pathlib import Path
import os
import json

def parse_file(file_path):
    """Parse a Python file and extract functions and classes"""
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=str(file_path))

    file_info = {"functions": [], "classes": []}

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            file_info["functions"].append(node.name)
        elif isinstance(node, ast.ClassDef):
            file_info["classes"].append(node.name)

    return file_info

def build_ccg(repo_path):
    """Build a simple Code Context Graph for all Python files"""
    ccg = {}
    for path in Path(repo_path).rglob("*.py"):
        relative_path = os.path.relpath(path, repo_path)
        ccg[relative_path] = parse_file(path)
    return ccg

if __name__ == "__main__":
    from repo_helpers import clone_repo, build_file_tree, read_readme

    # Test with Requests repo (public)
    repo_path = clone_repo("https://github.com/psf/requests")
    ccg = build_ccg(repo_path)
    
    print(json.dumps(ccg, indent=2))
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
