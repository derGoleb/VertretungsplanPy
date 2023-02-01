import sqlite3

def replace_abbreviations(database_name):
    database_name = database_name+".db"
    # Dictionary that maps abbreviations to real names
    abbreviation_mapping = {
        "Ost": "Osterhoff",
        "Nit": "Nitsch",
        "Ar": "Arndt",
        "Bgh": "Bögershausen",
        "Bo": "Born",
        "Le": "Lenz",
        "Hue": "Hüttner",
        "Win": "Winter",
        "Dru": "Druciak",
        "Stm": "Strothmüller",
        "Har": "Hartmann",
        "Reg": "Regner",
        "Bas": "Bass",
        "Mue": "Müller-Görgner",
        "Prt": "Preukschat",
        "Klz": "Kleinholz",
        "Gru": "Grunau",
        "Fb": "Fürstenberg",
        "Hub": "Hubanic",
        "Egb": "Engelbarts",
        "Al": "Albers",
        "Sik": "Sikora",
        "Du": "Dullat",
        "Kos": "Köster",
        "Rei": "Reinecke-Krämer",
        "No": "Nolte",
        "Woe": "Wöhl-Beer",
        "Klw": "Kleinwächter",
        "Sdr": "Schröder",
        "Ris": "Riese",
        "Psm": "Poschmann",
        "Ba": "Barsnick",
        "Pac": "Pack",
        "Por": "Porscha",
        "Sec": "Sechelmann",
        "Sar": "Sarx",
        "Sem": "Semerad",
    }

    # Connect to the SQLite database
    conn = sqlite3.connect(database_name)

    # Cursor object to execute SQL queries
    cursor = conn.cursor()

    # Retrieve the names of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = cursor.fetchall()

    # Loop through each table in the database
    for table_name in table_names:
        # Loop through each key-value pair in the abbreviation_mapping dictionary
        for abbreviation, real_name in abbreviation_mapping.items():
            # Replace the abbreviated name with the real name in all columns of the table
            cursor.execute(f"UPDATE {table_name[0]} SET teacher = REPLACE(teacher, '{abbreviation}', '{real_name}')")
            # Replace double spaces with single spaces in the course column
            cursor.execute(f"UPDATE {table_name[0]} SET course = REPLACE(course, '  ', ' ')")

    # Save the changes to the database
    conn.commit()
