"""empty message

Revision ID: c6ff2c9177eb
Revises: 
Create Date: 2023-08-24 13:30:11.436347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6ff2c9177eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('current_date',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.alter_column('meal',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('meal',
               existing_type=sa.VARCHAR(),
               nullable=False)

    op.drop_table('current_date')
    # ### end Alembic commands ###
