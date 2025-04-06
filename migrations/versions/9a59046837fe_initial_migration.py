"""Initial migration

Revision ID: 9a59046837fe
Revises: c30dbdb4c1a6
Create Date: 2024-12-23 11:01:40.941115

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a59046837fe'
down_revision: Union[str, None] = 'c30dbdb4c1a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
