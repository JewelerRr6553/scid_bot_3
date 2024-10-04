"""Update User, ContactManager models

Revision ID: 31916cbb37e1
Revises: 
Create Date: 2024-10-04 17:29:06.898325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '31916cbb37e1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contactmanager',
    sa.Column('first_name', sa.VARCHAR(length=32), nullable=False),
    sa.Column('phone_number', sa.VARCHAR(length=25), nullable=False),
    sa.Column('need_support', sa.BOOLEAN(), nullable=False),
    sa.Column('need_contact_with_manager', sa.BOOLEAN(), nullable=False),
    sa.Column('shipping_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('user', 'need_support')
    op.drop_column('user', 'name')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'shipping_date')
    op.drop_column('user', 'need_contact_with_manager')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('need_contact_with_manager', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('shipping_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('phone', sa.VARCHAR(length=25), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('name', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('need_support', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_table('contactmanager')
    # ### end Alembic commands ###
