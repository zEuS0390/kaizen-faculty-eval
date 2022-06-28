[![shields](https://img.shields.io/badge/Kaizen-Faculty%20Evaluation-brightgreen)](https://github.com/zEuS-0390/kaizen-faculty-eval) [![shields](https://img.shields.io/badge/TIP-Quezon%20City-yellow)](https://www.tip.edu.ph/)
# Kaizen Faculty Evaluation
It is a web application that manages evaluation of faculty members in computer engineering department at Technological Institute of the Philippines - Quezon City. The head of the department, Engr. Cecille Venal is the client of this project and the adviser is Engr. Jonathan V. Taylar. It was conducted for the faculty members to see their performance based on three sources, which are Human Resources (HR), Academic Improvement Visitation (AIV), and Learning Management System (LMS/Canvas).

### Team Members
These are all the team members of the Faculty Evaluation Project.
1. James Joshua Balles [Data Science]
2. Zeus James Baltazar [Intelligent Systems]
3. Jholet Mae Botona [System Administration]
4. Cynna Mae Crebello [System Administration]
5. Christian Dale Dela Cruz [System Administration]
6. Ian Gabriel Marquez [System Administration]
7. Ron Rasl Parman [System Administration]
8. Francis Gener Penuliar [System Administration]

### Tools/Dependencies
The following are the requirements needed in creating the Faculty Evaluation Project.
* [**Git**](https://git-scm.com/) (Local Version Control)
* [**GitHub**](https://github.com/) (Remote Version Control) 
* [**Python**](https://www.python.org/)  (Programming Language) 
* [**Pipenv**](https://pipenv.pypa.io/) (Packaging Tool with Virtual Environment) 
* [**Django**](https://www.djangoproject.com/) (Python Web Framework) 
* [**MySQL**](https://en.wikipedia.org/wiki/MySQL) (Server-based Database)
* [**XAMPP**](https://www.apachefriends.org/) (MySQL Server)
* [**HTML/CSS/JS**](https://en.wikipedia.org/wiki/Front-end_web_development) (Web Page Fundamentals)
* [**Bootstrap**](https://getbootstrap.com/) (CSS Framework)

## Development

Before starting the web application, we need to consider these things:
1. **Environment variables** - are necessary for the application to get working. They are hidden values that must be separated to the source code. These variables are: [*EMAIL_HOST_PASSWORD*](https://docs.djangoproject.com/en/4.0/ref/settings/#email-host-password), [*EMAIL_HOST_USER*](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-EMAIL_HOST_USER), [*SECRET_KEY*](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key). The *EMAIL_HOST_USER* and *EMAIL_HOST_PASSWORD* is used in the backend for sending emails. The *SECRET_KEY* is used for providing cryptographic signing to keep the system secure.
2. **Database settings** - should be configured because all the information in the system are stored in the database. They are in the .env configuration file and will be parsed by the decouple library in settings.py. The name should exist in the database and match the credentials.

### Create a virtual environment
In this project, we are using pipenv packaging tool to manage dependencies and virtual environemnt. To activate the virtual environment, run the following command or execute
the batch file **'shell.bat'**. Make sure the directory of your terminal is in the project folder. 
```python
python -m pipenv shell
```

### Install package dependencies
No need to worry about manual installation of package dependencies because there is a provided pipfile. All you need to do is to run the following command or execute the
batch file **'install.bat'**.
```python
python -m pipenv install
```

### Run the main entry point of the program
You will always use this particular command in the development because it is the main entry point of the program. There is also a provided batch file **'runserver.bat'** to run the web application. 
```python
python manage.py runserver
```
