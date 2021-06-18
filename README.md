# BookWorkshop
## Project setup
- `cd bookshop` 
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`

## Start Develop
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`
## init data
- `python manage.py loaddata fixdata/auth.user.json`
- `python manage.py loaddata fixdata/Contact.json`
- `python manage.py loaddata fixdata/Category.json`
- `python manage.py loaddata fixdata/bookshop.json`
- `python manage.py loaddata fixdata/PostImage.json`