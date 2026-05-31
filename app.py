from flask import Flask
import sqlite3
app=Flask(__name__)
DATABASE="lost_found.db"
def get_db_connection():
    connection=sqlite3.connect(DATABASE)
    connection.row_factory=sqlite3.Row
    return connection
@app.route("/")
def home():
    return "Lost & Found backend running"
if __name__=="__main__":
    app.run(debug=True)