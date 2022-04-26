[![shields](https://img.shields.io/badge/Kaizen-Faculty%20Evaluation-brightgreen)](https://github.com/zEuS-0390/kaizen-faculty-eval) [![shields](https://img.shields.io/badge/TIP-Quezon%20City-yellow)](https://www.tip.edu.ph/)

## Kaizen Faculty Evaluation Documentation

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
* **Git** (Local Version Control)
* **GitHub** (Remote Version Control) 
* **Python**  (Programming Language) 
* **Pipenv** (Packaging Tool with Virtual Environment) 
* **Django** (Python Web Framework) 
* **MySQL** (Server-based Database)
* **XAMPP** (MySQL Server)
* **HTML/CSS/JS** (Web Page Fundamentals)
* **Bootstrap** (CSS Framework)

## Development

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

