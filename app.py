from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        print("Email:", email)
        print("Password:", password)

        return "Login Submitted Successfully"

    return render_template("login.html")


# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        print("Name:", name)
        print("Email:", email)
        print("Password:", password)

        return "Registration Successful"

    return render_template("register.html")


# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)