"""Converted Birthday to String()

Revision ID: 2e81fad01e90
Revises: 5d9c13c3beb2
Create Date: 2023-08-12 23:35:03.619097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e81fad01e90'
down_revision = '5d9c13c3beb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('zookeepers', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('zookeepers', schema=None) as batch_op:
        batch_op.alter_column('birthday',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
