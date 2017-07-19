"""empty message

Revision ID: e9aac65532e1
Revises: 4a48ec7f25fa
Create Date: 2017-07-16 17:06:02.300937

"""

# revision identifiers, used by Alembic.
revision = 'e9aac65532e1'
down_revision = '4a48ec7f25fa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('metric',
    sa.Column('process', sa.String(length=45), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('p_overdesign', sa.Float(), nullable=False),
    sa.Column('p_optimum', sa.Float(), nullable=False),
    sa.Column('p_suboptimum', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('process')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('metric')
    # ### end Alembic commands ###
