#### if not installed
#### pip install virtualenv

#### in case the folder env does not exists in the project
#### python -m venv env

#### activate the virtual environment
// using cmd
#### env\Scripts\activate.bat   

#### pip install -r requirements.txt

// database
#### python manage.py makemigrations appCar

#### python manage.py migrate
//dummy data
#### python manage.py generate_dummy_data

//serve the pages

#### python manage.py runserver 9000 // or any other available port
