"""Add unique constraint together fot site.name and site.user_id

Revision ID: a85e2d53a84b
Revises: 99281e912a2a
Create Date: 2024-02-01 05:52:10.123156

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a85e2d53a84b"
down_revision = "99281e912a2a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.drop_constraint("unique_site_name", type_="unique")
        batch_op.drop_constraint("unique_site_url", type_="unique")
        batch_op.create_unique_constraint("unique_user_name", ["user_id", "name"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("sites", schema=None) as batch_op:
        batch_op.drop_constraint("unique_user_name", type_="unique")
        batch_op.create_unique_constraint("unique_site_url", ["url"])
        batch_op.create_unique_constraint("unique_site_name", ["name"])

    # ### end Alembic commands ###
