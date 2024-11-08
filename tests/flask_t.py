import unittest
from flask_testing import TestCase
from app import app

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

    def test_alzheimer_page(self):
        response = self.client.get('/alzheimer')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alzheimer', response.data)

if __name__ == '__main__':
    unittest.main()
