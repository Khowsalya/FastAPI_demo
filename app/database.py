
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = "root"
DB_PASSWORD = "KNani@146"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "msme_loan_db"

# 1. Connect to the specific MySQL database
DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

# 2. Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# 3. Create Base for all ORM models
Base = declarative_base()

# 4. Create session factory
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
