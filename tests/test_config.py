import os

class TestConfig:
    TESTING = True
    DEBUG = True
    UPLOAD_FOLDER = 'test_uploads'
    SECRET_KEY = 'test_secret_key'
    MONGODB_SETTINGS = {
        'db': 'test_db',
        'host': 'localhost',
        'port': 27017
    }
