"""User View tests."""

# how to run these tests:
#
#    FLASK_ENV=production python -m unittest test_user_views.py

import os
from unittest import TestCase

from models import db, User

# connect to test DB before we import app -- override env variable

os.environ['DATABASE_URL'] = "postgresql:///simple_auth_test"

# Now we can import app

from app import app, CURR_USER_KEY

# Create our tables once
# after / before each we'll refresh the data inside

db.create_all()

# Disabling WTForms CSRF for testing at all, since it causes problems

app.config['WTF_CSRF_ENABLED'] = False

class UserViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data to sign them up in DB"""

        User.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser")

        db.session.commit()

        self.testuser_id = self.testuser.id


    def tearDown(self):
        db.session.rollback()

    def test_get_home_page_logged_in(self):
        """Do we get correct page on logged in"""

        # change session trick to show we are 'logged in'

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

            # Go home to get logged in page

            resp = c.get("/")

            self.assertEqual(resp.status_code, 200)
            # Make sure that in the response, we get the username
            self.assertIn(f"{self.testuser.username}", str(resp.data))

    def test_get_home_page_logged_out(self):
        """Do we get correct page on logged out"""

        # dont 'log in' anyone. go to home page and see no username

        with self.client as c:

            # Go home to get logged out page

            resp = c.get("/")

            self.assertEqual(resp.status_code, 200)
            # Make sure that in the response, we get the new here? question
            self.assertIn("Welcome to AuthApp!", str(resp.data))

    def test_render_of_signup_form(self):
        """Do we get correct page on logged out"""

        # dont 'log in' anyone. go to home page and see no username

        with self.client as c:

            # Go home to get logged out page

            resp = c.get("/signup")

            self.assertEqual(resp.status_code, 200)
            # Make sure that in the response, we get the new here? question
            self.assertIn("Join Now", str(resp.data))
            
    def test_render_of_login_form(self):
        """Do we get correct page on logged out"""

        # dont 'log in' anyone. go to home page and see no username

        with self.client as c:

            # Go home to get logged out page

            resp = c.get("/login")

            self.assertEqual(resp.status_code, 200)
            # Make sure that in the response, we get the new here? question
            self.assertIn("Welcome back.", str(resp.data))
