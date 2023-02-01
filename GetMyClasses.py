import sqlite3

def get_table_data(db_file, table_name, courses):
    db_file = db_file +".db"
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    courses = tuple(courses)
    query = f"SELECT * FROM {table_name} WHERE course IN {courses}"

    try:
        c.execute(query)
        data = c.fetchall()
    except sqlite3.OperationalError:
        print(f"Table '{table_name}' not found in database '{db_file}'.")
        data = None

    conn.close()
    return data
