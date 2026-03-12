"""init

Revision ID: 9fc874e69ed1
Revises:
Create Date: 2026-03-13 05:26:23.626777

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "9fc874e69ed1"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade(engine_name: str) -> None:
    """Upgrade schema."""
    globals()[f"upgrade_{engine_name}"]()


def downgrade(engine_name: str) -> None:
    """Downgrade schema."""
    globals()[f"downgrade_{engine_name}"]()


def upgrade_app() -> None:
    """Upgrade app schema."""


def downgrade_app() -> None:
    """Downgrade app schema."""


def upgrade_logs() -> None:
    """Upgrade logs schema."""


def downgrade_logs() -> None:
    """Downgrade logs schema."""
