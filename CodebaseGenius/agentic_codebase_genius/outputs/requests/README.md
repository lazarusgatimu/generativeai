# 🧩 Codebase Genius Report: requests

## 📁 Repository Structure
```
{
  ".": [
    ".coveragerc",
    ".git-blame-ignore-revs",
    ".gitignore",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "AUTHORS.rst",
    "HISTORY.md",
    "LICENSE",
    "Makefile",
    "MANIFEST.in",
    "NOTICE",
    "pyproject.toml",
    "README.md",
    "requirements-dev.txt",
    "setup.cfg",
    "setup.py",
    "tox.ini"
  ],
  ".github": [
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "dependabot.yml",
    "FUNDING.yml",
    "ISSUE_TEMPLATE.md",
    "SECURITY.md"
  ],
  ".github/ISSUE_TEMPLATE": [
    "Bug_report.md",
    "Custom.md",
    "Feature_request.md"
  ],
  ".github/workflows": [
    "close-issues.yml",
    "codeql-analysis.yml",
    "lint.yml",
    "lock-issues.yml",
    "publish.yml",
    "run-tests.yml"
  ],
  "docs": [
    ".nojekyll",
    "api.rst",
    "conf.py",
    "index.rst",
    "make.bat",
    "Makefile",
    "requirements.txt"
  ],
  "docs/community": [
    "faq.rst",
    "out-there.rst",
    "recommended.rst",
    "release-process.rst",
    "support.rst",
    "updates.rst",
    "vulnerabilities.rst"
  ],
  "docs/dev": [
    "authors.rst",
    "contributing.rst"
  ],
  "docs/user": [
    "advanced.rst",
    "authentication.rst",
    "install.rst",
    "quickstart.rst"
  ],
  "docs/_static": [
    "custom.css",
    "requests-sidebar.png"
  ],
  "docs/_templates": [
    "hacks.html",
    "sidebarintro.html",
    "sidebarlogo.html"
  ],
  "docs/_themes": [
    ".gitignore",
    "flask_theme_support.py",
    "LICENSE"
  ],
  "ext": [
    "flower-of-life.jpg",
    "kr-compressed.png",
    "kr.png",
    "LICENSE",
    "psf-compressed.png",
    "psf.png",
    "requests-logo-compressed.png",
    "requests-logo.ai",
    "requests-logo.png",
    "requests-logo.svg",
    "ss-compressed.png",
    "ss.png"
  ],
  "src": [],
  "src/requests": [
    "adapters.py",
    "api.py",
    "auth.py",
    "certs.py",
    "compat.py",
    "cookies.py",
    "exceptions.py",
    "help.py",
    "hooks.py",
    "models.py",
    "packages.py",
    "sessions.py",
    "status_codes.py",
    "structures.py",
    "utils.py",
    "_internal_utils.py",
    "__init__.py",
    "__version__.py"
  ],
  "tests": [
    "compat.py",
    "conftest.py",
    "test_adapters.py",
    "test_help.py",
    "test_hooks.py",
    "test_lowlevel.py",
    "test_packages.py",
    "test_requests.py",
    "test_structures.py",
    "test_testserver.py",
    "test_utils.py",
    "utils.py",
    "__init__.py"
  ],
  "tests/certs": [
    "README.md"
  ],
  "tests/certs/expired": [
    "Makefile",
    "README.md"
  ],
  "tests/certs/expired/ca": [
    "ca-private.key",
    "ca.cnf",
    "ca.crt",
    "ca.srl",
    "Makefile"
  ],
  "tests/certs/expired/server": [
    "cert.cnf",
    "Makefile",
    "server.csr",
    "server.key",
    "server.pem"
  ],
  "tests/certs/mtls": [
    "Makefile",
    "README.md"
  ],
  "tests/certs/mtls/client": [
    "cert.cnf",
    "client.csr",
    "client.key",
    "client.pem",
    "Makefile"
  ],
  "tests/certs/valid": [],
  "tests/certs/valid/server": [
    "cert.cnf",
    "Makefile",
    "server.csr",
    "server.key",
    "server.pem"
  ],
  "tests/testserver": [
    "server.py",
    "__init__.py"
  ]
}
```

