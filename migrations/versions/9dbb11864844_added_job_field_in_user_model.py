"""added job field in user model

Revision ID: 9dbb11864844
Revises: 74fe697b482f
Create Date: 2020-04-25 17:52:48.029213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dbb11864844'
down_revision = '74fe697b482f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('job', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'job')
    # ### end Alembic commands ###
