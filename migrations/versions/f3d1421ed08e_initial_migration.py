"""Initial migration

Revision ID: f3d1421ed08e
Revises: 0058aae88603
Create Date: 2024-12-23 13:09:06.588219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3d1421ed08e'
down_revision: Union[str, None] = '0058aae88603'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
