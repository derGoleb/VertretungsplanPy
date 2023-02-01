import sqlite3
from bs4 import BeautifulSoup
import re
import os

def parse_html_table(html_file_path, database_name):

    database_name = database_name+".db"
    def sanitize_class_name(class_name):
        return re.sub(r"[^a-zA-Z0-9_]", "_", class_name)

    def add_underscore_to_class_name(class_name):
        if class_name[0].isdigit():
            class_name = f"_{class_name}"
        return class_name


    if os.path.exists(database_name):
        os.remove(database_name)

    # Open the HTML file and create a BeautifulSoup object
    with open(html_file_path, encoding="iso-8859-1") as f:
        soup = BeautifulSoup(f, features="html.parser", from_encoding="iso-8859-1")

    # Find the table in the HTML file
    table = soup.find("table", {"class": "mon_list"})

    # Create an empty dictionary to store the class tables
    class_tables = {}

    # Iterate over the rows of the table
    for row in table.find_all("tr"):
        # Find the first cell in the row (the class)
        first_cell = row.find("td")

        # If the first cell is empty, skip the row
        if not first_cell:
            continue

        # If there is no table for the class, create a new one
        class_name = first_cell.text.strip()
        if class_name not in class_tables:
            class_tables[class_name] = []

        # Store the data for the row in the table for the class
        class_tables[class_name].append([cell.text.strip() for cell in row.find_all("td")])

    # Iterate over the class tables
    for class_name, table in class_tables.items():
        # Create a new list to store the updated table
        updated_table = []

        # Iterate over the rows in the table
        for row in table:
            # If the row has more than one element, append it to the updated table
            if len(row) > 1:
                updated_table.append(row)

        # Update the class table in the dictionary with the updated table
        class_tables[class_name] = updated_table

    # Iterate over the class tables and delete the first column of each table
    for key in class_tables:
        for sublist in class_tables[key]:
            del sublist[0]



        # Create a connection to the SQLite database
    conn = sqlite3.connect(database_name)

    # Iterate over the class tables
    for class_name, table in class_tables.items():
        # Sanitize the class name and add an underscore if necessary
        class_name = sanitize_class_name(class_name)
        class_name = add_underscore_to_class_name(class_name)

        # Create a new table in the database for the class
        conn.execute(f"CREATE TABLE {class_name} (periods TEXT, teacher TEXT, course TEXT, room TEXT, type TEXT, info TEXT)")

        # Insert the data for the rows into the table for the class
        for row in table:
            conn.execute(f"INSERT INTO {class_name} VALUES (?, ?, ?, ?, ?, ?)", row)





    # Save the changes to the database
    conn.commit()


    # Close the connection to the database
    conn.close()