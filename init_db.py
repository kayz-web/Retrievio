import sqlite3
connection=sqlite3.connect("lost_found.db")
cursor=connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               type TEXT,
               name TEXT,
               description TEXT,
               location TEXT,
               contact TEXT,
               status TEXT,
               date_posted TEXT
               )
               """)
connection.commit()
connection.close()
print("Database and Table created succesfully")