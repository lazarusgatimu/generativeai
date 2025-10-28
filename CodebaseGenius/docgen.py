def generate_markdown(repo_name, repo_map=None, code_summary=None):
    if repo_map is None:
        print("⚠️ repo_map is None")
        return

    print("✅ repo_map exists:")
    print(repo_map)

    output = f"# Documentation for {repo_name}\n\n"

    if repo_map:
        output += "## Repository Structure\n"
        for folder, files in repo_map.items():
            output += f"### {folder}\n"
            for f in files:
                output += f"- {f}\n"
        output += "\n"

    if code_summary:
        output += "## Code Summary\n"
        output += f"{code_summary}\n"

    # Save to file
    import os
    os.makedirs(f"outputs/{repo_name}", exist_ok=True)
    with open(f"outputs/{repo_name}/README.md", "w") as f:
        f.write(output)

    print(f"✅ Markdown documentation created for {repo_name}")


