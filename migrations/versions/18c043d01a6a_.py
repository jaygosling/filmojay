"""empty message

Revision ID: 18c043d01a6a
Revises: 
Create Date: 2023-08-25 13:50:06.869871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18c043d01a6a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('languages',
    sa.Column('lang_id', sa.Integer(), nullable=False),
    sa.Column('lang_code', sa.String(length=120), nullable=False),
    sa.Column('lang_name', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('lang_id'),
    sa.UniqueConstraint('lang_code')
    )
    op.create_table('movies',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('movie_title', sa.String(length=120), nullable=False),
    sa.Column('movie_director', sa.String(length=80), nullable=False),
    sa.Column('movie_cast', sa.String(length=255), nullable=False),
    sa.Column('movie_runtime', sa.Integer(), nullable=False),
    sa.Column('movie_audio_lang', sa.String(length=255), nullable=True),
    sa.Column('movie_subs_lang', sa.String(length=255), nullable=True),
    sa.Column('tmdb_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('movie_id'),
    sa.UniqueConstraint('movie_title')
    )
    op.create_table('extras',
    sa.Column('extras_id', sa.Integer(), nullable=False),
    sa.Column('extras_title', sa.String(length=120), nullable=False),
    sa.Column('extras_description', sa.String(length=500), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('extras_runtime', sa.Integer(), nullable=False),
    sa.Column('extras_audio_lang', sa.String(length=255), nullable=True),
    sa.Column('extras_subs_lang', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.movie_id'], ),
    sa.PrimaryKeyConstraint('extras_id'),
    sa.UniqueConstraint('extras_title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('extras')
    op.drop_table('movies')
    op.drop_table('languages')
    # ### end Alembic commands ###
