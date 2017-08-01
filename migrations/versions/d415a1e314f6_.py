"""empty message

Revision ID: d415a1e314f6
Revises: 8dacbb0d795b
Create Date: 2017-07-28 20:07:49.634762

"""

# revision identifiers, used by Alembic.
revision = 'd415a1e314f6'
down_revision = '8dacbb0d795b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('check_in', sa.Column('avg_interarrival', sa.Float(), nullable=False))
    op.add_column('check_in', sa.Column('avg_processing', sa.Float(), nullable=False))
    op.add_column('emigration', sa.Column('avg_interarrival', sa.Float(), nullable=False))
    op.add_column('emigration', sa.Column('avg_processing', sa.Float(), nullable=False))
    op.add_column('security_checkpoint', sa.Column('avg_interarrival', sa.Float(), nullable=False))
    op.add_column('security_checkpoint', sa.Column('avg_processing', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('security_checkpoint', 'avg_processing')
    op.drop_column('security_checkpoint', 'avg_interarrival')
    op.drop_column('emigration', 'avg_processing')
    op.drop_column('emigration', 'avg_interarrival')
    op.drop_column('check_in', 'avg_processing')
    op.drop_column('check_in', 'avg_interarrival')
    # ### end Alembic commands ###
