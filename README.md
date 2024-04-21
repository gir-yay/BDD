# BDD
##Requirements for the project

#### pip install django
#### pip install djongo
#### python -m pip install pymongo==3.12.3

==> local mongoDB
==> create DB called <db-name>

==> open cmd in the project folder

run :
#### python manage.py makemigrations appCar
#### python manage.py migrate

// Generate dummy data for the database
// do not use yet ... Not set up
#### pip install faker 
#### python manage.py generate_dummy_data

//serve the pages
#### python manage.py runserver 9000  // or any other available port
			

==> CTRL + click on the resulting local link
