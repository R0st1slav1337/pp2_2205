import psycopg2
from config import load_config

def delete_user_by_name(first_name, last_name=None):
    """ Delete a user from the users table by their first name (and optionally last name) """
    sql = "DELETE FROM users WHERE first_name = %s"
    params = [first_name]

    # If last_name is provided, add it to the SQL query and parameters
    if last_name:
        sql += " AND last_name = %s"
        params.append(last_name)

    config = load_config()
    deleted_row_count = 0

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the DELETE statement
                cur.execute(sql, tuple(params))
                deleted_row_count = cur.rowcount

            # Commit the changes to the database
            conn.commit()
            print(f"Deleted {deleted_row_count} user(s) with name '{first_name}'{' ' + last_name if last_name else ''}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()  # Rollback in case of error
    finally:
        return deleted_row_count
    
if __name__ == '__main__':
    # Delete user by first name only
    delete_user_by_name(str(input("Enter first name: ")))

    # Delete user by first and last name
    delete_user_by_name("Jane", "Smith")