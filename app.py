from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        print("Username:", username)
        print("Password:", password)
        print("Role:", role)

        if role == "employee":
            return redirect(url_for("employee"))

        elif role == "manager":
            return redirect(url_for("manager"))

        elif role == "admin":
            return redirect(url_for("admin"))

    return render_template("login.html")

@app.route("/employee")
def employee():
    return render_template("employee.html")

@app.route("/manager")
def manager():
    return render_template("manager.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)