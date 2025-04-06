"""Initial migration

Revision ID: c159e09948c4
Revises: 9a59046837fe
Create Date: 2024-12-23 12:54:35.584369

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c159e09948c4'
down_revision: Union[str, None] = '9a59046837fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
