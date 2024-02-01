"""Update site

Revision ID: 9edb8ee05546
Revises: ea4ff1151528
Create Date: 2024-01-31 20:13:11.081998

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9edb8ee05546"
down_revision = "ea4ff1151528"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.add_column(sa.Column("data_received", sa.Integer(), nullable=False))
        batch_op.drop_column("data_recieved")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.add_column(sa.Column("data_recieved", sa.INTEGER(), nullable=False))
        batch_op.drop_column("data_received")

    # ### end Alembic commands ###
