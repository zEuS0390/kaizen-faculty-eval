python -m pipenv install
cls
cd ./facultyeval
cls
python -m pipenv run python ./manage.py makemigrations
cls
python -m pipenv run python ./manage.py migrate
cls
python -m pipenv run python ./manage.py runserver 0.0.0.0:8000
pause
