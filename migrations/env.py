import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import Connection
from sqlalchemy.ext.asyncio import AsyncEngine

from src.api.adapters.engines import AppAsyncEngine, LogsAsyncEngine
from src.api.adapters.orm.app import AppBaseORM
from src.api.adapters.orm.logs import LogsBaseORM
from src.api.di.container import container

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

METADATA_MAP = {"app": AppBaseORM.metadata, "logs": LogsBaseORM.metadata}
ENGINE_MAP: dict[str, AsyncEngine] = {
    "app": container.get_sync(AppAsyncEngine),
    "logs": container.get_sync(LogsAsyncEngine),
}


def validate_db_name(db_name: str) -> None:
    section_config = config.get_section(db_name)
    if section_config is None:
        raise RuntimeError(f"{db_name} block is absent in alembic.ini")
    if METADATA_MAP.get(db_name) is None:
        raise RuntimeError(f"{db_name} key is absent at env.METADATA_MAP")
    if ENGINE_MAP.get(db_name) is None:
        raise RuntimeError(f"{db_name} key is absent at env.ENGINE_MAP")


async def run_migrations_for(db_name: str) -> None:
    validate_db_name(db_name)

    target_metadata = METADATA_MAP[db_name]
    connectable = ENGINE_MAP[db_name]

    # TODO: Closuse with run sync because of `ENGINE_MAP[db_name].sync_engine`
    # Fails with greenlet spawn
    def do_run_migrations(connection: Connection) -> None:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


section = config.config_ini_section
databases = config.get_main_option("databases")

if section == "alembic" and databases:
    # No specific --name given: run all databases sequentially
    for name in [db.strip() for db in databases.split(",")]:
        asyncio.run(run_migrations_for(name))
else:
    # Only run the specified database (with --name or default section)
    asyncio.run(run_migrations_for(section))
