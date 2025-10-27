import os
import git
from pathlib import Path
from textwrap import shorten

def clone_repo(repo_url, tmp_dir="tmp_repo"):
    """Clone the given GitHub repository into a temporary directory."""
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(tmp_dir, repo_name)

    if os.path.exists(repo_path):
        print(f"Repository already exists at {repo_path}")
        return repo_path

    print(f"Cloning {repo_url} into {repo_path}...")
    git.Repo.clone_from(repo_url, repo_path)
    print("Clone completed!")
    return repo_path


def get_repo_map(repo_path):
    """Return a structured map of files and folders in the repository."""
    file_map = {}
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in [".git", "__pycache__", "node_modules"]]
        rel_path = os.path.relpath(root, repo_path)
        file_map[rel_path] = files
    return file_map


def summarize_readme(repo_path):
    """Summarize README.md if it exists."""
    readme_path = Path(repo_path) / "README.md"
    if not readme_path.exists():
        return "No README found."

    content = readme_path.read_text(encoding="utf-8")
    return shorten(content.strip().replace("\n", " "), width=400, placeholder="...")


if __name__ == "__main__":
    # For standalone testing
    repo_url = "https://github.com/pallets/flask.git"
    repo_path = clone_repo(repo_url)
    print(summarize_readme(repo_path))
    print(get_repo_map(repo_path))

