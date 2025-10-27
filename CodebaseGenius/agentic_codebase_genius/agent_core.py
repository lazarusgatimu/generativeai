import os
from repo_helpers import clone_repo, get_repo_map
from code_analyzer import analyze_codebase
from docgen import generate_markdown

class CodebaseAgent:
    def __init__(self, repo_url):
        self.repo_url = repo_url
        self.repo_name = os.path.splitext(os.path.basename(repo_url))[0]
        self.output_path = os.path.join("outputs", self.repo_name)

    def run(self):
        print(f"\n🚀 Running agent for {self.repo_name}...\n")

        repo_path = clone_repo(self.repo_url, self.repo_name)
        repo_map = get_repo_map(repo_path)
        code_summary = analyze_codebase(repo_path)
        generate_markdown(self.repo_name, repo_map, code_summary)

        print(f"✅ Documentation generated at {self.output_path}")
        self.reflect(self.output_path)
    def reflect(self, output_path):
        readme_path = os.path.join(output_path, "README.md")
        if not os.path.exists(readme_path):
            print(f"⚠️ No README.md found in {output_path}, skipping reflection.")
            return

        with open(readme_path, "r") as f:
            content = f.read()

        if len(content) < 200:
            print("⚠️ Output seems minimal — consider adding more analysis.")
        else:
            print("🧠 Reflection complete — documentation looks solid.")

