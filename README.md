# Django Discussion Board

A simple discussion board web application built with Django. Users can create posts, view posts, and leave replies on posts. The project uses Bootstrap for a modern and responsive interface.

## Features

- Create and view discussion posts.
- Reply to individual posts.
- Basic admin interface for managing posts and replies.
- Modern design using Bootstrap 5.

## Requirements

- Python 3.10+ (tested with Python 3.13)
- Django 5.1+
- SQLite (default; you can use another DB engine if needed)
- pip

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Lauri221/django_web_app_discussion_board_4_ai_course.git 
   cd django-discussion-board
2. **Create and activate a virtual environment:**
On Windows:
  python -m venv venv
  venv\Scripts\activate

3. **Install the dependencies:**
   pip install django

4. **Apply migrations:**
  python manage.py makemigrations
  python manage.py migrate

5. **Create a superuser (optional, for admin access):**
   python manage.py createsuperuser

##Running the App
**Start the development server with:**
  python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000 to view the discussion board.

##Running Tests
To run the tests for the application, execute:
  python manage.py test

##Project Structure
mysite/
├── discussion/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   └── discussion/
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── create_post.html
│   │       └── create_reply.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── tests.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

##Customization
Customize the templates located in discussion/templates/discussion/ to change the look and feel.
Update styles in base.html or add custom CSS as needed.

##Contributing
If you’d like to contribute to this project, feel free to fork the repository and submit a pull request.

##License
This project is licensed under the MIT License.
