"""empty message

Revision ID: 9ba31d8ad9a6
Revises: 53cc251a9bda
Create Date: 2017-07-25 10:25:54.717064

"""

# revision identifiers, used by Alembic.
revision = '9ba31d8ad9a6'
down_revision = '53cc251a9bda'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('check_in', sa.Column('waitingarea_breadth', sa.Float(), nullable=False))
    op.add_column('check_in', sa.Column('waitingarea_length', sa.Float(), nullable=False))
    op.add_column('emigration', sa.Column('waitingarea_breadth', sa.Float(), nullable=False))
    op.add_column('emigration', sa.Column('waitingarea_length', sa.Float(), nullable=False))
    op.add_column('security_checkpoint', sa.Column('waitingarea_breadth', sa.Float(), nullable=False))
    op.add_column('security_checkpoint', sa.Column('waitingarea_length', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('security_checkpoint', 'waitingarea_length')
    op.drop_column('security_checkpoint', 'waitingarea_breadth')
    op.drop_column('emigration', 'waitingarea_length')
    op.drop_column('emigration', 'waitingarea_breadth')
    op.drop_column('check_in', 'waitingarea_length')
    op.drop_column('check_in', 'waitingarea_breadth')
    # ### end Alembic commands ###
