"""Add outdoors instant

Revision ID: e869c1c289ff
Revises: 7f3247bd8b75
Create Date: 2018-03-10 22:24:16.919632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e869c1c289ff'
down_revision = '7f3247bd8b75'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'outdoor_instants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('temperature', sa.Float(), nullable=False),
        sa.Column('humidity', sa.Float(), nullable=False),
        sa.Column('timestamp', sa.String(length=25), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('outdoor_instants')
