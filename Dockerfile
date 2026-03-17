FROM ghcr.io/astral-sh/uv:alpine AS base

WORKDIR /app

COPY pyproject.toml uv.lock .python-version .
RUN	uv sync --frozen

COPY . .

FROM base AS dev
RUN uv sync --frozen --dev
ENV DEBUG=True
CMD ["uv", "run", "granian", "--interface", "asgi", "src/api/app.py", "--reload", "--log", "--access-log", "--host", "0.0.0.0"]

FROM base AS prod
CMD ["uv", "run", "granian", "--interface", "asgi", "src/api/app.py", "--host", "0.0.0.0"]

