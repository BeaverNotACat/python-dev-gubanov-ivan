format:
	uv run ruff format
	uv run ruff check --fix

lint:
	uv run ruff check
	uv run mypy .

migrate:
	uv run alembic --name app upgrade head
	uv run alembic --name logs upgrade head

make-migrations: make-app-migrations make-logs-migrations

make-app-migrations:
	uv run alembic --name app revision --autogenerate -m ${description}

make-logs-migrations:
	uv run alembic --name logs revision --autogenerate -m ${description}

run:
	uv run granian --interface asgi src/api/app.py --reload --log --access-log --host 0.0.0.0

test:
	uv run pytest
