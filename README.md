# Kaizen Faculty Evaluation

### Create a virtual environment
In this project, we are using pipenv packaging tool to manage dependcies and virtual environemnt. To activate the virtual environment, run the following command. Make sure the directory of your terminal is in the project folder. 
```python
python -m pipenv shell
```

### Install package dependencies
No need to worry about manual installing of package dependencies because there is a provided pipfile. All you need to do is to run the following command.
```python
python -m pipenv install
```

### Run the main entry point of the program
You will always use this particular command in the development because it is the main entry point of the program.
```python
python manage.py runserver
```