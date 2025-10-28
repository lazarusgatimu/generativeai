import py_module docgen;

walker docgen_walker {
    has str repo_url;

    can generate_docs {
        std.out("Starting DocGenie for repo: " + self.repo_url);
        docgen.run_generate(self.repo_url);
        std.out("Documentation generation completed!");
    }
}

