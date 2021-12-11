# IZZI-test-task

## Steps to run project locally:
1. Clone this repo locally.
2. To install all required libs to your venv run: pip install -r requirements.txt
3. To setup db run:
 - python manage.py makemigrations
 - python manage.py migrate
4. For testing issues create super user running the next command: python manage.py createsuperuser
5. Run server with the command: python manage.py runserver

___

## To try out main features:
1. Users import:
 - open admin panel;
 - go to Users section;
 - at the top, select csv-file with users data, hit "Upload";
 - on the reloaded page you can see the newly imported users.
2. Retrieving all users list:
 - use /api/users/ endpoint.
3. Retrieving users list according to their registration date:
 - use /api/users/ endpoint passing the registration date as 'date' get parameter (e.g.: /api/users/date_joined/?date=2018-05-09 , to retrive users registered on 2018-05-09).
