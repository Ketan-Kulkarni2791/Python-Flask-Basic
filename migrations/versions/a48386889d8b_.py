"""empty message

Revision ID: a48386889d8b
Revises: df1dfc451aae
Create Date: 2021-11-06 09:34:06.160184

"""

# revision identifiers, used by Alembic.
revision = 'a48386889d8b'
down_revision = 'df1dfc451aae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table('employee') as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))


def downgrade():
    with op.batch_alter_table('employee') as batch_op:
        batch_op.drop_column('age')
