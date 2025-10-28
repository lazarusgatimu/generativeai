#!/bin/bash

# File containing repository URLs
repo_file="repos.txt"

# Maximum number of parallel jobs
max_jobs=2

# Function to run a repository
run_repo() {
    local repo_url=$1
    python multi_repo.py "$repo_url"
}

# Export function for parallel
export -f run_repo

# Run each repository URL in parallel
cat $repo_file | xargs -n 1 -P $max_jobs -I {} bash -c 'run_repo "$@"' _ {}
echo "✅ All repositories have been processed!"
