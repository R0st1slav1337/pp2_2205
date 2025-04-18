import psycopg2
from config import load_config

def delete_data_by_username_or_phone(first_name=None, phone=None):
    """
    Call the stored procedure to delete data by first name or phone.
    """
    if not first_name and not phone:
        print("Please provide either a first name or a phone number.")
        return

    config = load_config()

    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                # Call the stored procedure
                cursor.execute("""
                    CALL delete_data_by_username_or_phone(%s, %s);
                """, (first_name, phone))
                conn.commit()
                print("Deletion completed successfully.")
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"An error occurred: {e}")
        conn.rollback()

if __name__ == '__main__':
    # Delete by username
    delete_data_by_username_or_phone(first_name='Alice')