"""Add wind speed and feels like to outdoor instant

Revision ID: 64173c208aae
Revises: e869c1c289ff
Create Date: 2018-03-10 22:39:19.945570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64173c208aae'
down_revision = 'e869c1c289ff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'outdoor_instants',
        sa.Column(
            'feels_like',
            sa.Integer()
        ))
    op.add_column(
        'outdoor_instants',
        sa.Column(
            'wind_speed',
            sa.Integer(),
        ))


def downgrade():
    op.drop_column('outdoor_instants', 'wind_speed')
    op.drop_column('outdoor_instants', 'feels_like')
