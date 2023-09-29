# Student Management

This Python application is a simple course management that is a web-based application developed using Django, designed to help users to manage their short-term courses. This system allows users to create, delete, view, and edit short-term courses through a user-friendly dashboard, as well as manage user accounts and passwords.

## Features

- Create new short-term courses with details such as course name, description, image etc.
- Delete existing courses.
- View a list of all available courses.
- Edit course information.
- User authentication and password management.
- User-friendly dashboard for easy navigation.


## Prerequisites

Make sure you have the following prerequisites installed before setting up the project:

Python (3.6 or higher)
## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/swalihmp/Student-Management.git

   Then create a virtual environment using the command "python3 -m venv env" and "source env/bin/activate"

   Then install all the dependencies using "pip install -r requirements.txt"



   2. Then direct to the Project Directory and follow the commands for run the project.
         "python manage.py makemigrations",
         "python manage.py migrate",
         "python manage.py runserver"


Pls note default Admin id and pass is :- Email : "admin@gmail.com"
                                         Pass : 12345

Pls note default User id and pass is :- Email : "swali@gmail.com"
                                         Pass : 12345

You can create the user using the command "python manae.py createsuperuser"
