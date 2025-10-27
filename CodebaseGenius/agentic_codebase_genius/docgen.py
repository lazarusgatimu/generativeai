# docgen.py
import os
import json

def generate_markdown(repo_name, repo_map, code_summary):
    output_path = os.path.join("outputs", repo_name)
    os.makedirs(output_path, exist_ok=True)
    readme_path = os.path.join(output_path, "README.md")

    with open(readme_path, "w") as f:
        f.write(f"# 🧩 Codebase Genius Report: {repo_name}\n\n")
        f.write("## 📁 Repository Structure\n")
        f.write("```\n")
        f.write(json.dumps(repo_map, indent=2))
        f.write("\n```\n\n")
        f.write("## 🧠 Code Analysis Summary\n")
        f.write("```\n")
        f.write(json.dumps(code_summary, indent=2))
        f.write("\n```\n")

    print(f"✅ Markdown documentation created at {readme_path}")
    return output_path

