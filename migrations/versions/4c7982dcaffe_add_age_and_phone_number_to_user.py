"""Add age and phone_number to user

Revision ID: 4c7982dcaffe
Revises: 08610bd32a5a
Create Date: 2025-02-16 15:12:54.302475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c7982dcaffe'
down_revision: Union[str, None] = '08610bd32a5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.String(), nullable=False))
    op.add_column('users', sa.Column('note', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'note')
    op.drop_column('users', 'active')
    # ### end Alembic commands ###
