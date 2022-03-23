# Kaizen Faculty Evaluation

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