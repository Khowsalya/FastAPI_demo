
from sqlalchemy import create_engine, text, URL

from app.database import Base, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


# 1. Connect to MySQL server
SERVER_URL = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

server_engine = create_engine(SERVER_URL)


# 2. Create database if it doesn't exist
with server_engine.connect() as connection:
    connection.execute(
        text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
    )


# 3. Import models to register their tables
from app.models.loan_model import Loan


# 4. Create all registered tables
def create_tables():
    print("Registered tables:", Base.metadata.tables.keys())

    Base.metadata.create_all(bind=engine)

    print("Tables created successfully!")


if __name__ == "__main__":
    from app.database import engine
    create_tables()
    server_engine.dispose()
