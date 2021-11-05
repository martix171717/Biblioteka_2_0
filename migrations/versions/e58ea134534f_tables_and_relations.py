"""tables and relations

Revision ID: e58ea134534f
Revises: 
Create Date: 2021-11-05 11:36:55.357669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e58ea134534f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_author_name'), 'author', ['name'], unique=False)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('year', sa.Numeric(precision=4, scale=0), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_table('author_book',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('author_id', 'book_id')
    )
    op.create_table('borrowing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('borrowed', sa.Boolean(), nullable=True),
    sa.Column('borrow_date', sa.String(length=10), nullable=True),
    sa.Column('where', sa.String(length=50), nullable=True),
    sa.Column('id_book', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_book'], ['book.title'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrowing')
    op.drop_table('author_book')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_author_name'), table_name='author')
    op.drop_table('author')
    # ### end Alembic commands ###
