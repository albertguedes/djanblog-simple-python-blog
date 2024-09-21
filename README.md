[![Stargazers](https://img.shields.io/github/stars/djanblog/djanblog?style=social)](https://github.com/djanblog/djanblog/stargazers)
[![Forks](https://img.shields.io/github/forks/djanblog/djanblog?style=social)](https://github.com/djanblog/djanblog/network/members)
[![Watchers](https://img.shields.io/github/watchers/djanblog/djanblog?style=social)](https://github.com/djanblog/djanblog/watchers)

# DjanBlog - A simple blog made with Django Framework

This project is a simple blog made with Django Framework.
It uses bootstrap and jquery, so it's fully responsive.
Come with a SQLITE3 database as sample.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=ffdd54)
![SQLite3](https://img.shields.io/badge/sqlite3-000000?style=for-the-badge&logo=sqlite3&logoColor=ffdd54)
![pytest-django](https://img.shields.io/badge/pytest-django-FFDD54?style=for-the-badge&logo=pytest-django&logoColor=000000)
![Bootstrap](https://img.shields.io/badge/bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![jQuery](https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)

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
