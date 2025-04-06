"""Initial migration

Revision ID: 0058aae88603
Revises: c159e09948c4
Create Date: 2024-12-23 13:02:05.275030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0058aae88603'
down_revision: Union[str, None] = 'c159e09948c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
