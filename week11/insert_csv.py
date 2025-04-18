import csv
import psycopg2
from config import load_config

# Function to read data from a CSV file
def read_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the header row
            for row in reader:
                data.append(dict(zip(headers, row)))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return data

# Function to write data to a CSV file
def write_csv(file_path, data, headers):
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to upload data to the users table
def upload_users_from_csv(file_path):
    """ Upload data from a CSV file into the users table """
    sql = """
        INSERT INTO users (first_name, last_name, email, address)
        VALUES (%s, %s, %s, %s)
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                data = read_csv(file_path)
                for row in data:
                    cur.execute(sql, (row['first_name'], row['last_name'], row['email'], row['address']))
                conn.commit()
                print(f"Data from {file_path} uploaded successfully to the users table.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()  # Rollback in case of error

# Function to upload data to the phone_numbers table
def upload_phone_numbers_from_csv(file_path):
    """ Upload data from a CSV file into the phone_numbers table """
    sql = """
        INSERT INTO phone_numbers (user_id, operator_id, phone_number)
        VALUES (%s, %s, %s)
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                data = read_csv(file_path)
                for row in data:
                    cur.execute(sql, (row['user_id'], row['operator_id'], row['phone_number']))
                conn.commit()
                print(f"Data from {file_path} uploaded successfully to the phone_numbers table.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

# Function to upload data to the operators table
def upload_operators_from_csv(file_path):
    """ Upload data from a CSV file into the operators table """
    sql = """
        INSERT INTO operators (operator_name)
        VALUES (%s)
    """
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                data = read_csv(file_path)
                for row in data:
                    cur.execute(sql, (row['operator_name'],))
                conn.commit()
                print(f"Data from {file_path} uploaded successfully to the operators table.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

# Example usage
if __name__ == "__main__":
    # Upload data to tables
    '''upload_users_from_csv('week11/users.csv')'''
    upload_operators_from_csv('week11/operators.csv')
    '''upload_phone_numbers_from_csv('week11/phone_numbers.csv')'''
