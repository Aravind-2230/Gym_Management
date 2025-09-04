# Fitness Tracker

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
   git clone https://github.com/Aravind-2230/Gym_Management.git
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

## Unit test using pytest

- To run the unit test using pytest from your local ; Make sure you install the pytest from pre-requistes using the `requirements.txt` file
- Run the unit test by `pytest test.py`

`venv1\Lib\site-packages\werkzeug\routing\rules.py:731
venv1\Lib\site-packages\werkzeug\routing\rules.py:731
venv1\Lib\site-packages\werkzeug\routing\rules.py:731
venv1\Lib\site-packages\werkzeug\routing\rules.py:731
venv1\Lib\site-packages\werkzeug\routing\rules.py:731
venv1\Lib\site-packages\werkzeug\routing\rules.py:731
  D:\Gym_Mang\flask-fitness-tracker\venv1\Lib\site-packages\werkzeug\routing\rules.py:731: DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
    ret[-1] = ast.Str(ret[-1].s + p.s)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================= `4 passed`, 63 warnings in 1.60s =========================================`

# Containerization

- To run the application in container based environment, First intall the `Docker Desktop` on windows machine
- Steps to build the local container image

`docker build -t gym_mang .`  # Name of the container image is `gym_mang`
`docker images` # List all the images

- REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
gym_mang                      latest    3de3d7e582c3   2 minutes ago   173MB
nginx                         latest    97662d24417b   7 months ago    192MB
ubuntu                        latest    a04dc4851cbc   7 months ago    78.1MB
mysql                         5.7       5107333e08a8   21 months ago   501MB

# Steps to build the local container and run it

- `docker run -d --name gym-app -p 5000:5000 gym_mang`  # Name of container is `gym-app`
3f22b2343b14e966d0d802a7f02648d684a4582cf50355ae97bb80e142027cbc

- `docker ps`

CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
3f22b2343b14   gym_mang   "flask run --host 0.…"   2 minutes ago   Up 2 minutes   0.0.0.0:5000->5000/tcp   gym-app

- `docker logs -f 3f22b2343b14`   

* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
