"""empty message

Revision ID: 7629809bbe2f
Revises: 
Create Date: 2023-08-18 15:50:36.473406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7629809bbe2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('van',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('van_number', sa.Integer(), nullable=True),
    sa.Column('milage', sa.Integer(), nullable=True),
    sa.Column('last_oil_change_milage', sa.Integer(), nullable=True),
    sa.Column('last_oil_change_date', sa.Date(), nullable=True),
    sa.Column('last_front_tire_change_date', sa.Date(), nullable=True),
    sa.Column('last_rear_tire_change_date', sa.Date(), nullable=True),
    sa.Column('last_trans_fluid_change_milage', sa.Integer(), nullable=True),
    sa.Column('last_battery_change_milage', sa.Integer(), nullable=True),
    sa.Column('last_air_filter_change_milage', sa.Integer(), nullable=True),
    sa.Column('last_spark_plug_change_milage', sa.Integer(), nullable=True),
    sa.Column('last_coil_change_milage', sa.Integer(), nullable=True),
    sa.Column('last_state_inspection_date', sa.Date(), nullable=True),
    sa.Column('last_registration_renewal_date', sa.Date(), nullable=True),
    sa.Column('last_front_brake_change_milage', sa.Integer(), nullable=True),
    sa.Column('last_rear_brake_change_milage', sa.Integer(), nullable=True),
    sa.Column('plate', sa.VARCHAR(), nullable=True),
    sa.Column('vin', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('van')
    op.drop_table('user')
    # ### end Alembic commands ###