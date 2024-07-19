"""empty message

Revision ID: df1dfc451aae
Revises: None
Create Date: 2021-11-05 19:10:55.080698

"""

# revision identifiers, used by Alembic.
revision = 'df1dfc451aae'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('cname', sa.String(), nullable=False),
    sa.Column('clocation', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('cid'),
    sa.UniqueConstraint('cname')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    op.drop_table('company')
    # ### end Alembic commands ###
