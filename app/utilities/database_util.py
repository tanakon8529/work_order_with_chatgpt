import time
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings.configs import DATABASE_NAME, DATABASE_SERVER, DATABASE_USERNAME, DATABASE_PASSWORD

class database_controls(object):
    def __init__(self):
        connect_args = {'connect_timeout': 60}
        # Change the connection URL to PostgreSQL
        self.db_str = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:5432/{DATABASE_NAME}"
        self.engine = create_engine(self.db_str, pool_size=5, max_overflow=10, pool_pre_ping=True, connect_args=connect_args)

    def get_db(self):
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=True, bind=self.engine)
        attempts = 0
        while attempts < 60:
            try:
                session = SessionLocal()
                return session
            except Exception as e:
                logger.error(f"Error establishing database connection: {e}")
                attempts += 1
                time.sleep(1)

        logger.error("Max retry attempts reached, giving up on database connection")
        return None
