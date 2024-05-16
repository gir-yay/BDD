# BDD

##Requirements for the project

#### #if not installed

#### pip install django

#### pip install djongo

#### python -m pip install pymongo==3.12.3

#### #if not installed

#### pip install faker

#### python -m pip install xhtml2pdf pip --upgrade
#### pip install celery[redis]
==> local mongoDB
==> create DB called locationv_db
==> open cmd in the project folder

// or setting up  a virtual environment :

#### pip install virtualenv
#### python -m venv <virtual-environment-name>
// using cmd
#### env/Scripts/activate.bat   
// using powershell
#### env/Scripts/activate.ps1
// now run the previous pip 
// in addition :
#### pip install pytz

#### pip freeze > requirements.txt
//case of installing the requirements of a project
#### pip install -r requirements.txt

// database
#### python manage.py makemigrations appCar

#### python manage.py migrate
//dummy data
#### python manage.py generate_dummy_data

//serve the pages

#### python manage.py runserver 9000 // or any other available port

==> CTRL + click on the resulting local link
