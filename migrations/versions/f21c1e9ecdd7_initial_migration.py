"""Initial migration

Revision ID: f21c1e9ecdd7
Revises: f3d1421ed08e
Create Date: 2024-12-23 13:21:21.652448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f21c1e9ecdd7'
down_revision: Union[str, None] = 'f3d1421ed08e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
