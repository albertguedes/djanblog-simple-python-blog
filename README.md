# Djanblog

A simple blog built with **Django**, Bootstrap, and jQuery. Features include post management, categories, contact form, and a populate command for testing with fake data.

## Features

- **Public pages**: Home (latest posts), post viewing, about, contact
- **Admin dashboard**: Post and category management
- **Content**: Categories, posts with rich text
- **Testing**: Fake data population via Django management command
- **Contact**: Email contact form

## Tech Stack

- Django 5.x
- Bootstrap 5.x
- jQuery 3.x
- SQLite (dev)

## Installation

```bash
git clone https://github.com/albertguedes/djanblog-simple-python-blog.git
cd djanblog-simple-python-blog
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py populate   # Populate with fake posts
python manage.py runserver
```

Access at `http://127.0.0.1:8000`

## License

MIT License - see [LICENSE](LICENSE)
