from flask import Flask, render_template, request, jsonify
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

    cur.execute("SELECT * FROM menu_items")
    menu_items = cur.fetchall()

    cur.execute("SELECT * FROM orders ORDER BY created_at DESC")
    orders = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", menu_items=menu_items, orders=orders)


@app.route("/place_order", methods=["POST"])
def place_order():
    data = request.get_json()
    items = data["items"]

    conn = get_conn()
    cur = conn.cursor()

    for item in items:
        for i in range(item["quantity"]):
            cur.execute(
                "INSERT INTO orders (item_name) VALUES (%s)",
                (item["name"],)
            )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
