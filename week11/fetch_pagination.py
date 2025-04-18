import psycopg2
from config import load_config

def fetch_paginated_data(table_name, limit, offset):
    """
    Fetch data from a table with pagination.

    :param table_name: Name of the table to query.
    :param limit: Number of rows to fetch.
    :param offset: Number of rows to skip before starting to fetch.
    :return: List of rows fetched from the table.
    """
    config = load_config()
    try:
        # Connect to the PostgreSQL database
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                # Prepare and execute the query
                query = f"SELECT * FROM {table_name} LIMIT %s OFFSET %s"
                cursor.execute(query, (limit, offset))

                # Fetch the results
                rows = cursor.fetchall()

                return rows
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"Database error: {e}")
        return []

if __name__ == '__main__':
    table_name = "operators"  # Replace with other table name
    limit = 5  # Number of rows per page
    offset = 0  # Start from the first row

    # Fetch the first page of data
    rows = fetch_paginated_data(table_name, limit, offset)

    if rows:
        print("Fetched rows:")
        for row in rows:
            print(row)
    else:
        print("No data found.")