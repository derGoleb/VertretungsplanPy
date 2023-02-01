import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('heute.db')

# Cursor object to execute SQL queries
cursor = conn.cursor()

# Check if the "Q2" table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Q2'")
if cursor.fetchone() is None:
    print("Es fällt nichts aus")


# Retrieve the records from the "Q2" table where the "course" column has the values "E L2", "D L2", or "E G1"
cursor.execute("SELECT * FROM Q2 WHERE course IN ('E  L2', 'D  L2', 'E  G1')")

# Fetch the records and print them
records = cursor.fetchall()
for record in records:
    print(record)

# Close the database connection
conn.close()