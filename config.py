import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'

    # Railway gives postgres:// but SQLAlchemy needs postgresql://
    uri = os.environ.get('DATABASE_URL') or 'sqlite:///contacts.db'
    if uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = uri

    SQLALCHEMY_TRACK_MODIFICATIONS = False
