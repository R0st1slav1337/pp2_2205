import psycopg2
import json
from config import load_config

def insert_many_users(user_data):
    """ Call the stored procedure to insert many users and return incorrect data """
    config = load_config()
    incorrect_data = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Convert user data to JSON
                user_data_json = json.dumps(user_data)

                # Call the stored procedure and fetch incorrect data
                cur.execute("""
                    CALL insert_many_users(%s, %s);
                """, (user_data_json, None))
                incorrect_data = cur.fetchone()[0]  # Fetch the incorrect data
                conn.commit()
                print("Users processed successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
    return incorrect_data

# Example usage
if __name__ == '__main__':
    user_data = [
        {"first_name": "Alice", "last_name": "Johnson", "phone": "1234567890", "operator_id": 4},
        {"first_name": "Bob", "last_name": "Smith", "phone": "987654321", "operator_id": 2},  # Invalid phone
        {"first_name": "Charlie", "last_name": "Brown", "phone": "abcdefghij", "operator_id": 3},  # Invalid phone
        {"first_name": "Diana", "last_name": "Prince", "phone": "0987654321", "operator_id": 5}
    ]

    incorrect = insert_many_users(user_data)

    if incorrect:
        print("The following records were not inserted due to errors:")
        print(json.dumps(incorrect, indent=4))
    else:
        print("All records were inserted successfully.")