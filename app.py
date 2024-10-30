from db_setup import connect_database
from flask import Flask, render_template, flash

app=Flask(__name__)
app.secret_key ="your_secret_key"


conn = connect_database()
db = conn.cursor()

def usd(value):
    return f"${value:,.2f}"

app.jinja_env.filters["usd"] = usd

@app.route("/shop", methods=["GET"])
def shop():
    all_items={}
    try:
        db.execute("SELECT * FROM inventory WHERE is_active = 'true'")
        all_items= db.fetchall()
        # 0: id 1:title 2:description 3:price 4:quantity 5:is_active
    except Exception as e:
        error_message = f"Error fetching inventory from database."
        flash(error_message, "error")
    return render_template("shop.html", all_items=all_items)
        