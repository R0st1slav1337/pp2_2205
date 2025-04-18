import psycopg2
from config import load_config

def insert_operators(operator_name):
    """ Insert a new operator into the operators table """

    sql = """INSERT INTO operators(operator_name)
             VALUES(%s) RETURNING operator_id;"""

    operator_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (operator_name,))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    operator_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
    finally:
        return operator_id

def insert_many_operators(operator_list):
    """ Insert multiple operators into the operators table  """

    sql = "INSERT INTO operators(operator_name) VALUES(%s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, operator_list)

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

def insert_users(first_name, last_name, email=None, address=None):
    """ Insert a new user into the users table """
    sql = """
        INSERT INTO users (first_name, last_name, email, address)
        VALUES (%s, %s, %s, %s)
        RETURNING user_id;
    """
    config = load_config()
    user_id = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (first_name, last_name, email, address))
                user_id = cur.fetchone()[0]  # Get the generated user_id
                conn.commit()
                print(f"User {first_name} {last_name} added with ID {user_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
    return user_id

def insert_phone_numbers(user_id, operator_id, phone_number):
    """ Insert a new phone numbers into the phone_numbers table """
    sql = """
        INSERT INTO phone_numbers (user_id, operator_id, phone_number)
        VALUES (%s, %s, %s)
        RETURNING phone_id;
    """
    config = load_config()
    phone_id = None
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_id, operator_id, phone_number))
                phone_id = cur.fetchone()[0]  # Get the generated phone_id
                conn.commit()
                print(f"Phone number {phone_number} added with ID {phone_id}.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()
    return phone_id


if __name__ == '__main__':   
    insert_operators("Beeline")
    insert_many_operators([
        ('Kcell',),
        ('Tele2',),
        ('Activ',),
        ('Altel',),
        ('IZI',)
    ])

    # Addition of a user
    user_id = insert_users(str(input("Enter first name:")), str(input("Enter last name:")), str(input("Enter email:")), str(input("Enter address:")))
    # Addition of a phone number for the user
    if user_id:
        operator_id = 1  # Assuming the operator_id for Beeline is 1
        insert_phone_numbers(user_id, operator_id, str(input("Enter phone number:")))
    
    user_id = insert_users("Rostislav", "Krivenko", "GhostRider1337@mail.ru", "Obshaga #3")
    if user_id:
        operator_id = 3
        insert_phone_numbers(user_id, operator_id, "+77772281337")
    
    user_id = insert_users("Nika", "Krivenko", "BTS#1@gmail.kz", "228 Erubaev St")
    if user_id:
        operator_id = 2
        insert_phone_numbers(user_id, operator_id, "+77056671234")

    user_id = insert_users("Tanzhar", "Kokishev", "GuardOfHighTab@inbox.com", "228 Street St")
    if user_id:
        operator_id = 5
        insert_phone_numbers(user_id, operator_id, "+77787881230") # real phone number

    user_id = insert_users("Alishka", "Kaliev", "bezprichin09@mail.ru", "Homeless")
    if user_id:
        operator_id = 6
        insert_phone_numbers(user_id, operator_id, "+77777777777")

    user_id = insert_users("Ernur", "Kuat", "ernur_kuat14@gmail.com", "Lesozavod")
    if user_id:
        operator_id = 4
        insert_phone_numbers(user_id, operator_id, "+77770688111") # real phone number

    user_id = insert_users("Ayim", "Esenova", "RobloxFan@mail.ru", "Obshaga #4")
    if user_id:
        operator_id = 3
        insert_phone_numbers(user_id, operator_id, "+77081239999")