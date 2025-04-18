import psycopg2
from config import load_config

def insert_or_update_user(first_name, last_name, email, address, phone_number, operator_id):
    """ Call the stored procedure to insert or update a user """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CALL insert_or_update_user(%s, %s, %s, %s, %s, %s);
                """, (first_name, last_name, email, address, phone_number, operator_id))
                conn.commit()
                print(f"User '{first_name} {last_name}' processed successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

# Example usage
if __name__ == '__main__':
    insert_or_update_user(
        first_name="Alice",
        last_name="Johnson",
        email="alice.johnson@example.com",
        address="123 Main St",
        phone_number="+77011234567",
        operator_id=1
    )
    insert_or_update_user(
        first_name="Bob",
        last_name="Smith",
        email="bob.smith@example.com",
        address="456 Elm St",
        phone_number="+77019876543",
        operator_id=2
    )
    insert_or_update_user(
        first_name="Alice",
        last_name="Johnson",
        email="alice.newemail@example.com",
        address="789 Oak St",
        phone_number="+77012345678",
        operator_id=3
    )