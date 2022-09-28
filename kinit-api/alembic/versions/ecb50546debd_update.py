"""update

Revision ID: ecb50546debd
Revises: d4898760c577
Create Date: 2022-09-15 20:59:40.938777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecb50546debd'
down_revision = 'd4898760c577'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vadmin_auth_menu', sa.Column('title_zh', sa.String(length=50), nullable=True, comment='中文名称'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vadmin_auth_menu', 'title_zh')
    # ### end Alembic commands ###