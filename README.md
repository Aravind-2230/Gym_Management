# Flask Fitness Tracker

This project is a simple fitness tracker web application built using Flask. It allows users to log their workouts and view a list of logged workouts.

## Project Structure

```
GYM_MANG
├── app.py                # Main entry point of the Flask application
├── templates             # Directory for HTML templates
│   └── index.html       # Main page template with workout form
├── static                # Directory for static files (CSS, images, etc.)
│   └── style.css        # CSS styles for the application
├── requirements.txt      # List of dependencies for the project
└── README.md             # Project documentation
└── test.py               # unit test of application
```

## Requirements

To run this application, you need to have Python installed on your machine. You also need to install the required packages listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd GYM_MANG
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv1
   source venv1/bin/activate  # On Windows use `venv1\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the Flask application, run the following command:
```
python app.py or flask run
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

- On the main page, you can add a workout by entering the workout name and duration in minutes.
- Click the "Add Workout" button to log the workout.
- You can view all logged workouts on the same page.
