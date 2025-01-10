from app import app
from app.seeders.user_seeder import seed_users


with app.app_context():#<--gives access to flask, sqlalcehmy and alembic
    seed_users()
