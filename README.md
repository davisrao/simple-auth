OVERVIEW:
* Simple auth app that allows user to log in / sign up to view 'private' page that displays their username
* Built with python / flask. Routes live on app.py file, DB models are in models.py. 
* DB is postgresql, using SQLAlchemy as ORM.
* Front end is rendered by flask using jinja templates
* Forms managed with WTForms

INSTALLING TECH STACK (homebrew):
* Python: MacOS comes with python installed but it is an old version. To use homebrew to install latest: brew install python
* Database: install postgres with homebrew -- brew install postgresql@13
* Start postgres: brew services start postgresql

INSTALLING DEPENDENCIES:
* initialize a venv within project directory -- python -m venv venv
* activate venv -- source venv/bin/activate
* install requirements. pip install -r requirements.txt
* create database in cmd line: createdb simple_auth
* create test database in cmd line (test files will connect to this DB but .env needs to be created as well per last step here): createdb simple_auth_test
* run seed.py with python to create latest db tables from models file (ensure this happened with PSQL -- db should just have users table with id, email, username, pwd)
* create .env file with SECRET_KEY=abc123 & DATABASE_URL=postgresql:///warbler
* create gitignore file with __pycache__, .env, and /venv

TEST NOTES:
* Tests exist for user model (repr, signup, authenticate) & user views (are we seeing correct home page with logged in / out users)

RUNNING TESTS:
* for test_user_views.py file: enter this in command line FLASK_ENV=production python -m unittest test_user_views.py
* for test_user_model.py: python -m unittest test_user_model.py

TODO - What would I do here with more time?
* mobile view - it's responsive but the buttons and text are small on cell phones. just want to update that.
* edit user credentials / information form. 
* style is basic bootstrap and can definitely be improved. Forms have too little spacing. 
* logout style and signup / login styles are slightly different which needs to be made uniform
* do something cooler with the home page :)
* 404 page is nothing special - I would want to style that a little better.