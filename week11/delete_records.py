import psycopg2
from config import load_config

def delete_all_records(table_name):
    """ Delete all records from the specified table """
    sql = f"DELETE FROM {table_name};"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit()
                print(f"All records deleted from table '{table_name}'.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

def reset_sequence(table_name, sequence_name):
    """ Reset the sequence for a table """
    sql = f"ALTER SEQUENCE {sequence_name} RESTART WITH 1;"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit()
                print(f"Sequence '{sequence_name}' reset for table '{table_name}'.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

if __name__ == '__main__':
    # Delete all records from table 
    delete_all_records("operators")
    # Replace with the desired table name ("users" or "phone_numbers")
    delete_all_records("users")
    delete_all_records("phone_numbers")

    # Reset sequence for table
    reset_sequence("operators", "operators_operator_id_seq") 
    # Replace with the desired table name and sequence name ("users" or "phone_numbers")
    reset_sequence("users", "users_user_id_seq")
    reset_sequence("phone_numbers", "phone_numbers_phone_id_seq")