from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
DATABASE="lost_found.db"
def get_db_connection():
    connection=sqlite3.connect(DATABASE)
    connection.row_factory=sqlite3.Row
    return connection
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/report-lost",methods=["GET","POST"])
def report_lost():
    if request.method=="POST":
        name=request.form["name"]
        description=request.form["description"]
        location=request.form["location"]
        contact=request.form["contact"]
        return f"Lost item recieved : {name}"
    return render_template("report_lost.html")
@app.route("/report-found",methods=["GET,POST"])
def report_found():
    if request.method=="POST":
        name=request.form["name"]
        description=request.form["description"]
        location=request.form["location"]
        contact=request.form["contact"]
        return f"Found item recieved : {name}"
    return render_template("report_found.html")
if __name__=="__main__":
    app.run(debug=True)