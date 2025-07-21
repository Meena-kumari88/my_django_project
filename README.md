# 📝 My Django Project

## 📁 Project Structure

MY_DJANGO_PROJECT/
│
├── config/ # (Virtual environment or settings folder)
├── env/ # (Python virtual environment folder)
│
├── my_project/ # Django main project folder
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
│
├── my_django_project/ # Django app folder
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── migrations/
│ └── templates/
│ └── my_django_project/
│ ├── base.html
│ └── user/
│ ├── detail.html
│ ├── new_user.html
│ └── users.html
│
├── db.sqlite3
├── manage.py
├── .gitignore

## ⚙️ Setup Instructions

1. Create virtual environment:

py -m venv env


2. Activate the environment:

env\\Scripts\\activate     # For Windows
source env/bin/activate    # For Linux/macOS


3. Create Django project:

django-admin startproject my_project


4. Create Django app inside project folder:

python manage.py startapp my_django_project


5. Run the app:

py manage.py runserver

6. Apply migrations (run these from your project path like: (env) PS C:\\Users\\...\\my_project>):

py manage.py makemigrations
py manage.py migrate
py manage.py runserver


---

## 🛠️ Project Description

This is a simple Django project that shows only the Users' information like their ID, Name, Email, and Role.  
You can add new users, view a list of all users, and view details of a specific user.  
It also includes a route \`/hello\` that returns the string **"Hello, World!"**.  
Tech used: **Django, HTML, Tailwind CSS**

---

## 💾 Database Interaction

Custom Users model created with the following fields:
- id (int, primary key)
- name (varchar)
- email (varchar)
- role (varchar)

### SQL-like queries using Django ORM (run inside shell):


py manage.py shell
from my_django_project.models import User

# Insert user
User.objects.create(name="Rani", email="rani@gmail.com", role="user")

# Retrieve all users
User.objects.all()
for user in User.objects.all():
    print(user.id, user.name, user.email, user.role)

# Retrieve user by ID
user = User.objects.get(id=2)
print(user.name, user.email, user.role)


---

## 🌐 Routes

- \`/hello\` → Returns "Hello, World!"
- \`/users\` → Display list of users in an HTML table
- \`/new_user\` → Render form to add a new user
- \`/users/<id>\` → Show details of a specific user

**urlpatterns:**

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('users/', views.user_list, name='users'),
    path('new_user/', views.new_user, name='new_user'),
    path('users/<int:id>/', views.user_detail, name='user_detail'),
]


---

## 🖥️ Git Workflow & Contribution

1. Create your GitHub repo (e.g. my_django_project)

2. In your local machine:


git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Meena-kumari88/my_django_project.git
git branch -M main
git push -u origin main


---


