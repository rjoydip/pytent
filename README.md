# Pytent

[![ci](https://github.com/rjoydip/pytent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rjoydip/pytent/actions/workflows/ci.yml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=flat-square)](https://conventionalcommits.org)
[![pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A monorepo project template with UV package manager and CI integration.

## 🚀 Features

- UV package manager
- Docker support
- Ruff for code formatting and linting
- Pytest for testing

## 📋 Prerequisites

- Python 3.12+
- Docker Desktop
- UV

## 🛠 Installation

- Clone the repository:

-----

Install project dependencies:

```bash
uv sync --all-packages
```

- Ruff

```bash
# Install Ruff
uv tool install ruff
```

- Pyright

```bash
# Install Pyright
uv tool install pyright
```

- Pip Audit

```bash
# Install Pyright
uv tool install pip-audit
```

- Pre-commit

```bash
# Install Pre-commit
uv tool install pre-commit

uvx pre-commit install
```

- Commitizen

```bash
# Install commitizen
uv tool install commitizen
```

## Upgrade Tools

```bash
uv tool upgrade [...TOOL_NAMES]
```

## Development

### Local Development

- Build modules:

```bash
uv build --all-packages
```

- Audit package vulnerability

```bash
uvx pip-audit -l
```

- Run Pre-commit against all the files

```bash
uvx pre-commit run --all-files
```

- Run code formatting and linting:

```bash
# Formatting
uvx ruff format .
# Linting check
uvx ruff check --output-format=json . > artifacts/ruff-output.json
```

- Run typechecking:

```bash
uvx pyright . --outputjson > artifacts/pyright-output.json 2>&1
```

- Run tests:

```bash
uv run pytest --cov=packages --cov-report=json:artifacts/coverage.json
```

- Complexity Analysis

```bash
uv run xenon . --paths-in-front > artifacts/complexity-report.json
```

### Local application development

```bash
cd services/api
uv run uvicorn main:app --port 8000 --reload
```

### Docker Development

Build and run the api in Docker:

```bash
docker build -t api .
docker run -p 8000:8000 api
```

## Commitizen Commands

| Command | Description | Alias |
|---------|-------------|-------|
| `cz init` | Initialize Commitizen configuration | - |
| `cz commit` | Create a new commit | `cz c` |
| `cz bump` | Bump version and update changelog | - |
| `cz changelog` | Generate changelog | `cz ch` |
| `cz check` | Validate commit messages | - |
| `cz version` | Show version information | - |

## ⚙️ Configuration

- Project dependencies and settings are managed in `pyproject.toml`
- Ruff is configured for code formatting and linting
- Pytest is set up for testing
- Logging configuration is available for different environments

## 🌐 API Endpoints

- `GET /`: Returns a "Hello from UV!" message

## 🧪 Testing

Tests are located in the `tests/` directory. Run the test suite using:

```bash
uv run pytest
```

## 🔍 Project Structure

```txt
python-monorepo-starter/
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
