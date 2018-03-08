"""empty message

Revision ID: 40f5a43ff963
Revises:
Create Date: 2018-03-08 21:56:20.289159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40f5a43ff963'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('instants')


def downgrade():
    op.create_table(
        'instants',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('temperature', sa.FLOAT(), nullable=False),
        sa.Column('humidity', sa.FLOAT(), nullable=False),
        sa.Column('timestamp', sa.VARCHAR(length=25), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