## 🧠 Code Analysis Summary
```
{
  ".": {
    "folders": [
      ".git",
      ".github",
      "docs",
      "ext",
      "src",
      "tests"
    ],
    "files": [
      ".coveragerc",
      ".git-blame-ignore-revs",
      ".gitignore",
      ".pre-commit-config.yaml",
      ".readthedocs.yaml",
      "AUTHORS.rst",
      "HISTORY.md",
      "LICENSE",
      "Makefile",
      "MANIFEST.in",
      "NOTICE",
      "pyproject.toml",
      "README.md",
      "requirements-dev.txt",
      "setup.cfg",
      "setup.py",
      "tox.ini"
    ]
  },
  ".git": {
    "folders": [
      "branches",
      "hooks",
      "info",
      "logs",
      "objects",
      "refs"
    ],
    "files": [
      "config",
      "description",
      "HEAD",
      "index",
      "packed-refs"
    ]
  },
  ".git/branches": {
    "folders": [],
    "files": []
  },
  ".git/hooks": {
    "folders": [],
    "files": [
      "applypatch-msg.sample",
      "commit-msg.sample",
      "fsmonitor-watchman.sample",
      "post-update.sample",
      "pre-applypatch.sample",
      "pre-commit.sample",
      "pre-merge-commit.sample",
      "pre-push.sample",
      "pre-rebase.sample",
      "pre-receive.sample",
      "prepare-commit-msg.sample",
      "push-to-checkout.sample",
      "sendemail-validate.sample",
      "update.sample"
    ]
  },
  ".git/info": {
    "folders": [],
    "files": [
      "exclude"
    ]
  },
  ".git/logs": {
    "folders": [
      "refs"
    ],
    "files": [
      "HEAD"
    ]
  },
  ".git/logs/refs": {
    "folders": [
      "heads",
      "remotes"
    ],
    "files": []
  },
  ".git/logs/refs/heads": {
    "folders": [],
    "files": [
      "main"
    ]
  },
  ".git/logs/refs/remotes": {
    "folders": [
      "origin"
    ],
    "files": []
  },
  ".git/logs/refs/remotes/origin": {
    "folders": [],
    "files": [
      "HEAD"
    ]
  },
  ".git/objects": {
    "folders": [
      "info",
      "pack"
    ],
    "files": []
  },
  ".git/objects/info": {
    "folders": [],
    "files": []
  },
  ".git/objects/pack": {
    "folders": [],
    "files": [
      "pack-c2159601159538d7e7caf19a2127b619d8389d03.idx",
      "pack-c2159601159538d7e7caf19a2127b619d8389d03.pack",
      "pack-c2159601159538d7e7caf19a2127b619d8389d03.rev"
    ]
  },
  ".git/refs": {
    "folders": [
      "heads",
      "remotes",
      "tags"
    ],
    "files": []
  },
  ".git/refs/heads": {
    "folders": [],
    "files": [
      "main"
    ]
  },
  ".git/refs/remotes": {
    "folders": [
      "origin"
    ],
    "files": []
  },
  ".git/refs/remotes/origin": {
    "folders": [],
    "files": [
      "HEAD"
    ]
  },
  ".git/refs/tags": {
    "folders": [],
    "files": []
  },
  ".github": {
    "folders": [
      "ISSUE_TEMPLATE",
      "workflows"
    ],
    "files": [
      "CODE_OF_CONDUCT.md",
      "CONTRIBUTING.md",
      "dependabot.yml",
      "FUNDING.yml",
      "ISSUE_TEMPLATE.md",
      "SECURITY.md"
    ]
  },
  ".github/ISSUE_TEMPLATE": {
    "folders": [],
    "files": [
      "Bug_report.md",
      "Custom.md",
      "Feature_request.md"
    ]
  },
  ".github/workflows": {
    "folders": [],
    "files": [
      "close-issues.yml",
      "codeql-analysis.yml",
      "lint.yml",
      "lock-issues.yml",
      "publish.yml",
      "run-tests.yml"
    ]
  },
  "docs": {
    "folders": [
      "community",
      "dev",
      "user",
      "_static",
      "_templates",
      "_themes"
    ],
    "files": [
      ".nojekyll",
      "api.rst",
      "conf.py",
      "index.rst",
      "make.bat",
      "Makefile",
      "requirements.txt"
    ]
  },
  "docs/community": {
    "folders": [],
    "files": [
      "faq.rst",
      "out-there.rst",
      "recommended.rst",
      "release-process.rst",
      "support.rst",
      "updates.rst",
      "vulnerabilities.rst"
    ]
  },
  "docs/dev": {
    "folders": [],
    "files": [
      "authors.rst",
      "contributing.rst"
    ]
  },
  "docs/user": {
    "folders": [],
    "files": [
      "advanced.rst",
      "authentication.rst",
      "install.rst",
      "quickstart.rst"
    ]
  },
  "docs/_static": {
    "folders": [],
    "files": [
      "custom.css",
      "requests-sidebar.png"
    ]
  },
  "docs/_templates": {
    "folders": [],
    "files": [
      "hacks.html",
      "sidebarintro.html",
      "sidebarlogo.html"
    ]
  },
  "docs/_themes": {
    "folders": [],
    "files": [
      ".gitignore",
      "flask_theme_support.py",
      "LICENSE"
    ]
  },
  "ext": {
    "folders": [],
    "files": [
      "flower-of-life.jpg",
      "kr-compressed.png",
      "kr.png",
      "LICENSE",
      "psf-compressed.png",
      "psf.png",
      "requests-logo-compressed.png",
      "requests-logo.ai",
      "requests-logo.png",
      "requests-logo.svg",
      "ss-compressed.png",
      "ss.png"
    ]
  },
  "src": {
    "folders": [
      "requests"
    ],
    "files": []
  },
  "src/requests": {
    "folders": [],
    "files": [
      "adapters.py",
      "api.py",
      "auth.py",
      "certs.py",
      "compat.py",
      "cookies.py",
      "exceptions.py",
      "help.py",
      "hooks.py",
      "models.py",
      "packages.py",
      "sessions.py",
      "status_codes.py",
      "structures.py",
      "utils.py",
      "_internal_utils.py",
      "__init__.py",
      "__version__.py"
    ]
  },
  "tests": {
    "folders": [
      "certs",
      "testserver"
    ],
    "files": [
      "compat.py",
      "conftest.py",
      "test_adapters.py",
      "test_help.py",
      "test_hooks.py",
      "test_lowlevel.py",
      "test_packages.py",
      "test_requests.py",
      "test_structures.py",
      "test_testserver.py",
      "test_utils.py",
      "utils.py",
      "__init__.py"
    ]
  },
  "tests/certs": {
    "folders": [
      "expired",
      "mtls",
      "valid"
    ],
    "files": [
      "README.md"
    ]
  },
  "tests/certs/expired": {
    "folders": [
      "ca",
      "server"
    ],
    "files": [
      "Makefile",
      "README.md"
    ]
  },
  "tests/certs/expired/ca": {
    "folders": [],
    "files": [
      "ca-private.key",
      "ca.cnf",
      "ca.crt",
      "ca.srl",
      "Makefile"
    ]
  },
  "tests/certs/expired/server": {
    "folders": [],
    "files": [
      "cert.cnf",
      "Makefile",
      "server.csr",
      "server.key",
      "server.pem"
    ]
  },
  "tests/certs/mtls": {
    "folders": [
      "client"
    ],
    "files": [
      "Makefile",
      "README.md"
    ]
  },
  "tests/certs/mtls/client": {
    "folders": [
      "ca"
    ],
    "files": [
      "cert.cnf",
      "client.csr",
      "client.key",
      "client.pem",
      "Makefile"
    ]
  },
  "tests/certs/valid": {
    "folders": [
      "ca",
      "server"
    ],
    "files": []
  },
  "tests/certs/valid/server": {
    "folders": [],
    "files": [
      "cert.cnf",
      "Makefile",
      "server.csr",
      "server.key",
      "server.pem"
    ]
  },
  "tests/testserver": {
    "folders": [],
    "files": [
      "server.py",
      "__init__.py"
    ]
  }
}
```
