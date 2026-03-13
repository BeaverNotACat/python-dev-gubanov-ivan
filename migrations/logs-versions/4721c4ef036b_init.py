"""init

Revision ID: 4721c4ef036b
Revises:
Create Date: 2026-03-13 05:38:47.819314

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

from src.api.adapters.orm.logs import (
    EventType,
    SpaceType,
)

# revision identifiers, used by Alembic.
revision: str = "4721c4ef036b"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    event_types_table = op.create_table(
        "event_types",
        sa.Column("id", sa.SmallInteger(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.bulk_insert(
        event_types_table,
        [
            {"name": EventType.LOGIN},
            {"name": EventType.COMMENT},
            {"name": EventType.CREATE_POST},
            {"name": EventType.DELETE_POST},
            {"name": EventType.LOGOUT},
        ],
    )
    space_types_table = op.create_table(
        "space_types",
        sa.Column("id", sa.SmallInteger(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.bulk_insert(
        space_types_table,
        [
            {"name": SpaceType.GLOBAL},
            {"name": SpaceType.BLOG},
            {"name": SpaceType.POST},
        ],
    )
    op.create_table(
        "logs",
        sa.Column("datetime", sa.DateTime(timezone=True), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("space_type_id", sa.SmallInteger(), nullable=False),
        sa.Column("event_type_id", sa.SmallInteger(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(["event_type_id"], ["event_types.id"]),
        sa.ForeignKeyConstraint(["space_type_id"], ["space_types.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("logs")
    op.drop_table("space_types")
    op.drop_table("event_types")
