from logging.config import fileConfig
from os import environ

import dotenv
from alembic import context

from masterplan.database.engine import engine
from masterplan.database.tables import Base

dotenv.load_dotenv(".env")
dotenv.load_dotenv(".env.local")

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_offline():
    context.configure(
        url=environ["IS_DB_URI"],
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
