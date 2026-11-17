import os

import psycopg
from dotnev import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

def get_connection():
    """Get a connection to the PostgreSQL database."""
    return psycopg.connect(DATABASE_URL)
