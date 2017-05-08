"""add article mkcontent

Revision ID: c17ad4b693d6
Revises: d6ccd88aa81c
Create Date: 2017-05-05 15:50:46.243379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c17ad4b693d6'
down_revision = 'd6ccd88aa81c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('mkcontent', sa.Text(), nullable=True))
    op.drop_column('article', 'aa')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('aa', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('article', 'mkcontent')
    # ### end Alembic commands ###