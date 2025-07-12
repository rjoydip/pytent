FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create the working directory first
WORKDIR /app

# Copy the application into the container.
COPY ./services/app/*.py ./
COPY ./packages/ ./packages/
COPY ./pyproject.toml ./uv.lock ./

# Install the application dependencies.
RUN uv sync --no-cache

# Run the application.
CMD ["/app/.venv/bin/python", "-m", "main"]