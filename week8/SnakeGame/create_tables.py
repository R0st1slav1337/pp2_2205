import psycopg2
from config import load_config 

def create_tables():
    """
    Create users and 'user_score' tables for the Snake game.
    """
    commands = (
    """
    CREATE TABLE users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        created_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP -- No milliseconds
    )
    """,
    """
    CREATE TABLE user_score (
        score_id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        score INT NOT NULL,
        level INT NOT NULL,
        achieved_at TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP, -- No milliseconds
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    )
    """
)

    try:
        config = load_config()  # Load database configuration from the config file
        # Connect to the PostgreSQL database
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute each command in the commands list
                for command in commands:
                    cur.execute(command)
                conn.commit()
                print("Tables 'users' and 'user_score' created successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

if __name__ == '__main__':
    create_tables()