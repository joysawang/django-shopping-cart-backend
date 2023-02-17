python3 -m venv env
source env/bin/activate
deactivate

docker-compose up

sudo docker compose run web django-admin startproject composeexample .

docker-compose run web python manage.py startapp api