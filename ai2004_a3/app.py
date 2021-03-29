from flask import Flask, json, jsonify
import mysql.connector
from mysql.connector import MySQLConnection

app = Flask(__name__)


def create_conn():
    conn = MySQLConnection(host="127.0.0.1",
                           user="root",
                           password="1234",
                           database="tejas",
                           auth_plugin='mysql_native_password')
    return conn


@app.route("/")
def home():
    return ""


@app.route("/read")
def read():
    query = "SELECT * FROM tejas.assignment_3 where first_name = 'Tejas';"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    resp = jsonify(row)
    return (resp)


@app.route("/readAll")
def readAll():
    query = "SELECT * FROM tejas.assignment_3"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    resp = jsonify(row)
    return (resp)


@app.route('/create')
def create():
    first_name = "John"
    last_name = "Mckenzie"
    dob = "1990-02-27"
    amount_due = "10000"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tejas.assignment_3(first_name, last_name, dob, amount_due) VALUES (%s, %s, %s, %s)",
                   (first_name, last_name, dob, amount_due))
    conn.commit()
    return "Inserted New Record"


@app.route("/update")
def update():
    query = "UPDATE tejas.assignment_3 SET amount_due = 4500 WHERE first_name = 'John';"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return "Updated Record"


@app.route("/delete")
def delete():
    query = "DELETE FROM tejas.assignment_3 where first_name = 'John';"
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return "Deleted record"


if __name__ == '__main__':
    app.run(debug=True)