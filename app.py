from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="rayaanyasar",
        password="Rayaan2007!",
        database="heavenly"
    )


@app.route("/")
def home():
    conn = get_conn()
    cur = conn.cursor()
    

    return render_template("index.html", menu_items=menu_items)


if __name__ == "__main__":
    app.run(debug=True)
