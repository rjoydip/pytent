# Pytent

[![ci](https://github.com/rjoydip/pytent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rjoydip/pytent/actions/workflows/ci.yml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org)
[![pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A project template with UV package manager and CI integration.

## 🚀 Features

- [UV](https://github.com/astral-sh/uv) - An extremely fast Python package and project manager, written in Rust.
- [Ruff](https://github.com/astral-sh/ruff) - An extremely fast Python linter and code formatter, written in Rust.
- [Pytest](https://github.com/pytest-dev/pytest) - The pytest framework makes it easy to write small tests, yet scales to support complex functional testing
- [Pyright](https://github.com/microsoft/pyright) - Static Type Checker for Python
- [uv-secure](https://github.com/owenlamont/uv-secure) - Scan your uv.lock file for dependencies with known vulnerabilities
- [pre-commit](https://github.com/pre-commit/pre-commit) - A framework for managing and maintaining multi-language pre-commit hooks
- [commitizen](https://github.com/commitizen-tools/commitizen) - Create committing rules for projects 🚀 auto bump versions ⬆️ and auto changelog generation 📂

## 📋 Prerequisites

- [Python >=3.12+](https://www.python.org/downloads) - Download the latest version
- [Docker Desktop](https://docs.docker.com/desktop) - Docker Desktop is a one-click-install
- [UV](https://github.com/astral-sh/uv) - An extremely fast Python package and project manager, written in Rust.

## 🛠 Installation

- Clone the repository:

-----

Install project dependencies:

```bash
uv sync --all-packages
```

- Ruff

```bash
uv tool install ruff
```

- Pyright

```bash
uv tool install pyright
```

- Pip Audit

```bash
uv tool install uv-secure
```

- Pre-commit

```bash
uv tool install pre-commit

uvx pre-commit install
```

- Commitizen

```bash
uv tool install commitizen
```

## Upgrade Tools

```bash
uv tool upgrade [...TOOL_NAMES]
```

## Development

### Local Development

- Audit package vulnerability

```bash
uvx uv-secure .
```

- Run Pre-commit against all the files

```bash
uvx pre-commit run --all-files
```

- Run code formatting and linting:

```bash
# local
uvx ruff check . --fix
# ci
uvx ruff check --output-format=json . > artifacts/ruff-output.json
```

- Run typechecking:

```bash
# local
uvx pyright .
# ci
uvx pyright . --outputjson > artifacts/pyright-output.json 2>&1
```

- Run tests:

```bash
# local
uv run pytest
# ci
uv run pytest --cov=packages --cov-report=json:artifacts/coverage.json
```

- Complexity Analysis

```bash
# local
uvx xenon .
# or
uvx xenon . --paths-in-front > artifacts/complexity-report.json
```

### Local application development

```bash
uv run servics/app
```

### Docker/Podman Development

Build and run the api in Docker:

```bash
docker build -t app .
docker run <IMAGE_NAME>

# Or
podman build -t app .
podman run <IMAGE_NAME>
```

## Commitizen Commands

| Command | Description | Alias |
|---------|-------------|-------|
| `cz commit` | Create a new commit | `cz c` |
| `cz bump` | Bump version and update changelog | - |
| `cz changelog` | Generate changelog | `cz ch` |
| `cz check` | Validate commit messages | - |
| `cz version` | Show version information | - |

## 🌐 API Endpoints

- `GET /`: Returns a "Hello from UV!" message

## 🧪 Testing

Tests are located in the `tests/` directory. Run the test suite using:

```bash
uv run pytest
```

## 🔍 Project Structure

```txt
pytent/
├─ .devcontainer/
│  └─ devcontainer.json
├─ .github/
│  ├─ actions/
│  │  └─ setup/
│  │     └─ action.yml
│  ├─ workflows/
│  │  ├─ ci.yml
│  │  └─ release.yml
│  └─ dependabot.yml
├─ artifacts/
│  └─ .gitkeep
├─ docs/
│  └─ .gitkeep
├─ packages/
│  ├─ database/
│  │  ├─ src/
│  │  │  └─ pytent_db/
│  │  │     ├─ __init__.py
│  │  │     ├─ base.py
│  │  │     ├─ connection.py
│  │  │     └─ session.py
│  │  └─ pyproject.toml
│  ├─ error/
│  │  ├─ src/
│  │  │  └─ pytent_error/
│  │  │     ├─ __init__.py
│  │  │     ├─ exceptions.py
│  │  │     └─ handler.py
│  │  └─ pyproject.toml
│  └─ log/
│     ├─ src/
│     │  └─ pytent_log/
│     │     ├─ __init__.py
│     │     └─ logger.py
│     └─ pyproject.toml
├─ scripts/
│  └─ .gitkeep
├─ services/
│  ├─ api/
│  │  ├─ tests/
│  │  │  └─ test_main.py
│  │  ├─ docker-compose.yml
│  │  ├─ Dockerfile
│  │  ├─ main.py
│  │  └─ pyproject.toml
│  └─ functions/
│     ├─ src/
│     │  └─ pytent.func.py
│     └─ pyproject.toml
├─ tests/
│  ├─ e2e/
│  │  └─ .gitkeep
│  ├─ fixtures/
│  │  └─ .gitkeep
│  └─ integration/
│     └─ .gitkeep
├─ tools/
│  ├─ deploy/
│  │  ├─ src/
│  │  │  └─ init.py
│  │  └─ pyproject.toml
│  └─ docgen/
│     ├─ src/
│     │  └─ init.py
│     └─ pyproject.toml
├─ .gitattributes
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .python-version
├─ .tool-versions
├─ CHANGELOG.md
├─ LICENSE
├─ pyproject.toml
├─ README.md
└─ uv.lock
```

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Released under [MIT](./LICENSE) by [@rjoydip](https://github.com/rjoydip).