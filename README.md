# Quadratic Equation Solver

A Flask web app to solve quadratic equations and visualize them with a plot.

## Setup
1. Clone repo.
2. `python -m venv venv` or `pipenv shell`
3. Activate venv: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux).
4. `pip install -r requirements.txt`
5. `python app.py`

Access at http://127.0.0.1:5000/

## Features
- Solve quadratic equations (ax² + bx + c = 0).
- Display real roots or error messages.
- Visualize the quadratic function with a Matplotlib plot.

## Dependencies
- Flask
- Matplotlib
- Gunicorn (for deployment)