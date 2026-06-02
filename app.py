from flask import Flask,render_template,request,redirect
import sqlite3
app=Flask(__name__)
DATABASE="lost_found.db"
def get_db_connection():
    connection=sqlite3.connect(DATABASE)
    connection.row_factory=sqlite3.Row
    return connection
@app.route("/")
def home():
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("""
SELECT * FROM items
                   WHERE status =?
                   ORDER BY id DESC
                   """,("Active",))
    items=cursor.fetchall()
    connection.close()
    return render_template(
        "home.html",
        items=items
    )
@app.route("/report-lost",methods=["GET","POST"])
def report_lost():
    if request.method=="POST":
        name=request.form["name"].strip()
        description=request.form["description"].strip()
        location=request.form["location"].strip()
        contact=request.form["contact"].strip()
        if not name:
            return "Name is required"

        if not description:
            return "Description is required"

        if not location:
            return "Location is required"

        if not contact:
           return "Contact is required"
        connection = get_db_connection()
        cursor=connection.cursor()
        cursor.execute("""
            INSERT INTO items
            (type,name,description,location,contact,status,date_posted)
            VALUES(?,?,?,?,?,?,DATE('now'))"""
        ,(
            "Lost",
            name,
            description,
            location,
            contact,
            "Active"
        ))
        connection.commit()
        connection.close()
        return f"Lost item recieved : {name}"
    return render_template("report_lost.html")
@app.route("/report-found",methods=["GET","POST"])
def report_found():
    if request.method=="POST":
        name=request.form["name"].strip()
        description=request.form["description"].strip()
        location=request.form["location"].strip()
        contact=request.form["contact"].strip()
        if not name:
            return "Name is required"

        if not description:
            return "Description is required"

        if not location:
            return "Location is required"

        if not contact:
           return "Contact is required"
        connection = get_db_connection()
        cursor=connection.cursor()
        cursor.execute("""
            INSERT INTO items
            (type,name,description,location,contact,status,date_posted)
            VALUES(?,?,?,?,?,?,DATE('now'))"""
        ,(
            "Found",
            name,
            description,
            location,
            contact,
            "Active"
        ))
        connection.commit()
        connection.close()
        return f"Found item recieved : {name}"
    return render_template("report_found.html")
@app.route("/lost-items")
def lost_items():
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("""
SELECT * FROM items
                   WHERE type = ?
                   AND status=?
                   ORDER BY id DESC""",("Lost","Active"))
    items=cursor.fetchall()
    connection.close()
    return render_template("lost_items.html",items=items)
@app.route("/found-items")
def found_items():
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("""
SELECT * FROM items
                   WHERE type = ?
                   AND status=?
                   ORDER BY id DESC""",("Found","Active"))
    items=cursor.fetchall()
    connection.close()
    return render_template("found_items.html",items=items)
@app.route("/claim-item/<int:item_id>")
def claim_item(item_id):
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("""
UPDATE items
                   SET status=?
                   WHERE id=?"""
                   ,("Claimed",item_id))
    connection.commit()
    connection.close()
    return redirect("/found-items")
if __name__=="__main__":
    app.run(debug=True)