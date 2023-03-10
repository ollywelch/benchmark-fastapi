"""init

Revision ID: ac9f84795a1a
Revises: 
Create Date: 2023-01-30 19:32:13.713928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ac9f84795a1a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "addresses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    users = sa.table("users", sa.column("id", sa.Integer), sa.column("name", sa.String))
    addresses = sa.table(
        "addresses",
        sa.column("id", sa.Integer),
        sa.column("email", sa.String),
        sa.column("user_id", sa.Integer),
    )
    op.bulk_insert(
        users,
        [
            {
                "id": 1,
                "name": "John Smith",
            },
            {"id": 2, "name": "Bob Richards"},
        ],
    )
    op.bulk_insert(
        addresses,
        [
            {
                "id": 1,
                "email": "john@smith.com",
                "user_id": 1,
            },
            {
                "id": 2,
                "email": "john2@smith.com",
                "user_id": 1,
            },
            {"id": 3, "email": "bob@richards.com", "user_id": 2},
        ],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("addresses")
    op.drop_table("users")
    # ### end Alembic commands ###
