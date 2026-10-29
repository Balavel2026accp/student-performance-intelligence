
"""Baseline existing student performance schema.

Revision ID: 49b435b57431
Revises:
"""

revision: str = "49b435b57431"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Record the existing schema baseline without changing tables."""
    pass


def downgrade() -> None:
    """Keep the existing schema and data intact."""
    pass
