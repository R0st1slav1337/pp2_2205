import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE operators (
            operator_id SERIAL PRIMARY KEY,
            operator_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            address TEXT
        )
        """,
        """
        CREATE TABLE phone_numbers (
            phone_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            operator_id INTEGER NOT NULL,
            phone_number VARCHAR(20) NOT NULL UNIQUE,
            FOREIGN KEY (user_id)
                REFERENCES users (user_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (operator_id)
                REFERENCES operators (operator_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error: {error}")
        conn.rollback()

if __name__ == '__main__':
    create_tables()