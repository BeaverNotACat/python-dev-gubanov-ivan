import asyncio

import rich_click as click

from src.cli.mocks import mock_app, mock_logs


@click.group()
def cli() -> None: ...


@cli.command()
@click.option("--count", "-c", default=1000)
def mock_app_database(count: int) -> None:
    asyncio.run(mock_app(count))


@cli.command()
@click.option("--count", "-c", default=1000)
def mock_logs_database(count: int) -> None:
    asyncio.run(mock_logs(count))


if __name__ == "__main__":
    cli()
