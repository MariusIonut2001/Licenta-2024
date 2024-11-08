from mongoengine import connect
from config import _settings

def init():
    connect(host=str(_settings.MONGO_HOST))
