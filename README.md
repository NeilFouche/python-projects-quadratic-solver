# Basic Flask app
This project is about creating and deploying a Flask app.

As an example, this application computes the roots of a quadratic equation. The user specifies the coefficients and the app computes the roots. Real roots are computed while complex roots are noted.

## Folder Structure
```quadratic_solver/
├── app.py           # Main Flask app
├── templates/
│   └── index.html   # HTML template for form and results
├── requirements.txt # Dependencies
└── README.md        # Basic docs
```

## Project setup
* Create a project folder
* Create a virtual environment for the project
  * Run `pipenv shell`
  * Activate the venv:
    * Run `C:\Users\...\.virtualenvs\quadratic-solver...\scripts\activate.ps1`
* Install Flask
  * Run `pipenv install flask`
* Create `requirements.txt`
  * Run `pip freeze > requirements.txt`
  * Add `gunicorn`

## Develop application logic
* Create `app.py`
* Create the HTML Template
  * Create a `template` folder
  * Add `index.html`
* Document the app
  * Add `README.md`

## Test and iterate
* Run the app
  * Run `python app.py`
* Preview the app
  * Open the app at the localhost

## Create local and remote `git` repositories
Commit the source code to a local repository and then push it to a remote repository where the host can access it.

* Review and commit the source code
  * Run `git commit -m 'Initial commit'`
  * Create a remote repository on GitHub
    * Log in and create remote repository
    * Follow the instructions to link the local repository with the remote repository
  * Push the code to the remote repository
    * This step is included as part of the steps to link the local and remote repos

## Deploy the application
Use render.com to host the application.

* Sign up at render.com
* Create a new *Web Service*
  * Connect the remote GitHub repo
* Settings:
  * Runtime: Python
  * Build command: `pip install -r requirements.txt`
  * Start command: `gunicorn app:app`

Access the app at the provided URL.