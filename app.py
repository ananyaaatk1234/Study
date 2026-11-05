from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
import prac


app = Flask(__name__)
app.secret_key = "change-this-to-a-long-random-secret"


@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        connection = prac.connection_db()
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT Employee_Name, Username, Password, Role
            FROM admin_log
            WHERE Username = ?""", (username,))

        user = cursor.fetchone()

        if user is None:
            connection.close()
            flash("Invalid username or password.")
            return render_template("login.html")
        
        employee_name, db_username, stored_password, role = user

        # Check password
        password_valid = False

        try:
            password_valid = check_password_hash(
                stored_password, password
            )
        except (ValueError, TypeError):
            password_valid = False

        # Convert an old plain-text password into a hash
        if not password_valid and stored_password == password:

            password_valid = True

            new_hash = generate_password_hash(password)
            cursor.execute("""
                UPDATE admin_log
                SET Password = ?
                WHERE Username = ?
            """, (new_hash, db_username))

            connection.commit()

        connection.close()

        if not password_valid:
            flash("Invalid username or password.")
            return render_template("login.html")

        # Store login information
        session.clear()
        session["username"] = db_username
        session["employee_name"] = employee_name
        session["role"] = role.strip().lower()

        # Redirect according to database role
        if session["role"] == "employee":
            return redirect(url_for("employee"))

        elif session["role"] == "manager":
            return redirect(url_for("manager"))

        elif session["role"] == "admin":
            return redirect(url_for("admin"))

        session.clear()
        flash("Invalid account role.")
        return redirect(url_for("login"))

    return render_template("login.html")

def role_required(required_role):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            if "username" not in session:
                flash("Please log in first.")
                return redirect(url_for("login"))

            if session.get("role") != required_role:
                flash("You do not have permission.")
                return redirect(url_for("login"))

            return function(*args, **kwargs)

        return wrapper

    return decorator

@app.route("/employee")
@role_required("employee")
def employee():
    return render_template("employee.html")

@app.route("/manager")
@role_required("manager")
def manager():
    return render_template("manager.html")

@app.route("/admin")
@role_required("admin")
def admin():
    return render_template("admin.html")

@app.route("/logout")
def logout():

    session.clear()
    flash("You have been logged out.")

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

    https://chatgpt.com/c/6ae008a2-5a10-83ec-ae80-17fdbd772fb4