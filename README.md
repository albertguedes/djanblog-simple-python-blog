# DjanBlog - A simple blog made with Django Framework

This project is a simple blog made with Django Framework.
It uses bootstrap and jquery, so it's fully responsive.
Come with a SQLITE3 database as sample.

## Requirements

- Python 3
- Django 5.0.9
- SQLite3
- pytest-django 
- Faker for python

## Features

This blog contains:

- A home page that list all posts
- A post page to show a post 
- An about page
- A contact page with a form to send an email
- A success page after sending an email
- An error page when an error occurs
- An custom "populate" command to populate the database with fake posts
- Was used bootstrap 5.3.3 and Jquery 3.7.1 for the frontend

## Installation

First, clone the repository from github:

```
git clone https://github.com/josé-da-silva/djanblog.git
```

Go to the project directory:

```
cd djanblog
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

```
source venv/bin/activate
```

Install Django:

``` 
pip install django
```

Then, install the dependencies:

```
pip install -r requirements.txt
```

Run the migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Populate the database:

```
python manage.py populate
```

Then, run the server:

```
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser and you should see the home page.

## Usage 

This project is simple enought to be expanded to your needs.
Any doubt or feedback is welcome.

## Tests

If you do some modifications on project, add or alter the tests with that come 
with the project, and run with the following command:

```
python manage.py test
```

## References

- Python Project: https://python.org/
- Django Project: https://www.djangoproject.com/
- SQLITE3: https://www.sqlite.org/
- Bootstrap: https://getbootstrap.com/
- Jquery: https://jquery.com/
- Faker: https://faker.readthedocs.io/en/master
- pytest-django: https://pytest-django.readthedocs.io/en/latest
