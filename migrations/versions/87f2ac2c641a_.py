"""empty message

Revision ID: 87f2ac2c641a
Revises: 18c043d01a6a
Create Date: 2023-08-25 13:50:38.439169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87f2ac2c641a'
down_revision = '18c043d01a6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('extras', schema=None) as batch_op:
        batch_op.alter_column('extras_audio_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('extras_subs_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('movie_audio_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('movie_subs_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('movie_subs_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('movie_audio_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('extras', schema=None) as batch_op:
        batch_op.alter_column('extras_subs_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('extras_audio_lang',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###