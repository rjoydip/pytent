# Pytent

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![image](https://img.shields.io/pypi/v/uv.svg)](https://pypi.python.org/pypi/uv)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![CI](https://github.com/rjoydip/pytent/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rjoydip/pytent/actions/workflows/ci.yml)

A monorepo project template with UV package manager and CI integration.

## 🚀 Features

- UV package manager
- Docker support
- Ruff for code formatting and linting
- Pytest for testing

## 📋 Prerequisites

- Python 3.13+
- Docker Desktop
- UV

## 🛠 Installation

1. Clone the repository:

-----

Install project dependencies:

```bash
uv sync --all-packages
```

## Development

### Local Development

- Build modules:

```bash
uv build --all-packages
```

- Audit package vulnerability

```bash
uv run --all-groups --with pip-audit pip-audit -l
```

- Run UV application locally:

```bash
cd services/api
uv run uvicorn main:app --port 8000 --reload
```

- Run code formatting and linting:

```bash
uv run ruff format .
# or
uv run ruff check --fix
```

- Run typechecking:

```bash
uv run pyright
```

- Run tests:

```bash
uv run pytest
```

### Docker Development

Build and run the api in Docker:

```bash
docker build -t api .
docker run -p 8000:8000 api
```

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
│  └─ README.md
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
│  ├─ build.py
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
│  ├─ codegen/
│  │  ├─ src/
│  │  │  └─ init.py
│  │  └─ pyproject.toml
│  └─ deploy/
│     ├─ src/
│     │  └─ init.py
│     └─ pyproject.toml
├─ .coverage
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .python-version
├─ .tool-versions
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
