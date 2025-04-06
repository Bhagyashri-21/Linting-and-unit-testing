"""Initial migration

Revision ID: 527fe95523be
Revises: f21c1e9ecdd7
Create Date: 2024-12-23 14:14:11.302091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '527fe95523be'
down_revision: Union[str, None] = 'f21c1e9ecdd7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
