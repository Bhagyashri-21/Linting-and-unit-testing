"""Initial migration

Revision ID: c30dbdb4c1a6
Revises: 85839ee21871
Create Date: 2024-12-21 16:05:46.488389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c30dbdb4c1a6'
down_revision: Union[str, None] = '85839ee21871'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
