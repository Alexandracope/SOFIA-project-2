import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app
# from application import db
# from application.models import Users, Posts
class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        # app.config.update(
        #    SQLALCHEMY_DATABASE_URI='mysql+pymysql://(YOUR TEST DB INFO)'        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        # db.session.commit()
        # db.drop_all()
        # db.create_all()

        # create test admin user
        # admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        # employee = Users(first_name="test", last_name="user", email="test@user.com", password="test2016")

        # save users to database
        # db.session.add(admin)
        # db.session.add(employee)
        # db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        # db.session.remove()
        # db.drop_all()

class TestViews(TestBase):
    
    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
