"""test

Revision ID: d6ccd88aa81c
Revises: 56f30a2bf485
Create Date: 2017-04-25 18:28:05.567394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6ccd88aa81c'
down_revision = '56f30a2bf485'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('aa', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'aa')
    # ### end Alembic commands ###
