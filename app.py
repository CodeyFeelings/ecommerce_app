from db_setup import connect_database
from flask import Flask, render_template, flash, redirect, jsonify, request,session, g
from werkzeug.security import check_password_hash, generate_password_hash
from models import *
app=Flask(__name__)
app.secret_key ="your_secret_key"

# Session details 
@app.before_request
def before_request():
    g.user_type = session.get("user_type",None)
    

conn = connect_database()
db = conn.cursor()

def usd(value):
    return f"${value:,.2f}"

app.jinja_env.filters["usd"] = usd
# SECTION: SHOP
@app.route("/shop", methods=["GET"])
def shop():
    all_items={}
    try:
        db.execute(SELECT_ACTIVE_INVENTORY)
        all_items= db.fetchall()
        # 0: id 1:title 2:description 3:price 4:quantity 5:is_active
    except Exception as e:
        error_message = f"Error fetching inventory from database."
        flash(error_message, "error")
    return render_template("shop.html", all_items=all_items, user=g.user_type)
        
# SECTION: LOGIN
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        # get data from form
        username= request.form.get("username")
        password= request.form.get("password")
        # check that fields are filled
        if (not username) or (not password):
            return jsonify(success= False, message=f"Please enter all fields")
        # check if user data exists
        try:
            db.execute(SELECT_USERNAME,(username,))
            user_exists= db.fetchone()
            if (not user_exists):
                return jsonify(success=False, message=f"This username doesn't exist")
            # get password
            db.execute(SELECT_PASSWORD, (username,))
            user_password = db.fetchone()[0]
        except Exception as e:
            return jsonify(success=False, message=f"Error fetching data from database: {e}")
        # check that passwords match
        if (not check_password_hash(user_password, password)):
            return jsonify(success=False, message=f"Wrong Password")
        # get user_type
        try:
            db.execute(SELECT_USER_TYPE,(username,))
            session["user_type"] = db.fetchone()[0]
            
        except Exception as e:
            return jsonify(success=False, message=f"Error getting user type")
        # redirect to shop page
        success_message = f"Logged in successfully"
        flash(success_message, "success")
        return jsonify(success=True, redirect_url="/shop")
    return render_template("login.html")

# SECTION: REGISTER
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        first_name= request.form.get("first-name")
        last_name= request.form.get("last-name")
        email = request.form.get("email")
        username=request.form.get("username")
        password=request.form.get("password")
        re_password=request.form.get("re-password")
        # check all fields are entered
        if (not first_name) or (not last_name) or (not email) or (not username) or (not password) or (not re_password):
            return jsonify(success=False, message=f"Please enter all fields")
        # check that the passwords match
        if not password == re_password:
            return jsonify(success=False, message=f"Passwords Do Not Match")
        # check if email is availiable
        try:
            db.execute(SELECT_EMAIL,(email,))
            email_taken = db.fetchone()
        except Exception as e:
            return jsonify(success=False, message=f"Error checking email availability: {e}")
        if email_taken:
            return jsonify(success=False, message=f"Sorry, this email is already taken")           
        # check if username is availiable
        try:
            db.execute(SELECT_USERNAME,(username,))
            username_taken = db.fetchone()
        except Exception as e:
            return jsonify(success=False, message=f"Error checking username availability: {e}")
        if username_taken:
            return jsonify(success=False, message=f"Sorry, this username is already taken", )
        # generate hash password
        hash_password = generate_password_hash(password, method='pbkdf2:sha256')
        # insert data in table
        try:
            db.execute(REGISTER_USER,(email, username, hash_password, first_name, last_name, 'user',))
            conn.commit()
        except Exception as e:
            return jsonify(success=False, message=f"Error inserting data: {e}")
        # get user_type
        try:
            db.execute(SELECT_USER_TYPE,(username,))
            session["user_type"] = db.fetchone()[0]
        except Exception as e:
            return jsonify(success=False, message=f"Error getting user type")
        # redirect to shop page
        success_message = f"Registered successfully"
        flash(success_message, "success")
        return jsonify(success=True, redirect_url="/shop")
    return render_template("register.html")

# SECTION LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    success_message="Logged Out"
    flash(success_message, "success")
    return redirect("/shop")

# SECTION CART



