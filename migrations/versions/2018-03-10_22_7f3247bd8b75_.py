"""base migration

Revision ID: 7f3247bd8b75
Revises: None
Create Date: 2018-03-10 22:02:28.039670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f3247bd8b75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'instants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('temperature', sa.Float(), nullable=False),
        sa.Column('humidity', sa.Float(), nullable=False),
        sa.Column('timestamp', sa.String(length=25), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('instants')
