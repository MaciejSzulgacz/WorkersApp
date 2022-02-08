# Django Application #

### Introduction ###

This application is workers database. By downloading the report in .csv format, 
you can check the average age for the professions covered by workers.

### Technology stack ###

Python 3.8.10, Django 4.0, Docker, Git

### Requirements ###

* Python 3.8.10
* Unoccupied port 8000

### Prepare virtualenv (Linux) ###

* Prepare directory for virtual env (on the root of project):
	`mkdir venv`
* Prepare virtual env module:
	`sudo apt-get install python3-venv`
* Create venv:
	`python3 -m venv ./venv/`
* Checkout to venv:
	`source venv/bin/activate`
* Install requirements:
	`pip install -r requirements.txt`
* Check requirements:
	`pip list`

### Run application locally ###

* Source the virtual environment:
    `source ./vevn/bin/activate`
* Make migrations:
	`python3 manage.py migrate`
* Run django application:
    `python3 manage.py runserver`