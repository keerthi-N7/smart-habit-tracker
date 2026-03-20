from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# TEMPORARY STORAGE (for MVP)
users = []
habits = []


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# REGISTER PAGE
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = {
            "name": name,
            "email": email,
            "password": password
        }

        users.append(user)

        print("Registered Users:", users)

        return render_template("success.html")

    return render_template("register.html")


# LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        for user in users:
            if user["email"] == email and user["password"] == password:
                return redirect(url_for("dashboard"))

        return "Invalid Login"

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", habits=habits)


# ADD HABIT
@app.route("/add_habit", methods=["GET", "POST"])
def add_habit():

    if request.method == "POST":

        habit_name = request.form["habit_name"]
        description = request.form["description"]
        category = request.form["category"]
        reminder_time = request.form["reminder_time"]
        priority = request.form["priority"]

        habit = {
            "habit_name": habit_name,
            "description": description,
            "category": category,
            "reminder_time": reminder_time,
            "priority": priority,
            "completed": False
        }

        habits.append(habit)

        print("Habits:", habits)

        return render_template("success.html")

    return render_template("add_habit.html")

@app.route("/complete_habit/<int:index>")
def complete_habit(index):

    if 0 <= index < len(habits):
        habits[index]["completed"] = True

    return redirect(url_for("dashboard"))
# SUCCESS PAGE
@app.route("/success")
def success():
    return render_template("success.html")


# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)