from flask import Flask, render_template, request
import random

app = Flask(_name_)

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
ROOMS = 4  # Number of available lecture rooms

# Function to generate the timetable
def generate_timetable(teachers, subjects):
    timetable = {day: [] for day in DAYS}
    
    for day in DAYS:
        available_teachers = teachers.copy()
        available_subjects = subjects.copy()
        for hour in range(9, 16):  # 9 AM - 4 PM (college hours)
            if hour == 12:  # Skip Lunch Break
                continue

            if not available_teachers or not available_subjects:
                break  # Stop if no more subjects or teachers left

            subject = random.choice(available_subjects)
            teacher = random.choice(available_teachers)
            room = random.randint(1, ROOMS)

            timetable[day].append(f"{hour}:00 - {hour+1}:00 | {subject} ({teacher}) | Room {room}")

            available_subjects.remove(subject)
            available_teachers.remove(teacher)

    return timetable

@app.route("/", methods=["GET", "POST"])
def home():
    timetable = None
    if request.method == "POST":
        teachers = request.form.getlist("teacher")
        subjects = request.form.getlist("subject")
        timetable = generate_timetable(teachers, subjects)

    return render_template("index.html", timetable=timetable)

if _name_ == "_main_":
    app.run(debug=True)