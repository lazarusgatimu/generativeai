# multi_repo.py
import sys
from main import run_agentic_pipeline

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python multi_repo.py <repo1_url> <repo2_url> ...")
        sys.exit(1)

    repo_urls = sys.argv[1:]
    for repo_url in repo_urls:
        print(f"\n🚀 Processing {repo_url} ...")
        run_agentic_pipeline(repo_url)

