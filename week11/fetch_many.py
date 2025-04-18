import psycopg2
from config import load_config

def iter_row(cursor, size=10):
    """ Iterator to fetch rows in chunks """
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_user_phone_operators():
    """ Retrieve data from users, phone_numbers, and operators tables """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the SQL query to join the tables
                cur.execute("""
                    SELECT 
                        u.first_name, 
                        u.last_name, 
                        p.phone_number, 
                        o.operator_name
                    FROM users u
                    INNER JOIN phone_numbers p ON u.user_id = p.user_id
                    INNER JOIN operators o ON p.operator_id = o.operator_id
                    ORDER BY u.first_name;
                """)
                # Use the iterator to fetch rows in chunks
                for row in iter_row(cur, 10):
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

if __name__ == '__main__':
    get_user_phone_operators()