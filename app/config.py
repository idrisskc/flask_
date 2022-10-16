import os 
from dotenv import load_dotenv
load_dotenv(dotenv_path= '.env', override=True)


basedir = os.path.abspath(os.path.dirname(__file__))
secret_key = os.urandom(32)
print(basedir)

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
NAME_DB = os.getenv('NAME_DB')
PORT_DB = os.getenv('PORT_DB')
SECRET_KEY = os.getenv('SECRET_KEY')

class Config(object):
    DEBUG = False
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER_NAME}:{PASSWORD}@localhost{PORT_DB}/{NAME_DB}'

# print(Config.SECRET_KEY)   

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    
class ProductionConfig(Config):
    DEBUG = False    
    
class TestingConfig(Config):
    TESTING = True    