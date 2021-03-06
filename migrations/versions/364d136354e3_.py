"""empty message

Revision ID: 364d136354e3
Revises: 27f83fc38c35
Create Date: 2014-04-29 22:58:31.359828

"""

# revision identifiers, used by Alembic.
revision = '364d136354e3'
down_revision = '27f83fc38c35'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('measure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('val', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measure')
    op.drop_table('sensor')
    ### end Alembic commands ###
