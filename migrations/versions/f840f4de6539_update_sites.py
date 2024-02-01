"""Update sites

Revision ID: f840f4de6539
Revises: f3c44bce517a
Create Date: 2024-01-28 16:42:54.751813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f840f4de6539'
down_revision = 'f3c44bce517a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sites', schema=None) as batch_op:
        batch_op.alter_column('custom_url',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sites', schema=None) as batch_op:
        batch_op.alter_column('custom_url',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###