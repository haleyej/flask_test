# use python class to store config vars
import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'