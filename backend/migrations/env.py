import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# Import model modules so their tables register with Base.metadata.
import app.models.academic_year
import app.models.exam_result
import app.models.student
import app.models.subject
import app.models.user
from app.core.config import settings
from app.db.base import Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

database_url = (
    os.getenv("DATABASE_URL")
    or settings.database_url
    or config.get_main_option("sqlalchemy.url")
)

if not database_url:
    raise RuntimeError(
        "Set DATABASE_URL in the environment or sqlalchemy.url in alembic.ini."
    )

config.set_main_option(
    "sqlalchemy.url",
    database_url.replace("%", "%%"),
)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations without creating a database connection."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations using a live database connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

# Import model modules so their tables register with Base.metadata.
import app.models.academic_year
import app.models.exam_result
import app.models.student
import app.models.subject
import app.models.user  # noqa: F401
