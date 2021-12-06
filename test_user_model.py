"""User model tests."""

# how to run these tests:

#    python -m unittest test_user_model.py

import os
from unittest import TestCase

from models import db, User
from flask_bcrypt import Bcrypt
from sqlalchemy import exc

# Setting env variable to use different DB for tests.
# need to do before the app is imported.

os.environ['DATABASE_URL'] = "postgresql:///simple_auth_test"

#now we can import app
from app import app

bcrypt = Bcrypt()

# Create our tables once
# after / before each we'll refresh the data inside

db.create_all()

class UserModelTestCase(TestCase):
    """Test the user model in DB"""

    def setUp(self):
        """Create test client, add sample data."""
        
        #delete from the db so we can refresh
        User.query.delete()

        #create client
        self.client = app.test_client()

        #create data
        test_u1 = User(email="testemail1@test.com",
                        username="testuser1",
                        password="pass1")

        test_u2 = User(email="testemail2@test.com",
                        username="testuser2",
                        password="pass2")

        test_u3 = User(email="testemail3@test.com",
                        username="testuser3",
                        password="pass3")


        #add and commit that to the db
        db.session.add(test_u1)
        db.session.add(test_u2)
        db.session.add(test_u3)

        db.session.commit()

        #grabbing here as we are not sure what we are gonna get as ID because 
        # of auto incrementing primary key
        self.test_u1_id = test_u1.id
        self.test_u2_id = test_u2.id
        self.test_u3_id = test_u3.id
    
    def tearDown(self):
        """Roll back after each test"""
        db.session.rollback()


    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        self.assertEqual(u.email, "test@test.com")

    def test_repr_method(self):
        """does the repr method work?"""

        test_user = User.query.get(self.test_u1_id)
        
        self.assertEqual(test_user.__repr__(), f"<User #{test_user.id}: {test_user.username}, {test_user.email}>")

    def test_user_signup(self):
        """Does signup return the correct user"""

        test_user_sign_up = User.signup("test_user_1", "test1@test.com", "testing123")

        db.session.commit()

        #tests successful username entered
        self.assertEqual(test_user_sign_up.username, "test_user_1")

        #tests successful email entered
        self.assertEqual(test_user_sign_up.email, "test1@test.com")

        #tests successful password hash
        self.assertTrue(bcrypt.check_password_hash(test_user_sign_up.password, "testing123"))

    def test_unsuccessful_email_signup(self):
        """testing if error raises on blank email"""
        test_user_sign_up = User.signup("useruseruser", None, "testing123")

        db.session.add(test_user_sign_up)

        #should raise error given no email
        with self.assertRaises(exc.IntegrityError):
            db.session.commit()

    def test_unsuccessful_username_signup(self):
        """testing if error raises on blank UN"""
        test_user_sign_up = User.signup(None, "test123@test.com", "testing123")

        db.session.add(test_user_sign_up)

        #should raise error given no username
        with self.assertRaises(exc.IntegrityError):
            db.session.commit()


    def test_successful_authentication(self):
        """checks to see if user is successfully authenticated with correct UN and PW"""

        test_user_2 = User.signup(
                username="new_user",
                password="test_new",
                email="test2@testuser.com"
            )

        db.session.commit()

        #authentication should work
        self.assertTrue(test_user_2.authenticate(test_user_2.username,"test_new"))

    def test_failed_password_authentication(self):
        """checks to see if user is NOT authenticated with incorrect PW"""
        user_1 = User.query.get(self.test_u1_id)

        with self.assertRaises(ValueError):
            user_1.authenticate(user_1.username,"12345")

    def test_failed_username_authentication(self):
        """checks to see if user is NOT authenticated with incorrect UN"""
        user_1 = User.query.get(self.test_u1_id)

        self.assertFalse(user_1.authenticate("123","pass1"))