"""added requests updated

Revision ID: 5aedde6cf00f
Revises: 6dd18e57f03c
Create Date: 2023-12-22 23:56:00.563347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aedde6cf00f'
down_revision = '6dd18e57f03c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('is_active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('request', 'is_active')
    # ### end Alembic commands ###
