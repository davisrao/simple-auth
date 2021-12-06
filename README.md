OVERVIEW:
* Simple auth app that allows user to log in / sign up to view 'private' page that displays their username
* Built with python / flask. Routes live on app.py file, DB models are in models.py. 
* DB is postgresql
* Front end is rendered by flask using jinjda templates
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
* create test database in cmd line: createdb simple_auth_test
* run seed.py with python to create latest db tables from models file
* create .env file with SECRET_KEY=abc123 & DATABASE_URL=postgresql:///warbler

TEST NOTES:
* Tests exist for user model & user views. 

RUNNING TESTS:
* for test_user_views.py file: enter this in command line FLASK_ENV=production python -m unittest test_user_views.py
* for test_user_model.py: python -m unittest test_user_model.py

TODO - What would I do here with more time?
* edit user credentials / information
* mobile view - it's responsive but the buttons and text are small on cell phones. just want to update that.
* style is basic bootstrap - can be improved
* do something cooler with the home page :)