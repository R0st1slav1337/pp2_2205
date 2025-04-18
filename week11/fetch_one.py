import psycopg2
from config import load_config

def get_operators():
    """ Retrieve data from the operators table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT operator_id, operator_name FROM operators ORDER BY operator_name")
                print("The number of operators:", cur.rowcount)
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        conn.rollback()

if __name__ == '__main__':
    get_operators()