"""Initial migration

Revision ID: 07726b792835
Revises: 527fe95523be
Create Date: 2024-12-23 14:16:48.643611

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07726b792835'
down_revision: Union[str, None] = '527fe95523be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
