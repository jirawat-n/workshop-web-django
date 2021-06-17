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
- `python manage.py loaddata fixtdata/auth.user.json`
- `python manage.py loaddata fixtdata/Contact.json`
- `python manage.py loaddata fixtdata/Category.json`
- `python manage.py loaddata fixtdata/bookshop.json`
- `python manage.py loaddata fixtdata/PostImage.json`