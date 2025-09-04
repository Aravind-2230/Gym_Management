from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # Initialize the Flask application

workouts = [] # In-memory storage for workouts

@app.route("/", methods=["GET"]) # Define the route for the home page
def index():
    return render_template("index.html", workouts=workouts)

@app.route("/add", methods=["POST"]) # Define the route to add a new workout
def add():
    workout = request.form.get("workout")
    duration = request.form.get("duration")
    if workout and duration:
        try:
            duration_int = int(duration)
            workouts.append({"workout": workout, "duration": duration_int})
        except ValueError:
            pass  # Optionally handle invalid input
    return redirect(url_for("index"))

if __name__ == "__main__": # Run the application
    app.run(debug=True)