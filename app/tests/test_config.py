import json
import unittest
from flask import current_app
from flask_testing import TestCase
from manage import app
from app.main.config import basedir

class TestDevelopmentConfig(TestCase):
    '''Test development enviroment configurations'''

    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app
        
    def test_env_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'yoyo')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

class TestTestingConfig(TestCase):
    '''Test testing enviroment configurations'''

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_env_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is True)

class TestProductionConfig(TestCase):
    '''Test production enviroment configurations'''

    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_env_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is False)
