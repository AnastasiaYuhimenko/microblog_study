import os


class Config:
    SECRET_KEY = os.environ.get('Secret key') or 'you-will-never-guess!'
