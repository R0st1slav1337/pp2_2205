import psycopg2
from config import load_config


def update_operator(operator_id, operator_name):
    """ Update operator name based on the operator id """

    updated_row_count = 0

    sql = """ UPDATE operators
                SET operator_name = %s
                WHERE operator_id = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                # execute the UPDATE statement
                cur.execute(sql, (operator_name, operator_id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
    finally:
        return updated_row_count
    
def update_user(user_id, first_name=None, last_name=None, email=None, address=None):
    """ Update user details based on the user id """
    updated_row_count = 0

    # SQL query to update user details
    sql = "UPDATE users SET "
    updates = []
    params = []

    if first_name:
        updates.append("first_name = %s")
        params.append(first_name)
    if last_name:
        updates.append("last_name = %s")
        params.append(last_name)
    if email:
        updates.append("email = %s")
        params.append(email)
    if address:
        updates.append("address = %s")
        params.append(address)

    sql += ", ".join(updates) + " WHERE user_id = %s"
    params.append(user_id)

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the UPDATE statement
                cur.execute(sql, tuple(params))
                updated_row_count = cur.rowcount

            # Commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
    finally:
        return updated_row_count   

def update_phone_number(phone_id, phone_number=None, operator_id=None):
    """ Update phone number details based on the phone id """
    updated_row_count = 0

    # SQL query to update phone number details
    sql = "UPDATE phone_numbers SET "
    updates = []
    params = []

    if phone_number:
        updates.append("phone_number = %s")
        params.append(phone_number)
    if operator_id:
        updates.append("operator_id = %s")
        params.append(operator_id)

    sql += ", ".join(updates) + " WHERE phone_id = %s"
    params.append(phone_id)

    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the UPDATE statement
                cur.execute(sql, tuple(params))
                updated_row_count = cur.rowcount

            # Commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
    finally:
        return updated_row_count

if __name__ == '__main__':
    # Update operator details
    update_operator(5, "Altel4G")

    # Update user details
    updated_users = update_user(
        user_id=1,
        first_name="Diar",
        last_name="Tagambaev",
        email="FaceitLVL10@gmail.com",
        address="NU obshaga"
    )
    print(f"Updated {updated_users} user(s).")

    # Update phone number details
    updated_phones = update_phone_number(
        phone_id=1,
        phone_number="+77019876543",
        operator_id=1
    )
    print(f"Updated {updated_phones} phone number(s).")