# Generate alembic revision
cd .. && source .env
# shellcheck disable=SC2164
cd src
alembic revision --autogenerate

# Run migrations
alembic upgrade head

# Create initial data in DB
python initial_db.py

