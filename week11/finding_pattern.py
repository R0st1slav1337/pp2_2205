import psycopg2
from config import load_config

def search_records(pattern):
    """ Search for records in the PhoneBook based on a pattern """
    sql = """
        SELECT 
            u.first_name, 
            u.last_name, 
            p.phone_number, 
            o.operator_name
        FROM users u
        INNER JOIN phone_numbers p ON u.user_id = p.user_id
        INNER JOIN operators o ON p.operator_id = o.operator_id
        WHERE 
            u.first_name ILIKE %s OR 
            u.last_name ILIKE %s OR 
            p.phone_number ILIKE %s
        ORDER BY u.first_name;
    """
    config = load_config()
    results = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the query with the pattern
                cur.execute(sql, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
                results = cur.fetchall()
 
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
    finally:
        return results
    
if __name__ == '__main__':
    # Prompt the user for a search pattern
    pattern = input("Enter a search pattern (e.g., part of name, surname, or phone number): ")
    records = search_records(pattern)

    if records:
        print("Search results:")
        for record in records:
            print(record)
    else:
        print("No records found.")