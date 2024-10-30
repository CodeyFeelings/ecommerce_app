import psycopg2
from psycopg2 import sql
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from table_definitions import table_definitions
# THIS SETS UP THE DATABASE USING THE .env AND table_definitions

# confirms DB connection by connecting to the default DB


def connect_default():
    print("Connected to default DB")
    return psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

# CREATES DATABASE


def create_database_if_not_exists(db_name):
    # try to connect to default
    conn = connect_default()
    conn.autocommit = True
    db = conn.cursor()

    # check if DB exists
    db.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
    exists = db.fetchone()
    # if not create DB
    if not exists:
        db.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(db_name)))
    db.close()
    conn.close()
    print("Database created")

# CONNECTS TO DATABASE


def connect_database():
    print("Database connected")
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


# CREATE TABLES
def create_tables_if_not_exists(conn):
    db = conn.cursor()
    for table_name, table_definition in table_definitions.items():
        db.execute(table_definition)
    conn.commit()
    print("Tables created")
    db.close()


# RUN THE DATATBASE SETUP
if __name__ == "__main__":
    db_name = DB_NAME
    create_database_if_not_exists(db_name)

    conn = connect_database()
    create_tables_if_not_exists(conn)
    conn.close()
