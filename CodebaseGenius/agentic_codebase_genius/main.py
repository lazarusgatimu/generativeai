# main.py
import sys
from agent_core import CodebaseAgent

def run_agentic_pipeline(repo_url):
    agent = CodebaseAgent(repo_url)
    agent.run()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <repo_url>")
    else:
        run_agentic_pipeline(sys.argv[1])

