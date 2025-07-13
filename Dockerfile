FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create the working directory first
WORKDIR /app

# Copy the application into the container.
COPY ./services/api/*.py ./
COPY ./packages/ ./packages/
COPY ./pyproject.toml ./uv.lock ./

# Install the application dependencies.
RUN uv sync --no-cache

ENV PATH="/app/.venv/bin:$PATH"

# Run the application.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]