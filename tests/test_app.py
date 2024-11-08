import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object('test_config.TestConfig')
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_alzheimer_page(self):
        response = self.app.get('/alzheimer')
        self.assertEqual(response.status_code, 200)

    def test_upload_image(self):
        with open('test_image.jpg', 'rb') as img:
            response = self.app.post('/resulta', data={
                'firstname': 'John',
                'lastname': 'Doe',
                'email': 'john.doe@example.com',
                'phone': '1234567890',
                'gender': 'male',
                'age': '50',
                'gidentifier': 'test_identifier',
                'symptom': 'memory loss',
                'file': img
            })
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
