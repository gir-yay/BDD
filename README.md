#### if not installed
#### pip install virtualenv

#### in case the folder env does not exists in the project
#### python -m venv env

#### activate the virtual environment
// using cmd
#### env\Scripts\activate.bat   

#### (env) pip install -r requirements.txt

// database
#### (env) python manage.py makemigrations appCar

#### (env) python manage.py migrate
//dummy data
#### (env) python manage.py generate_dummy_data

//serve the pages

#### (env) python manage.py runserver 9000 // or any other available port

[!note "NB: Do not add (env) to the commands"]
