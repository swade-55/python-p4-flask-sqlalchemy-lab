"""Created DB

Revision ID: 5d9c13c3beb2
Revises: 
Create Date: 2023-08-12 23:26:35.091171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d9c13c3beb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enclosures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('environment', sa.String(), nullable=True),
    sa.Column('open_to_visitors', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zookeepers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.Column('zookeeper', sa.Integer(), nullable=True),
    sa.Column('enclosure', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['enclosure'], ['enclosures.id'], name=op.f('fk_animals_enclosure_enclosures')),
    sa.ForeignKeyConstraint(['zookeeper'], ['zookeepers.id'], name=op.f('fk_animals_zookeeper_zookeepers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('animals')
    op.drop_table('zookeepers')
    op.drop_table('enclosures')
    # ### end Alembic commands ###
