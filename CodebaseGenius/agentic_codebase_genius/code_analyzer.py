import os

def analyze_codebase(repo_path):
    """
    Scans the given repository path and returns a structured summary
    of its folders and files.
    """
    repo_summary = {}

    for root, dirs, files in os.walk(repo_path):
        relative_path = os.path.relpath(root, repo_path)
        repo_summary[relative_path] = {
            "folders": dirs,
            "files": files
        }

    return repo_summary

