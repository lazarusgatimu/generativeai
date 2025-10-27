# 🧩 Codebase Genius Report: flask

## 📁 Repository Structure
```
{
  ".": [
    ".editorconfig",
    ".gitignore",
    ".pre-commit-config.yaml",
    ".readthedocs.yaml",
    "CHANGES.rst",
    "LICENSE.txt",
    "pyproject.toml",
    "README.md",
    "uv.lock"
  ],
  ".devcontainer": [
    "devcontainer.json",
    "on-create-command.sh"
  ],
  ".github": [
    "pull_request_template.md"
  ],
  ".github/ISSUE_TEMPLATE": [
    "bug-report.md",
    "config.yml",
    "feature-request.md"
  ],
  ".github/workflows": [
    "lock.yaml",
    "pre-commit.yaml",
    "publish.yaml",
    "tests.yaml"
  ],
  "docs": [
    "api.rst",
    "appcontext.rst",
    "async-await.rst",
    "blueprints.rst",
    "changes.rst",
    "cli.rst",
    "conf.py",
    "config.rst",
    "contributing.rst",
    "debugging.rst",
    "design.rst",
    "errorhandling.rst",
    "extensiondev.rst",
    "extensions.rst",
    "index.rst",
    "installation.rst",
    "license.rst",
    "lifecycle.rst",
    "logging.rst",
    "make.bat",
    "Makefile",
    "quickstart.rst",
    "reqcontext.rst",
    "server.rst",
    "shell.rst",
    "signals.rst",
    "templating.rst",
    "testing.rst",
    "views.rst",
    "web-security.rst"
  ],
  "docs/deploying": [
    "apache-httpd.rst",
    "asgi.rst",
    "eventlet.rst",
    "gevent.rst",
    "gunicorn.rst",
    "index.rst",
    "mod_wsgi.rst",
    "nginx.rst",
    "proxy_fix.rst",
    "uwsgi.rst",
    "waitress.rst"
  ],
  "docs/patterns": [
    "appdispatch.rst",
    "appfactories.rst",
    "caching.rst",
    "celery.rst",
    "deferredcallbacks.rst",
    "favicon.rst",
    "fileuploads.rst",
    "flashing.rst",
    "index.rst",
    "javascript.rst",
    "jquery.rst",
    "lazyloading.rst",
    "methodoverrides.rst",
    "mongoengine.rst",
    "packages.rst",
    "requestchecksum.rst",
    "singlepageapplications.rst",
    "sqlalchemy.rst",
    "sqlite3.rst",
    "streaming.rst",
    "subclassing.rst",
    "templateinheritance.rst",
    "urlprocessors.rst",
    "viewdecorators.rst",
    "wtforms.rst"
  ],
  "docs/tutorial": [
    "blog.rst",
    "database.rst",
    "deploy.rst",
    "factory.rst",
    "flaskr_edit.png",
    "flaskr_index.png",
    "flaskr_login.png",
    "index.rst",
    "install.rst",
    "layout.rst",
    "next.rst",
    "static.rst",
    "templates.rst",
    "tests.rst",
    "views.rst"
  ],
  "docs/_static": [
    "debugger.png",
    "flask-icon.svg",
    "flask-logo.svg",
    "flask-name.svg",
    "pycharm-run-config.png"
  ],
  "examples": [],
  "examples/celery": [
    "make_celery.py",
    "pyproject.toml",
    "README.md",
    "requirements.txt"
  ],
  "examples/celery/src": [],
  "examples/celery/src/task_app": [
    "tasks.py",
    "views.py",
    "__init__.py"
  ],
  "examples/celery/src/task_app/templates": [
    "index.html"
  ],
  "examples/javascript": [
    ".gitignore",
    "LICENSE.txt",
    "pyproject.toml",
    "README.rst"
  ],
  "examples/javascript/js_example": [
    "views.py",
    "__init__.py"
  ],
  "examples/javascript/js_example/templates": [
    "base.html",
    "fetch.html",
    "jquery.html",
    "xhr.html"
  ],
  "examples/javascript/tests": [
    "conftest.py",
    "test_js_example.py"
  ],
  "examples/tutorial": [
    ".gitignore",
    "LICENSE.txt",
    "pyproject.toml",
    "README.rst"
  ],
  "examples/tutorial/flaskr": [
    "auth.py",
    "blog.py",
    "db.py",
    "schema.sql",
    "__init__.py"
  ],
  "examples/tutorial/flaskr/static": [
    "style.css"
  ],
  "examples/tutorial/flaskr/templates": [
    "base.html"
  ],
  "examples/tutorial/flaskr/templates/auth": [
    "login.html",
    "register.html"
  ],
  "examples/tutorial/flaskr/templates/blog": [
    "create.html",
    "index.html",
    "update.html"
  ],
  "examples/tutorial/tests": [
    "conftest.py",
    "data.sql",
    "test_auth.py",
    "test_blog.py",
    "test_db.py",
    "test_factory.py"
  ],
  "src": [],
  "src/flask": [
    "app.py",
    "blueprints.py",
    "cli.py",
    "config.py",
    "ctx.py",
    "debughelpers.py",
    "globals.py",
    "helpers.py",
    "logging.py",
    "py.typed",
    "sessions.py",
    "signals.py",
    "templating.py",
    "testing.py",
    "typing.py",
    "views.py",
    "wrappers.py",
    "__init__.py",
    "__main__.py"
  ],
  "src/flask/json": [
    "provider.py",
    "tag.py",
    "__init__.py"
  ],
  "src/flask/sansio": [
    "app.py",
    "blueprints.py",
    "README.md",
    "scaffold.py"
  ],
  "tests": [
    "conftest.py",
    "test_appctx.py",
    "test_async.py",
    "test_basic.py",
    "test_blueprints.py",
    "test_cli.py",
    "test_config.py",
    "test_converters.py",
    "test_helpers.py",
    "test_instance_config.py",
    "test_json.py",
    "test_json_tag.py",
    "test_logging.py",
    "test_regression.py",
    "test_reqctx.py",
    "test_request.py",
    "test_session_interface.py",
    "test_signals.py",
    "test_subclassing.py",
    "test_templating.py",
    "test_testing.py",
    "test_user_error_handler.py",
    "test_views.py"
  ],
  "tests/static": [
    "config.json",
    "config.toml",
    "index.html"
  ],
  "tests/templates": [
    "context_template.html",
    "escaping_template.html",
    "mail.txt",
    "non_escaping_template.txt",
    "simple_template.html",
    "template_filter.html",
    "template_test.html",
    "_macro.html"
  ],
  "tests/templates/nested": [
    "nested.txt"
  ],
  "tests/test_apps": [
    ".env",
    ".flaskenv"
  ],
  "tests/test_apps/blueprintapp": [
    "__init__.py"
  ],
  "tests/test_apps/blueprintapp/apps": [
    "__init__.py"
  ],
  "tests/test_apps/blueprintapp/apps/admin": [
    "__init__.py"
  ],
  "tests/test_apps/blueprintapp/apps/admin/static": [
    "test.txt"
  ],
  "tests/test_apps/blueprintapp/apps/admin/static/css": [
    "test.css"
  ],
  "tests/test_apps/blueprintapp/apps/admin/templates": [],
  "tests/test_apps/blueprintapp/apps/admin/templates/admin": [
    "index.html"
  ],
  "tests/test_apps/blueprintapp/apps/frontend": [
    "__init__.py"
  ],
  "tests/test_apps/blueprintapp/apps/frontend/templates": [],
  "tests/test_apps/blueprintapp/apps/frontend/templates/frontend": [
    "index.html"
  ],
  "tests/test_apps/cliapp": [
    "app.py",
    "factory.py",
    "importerrorapp.py",
    "message.txt",
    "multiapp.py",
    "__init__.py"
  ],
  "tests/test_apps/cliapp/inner1": [
    "__init__.py"
  ],
  "tests/test_apps/cliapp/inner1/inner2": [
    "flask.py",
    "__init__.py"
  ],
  "tests/test_apps/helloworld": [
    "hello.py",
    "wsgi.py"
  ],
  "tests/test_apps/subdomaintestmodule": [
    "__init__.py"
  ],
  "tests/test_apps/subdomaintestmodule/static": [
    "hello.txt"
  ],
  "tests/type_check": [
    "typing_app_decorators.py",
    "typing_error_handler.py",
    "typing_route.py"
  ]
}
```

