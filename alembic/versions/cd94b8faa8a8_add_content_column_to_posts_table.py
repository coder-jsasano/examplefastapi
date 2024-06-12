"""add content column to posts table

Revision ID: cd94b8faa8a8
Revises: 047e7454ece0
Create Date: 2024-06-11 17:45:32.915441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd94b8faa8a8'
down_revision: Union[str, None] = '047e7454ece0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
