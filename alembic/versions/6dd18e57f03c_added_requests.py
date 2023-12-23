"""added requests

Revision ID: 6dd18e57f03c
Revises: 79393285d6d5
Create Date: 2023-12-22 23:52:52.443041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dd18e57f03c'
down_revision = '79393285d6d5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('request_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('subject', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('section', sa.String(), nullable=False),
    sa.Column('campus', sa.String(), nullable=False),
    sa.Column('added_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('request_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request')
    # ### end Alembic commands ###