## 🧠 Code Analysis Summary
```
{
  ".": {
    "folders": [
      ".devcontainer",
      ".git",
      ".github",
      "docs",
      "examples",
      "src",
      "tests"
    ],
    "files": [
      ".editorconfig",
      ".gitignore",
      ".pre-commit-config.yaml",
      ".readthedocs.yaml",
      "CHANGES.rst",
      "LICENSE.txt",
      "pyproject.toml",
      "README.md",
      "uv.lock"
    ]
  },
  ".devcontainer": {
    "folders": [],
    "files": [
      "devcontainer.json",
      "on-create-command.sh"
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
      "pack-8a4b58a031d55241b781a9d3e8f9a35605e4438a.idx",
      "pack-8a4b58a031d55241b781a9d3e8f9a35605e4438a.pack",
      "pack-8a4b58a031d55241b781a9d3e8f9a35605e4438a.rev"
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
      "pull_request_template.md"
    ]
  },
  ".github/ISSUE_TEMPLATE": {
    "folders": [],
    "files": [
      "bug-report.md",
      "config.yml",
      "feature-request.md"
    ]
  },
  ".github/workflows": {
    "folders": [],
    "files": [
      "lock.yaml",
      "pre-commit.yaml",
      "publish.yaml",
      "tests.yaml"
    ]
  },
  "docs": {
    "folders": [
      "deploying",
      "patterns",
      "tutorial",
      "_static"
    ],
    "files": [
      "api.rst",
      "appcontext.rst",
      "async-await.rst",
      "blueprints.rst",
      "changes.rst",
      "cli.rst",
      "conf.py",
      "config.rst",
      "contributing.rst",
      "debugging.rst",
      "design.rst",
      "errorhandling.rst",
      "extensiondev.rst",
      "extensions.rst",
      "index.rst",
      "installation.rst",
      "license.rst",
      "lifecycle.rst",
      "logging.rst",
      "make.bat",
      "Makefile",
      "quickstart.rst",
      "reqcontext.rst",
      "server.rst",
      "shell.rst",
      "signals.rst",
      "templating.rst",
      "testing.rst",
      "views.rst",
      "web-security.rst"
    ]
  },
  "docs/deploying": {
    "folders": [],
    "files": [
      "apache-httpd.rst",
      "asgi.rst",
      "eventlet.rst",
      "gevent.rst",
      "gunicorn.rst",
      "index.rst",
      "mod_wsgi.rst",
      "nginx.rst",
      "proxy_fix.rst",
      "uwsgi.rst",
      "waitress.rst"
    ]
  },
  "docs/patterns": {
    "folders": [],
    "files": [
      "appdispatch.rst",
      "appfactories.rst",
      "caching.rst",
      "celery.rst",
      "deferredcallbacks.rst",
      "favicon.rst",
      "fileuploads.rst",
      "flashing.rst",
      "index.rst",
      "javascript.rst",
      "jquery.rst",
      "lazyloading.rst",
      "methodoverrides.rst",
      "mongoengine.rst",
      "packages.rst",
      "requestchecksum.rst",
      "singlepageapplications.rst",
      "sqlalchemy.rst",
      "sqlite3.rst",
      "streaming.rst",
      "subclassing.rst",
      "templateinheritance.rst",
      "urlprocessors.rst",
      "viewdecorators.rst",
      "wtforms.rst"
    ]
  },
  "docs/tutorial": {
    "folders": [],
    "files": [
      "blog.rst",
      "database.rst",
      "deploy.rst",
      "factory.rst",
      "flaskr_edit.png",
      "flaskr_index.png",
      "flaskr_login.png",
      "index.rst",
      "install.rst",
      "layout.rst",
      "next.rst",
      "static.rst",
      "templates.rst",
      "tests.rst",
      "views.rst"
    ]
  },
  "docs/_static": {
    "folders": [],
    "files": [
      "debugger.png",
      "flask-icon.svg",
      "flask-logo.svg",
      "flask-name.svg",
      "pycharm-run-config.png"
    ]
  },
  "examples": {
    "folders": [
      "celery",
      "javascript",
      "tutorial"
    ],
    "files": []
  },
  "examples/celery": {
    "folders": [
      "src"
    ],
    "files": [
      "make_celery.py",
      "pyproject.toml",
      "README.md",
      "requirements.txt"
    ]
  },
  "examples/celery/src": {
    "folders": [
      "task_app"
    ],
    "files": []
  },
  "examples/celery/src/task_app": {
    "folders": [
      "templates"
    ],
    "files": [
      "tasks.py",
      "views.py",
      "__init__.py"
    ]
  },
  "examples/celery/src/task_app/templates": {
    "folders": [],
    "files": [
      "index.html"
    ]
  },
  "examples/javascript": {
    "folders": [
      "js_example",
      "tests"
    ],
    "files": [
      ".gitignore",
      "LICENSE.txt",
      "pyproject.toml",
      "README.rst"
    ]
  },
  "examples/javascript/js_example": {
    "folders": [
      "templates"
    ],
    "files": [
      "views.py",
      "__init__.py"
    ]
  },
  "examples/javascript/js_example/templates": {
    "folders": [],
    "files": [
      "base.html",
      "fetch.html",
      "jquery.html",
      "xhr.html"
    ]
  },
  "examples/javascript/tests": {
    "folders": [],
    "files": [
      "conftest.py",
      "test_js_example.py"
    ]
  },
  "examples/tutorial": {
    "folders": [
      "flaskr",
      "tests"
    ],
    "files": [
      ".gitignore",
      "LICENSE.txt",
      "pyproject.toml",
      "README.rst"
    ]
  },
  "examples/tutorial/flaskr": {
    "folders": [
      "static",
      "templates"
    ],
    "files": [
      "auth.py",
      "blog.py",
      "db.py",
      "schema.sql",
      "__init__.py"
    ]
  },
  "examples/tutorial/flaskr/static": {
    "folders": [],
    "files": [
      "style.css"
    ]
  },
  "examples/tutorial/flaskr/templates": {
    "folders": [
      "auth",
      "blog"
    ],
    "files": [
      "base.html"
    ]
  },
  "examples/tutorial/flaskr/templates/auth": {
    "folders": [],
    "files": [
      "login.html",
      "register.html"
    ]
  },
  "examples/tutorial/flaskr/templates/blog": {
    "folders": [],
    "files": [
      "create.html",
      "index.html",
      "update.html"
    ]
  },
  "examples/tutorial/tests": {
    "folders": [],
    "files": [
      "conftest.py",
      "data.sql",
      "test_auth.py",
      "test_blog.py",
      "test_db.py",
      "test_factory.py"
    ]
  },
  "src": {
    "folders": [
      "flask"
    ],
    "files": []
  },
  "src/flask": {
    "folders": [
      "json",
      "sansio"
    ],
    "files": [
      "app.py",
      "blueprints.py",
      "cli.py",
      "config.py",
      "ctx.py",
      "debughelpers.py",
      "globals.py",
      "helpers.py",
      "logging.py",
      "py.typed",
      "sessions.py",
      "signals.py",
      "templating.py",
      "testing.py",
      "typing.py",
      "views.py",
      "wrappers.py",
      "__init__.py",
      "__main__.py"
    ]
  },
  "src/flask/json": {
    "folders": [],
    "files": [
      "provider.py",
      "tag.py",
      "__init__.py"
    ]
  },
  "src/flask/sansio": {
    "folders": [],
    "files": [
      "app.py",
      "blueprints.py",
      "README.md",
      "scaffold.py"
    ]
  },
  "tests": {
    "folders": [
      "static",
      "templates",
      "test_apps",
      "type_check"
    ],
    "files": [
      "conftest.py",
      "test_appctx.py",
      "test_async.py",
      "test_basic.py",
      "test_blueprints.py",
      "test_cli.py",
      "test_config.py",
      "test_converters.py",
      "test_helpers.py",
      "test_instance_config.py",
      "test_json.py",
      "test_json_tag.py",
      "test_logging.py",
      "test_regression.py",
      "test_reqctx.py",
      "test_request.py",
      "test_session_interface.py",
      "test_signals.py",
      "test_subclassing.py",
      "test_templating.py",
      "test_testing.py",
      "test_user_error_handler.py",
      "test_views.py"
    ]
  },
  "tests/static": {
    "folders": [],
    "files": [
      "config.json",
      "config.toml",
      "index.html"
    ]
  },
  "tests/templates": {
    "folders": [
      "nested"
    ],
    "files": [
      "context_template.html",
      "escaping_template.html",
      "mail.txt",
      "non_escaping_template.txt",
      "simple_template.html",
      "template_filter.html",
      "template_test.html",
      "_macro.html"
    ]
  },
  "tests/templates/nested": {
    "folders": [],
    "files": [
      "nested.txt"
    ]
  },
  "tests/test_apps": {
    "folders": [
      "blueprintapp",
      "cliapp",
      "helloworld",
      "subdomaintestmodule"
    ],
    "files": [
      ".env",
      ".flaskenv"
    ]
  },
  "tests/test_apps/blueprintapp": {
    "folders": [
      "apps"
    ],
    "files": [
      "__init__.py"
    ]
  },
  "tests/test_apps/blueprintapp/apps": {
    "folders": [
      "admin",
      "frontend"
    ],
    "files": [
      "__init__.py"
    ]
  },
  "tests/test_apps/blueprintapp/apps/admin": {
    "folders": [
      "static",
      "templates"
    ],
    "files": [
      "__init__.py"
    ]
  },
  "tests/test_apps/blueprintapp/apps/admin/static": {
    "folders": [
      "css"
    ],
    "files": [
      "test.txt"
    ]
  },
  "tests/test_apps/blueprintapp/apps/admin/static/css": {
    "folders": [],
    "files": [
      "test.css"
    ]
  },
  "tests/test_apps/blueprintapp/apps/admin/templates": {
    "folders": [
      "admin"
    ],
    "files": []
  },
  "tests/test_apps/blueprintapp/apps/admin/templates/admin": {
    "folders": [],
    "files": [
      "index.html"
    ]
  },
  "tests/test_apps/blueprintapp/apps/frontend": {
    "folders": [
      "templates"
    ],
    "files": [
      "__init__.py"
    ]
  },
  "tests/test_apps/blueprintapp/apps/frontend/templates": {
    "folders": [
      "frontend"
    ],
    "files": []
  },
  "tests/test_apps/blueprintapp/apps/frontend/templates/frontend": {
    "folders": [],
    "files": [
      "index.html"
    ]
  },
  "tests/test_apps/cliapp": {
    "folders": [
      "inner1"
    ],
    "files": [
      "app.py",
      "factory.py",
      "importerrorapp.py",
      "message.txt",
      "multiapp.py",
      "__init__.py"
    ]
  },
  "tests/test_apps/cliapp/inner1": {
    "folders": [
      "inner2"
    ],
    "files": [
      "__init__.py"
    ]
  },
  "tests/test_apps/cliapp/inner1/inner2": {
    "folders": [],
    "files": [
      "flask.py",
      "__init__.py"
    ]
  },
  "tests/test_apps/helloworld": {
    "folders": [],
    "files": [
      "hello.py",
      "wsgi.py"
    ]
  },
  "tests/test_apps/subdomaintestmodule": {
    "folders": [
      "static"
    ],
    "files": [
      "__init__.py"
    ]
  },
  "tests/test_apps/subdomaintestmodule/static": {
    "folders": [],
    "files": [
      "hello.txt"
    ]
  },
  "tests/type_check": {
    "folders": [],
    "files": [
      "typing_app_decorators.py",
      "typing_error_handler.py",
      "typing_route.py"
    ]
  }
}
```
