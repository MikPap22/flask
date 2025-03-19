from flask import Flask, render_template, request

app = Flask(__name__)


import sqlite3
con = sqlite3.connect("login.db")
cur = con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS Users ( 
                UserName VARCHAR(10) NOT NULL PRIMARY KEY,
                UserPassword VARCHAR(20) NOT NULL
                )""")
con.commit()
con.close()


@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if  "bob" == request.form["username"] and \
            "123" == request.form["password"]:
            return "Hello " + "bob"
        else:
            return "wrong password"


@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
       
        return "signup success"

if __name__ == "__main__":
    app.run(debug = True)

